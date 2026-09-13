#!/usr/bin/env python3
"""
SAS IDeaS Enterprise Composite Triage Super-Tools
=================================================
Autonomous multi-domain workflow orchestration tools designed for:
1. OHM Agent (Deep automated RCA, rich structured payloads, correlation IDs)
2. Microsoft 365 Copilot (Teams/Outlook cards, concise summaries, <10s response SLA)

Primary Super-Tools:
- ideas_triage_case_e2e: End-to-end case investigation correlating SFDC, UPS, CMA, Datadog & Runbooks.
- ideas_diagnose_rate_upload: Pinpoints pricing delivery, LRV constraint, and SFTP transmission failures.
- ideas_reconcile_revenue_pace: Automated 10-tab Accom_Activity vs PACE_Accom_Activity variance audit.
"""

import os
import re
import json
import time
import asyncio
import logging
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger("composite-triage-tools")

# Import domain subsystems
import sfdc_mcp_server
import cma_mcp_server
import optix_mcp_server
import confluence_mcp_server
import datadog_mcp_server
from ups_mcp_server import dispatch_ups_tool

# Regex helpers for extracting property codes from text (e.g. "(H8808)", "property HLT01", "8808")
PROP_CODE_PAREN_REGEX = re.compile(r"\(([A-Za-z0-9_\-]{3,10})\)")
PROP_CODE_EXPLICIT_REGEX = re.compile(r"\b(?:property|hotel|tenant|prop|code)[:\s=]+([A-Za-z0-9_\-]{3,10})\b", re.IGNORECASE)


def extract_property_code(case_record: Dict[str, Any]) -> Optional[str]:
    """Heuristically extracts property code from case fields, subject, or description."""
    # 1. Direct fields if present
    for f in ("property_code", "property_code__c", "property_id", "property_name"):
        val = case_record.get(f)
        if val and isinstance(val, str):
            # Check for pattern like "Novotel Jazan (H8808)"
            m = PROP_CODE_PAREN_REGEX.search(val)
            if m:
                return m.group(1).strip()
            # If short alphanumeric code
            if len(val.strip()) <= 8 and val.strip().isalnum():
                return val.strip()

    # 2. Account Name (e.g. "Novotel Jazan (H8808)")
    acc = case_record.get("account_name", "")
    if acc:
        m = PROP_CODE_PAREN_REGEX.search(acc)
        if m:
            return m.group(1).strip()

    # 3. Subject or Description explicit mentions
    text = f"{case_record.get('subject', '')} {case_record.get('description', '')}"
    m_exp = PROP_CODE_EXPLICIT_REGEX.search(text)
    if m_exp:
        return m_exp.group(1).strip()

    m_paren = PROP_CODE_PAREN_REGEX.search(text)
    if m_paren:
        return m_paren.group(1).strip()

    return None


async def execute_ideas_triage_case_e2e(
    case_number: str,
    property_code: Optional[str] = None,
    include_logs: bool = True,
    include_runbook: bool = True,
    client_type: str = "auto",
) -> Dict[str, Any]:
    """
    Executes an autonomous end-to-end investigation for a Salesforce Case across all 5 enterprise domains:
    1. Salesforce: Case details, subject, description, priority, engineer comments.
    2. Property Resolution (UPS/CMA): Hotel name, PMS interface type, cluster tier (PROD_1..6).
    3. CMA Batch Health: Active Spring Batch chains, tenant chains, execution status.
    4. Datadog Observability: Scans for error spikes and timeouts around case context.
    5. Knowledge Base & Runbooks: Matches diagnostic runbooks, SOPs, and troubleshooting guides.
    """
    t0 = time.monotonic()
    case_clean = str(case_number).strip().lstrip("#")
    
    # --------------------------------------------------------------------------
    # STEP 1: Salesforce Case Lookup (Postgres Clone or Live SFDC)
    # --------------------------------------------------------------------------
    sfdc_res = await asyncio.to_thread(
        sfdc_mcp_server.dispatch_sfdc_tool,
        "sfdc_get_case",
        {"case_number": case_clean, "include_comments": True},
    )

    if not sfdc_res or not sfdc_res.get("found"):
        return {
            "status": "NOT_FOUND",
            "error": f"Salesforce Case #{case_clean} could not be found in PostgreSQL clone or live Salesforce.",
            "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
        }

    case_data = sfdc_res
    subject = case_data.get("subject", "No Subject")
    description = case_data.get("description", "")
    account_name = case_data.get("account_name", "Unknown Account")
    priority = case_data.get("priority", "Normal")
    case_status = case_data.get("status", "Unknown")
    owner_name = case_data.get("owner_name", "Unassigned")
    created_date = case_data.get("created_date", "")
    comments = case_data.get("comments", [])

    # --------------------------------------------------------------------------
    # STEP 2: Property Code Resolution
    # --------------------------------------------------------------------------
    resolved_prop_code = property_code or extract_property_code(case_data)
    # Strip leading 'H' if format is H8808 and numeric lookup needed
    numeric_prop_code = resolved_prop_code
    if resolved_prop_code and resolved_prop_code.startswith("H") and resolved_prop_code[1:].isdigit():
        numeric_prop_code = resolved_prop_code[1:]

    # --------------------------------------------------------------------------
    # STEP 3: Multi-Domain Parallel Investigation
    # --------------------------------------------------------------------------
    cma_env_task = None
    cma_chains_task = None
    ups_prop_task = None
    dd_logs_task = None
    runbook_task = None
    help_doc_task = None

    # A. CMA Environment & Batch Chains
    if resolved_prop_code:
        # Search by both alphanumeric and numeric code
        query_code = numeric_prop_code or resolved_prop_code
        cma_env_task = cma_mcp_server.mcp_server.call_tool(
            "cma_resolve_tenant_environment",
            {"property_code": query_code}
        )
        cma_chains_task = cma_mcp_server.mcp_server.call_tool(
            "cma_search_chains",
            {"keyword": resolved_prop_code}
        )
        ups_prop_task = asyncio.to_thread(
            dispatch_ups_tool,
            "ups_search_properties",
            {"query": resolved_prop_code}
        )

    # B. Datadog Log Inspection
    if include_logs:
        log_query = f"service:g3_app-prod-log status:error"
        if resolved_prop_code:
            log_query += f" ({resolved_prop_code} OR {numeric_prop_code})"
        dd_logs_task = asyncio.to_thread(
            datadog_mcp_server.execute_tool,
            "datadog_search_logs",
            {"query": log_query, "limit": 4}
        )

    # C. Confluence Runbook & Knowledge Base Matching
    if include_runbook:
        # Extract symptom keywords from subject
        symptom = subject
        runbook_task = asyncio.to_thread(
            confluence_mcp_server.execute_tool,
            "confluence_match_runbook_by_symptom",
            {"symptom": symptom}
        )
        # Search local markdown help docs for relevant keywords
        help_query = "pricing" if "pricing" in subject.lower() else ("rate" if "rate" in subject.lower() else "decision")
        help_doc_task = asyncio.to_thread(
            confluence_mcp_server.execute_tool,
            "confluence_search_help_docs",
            {"query": help_query}
        )

    # Execute all inspections concurrently
    cma_env_res = {}
    cma_chains_res = {}
    ups_prop_res = {}
    dd_logs_res = {}
    runbook_res = {}
    help_doc_res = {}

    if cma_env_task:
        try:
            raw = await cma_env_task
            cma_env_res = json.loads(raw.content[0].text) if hasattr(raw.content[0], "text") else {}
        except Exception as exc:
            logger.warning("CMA env resolution error: %s", exc)

    if cma_chains_task:
        try:
            raw = await cma_chains_task
            cma_chains_res = json.loads(raw.content[0].text) if hasattr(raw.content[0], "text") else {}
        except Exception as exc:
            logger.warning("CMA chains search error: %s", exc)

    if ups_prop_task:
        try:
            ups_prop_res = await ups_prop_task
        except Exception as exc:
            logger.warning("UPS search error: %s", exc)

    if dd_logs_task:
        try:
            dd_logs_res = await dd_logs_task
        except Exception as exc:
            logger.warning("Datadog search error: %s", exc)

    if runbook_task:
        try:
            runbook_res = await runbook_task
        except Exception as exc:
            logger.warning("Runbook match error: %s", exc)

    if help_doc_task:
        try:
            help_doc_res = await help_doc_task
        except Exception as exc:
            logger.warning("Help doc search error: %s", exc)

    # --------------------------------------------------------------------------
    # STEP 4: Synthesize Root-Cause Hypotheses & Triage Verdict
    # --------------------------------------------------------------------------
    cluster = cma_env_res.get("cluster", "Unknown Cluster")
    prop_details = cma_env_res.get("property_details", {})
    tenant_chains = cma_chains_res.get("results", [])

    # Heuristic Failure Mode Classification based on IDeaS Triage Knowledge Base
    failure_category = "General System Inquiry / Investigation"
    root_cause_summary = "General inquiry or configuration review."
    recommended_actions = []

    sub_lower = subject.lower()
    desc_lower = description.lower()

    if any(k in sub_lower or k in desc_lower for k in ["competitor", "match price", "exact price", "positioning"]):
        failure_category = "Competitive Market Position & Pricing Positioning Policy"
        root_cause_summary = (
            "G3 RMS Optimizer evaluates competitive ranges and percentiles rather than directly mirroring "
            "a single competitor's absolute price. Single competitor matching is constrained by LRV floors, "
            "rate ceilings, and Room Class Price Rank Hierarchy rules."
        )
        recommended_actions = [
            "Review Competitor Positioning Constraints in G3: Configure -> Pricing -> Competitive Position.",
            "Verify whether target competitor rates are active and open (G3 ignores closed rates).",
            "Check Optix tables 'Competitive_Constraint' and 'Competitor_Ignore' for active date restrictions.",
        ]
    elif any(k in sub_lower or k in desc_lower for k in ["rate not update", "pricing not upload", "upload fail", "not publishing"]):
        failure_category = "PMS / CRS Rate Delivery Failure"
        root_cause_summary = (
            "Pricing decisions were generated but delivery to PMS/CRS encountered a transmission delay, "
            "LRV floor restriction, or partner listener timeout."
        )
        recommended_actions = [
            "In G3 RMS UI -> Pricing -> Decision Delivery -> Check delivery status and click 'Force Redelivery'.",
            "Verify CEDF extract job status using 'cedf_get_job_status' or 'cedf_trigger_resend_job'.",
            "Inspect PMS listener endpoint connectivity in UPS HAL Explorer.",
        ]
    elif any(k in sub_lower or k in desc_lower for k in ["chain", "batch", "optimization delay", "nightly run", "deadlock"]):
        failure_category = "Spring Batch / CMA Optimization Pipeline Delay"
        root_cause_summary = (
            "Batch execution delayed or blocked due to database lock contention, PMS extract data dependency, "
            "or worker thread starvation during the nightly optimization cycle."
        )
        recommended_actions = [
            f"Check CMA batch chain status for {resolved_prop_code} using 'cma_get_chain_details'.",
            "Inspect Job DB for active lock contention or blocked steps.",
            "Review Datadog monitors for cluster error rate spikes.",
        ]
    elif any(k in sub_lower or k in desc_lower for k in ["discrepancy", "revenue", "occupancy", "pace", "variance"]):
        failure_category = "Revenue & Occupancy Data Discrepancy"
        root_cause_summary = (
            "Variance between Optix Data Warehouse and PMS transaction logs, often caused by intraday sync lag, "
            "unmapped market segments, or net-vs-gross tax adjustments."
        )
        recommended_actions = [
            "Execute Optix 10-tab discrepancy audit comparing Accom_Activity and PACE_Accom_Activity.",
            "Check unmapped market segment codes in tenant database.",
            "Verify STLY 364-day Day-of-Week shift alignments.",
        ]

    # Best Runbook Match
    best_runbook = runbook_res.get("best_match") or {}
    runbook_title = best_runbook.get("title", "Standard G3 Operations Triage SOP")
    runbook_url = best_runbook.get("confluence_url", "")
    runbook_summary = best_runbook.get("summary", "")
    runbook_remediation = best_runbook.get("suggested_remediation", "")

    # Top relevant help docs
    matched_help_docs = [
        {"title": d.get("title"), "file": d.get("file")}
        for d in help_doc_res.get("results", [])[:3]
    ]

    # --------------------------------------------------------------------------
    # STEP 5: Generate Copilot-Ready Markdown Card
    # --------------------------------------------------------------------------
    elapsed_total = round((time.monotonic() - t0) * 1000, 2)

    md_card = []
    md_card.append(f"### 📋 Case {case_clean} Autonomous Triage Assessment")
    md_card.append(f"**Subject**: {subject}")
    md_card.append(f"- **Account**: {account_name} | **Property Code**: `{resolved_prop_code or 'N/A'}`")
    md_card.append(f"- **Status**: `{case_status}` | **Priority**: `{priority}` | **Owner**: {owner_name}")
    md_card.append(f"- **Environment**: Cluster `{cluster}` | **Created**: {created_date}")
    md_card.append("")
    md_card.append("#### 🔍 Root-Cause Diagnosis")
    md_card.append(f"- **Category**: **{failure_category}**")
    md_card.append(f"- **Assessment**: {root_cause_summary}")
    if tenant_chains:
        chain_names = ", ".join([f"`{c.get('chain_name')}`" for c in tenant_chains[:2]])
        md_card.append(f"- **Associated Batch Chains**: {chain_names}")
    md_card.append("")
    md_card.append("#### 🛠️ Recommended Remediation Actions")
    for idx, act in enumerate(recommended_actions, 1):
        md_card.append(f"{idx}. {act}")
    if runbook_remediation:
        md_card.append(f"4. **Runbook Action**: {runbook_remediation.splitlines()[0]}")
    md_card.append("")
    md_card.append("#### 📚 Reference Documentation & Runbooks")
    if runbook_title and runbook_url:
        md_card.append(f"- **Confluence SOP**: [{runbook_title}]({runbook_url})")
    elif runbook_title:
        md_card.append(f"- **Confluence SOP**: {runbook_title}")
    for hd in matched_help_docs:
        md_card.append(f"- **G3 Guide**: {hd['title']}")

    markdown_rendered = "\n".join(md_card)

    # --------------------------------------------------------------------------
    # STEP 6: Return Structured Response for OHM Agent & Copilot
    # --------------------------------------------------------------------------
    return {
        "status": "SUCCESS",
        "case_number": case_clean,
        "property_code": resolved_prop_code,
        "elapsed_ms": elapsed_total,
        "markdown_card": markdown_rendered,
        "case_overview": {
            "case_id": case_data.get("case_id"),
            "case_number": case_clean,
            "subject": subject,
            "account_name": account_name,
            "priority": priority,
            "status": case_status,
            "owner": owner_name,
            "created_date": created_date,
            "recent_comments_count": len(comments),
        },
        "environment_context": {
            "property_code": resolved_prop_code,
            "numeric_property_code": numeric_prop_code,
            "cluster": cluster,
            "client_code": prop_details.get("Client_Code"),
            "property_name": prop_details.get("Property_Name"),
            "property_stage": prop_details.get("Stage"),
            "associated_chains": tenant_chains,
        },
        "triage_diagnosis": {
            "failure_category": failure_category,
            "root_cause_summary": root_cause_summary,
            "recommended_actions": recommended_actions,
            "relevant_runbook": {
                "title": runbook_title,
                "url": runbook_url,
                "summary": runbook_summary,
                "remediation": runbook_remediation,
            },
            "relevant_help_docs": matched_help_docs,
        },
        "telemetry_findings": {
            "datadog_errors_found": len(dd_logs_res.get("logs", [])) if isinstance(dd_logs_res, dict) else 0,
        },
    }


# ==============================================================================
# SUPER-TOOL 2: ideas_diagnose_rate_upload
# ==============================================================================
async def execute_ideas_diagnose_rate_upload(
    property_code: str,
    lookback_hours: int = 24,
    target_date: Optional[str] = None,
    client_type: str = "auto",
) -> Dict[str, Any]:
    """
    Autonomously diagnoses pricing/rate upload and delivery failures across Optix, CMA, CEDF, and Datadog:
    1. Environment & Chain Resolution: Identifies cluster, tenant chain, and external partner endpoints.
    2. Decision Delivery History: Inspects CMA decision delivery records for BAR, AgileRates, and LRV uploads.
    3. CEDF Upload Pipeline: Checks if client upload feed is active in Cloud Enterprise Datafeed.
    4. Datadog APM Telemetry: Scans outbound decision delivery logs for ERR_PMS_TIMEOUT or dropouts.
    5. Constraint & Runbook Matching: Correlates with HTNG and Competitive Market Position runbooks.
    """
    t0 = time.monotonic()
    prop_clean = str(property_code).strip()
    numeric_code = prop_clean
    if prop_clean.startswith("H") and prop_clean[1:].isdigit():
        numeric_code = prop_clean[1:]

    # Step 1: Resolve Environment & Tenant Chain via CMA
    cma_env_res = {}
    tenant_chain_name = None
    client_code = None
    cluster = "Unknown Cluster"
    property_name = prop_clean

    try:
        raw_env = await cma_mcp_server.mcp_server.call_tool(
            "cma_resolve_tenant_environment",
            {"property_code": numeric_code}
        )
        cma_env_res = json.loads(raw_env.content[0].text) if hasattr(raw_env.content[0], "text") else {}
        cluster = cma_env_res.get("cluster", cluster)
        p_details = cma_env_res.get("property_details", {})
        client_code = p_details.get("Client_Code")
        property_name = p_details.get("Property_Name", property_name)
        suggested_chains = cma_env_res.get("suggested_tenant_chains", [])
        if suggested_chains:
            tenant_chain_name = suggested_chains[0].get("chain_name")
    except Exception as exc:
        logger.warning("Error resolving tenant environment for %s: %s", prop_clean, exc)

    # Step 2: Concurrently query CMA Delivery Records, CEDF Status, Datadog Logs & Runbooks
    cma_delivery_task = None
    if tenant_chain_name:
        cma_delivery_task = cma_mcp_server.mcp_server.call_tool(
            "cma_get_decision_delivery_details",
            {"tenant_chain": tenant_chain_name}
        )

    cedf_task = None
    if client_code:
        cedf_task = asyncio.to_thread(
            dispatch_ups_tool,
            "cedf_check_client_upload_status",
            {"client_code": client_code}
        )

    dd_task = asyncio.to_thread(
        datadog_mcp_server.execute_tool,
        "datadog_trace_decision_delivery_errors",
        {"property_code": numeric_code, "hours_ago": lookback_hours}
    )

    runbook_timeout_task = asyncio.to_thread(
        confluence_mcp_server.execute_tool,
        "confluence_get_runbook",
        {"runbook_key": "DECISION_DELIVERY_TIMEOUT"}
    )

    runbook_conflict_task = asyncio.to_thread(
        confluence_mcp_server.execute_tool,
        "confluence_get_runbook",
        {"runbook_key": "COMPETITIVE_CONSTRAINT_CONFLICT"}
    )

    # Await concurrent tasks
    cma_delivery_res = {}
    cedf_res = {}
    dd_res = {}
    rb_timeout = {}
    rb_conflict = {}

    if cma_delivery_task:
        try:
            raw_del = await cma_delivery_task
            cma_delivery_res = json.loads(raw_del.content[0].text) if hasattr(raw_del.content[0], "text") else {}
        except Exception as exc:
            logger.warning("CMA delivery details error: %s", exc)

    if cedf_task:
        try:
            cedf_res = await cedf_task
        except Exception as exc:
            logger.warning("CEDF status error: %s", exc)

    try:
        dd_res = await dd_task
    except Exception as exc:
        logger.warning("Datadog delivery trace error: %s", exc)

    try:
        rb_timeout = (await runbook_timeout_task).get("runbook", {})
    except Exception as exc:
        logger.warning("Runbook timeout error: %s", exc)

    try:
        rb_conflict = (await runbook_conflict_task).get("runbook", {})
    except Exception as exc:
        logger.warning("Runbook conflict error: %s", exc)

    # Step 3: Analyze Delivery Telemetry
    delivery_records = cma_delivery_res.get("data", [])
    recent_uploads = []
    latest_upload_status = "UNKNOWN"
    latest_upload_time = "N/A"
    latest_external_system = "N/A"

    if delivery_records:
        recent_uploads = delivery_records[:6]
        latest = delivery_records[0]
        latest_upload_status = latest.get("Status", "UNKNOWN")
        latest_upload_time = latest.get("Last_Upload_DTTM", "N/A")
        latest_external_system = latest.get("External_System_Name", "N/A")

    dd_errors_count = dd_res.get("error_count", 0) if isinstance(dd_res, dict) else 0
    cedf_enabled = cedf_res.get("is_client_upload_enabled", True) if isinstance(cedf_res, dict) else True

    # Step 4: Root-Cause Synthesis
    verdict_type = "UNKNOWN"
    diagnosis_title = "Pricing Decision Delivery Assessment"
    root_cause_detail = ""
    remediation_steps = []
    attached_runbook = {}

    if dd_errors_count > 0 or latest_upload_status == "FAIL":
        verdict_type = "PMS_DELIVERY_TIMEOUT"
        diagnosis_title = "Outbound PMS / CRS Delivery Timeout (ERR_PMS_TIMEOUT)"
        root_cause_detail = (
            f"Outbound decision publication failed or timed out during transmission to partner system "
            f"'{latest_external_system}'. Datadog detected {dd_errors_count} transmission error(s). "
            f"Partner listener likely timed out (>30s) or rejected payload XML."
        )
        remediation_steps = [
            "In G3 RMS UI -> Pricing -> Decision Delivery -> Delivery Status -> Click 'Force Redelivery'.",
            f"Verify partner endpoint credentials in UPS HAL Explorer for property '{prop_clean}'.",
            "Instruct hotel IT / PMS vendor to verify local HTNG receiver service status.",
        ]
        attached_runbook = rb_timeout
    elif not cedf_enabled:
        verdict_type = "CEDF_UPLOAD_DISABLED"
        diagnosis_title = "Cloud Enterprise Datafeed (CEDF) Upload Pipeline Disabled"
        root_cause_detail = (
            f"Client upload pipeline for client '{client_code}' is currently disabled in CEDF. "
            f"Pricing exports cannot be routed to SFTP transmission queues."
        )
        remediation_steps = [
            f"In CEDF Admin Console -> Clients -> Enable upload toggle for '{client_code}'.",
            "Trigger a test CEDF feed upload via 'cedf_trigger_resend_job'.",
        ]
        attached_runbook = rb_timeout
    elif latest_upload_status == "SUC":
        verdict_type = "PRICING_PUBLISHED_SUCCESSFULLY"
        diagnosis_title = "Rate Decisions Publishing Successfully (Check LRV & Competitor Constraints)"
        root_cause_detail = (
            f"Latest pricing decisions published successfully to '{latest_external_system}' at {latest_upload_time} "
            f"with Status: SUC. If user reports that published rates appear frozen or unchanged, the cause is "
            f"a Competitive Market Position constraint conflict (e.g. competitor rates closed or LRV floor restriction)."
        )
        remediation_steps = [
            "In G3 RMS UI -> Pricing -> Competitive Intelligence -> Inspect Positioning Rules.",
            "Verify whether competitor rates are closed (G3 ignores closed rates by default).",
            "Check LRV floor table in Optix for active hurdle constraints blocking price drops.",
        ]
        attached_runbook = rb_conflict
    else:
        verdict_type = "NO_RECENT_DELIVERY_RECORDS"
        diagnosis_title = "No Recent Decision Delivery Activity Recorded"
        root_cause_detail = (
            f"No decision delivery activity was recorded for tenant chain '{tenant_chain_name or prop_clean}' "
            f"in the last {lookback_hours} hours. Nightly optimization batch may be pending or delayed."
        )
        remediation_steps = [
            f"Inspect batch chain status for {prop_clean} using 'cma_get_chain_details'.",
            "Verify property is marked ACTIVE in G3 tenant registry.",
        ]
        attached_runbook = rb_timeout

    elapsed_ms = round((time.monotonic() - t0) * 1000, 2)

    # Step 5: Render Markdown Card for Copilot / Teams
    md = []
    status_badge = "🟢 SUCCESS" if latest_upload_status == "SUC" and dd_errors_count == 0 else "🔴 ISSUE DETECTED"
    md.append(f"### 🚀 Rate Upload & Delivery Diagnostic: {property_name} (`{prop_clean}`)")
    md.append(f"- **Overall Pipeline Status**: {status_badge} | **Cluster**: `{cluster}`")
    md.append(f"- **Tenant Chain**: `{tenant_chain_name or 'N/A'}` | **Client Code**: `{client_code or 'N/A'}`")
    md.append("")
    md.append("#### 📊 Subsystem Telemetry Checkpoints")
    md.append(f"- **Latest CMA Delivery Push**: `{latest_upload_status}` to `{latest_external_system}` at `{latest_upload_time}`")
    md.append(f"- **CEDF Client Upload Status**: `{'ENABLED' if cedf_enabled else 'DISABLED'}`")
    md.append(f"- **Datadog Outbound APM Logs**: `{dd_errors_count} error(s) in last {lookback_hours}h`")
    md.append("")
    md.append(f"#### 🔍 Root-Cause Diagnosis: {diagnosis_title}")
    md.append(f"{root_cause_detail}")
    md.append("")
    md.append("#### 🛠️ Recommended Actionable Remediation")
    for idx, step in enumerate(remediation_steps, 1):
        md.append(f"{idx}. {step}")
    md.append("")
    if attached_runbook and attached_runbook.get("title"):
        md.append("#### 📚 Engineering SOP Reference")
        url = attached_runbook.get("confluence_url", "")
        title = attached_runbook.get("title", "")
        if url:
            md.append(f"- **Confluence Runbook**: [{title}]({url})")
        else:
            md.append(f"- **Confluence Runbook**: {title}")
        remed = attached_runbook.get("suggested_remediation", "")
        if remed:
            md.append(f"- **Runbook Fix**: {remed.splitlines()[0]}")

    markdown_rendered = "\n".join(md)

    # Step 6: Return Structured Object for OHM Agent & Copilot
    return {
        "status": "SUCCESS",
        "property_code": prop_clean,
        "numeric_property_code": numeric_code,
        "elapsed_ms": elapsed_ms,
        "markdown_card": markdown_rendered,
        "verdict_type": verdict_type,
        "diagnosis_title": diagnosis_title,
        "root_cause_detail": root_cause_detail,
        "remediation_steps": remediation_steps,
        "environment": {
            "property_name": property_name,
            "property_code": prop_clean,
            "cluster": cluster,
            "client_code": client_code,
            "tenant_chain": tenant_chain_name,
        },
        "delivery_telemetry": {
            "latest_upload_status": latest_upload_status,
            "latest_upload_time": latest_upload_time,
            "external_system": latest_external_system,
            "recent_upload_history": recent_uploads,
            "cedf_upload_enabled": cedf_enabled,
            "datadog_error_count": dd_errors_count,
        },
        "attached_runbook": attached_runbook,
    }

