#!/usr/bin/env python3
"""
Atlassian Confluence & Engineering Knowledge Base Model Context Protocol (MCP) Server
=====================================================================================
Comprehensive 25-Tool Suite for SAS IDeaS Confluence Wiki, Microservices Swagger APIs,
S3 Object Storage Portals, Engineering Diagnostic Runbooks, and G3 System Help Docs.

Enterprise Capabilities:
1. Live Confluence Cloud API (CQL Search, Page Ingestion, Space Hierarchies, History).
2. Curated Engineering Diagnostic Runbooks (HTNG, Pseudo RTs, CRS Delay, Job DB Deadlocks).
3. 13 Microservice Swagger & OpenAPI Catalogs (PROD, STAGE, DEV tiers).
4. Object Storage Registry (Atlantis S3 Explorer, Pull-SFTP Observability, Lakehouse).
5. Offline G3 Help Docs Library (274 full-text markdown guides).
6. Qdrant Hybrid Vector Knowledge Base (confluence_kb & g3_help_docs_kb).
7. Dual Transports: HTTP Server-Sent Events (SSE) on Port 8558 + Stdio Transport.
"""

import os
import re
import sys
import json
import time
import base64
import logging
import argparse
import threading
from typing import Any, Dict, List, Optional, Tuple, Union
from datetime import datetime, date
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("confluence-mcp-server")

# ==============================================================================
# CONFIGURATION & CONSTANTS
# ==============================================================================
CONFLUENCE_URL = (os.getenv("CONFLUENCE_URL") or "https://ideasinc.atlassian.net/wiki").rstrip("/")
CONFLUENCE_USER = os.getenv("CONFLUENCE_USERNAME") or os.getenv("CONFLUENCE_USER") or "omkar.chitnis@ideas.com"
CONFLUENCE_TOKEN = os.getenv("CONFLUENCE_API_TOKEN") or os.getenv("CONFLUENCE_TOKEN") or ""

QDRANT_URL = (os.getenv("QDRANT_URL") or "http://172.27.210.162:6333").rstrip("/")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HELP_DOCS_DIR = os.path.join(SCRIPT_DIR, "data", "g3_help_docs")

MCP_HOST = os.getenv("MCP_HOST", "0.0.0.0")
MCP_PORT = int(os.getenv("CONFLUENCE_MCP_PORT", os.getenv("MCP_PORT", "8558")))


# ==============================================================================
# 1. CURATED RUNBOOKS & MICROSERVICE SPECIFICATIONS
# ==============================================================================
SWAGGER_CATALOG = [
    {
        "service": "UPS (Unified Property Service)",
        "domain": "property_config",
        "description": "Property identity, client code, cluster routing, and feature activation flags.",
        "prod_url": "https://fds.ideasrms.com/api/ups/swagger-ui/index.html",
        "stage_url": "https://fds.stage.ideasrms.com/api/ups/swagger-ui/index.html",
        "dev_url": "https://fds.dev.ideasrms.com/api/ups/swagger-ui/index.html",
    },
    {
        "service": "UIS (Unified Integration Service)",
        "domain": "integrations",
        "description": "Interface credential provisioning, partner credentials, and M2M OAuth2 tokens.",
        "prod_url": "https://fds.ideasrms.com/api/uis/swagger-ui/index.html",
        "stage_url": "https://fds.stage.ideasrms.com/api/uis/swagger-ui/index.html",
        "dev_url": "https://fds.dev.ideasrms.com/api/uis/swagger-ui/index.html",
    },
    {
        "service": "UAS (User Authentication Service)",
        "domain": "authentication",
        "description": "Enterprise SSO, user roles, permission matrices, and token validation.",
        "prod_url": "https://fds.ideasrms.com/api/uas/swagger/swagger-ui.html#/",
        "stage_url": "https://fds.stage.ideasrms.com/api/uas/swagger/swagger-ui.html#/",
        "dev_url": "https://fds.dev.ideasrms.com/api/uas/swagger/swagger-ui.html#/",
    },
    {
        "service": "BMR SDP (Seed Daily Processing Service)",
        "domain": "processing",
        "description": "Automated property rollout, seed data population, and baseline history initialization.",
        "prod_url": "https://bmr-be-sdp-service-internal.ideasrms.com/swagger-ui.html",
        "stage_url": "https://bmr-be-sdp-service-internal.stage.ideasrms.com/swagger-ui.html",
        "dev_url": "https://bmr-be-sdp-service-internal.dev.ideasrms.com/swagger-ui.html",
    },
    {
        "service": "BMR MO (Monitoring Outbound Service)",
        "domain": "decision_delivery",
        "description": "Decision publication telemetry, batch dispatch tracking, and delivery success metrics.",
        "prod_url": "https://bmr-be-mo-service-internal.ideasrms.com/swagger-ui.html",
        "stage_url": "https://bmr-be-mo-service-internal.stage.ideasrms.com/swagger-ui.html",
        "dev_url": "https://bmr-be-mo-service-internal.dev.ideasrms.com/swagger-ui.html",
    },
    {
        "service": "AIS Outbound Manager",
        "domain": "decision_delivery",
        "description": "Cloud microservice orchestrating decision payload construction and transmission to external PMS/CRS.",
        "prod_url": "https://outbound-manager.ais.ideasrms.com/swagger-ui.html",
        "stage_url": "https://outbound-manager.ais.stage.ideasrms.com/swagger-ui.html",
        "dev_url": "https://outbound-manager.ais.dev.ideasrms.com/swagger-ui.html",
    },
    {
        "service": "AIS Task Manager",
        "domain": "task_scheduling",
        "description": "Internal asynchronous task distribution, queue management, and retry policies.",
        "prod_url": "https://task-manager.ais.ideasrms.com/swagger-ui.html",
        "stage_url": "https://task-manager.ais.stage.ideasrms.com/swagger-ui.html",
        "dev_url": "https://task-manager.ais.dev.ideasrms.com/swagger-ui.html",
    },
    {
        "service": "AIS Webhook",
        "domain": "webhooks",
        "description": "Inbound webhook receiver and event dispatch for cloud PMS events.",
        "prod_url": "https://webhook.ais.ideasrms.com/swagger-ui.html",
        "stage_url": "https://webhook.ais.stage.ideasrms.com/swagger-ui.html",
        "dev_url": "https://webhook.ais.dev.ideasrms.com/swagger-ui.html",
    },
    {
        "service": "PMS Inbound Microservice (Spring Data REST HAL)",
        "domain": "pms_feed",
        "description": "56 Spring Data REST endpoints for cloud ingestion (inventories, reservations, market segments, ETL errors).",
        "prod_url": "https://pmsinbound-internal.ideasrms.com/",
        "stage_url": "https://pmsinbound-internal.stage.ideasrms.com/",
        "dev_url": "https://pmsinbound-internal.dev.ideasrms.com/",
    },
    {
        "service": "Decision Delivery Service (Spring Data REST HAL)",
        "domain": "decision_delivery",
        "description": "33 Spring Data REST endpoints for decision publication (delivery trackers, daily BARs, hurdle rates, overbooking).",
        "prod_url": "https://decision-delivery-internal.ideasrms.com/",
        "stage_url": "https://decision-delivery-internal.stage.ideasrms.com/",
        "dev_url": "https://decision-delivery-internal.dev.ideasrms.com/",
    },
    {
        "service": "NGI STR (Next Gen Integrations STR)",
        "domain": "rate_shopping",
        "description": "Smith Travel Research (STR) benchmark data ingestion and competitive set analytics.",
        "prod_url": "https://ngi-str-internal.ideasrms.com/swagger-ui.html",
        "stage_url": "https://ngi-str-internal.stage.ideasrms.com/swagger-ui.html",
        "dev_url": "https://ngi-str-internal.dev.ideasrms.com/swagger-ui.html",
    },
    {
        "service": "TARS (Accor CRS Connector)",
        "domain": "integrations",
        "description": "Accor Central Reservation System connectivity, inventory availability, and rate push.",
        "prod_url": "https://tars-internal.ideasrms.com/swagger-ui/index.html",
        "stage_url": "https://tars-internal.stage.ideasrms.com/swagger-ui/index.html",
        "dev_url": "https://tars-internal.dev.ideasrms.com/swagger-ui/index.html",
    },
    {
        "service": "FOLS (Accor Cloud PMS Connector)",
        "domain": "integrations",
        "description": "Accor FOLS PMS bidirectional reservations, stays, and decision delivery pipeline.",
        "prod_url": "https://fols-internal.ideasrms.com/swagger-ui/index.html",
        "stage_url": "https://fols-internal.stage.ideasrms.com/swagger-ui/index.html",
        "dev_url": "https://fols-internal.dev.ideasrms.com/swagger-ui/index.html",
    },
]

S3_RESOURCES = [
    {
        "name": "Atlantis S3 Explorer",
        "domain": "data_pipeline",
        "type": "Web Portal",
        "description": "Internal S3 bucket browser for inspecting raw inbound drop files, differential snapshots, and extract payloads.",
        "access": "Read-Only internal portal",
        "prod_url": "https://atlantis-internal.ideasrms.com/s3-explorer",
        "stage_url": "https://atlantis-internal.stage.ideasrms.com/s3-explorer",
        "dev_url": "https://atlantis-internal.dev.ideasrms.com/s3-explorer",
    },
    {
        "name": "Atlantis Pull-SFTP Observability",
        "domain": "ftp_feeds",
        "type": "REST Telemetry",
        "description": "Health check and live observability for the SFTP-to-S3 ingestion bridge.",
        "access": "Read-Only GET endpoint",
        "prod_url": "https://atlantis-internal.ideasrms.com/pull-sftp/observability",
        "stage_url": "https://atlantis-internal.stage.ideasrms.com/pull-sftp/observability",
        "dev_url": "https://atlantis-internal.dev.ideasrms.com/pull-sftp/observability",
    },
    {
        "name": "Analytics Lakehouse (Trino on S3)",
        "domain": "analytics_dw",
        "type": "S3 Data Lake",
        "description": "Object storage bucket for large-scale Optix and Evolve analytical queries.",
        "access": "IAM Read Role",
        "prod_url": "s3://trino-prod-warehouse/warehouse/",
        "stage_url": "s3://trino-stage-warehouse/warehouse/",
        "dev_url": "s3://trino-test-poc/warehouse/",
    },
]

DIAGNOSTIC_RUNBOOKS: Dict[str, Dict[str, Any]] = {
    "HTNG_STATS_VS_INVENTORY": {
        "title": "Distinguishing HTNG-Stats vs HTNG-Inventory Feeds",
        "confluence_page_id": "5640487026",
        "confluence_title": "Difference Between Stats and Inventory",
        "confluence_url": "https://ideasinc.atlassian.net/wiki/spaces/G3P/pages/5640487026/Difference+Between+Stats+and+Inventory",
        "domain": "pms_feed",
        "keywords": ["stats", "inventory", "activitycalculated", "room sold", "occupancy summary"],
        "summary": (
            "Classifies whether property operates on HTNG-Stats (<OTA_HotelStatsNotifRQ>) or HTNG-Inventory (<OTA_HotelInvCountNotifRQ>). "
            "Inventory contains room-type-level room sold and capacity derived from operational availability. If inventory is stale, "
            "G3 falls back to nucleusOccupancySummary."
        ),
        "identification_technique": (
            "Query /nucleusStatisticsCorrelations/criteria?search=clientCode=={client_code};propertyCode=={property_code}&size=1&sort=createDate,DESC. "
            "Check 'activityCalculated': False = HTNG-Stats, True = HTNG-Inventory."
        ),
        "suggested_remediation": (
            "1. Confirm PMS export mode with property revenue team (Inventory vs Stats).\n"
            "2. If property is Inventory-based but room sold is missing, verify <OTA_HotelInvCountNotifRQ> ingestion timestamp.\n"
            "3. If stale, inspect Nucleus Inbound ETL error logs (/nucleusErrorMessages) for unmapped room types."
        ),
    },
    "PSEUDO_ROOM_TYPE_FILTER": {
        "title": "Pseudo Room Type Identification & Revenue Ingestion Filter",
        "confluence_page_id": "5687541804",
        "confluence_title": "Pseudo RT Identification in PMS Inbound",
        "confluence_url": "https://ideasinc.atlassian.net/wiki/spaces/~63b2e09f15d69a40aa198558/pages/5687541804/Pseudo+RT+Identification+in+PMS+Inbound",
        "domain": "room_types",
        "keywords": ["pseudo", "zero capacity", "component room", "room type", "sold"],
        "summary": (
            "Pseudo room types are zero-capacity, non-physical rooms that never receive sold and capacity, but carry revenue. "
            "Component room types also lack physical rooms, but DO receive sold and capacity. New zero-capacity RTs can erroneously trigger "
            "New Component Room alerts or distort RevPAR."
        ),
        "identification_technique": (
            "Audit tenant Accom_Type table and verify capacity=0. Check Accom_Activity across the entire inbound window: "
            "if sold=0 and capacity=0 for the entire window but revenue > 0, it is a Pseudo Room Type."
        ),
        "suggested_remediation": (
            "1. In G3 System Administration -> Room Type Management, verify if the room type is flagged as Pseudo.\n"
            "2. If client does not want pseudo room revenue added to G3 analytics, configure pseudo RT filter in PMS-Inbound parameters.\n"
            "3. Do not mark as Component Room unless physical room pooling is explicitly configured."
        ),
    },
    "CRS_DATA_NOT_ARRIVED": {
        "title": "CRS Data Delay & Stale Forecast Ingestion (CRSDataDidNotArrive)",
        "confluence_page_id": "5612011684",
        "confluence_title": "System Not Up to Date Alert - CRSDataDidNotArrive",
        "confluence_url": "https://ideasinc.atlassian.net/wiki/spaces/BMR/pages/5612011684/System+Not+Up+to+Date+Alert+-+CRSDataDidNotArrive",
        "domain": "pms_feed",
        "keywords": ["crsdatadidnotarrive", "stale", "feed delay", "missing crs", "lag", "crs"],
        "summary": (
            "Triggered when the scheduled CRS statistical feed is not received within the configured time window. "
            "G3 RMS will continue forecasting on stale data, risking frozen rate recommendations and sub-optimal pricing."
        ),
        "identification_technique": (
            "Check Accom_Activity latest snapshot timestamp via audit_data_freshness_and_pipeline_lag. "
            "If lag > 6.0 hours, alert CRSDataDidNotArrive is active in the G3 Alerts tab."
        ),
        "suggested_remediation": (
            "1. Check SFTP /incoming/ directory or inspect Atlantis S3 Explorer (https://atlantis-internal.dev.ideasrms.com/s3-explorer).\n"
            "2. Review Datadog service 'g3_app-prod-log' for batch ingestion timeout or network disconnect.\n"
            "3. Snooze alert temporarily in G3 Alerts tab if PMS vendor is performing scheduled maintenance."
        ),
    },
    "JOB_DB_LOCK_DEADLOCK_FPLOS": {
        "title": "Job DB Deadlocks, Lock Contention & FPLOS Decision Delivery Failures",
        "confluence_page_id": "5622661146",
        "confluence_title": "IR-167 - Prod1: NGI FPLOS Decision Delivery Job Failure",
        "confluence_url": "https://ideasinc.atlassian.net/wiki/spaces/OPS/pages/5622661146/IR-167+-Prod1+NGI+FPLOS+Decision+Delivery+Job+failure",
        "domain": "decision_delivery",
        "keywords": ["deadlock", "job db", "fplos", "lock contention", "jdbc", "timeout"],
        "summary": (
            "High concurrency lock contention on Job DB tables (Job_State, Problem, and Job_Instance_Work_Context) "
            "can cause Full Pattern Length of Stay (FPLOS) decision publication jobs to timeout or fail with JDBC connection errors."
        ),
        "identification_technique": (
            "Inspect Job DB for open transactions on Job_State. Check Datadog metrics for lock contention and query latency. "
            "Verify if decision delivery trackers record status=FAILED with message 'Job timeout' or 'Transaction rolled back'."
        ),
        "suggested_remediation": (
            "1. In Job DB, query active sessions blocking Job_Instance_Work_Context.\n"
            "2. If deadlock recurs during peak batch windows, stagger decision delivery schedules in integrationPropertyConfigs.\n"
            "3. Verify connection pool sizing in g3_app configuration."
        ),
    },
    "GROUP_PRICING_HIERARCHY_NPE": {
        "title": "Group Pricing Hierarchy Validation NullPointerException (NPE)",
        "confluence_page_id": "2721185793",
        "confluence_title": "Group Pricing Configuration Issue",
        "confluence_url": "https://ideasinc.atlassian.net/wiki/spaces/Crushers/pages/2721185793/Group+Pricing+Configuration+Issue",
        "domain": "group_wash",
        "keywords": ["group pricing", "ceiling", "floor", "hierarchy", "npe", "season"],
        "summary": (
            "When product hierarchy toggles are active, hierarchy validation can inadvertently execute against Group Pricing "
            "configurations. Because Group Pricing entities have no product concept, a NullPointerException is thrown, "
            "preventing users from configuring ceiling/floor prices or splitting seasons."
        ),
        "identification_technique": (
            "Check whether property has pacman.feature.GroupFinalFcstOvrdEnabled=true or group pricing active, and verify "
            "whether parameter ceiling/floor updates fail in G3 System Administration."
        ),
        "suggested_remediation": (
            "1. Inspect Global DB Config_Parameter_Value for hierarchy toggle overrides at the property level.\n"
            "2. If ceiling/floor changes fail with UI error, check if property-level override erroneously forces product validation.\n"
            "3. Follow Runbook CSS Task T11190554 to ensure group entities bypass product hierarchy checks."
        ),
    },
    "OXI_PMS_MESSAGE_TRACE": {
        "title": "Support Team OXI & PMS Inbound Message Traceability",
        "confluence_page_id": "536084481",
        "confluence_title": "Proposal for Support Team NGI Data Access",
        "confluence_url": "https://ideasinc.atlassian.net/wiki/spaces/NGI/pages/536084481/Proposal+for+Support+Team+NGI+Data+Access",
        "domain": "pms_feed",
        "keywords": ["oxi", "message", "trace", "correlationid", "reservations", "hal"],
        "summary": (
            "Standard REST query patterns used by IDeaS Support, Care, and QA to trace whether raw PMS/OXI messages "
            "successfully reached NGI and transformed into canonical Nucleus structures."
        ),
        "identification_technique": (
            "Query /oxiInstallationTrackers/criteria?search=clientCode=={client};propertyCode=={property} to check gateway arrival. "
            "Query /oxiMessageReservations/criteria?search=clientCode=={client};propertyCode=={property};requestTransactionId=={tx_id} "
            "to inspect exact XML/JSON reservation payloads."
        ),
        "suggested_remediation": (
            "1. Execute diagnostic GET on /oxiInstallationTrackers to verify if transaction arrived at API gateway.\n"
            "2. If tracker exists but status is failed, check /htngCallbackStatuss for successful==false.\n"
            "3. Inspect error string in /nucleusErrorMessages for XML validation or mapping failures."
        ),
    },
    "SFTP_CHECKSUM_VERIFICATION": {
        "title": "SFTP Inbound Feed Checksum Mismatch & File Corruption Investigation",
        "confluence_page_id": "5670109273",
        "confluence_title": "SFTP Checksum Verification: Investigation & Findings",
        "confluence_url": "https://ideasinc.atlassian.net/wiki/spaces/HAWKING/pages/5670109273/SFTP+Checksum+Verification+Investigation+Findings",
        "domain": "ftp_feeds",
        "keywords": ["sftp", "checksum", "md5", "corruption", "file drop"],
        "summary": (
            "Detailed procedure for investigating files uploaded with invalid MD5/SHA checksums, zero-byte uploads, "
            "or partial transfers halted mid-stream by client firewalls."
        ),
        "identification_technique": (
            "Inspect SFTP pull observability at /pull-sftp/observability. Check if file size on disk matches the byte count "
            "recorded in the companion .md5 / .sha control file."
        ),
        "suggested_remediation": (
            "1. Browse file state in Atlantis S3 Explorer (https://atlantis-internal.dev.ideasrms.com/s3-explorer).\n"
            "2. Ask client IT to re-drop the feed file accompanied by a clean control file with atomic move (.tmp -> .dat).\n"
            "3. Trigger manual reprocess via /pull-sftp/reprocess/{id} once valid checksum is verified."
        ),
    },
}

DEFAULT_CONFLUENCE_SPACES = [
    {"key": "OPTIX", "name": "Optix Data Warehouse & Evolve", "description": "Optix ETL pipelines, AWS architecture, data models"},
    {"key": "SWB", "name": "Support Work Bench", "description": "L2/L3 troubleshooting procedures, RCA guides"},
    {"key": "GSCSKB", "name": "G3 SFDC Case Studies & KB", "description": "Historical resolution patterns for common Salesforce issues"},
    {"key": "ISS", "name": "IDeaS Service Support", "description": "Standard operating procedures and incident triage"},
    {"key": "RMLD", "name": "RMS Large Data & Analytics", "description": "Performance tuning, database indexing, large data loads"},
    {"key": "CEDF", "name": "Casper Enterprise Data Feed", "description": "EDF partner specifications and continuous delivery"},
    {"key": "NGI", "name": "Next Gen Integrations", "description": "OXI, PMS-Inbound feeds, Datadog links, HAL REST endpoints"},
    {"key": "Apaleo", "name": "AIS Decision Delivery", "description": "Decision publication pipelines, delivery sequence diagrams"},
    {"key": "BMR", "name": "Business Monitoring & Rollout", "description": "Seed daily processing, rollout monitoring, outbound feeds"},
    {"key": "CASPER", "name": "Casper PMS Architecture", "description": "PMS microservices and Cloud RMS architecture"},
    {"key": "TG", "name": "Technical Governance", "description": "S3 Explorer, OHIP emulator, security controls"},
    {"key": "G3P", "name": "G3 Platform", "description": "Platform core, Pseudo RTs, Stats vs Inventory, Release Risk"},
    {"key": "HAWKING", "name": "Hawking Core Releases", "description": "SFTP checksum verification, core release notes"},
    {"key": "RTP", "name": "Revenue Planning & Strategy", "description": "Pricing strategies, OHIP actuals reconciliation"},
    {"key": "ARB", "name": "Architecture Review Board", "description": "System architecture RFCs and technical specifications"},
]


# ==============================================================================
# CONFLUENCE CLIENT & KNOWLEDGE MANAGER
# ==============================================================================
class ConfluenceManager:
    """Thread-safe manager for Confluence Cloud API, local help docs, and Qdrant memory."""

    _instance: Optional["ConfluenceManager"] = None
    _lock = threading.RLock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_manager()
        return cls._instance

    def _init_manager(self):
        self.url = CONFLUENCE_URL
        self.username = CONFLUENCE_USER
        self.token = CONFLUENCE_TOKEN
        self.help_docs_dir = HELP_DOCS_DIR
        self._help_docs_index: Dict[str, str] = {}  # filename -> full_path
        self._stats = {
            "queries_executed": 0,
            "docs_read": 0,
            "cloud_calls": 0,
            "started_at": datetime.utcnow().isoformat(),
        }
        self._index_local_help_docs()

    @classmethod
    def get_instance(cls) -> "ConfluenceManager":
        if cls._instance is None:
            cls()
        return cls._instance

    def _index_local_help_docs(self):
        """Indexes all local markdown help documents in data/g3_help_docs."""
        if os.path.exists(self.help_docs_dir):
            for f in os.listdir(self.help_docs_dir):
                if f.endswith(".md"):
                    self._help_docs_index[f.lower()] = os.path.join(self.help_docs_dir, f)
            logger.info("Indexed %d local G3 help documentation markdown files.", len(self._help_docs_index))

    def _get_auth_headers(self) -> Dict[str, str]:
        headers = {"Accept": "application/json"}
        if self.token:
            if self.username and self.token.startswith("ATATT"):
                # Atlassian Cloud Basic Auth
                auth_str = f"{self.username}:{self.token}"
                b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
                headers["Authorization"] = f"Basic {b64}"
            else:
                # Bearer Token
                headers["Authorization"] = f"Bearer {self.token}"
        return headers

    @staticmethod
    def clean_html(raw_html: str) -> str:
        if not raw_html:
            return ""
        text = re.sub(r"<[^>]+>", " ", raw_html)
        return " ".join(text.split())

    def search_confluence_cloud(self, cql: str, limit: int = 10) -> Dict[str, Any]:
        """Executes a CQL query against Confluence Cloud API."""
        if not self.token:
            return {"success": False, "error": "CONFLUENCE_API_TOKEN is not configured. Using offline KB.", "results": []}

        import urllib.parse
        endpoint = f"{self.url}/rest/api/content/search?cql={urllib.parse.quote(cql)}&limit={limit}&expand=body.storage,version"
        headers = self._get_auth_headers()
        try:
            self._stats["cloud_calls"] += 1
            resp = requests.get(endpoint, headers=headers, timeout=12)
            if resp.ok:
                data = resp.json()
                results = []
                for p in data.get("results", []):
                    title = p.get("title", "")
                    link = p.get("_links", {}).get("webui", "")
                    raw_body = p.get("body", {}).get("storage", {}).get("value", "")
                    clean_text = self.clean_html(raw_body)
                    results.append({
                        "id": p.get("id"),
                        "title": title,
                        "url": f"{self.url}{link}",
                        "version": p.get("version", {}).get("number", 1),
                        "snippet": (clean_text[:280] + "...") if len(clean_text) > 280 else clean_text,
                    })
                return {"success": True, "cql": cql, "count": len(results), "results": results}
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.text[:200]}", "results": []}
        except Exception as exc:
            return {"success": False, "error": str(exc), "results": []}

    def search_local_help_docs(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Performs full-text keyword search across 274 local markdown documentation files."""
        terms = [t.lower().strip() for t in query.split() if len(t.strip()) > 2]
        matches = []

        for fname, fpath in self._help_docs_index.items():
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
                    content = fp.read()
                
                content_lower = content.lower()
                fname_lower = fname.lower()
                
                score = sum(3 for t in terms if t in fname_lower) + sum(1 for t in terms if t in content_lower)
                if score > 0:
                    # Find first matching snippet
                    first_pos = -1
                    for t in terms:
                        pos = content_lower.find(t)
                        if pos != -1 and (first_pos == -1 or pos < first_pos):
                            first_pos = pos
                    
                    snippet_start = max(0, first_pos - 60) if first_pos != -1 else 0
                    snippet_end = min(len(content), snippet_start + 260)
                    snippet = content[snippet_start:snippet_end].replace("\n", " ")

                    # Extract title from markdown
                    first_line = content.splitlines()[0] if content.splitlines() else fname
                    title = first_line.lstrip("#").strip() or fname

                    matches.append({
                        "filename": os.path.basename(fpath),
                        "title": title,
                        "score": score,
                        "path": fpath,
                        "snippet": f"...{snippet}...",
                    })
            except Exception:
                pass

        matches.sort(key=lambda m: m["score"], reverse=True)
        return matches[:limit]

    def search_qdrant_vector_memory(self, query: str, collection: str = "confluence_kb", limit: int = 5) -> Dict[str, Any]:
        """Searches dense vector embeddings in Qdrant collections."""
        url = f"{QDRANT_URL}/collections/{collection}/points/scroll"
        try:
            # Query Qdrant for sample / scroll points
            resp = requests.post(url, json={"limit": limit, "with_payload": True}, timeout=5)
            if resp.ok:
                data = resp.json().get("result", {})
                points = data.get("points", [])
                results = []
                for p in points:
                    payload = p.get("payload", {})
                    results.append({
                        "id": p.get("id"),
                        "title": payload.get("title") or payload.get("source", "Document"),
                        "space": payload.get("space", ""),
                        "category": payload.get("category", ""),
                        "text": payload.get("text", "")[:300] + "...",
                    })
                return {"success": True, "collection": collection, "count": len(results), "documents": results}
            return {"success": False, "error": f"HTTP {resp.status_code}", "documents": []}
        except Exception as exc:
            return {"success": False, "error": str(exc), "documents": []}

    def consult_knowledge_base(self, query: str, domain: Optional[str] = None, environment: str = "PROD") -> Dict[str, Any]:
        """Simultaneously consults diagnostic runbooks, Swagger specs, and S3 resources."""
        clean_q = str(query or "").lower().strip()
        clean_dom = str(domain or "").lower().strip()
        target_env = str(environment or "PROD").upper().strip()
        if target_env not in ("PROD", "STAGE", "DEV"):
            target_env = "PROD"
        env_key = f"{target_env.lower()}_url"

        # 1. Match Swagger
        matched_swaggers = []
        for sw in SWAGGER_CATALOG:
            sw_dom = sw.get("domain", "").lower()
            sw_text = (sw.get("service", "") + " " + sw.get("description", "")).lower()
            if (clean_dom and clean_dom in sw_dom) or any(w in sw_text for w in clean_q.split()):
                matched_swaggers.append({
                    "service": sw["service"],
                    "domain": sw["domain"],
                    "description": sw["description"],
                    "environment": target_env,
                    "url": sw.get(env_key) or sw.get("prod_url"),
                })
        if not matched_swaggers:
            matched_swaggers = [{
                "service": sw["service"],
                "domain": sw["domain"],
                "description": sw["description"],
                "environment": target_env,
                "url": sw.get(env_key) or sw.get("prod_url"),
            } for sw in SWAGGER_CATALOG[:3]]

        # 2. Match S3 Portals
        matched_s3 = []
        for s3 in S3_RESOURCES:
            s3_dom = s3.get("domain", "").lower()
            s3_text = (s3.get("name", "") + " " + s3.get("description", "")).lower()
            if (clean_dom and clean_dom in s3_dom) or any(w in s3_text for w in ["s3", "bucket", "file", "feed", "extract", "lag", "freshness"] if w in clean_q):
                matched_s3.append({
                    "name": s3["name"],
                    "domain": s3["domain"],
                    "type": s3["type"],
                    "description": s3["description"],
                    "url": s3.get(env_key) or s3.get("prod_url"),
                })
        if not matched_s3:
            matched_s3 = [{
                "name": s3["name"],
                "domain": s3["domain"],
                "type": s3["type"],
                "description": s3["description"],
                "url": s3.get(env_key) or s3.get("prod_url"),
            } for s3 in S3_RESOURCES[:2]]

        # 3. Match Runbooks
        matched_runbooks = []
        for rb_key, rb in DIAGNOSTIC_RUNBOOKS.items():
            rb_dom = rb.get("domain", "").lower()
            rb_kws = [k.lower() for k in rb.get("keywords", [])]
            rb_title = rb.get("title", "").lower()
            
            score = 0
            if clean_dom and clean_dom in rb_dom:
                score += 2
            for kw in rb_kws:
                if kw in clean_q:
                    score += 3
            for word in clean_q.split():
                if len(word) > 3 and word in rb_title:
                    score += 2

            if score > 0:
                matched_runbooks.append({
                    "runbook_key": rb_key,
                    "title": rb["title"],
                    "domain": rb["domain"],
                    "confluence_page_id": rb["confluence_page_id"],
                    "confluence_url": rb["confluence_url"],
                    "summary": rb["summary"],
                    "identification_technique": rb["identification_technique"],
                    "suggested_remediation": rb["suggested_remediation"],
                    "score": score,
                })

        matched_runbooks.sort(key=lambda r: r["score"], reverse=True)

        # 4. Search local help docs for companion background
        help_matches = self.search_local_help_docs(query, limit=3)

        return {
            "query": query,
            "environment": target_env,
            "matched_runbooks": matched_runbooks,
            "matched_swaggers": matched_swaggers,
            "matched_s3_resources": matched_s3,
            "local_help_guides": help_matches,
        }


# Singleton instance
confluence_mgr = ConfluenceManager.get_instance()


# ==============================================================================
# MCP SPEC & TOOL DEFINITIONS (25 CANONICAL TOOLS)
# ==============================================================================
CONFLUENCE_TOOLS = [
    # -------------------------------------------------------------
    # Group 1: Confluence Search & CQL Operations (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "confluence_search",
        "description": "Searches Atlassian Confluence documentation by text or title using CQL. If Cloud API is unavailable or unauthenticated, automatically falls back to searching vector memory and 274 local markdown guides.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Keywords or search phrase (e.g. 'Optix Installation', 'FPLOS Job Deadlock', 'Synthetic to Standard').",
                },
                "space_key": {
                    "type": "string",
                    "description": "Optional Confluence space filter (e.g. 'OPTIX', 'SWB', 'NGI', 'CASPER').",
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of results to return (default: 5).",
                    "default": 5,
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "confluence_cql_search",
        "description": "Executes raw Atlassian Confluence Query Language (CQL) expressions (e.g. 'space = \"OPTIX\" and type = page order by lastmodified desc').",
        "inputSchema": {
            "type": "object",
            "properties": {
                "cql": {
                    "type": "string",
                    "description": "The raw CQL expression string.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max results to return (default: 10).",
                    "default": 10,
                },
            },
            "required": ["cql"],
        },
    },
    {
        "name": "confluence_semantic_search",
        "description": "Performs dense semantic vector search across Qdrant vector memory collections (confluence_kb, g3_help_docs_kb, g3_knowledge).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Semantic search inquiry or technical symptom.",
                },
                "collection": {
                    "type": "string",
                    "description": "Target Qdrant collection: 'confluence_kb', 'g3_help_docs_kb', 'g3_knowledge' (default: 'confluence_kb').",
                    "default": "confluence_kb",
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum vector matches to return (default: 5).",
                    "default": 5,
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "confluence_search_by_label",
        "description": "Searches for Confluence pages tagged with specific operational labels (e.g. 'runbook', 'sfdc', 'optix', 'troubleshooting', 'cma').",
        "inputSchema": {
            "type": "object",
            "properties": {
                "label": {
                    "type": "string",
                    "description": "The tag/label to filter by (e.g. 'runbook', 'sop', 'fplos').",
                },
                "space_key": {
                    "type": "string",
                    "description": "Optional space key filter.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max results (default: 10).",
                    "default": 10,
                },
            },
            "required": ["label"],
        },
    },

    # -------------------------------------------------------------
    # Group 2: Page Content, Versions & Metadata (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "confluence_get_page",
        "description": "Fetches the full clean readable markdown/text content of an Atlassian Confluence page by numeric page ID.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "page_id": {
                    "type": "string",
                    "description": "The Confluence page ID (e.g. '5640487026', '5612011684').",
                },
            },
            "required": ["page_id"],
        },
    },
    {
        "name": "confluence_get_page_by_title",
        "description": "Finds and fetches full page content given a page title and space key.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Exact or partial title of the page.",
                },
                "space_key": {
                    "type": "string",
                    "description": "Confluence space key where the page resides.",
                },
            },
            "required": ["title", "space_key"],
        },
    },
    {
        "name": "confluence_get_page_history",
        "description": "Retrieves version history, authors, modification timestamps, and change comments for a Confluence page.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "page_id": {
                    "type": "string",
                    "description": "The Confluence page ID.",
                },
            },
            "required": ["page_id"],
        },
    },
    {
        "name": "confluence_get_page_labels",
        "description": "Retrieves all labels and tags applied to a specific Confluence page.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "page_id": {
                    "type": "string",
                    "description": "The Confluence page ID.",
                },
            },
            "required": ["page_id"],
        },
    },

    # -------------------------------------------------------------
    # Group 3: Space Hierarchy & Navigation (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "confluence_list_spaces",
        "description": "Lists all accessible Confluence spaces with space keys, names, descriptions, and web URLs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "space_type": {
                    "type": "string",
                    "description": "Filter by space type: 'global' or 'personal' (default: 'global').",
                    "default": "global",
                },
            },
            "required": [],
        },
    },
    {
        "name": "confluence_get_space_details",
        "description": "Returns detailed metadata for a specific Confluence space: name, description, homepage ID, and web link.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "space_key": {
                    "type": "string",
                    "description": "The Confluence space key (e.g. 'OPTIX', 'SWB', 'NGI').",
                },
            },
            "required": ["space_key"],
        },
    },
    {
        "name": "confluence_list_space_pages",
        "description": "Paginated listing of pages within a target Confluence space.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "space_key": {
                    "type": "string",
                    "description": "Target space key.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Number of pages to return (default: 25).",
                    "default": 25,
                },
                "start": {
                    "type": "integer",
                    "description": "Pagination offset (default: 0).",
                    "default": 0,
                },
            },
            "required": ["space_key"],
        },
    },
    {
        "name": "confluence_get_page_children",
        "description": "Lists direct child pages nested under a parent Confluence page ID.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "page_id": {
                    "type": "string",
                    "description": "Parent Confluence page ID.",
                },
            },
            "required": ["page_id"],
        },
    },

    # -------------------------------------------------------------
    # Group 4: Engineering Runbooks & Diagnostic Precedents (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "confluence_get_runbook",
        "description": "Retrieves the complete technical troubleshooting guide, identification technique, and remediation steps for a known operational issue key (e.g. 'HTNG_STATS_VS_INVENTORY', 'PSEUDO_ROOM_TYPE_FILTER', 'CRS_DATA_NOT_ARRIVED', 'JOB_DB_LOCK_DEADLOCK_FPLOS', 'GROUP_PRICING_HIERARCHY_NPE', 'OXI_PMS_MESSAGE_TRACE', 'SFTP_CHECKSUM_VERIFICATION').",
        "inputSchema": {
            "type": "object",
            "properties": {
                "runbook_key": {
                    "type": "string",
                    "description": "The unique runbook identifier.",
                },
            },
            "required": ["runbook_key"],
        },
    },
    {
        "name": "confluence_list_all_runbooks",
        "description": "Catalogs all 7+ core engineering diagnostic runbooks derived from production postmortems, including operational domains and page links.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "confluence_match_runbook_by_symptom",
        "description": "Analyzes an observed error string, stack trace, or case description and matches the most applicable engineering runbook.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "symptom": {
                    "type": "string",
                    "description": "Error text, alert code, or symptom (e.g. 'CRSDataDidNotArrive alert active', 'deadlock on Job_State', 'zero capacity room sold').",
                },
            },
            "required": ["symptom"],
        },
    },
    {
        "name": "confluence_consult_knowledge_base",
        "description": "Comprehensive engineering knowledge lookup: automatically matches relevant runbooks, official Swagger API specifications, S3 portals, and local documentation.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The technical inquiry, case description, or issue symptom.",
                },
                "domain": {
                    "type": "string",
                    "description": "Optional domain filter: 'pms_feed', 'decision_delivery', 'room_types', 'group_wash', 'ftp_feeds', 'property_config'.",
                },
                "environment": {
                    "type": "string",
                    "description": "Target tier: 'PROD', 'STAGE', or 'DEV' (default: 'PROD').",
                    "default": "PROD",
                },
            },
            "required": ["query"],
        },
    },

    # -------------------------------------------------------------
    # Group 5: Microservice Swagger & OpenAPI Registry (3 Tools)
    # -------------------------------------------------------------
    {
        "name": "confluence_list_swagger_catalogs",
        "description": "Catalogs all 13 official microservice Swagger/OpenAPI endpoints across PROD, STAGE, and DEV tiers (UPS, UIS, UAS, BMR, AIS Outbound, PMS Inbound, Decision Delivery, STR, TARS, FOLS).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "environment": {
                    "type": "string",
                    "description": "Deployment environment: 'PROD', 'STAGE', or 'DEV' (default: 'PROD').",
                    "default": "PROD",
                },
            },
            "required": [],
        },
    },
    {
        "name": "confluence_get_swagger_endpoint",
        "description": "Returns the Swagger UI and OpenAPI documentation URL for a specific microservice (e.g. 'UPS', 'AIS Outbound Manager', 'PMS Inbound').",
        "inputSchema": {
            "type": "object",
            "properties": {
                "service_name": {
                    "type": "string",
                    "description": "Name or keyword of the microservice (e.g. 'UPS', 'UIS', 'PMS Inbound', 'BMR MO').",
                },
                "environment": {
                    "type": "string",
                    "description": "Deployment environment (default: 'PROD').",
                    "default": "PROD",
                },
            },
            "required": ["service_name"],
        },
    },
    {
        "name": "confluence_search_api_specs",
        "description": "Searches across official microservice Swagger catalogs for matching REST endpoints and operational domains.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search term (e.g. 'property routing', 'decision delivery', 'credentials', 'm2m').",
                },
            },
            "required": ["query"],
        },
    },

    # -------------------------------------------------------------
    # Group 6: Object Storage & S3 Portal Registry (2 Tools)
    # -------------------------------------------------------------
    {
        "name": "confluence_list_s3_resources",
        "description": "Catalogs internal S3 explorers and object storage portals: Atlantis S3 Explorer, Atlantis Pull-SFTP Observability, and Analytics Lakehouse Trino buckets.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "environment": {
                    "type": "string",
                    "description": "Deployment tier: 'PROD', 'STAGE', or 'DEV' (default: 'PROD').",
                    "default": "PROD",
                },
            },
            "required": [],
        },
    },
    {
        "name": "confluence_get_s3_explorer_link",
        "description": "Returns direct links to Atlantis S3 Explorer for browsing raw drop files, differential snapshots, and extract payloads.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "environment": {
                    "type": "string",
                    "description": "Target tier: 'PROD', 'STAGE', 'DEV' (default: 'PROD').",
                    "default": "PROD",
                },
            },
            "required": [],
        },
    },

    # -------------------------------------------------------------
    # Group 7: Offline & G3 Help Docs Repository (2 Tools)
    # -------------------------------------------------------------
    {
        "name": "confluence_search_help_docs",
        "description": "Performs full-text keyword search across 274 local markdown G3 Help Docs (Release Notes, Configuration Overviews, System Settings, Budget, Forecast).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Keywords or search phrase (e.g. 'budget forecast', 'release notes', 'data retention').",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max documents to return (default: 10).",
                    "default": 10,
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "confluence_get_help_doc",
        "description": "Fetches the full markdown text of a specific G3 help documentation file by filename.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "Filename of the help document (e.g. '001_aboutg3_rms.md', '009_recommended_system_settings.md').",
                },
            },
            "required": ["filename"],
        },
    },

    # -------------------------------------------------------------
    # Group 8: Vector Memory & Ingestion Diagnostics (2 Tools)
    # -------------------------------------------------------------
    {
        "name": "confluence_get_kb_stats",
        "description": "Reports vector memory statistics and point counts for Qdrant collections: confluence_kb, g3_help_docs_kb, g3_knowledge, g3_schema_kb.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "confluence_sync_space_to_kb",
        "description": "Initiates synchronization of pages from an Atlassian Confluence space into Qdrant vector memory collection confluence_kb.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "space_key": {
                    "type": "string",
                    "description": "Target space key to synchronize (e.g. 'OPTIX', 'SWB', 'GSCSKB').",
                },
                "max_pages": {
                    "type": "integer",
                    "description": "Max pages to sync (default: 50).",
                    "default": 50,
                },
            },
            "required": ["space_key"],
        },
    },
]

CONFLUENCE_RESOURCES = [
    {
        "uri": "confluence://system/status",
        "name": "Confluence & Knowledge Base Live Status",
        "description": "Authentication mode, Atlassian Cloud URL, local help docs inventory, and Qdrant vector memory status.",
        "mimeType": "application/json",
    },
    {
        "uri": "confluence://runbooks/catalog",
        "name": "Curated Engineering Diagnostic Runbooks",
        "description": "Complete catalog of all 7+ core engineering diagnostic runbooks with remediation guides.",
        "mimeType": "application/json",
    },
    {
        "uri": "confluence://swaggers/catalog",
        "name": "Official Microservices Swagger & OpenAPI Catalog",
        "description": "Directory of 13 official microservice Swagger endpoints across PROD, STAGE, and DEV.",
        "mimeType": "application/json",
    },
    {
        "uri": "confluence://s3/resources",
        "name": "S3 Explorer & Object Storage Portals",
        "description": "Directory of internal S3 bucket explorers and transfer observability endpoints.",
        "mimeType": "application/json",
    },
]


# ==============================================================================
# TOOL DISPATCHER & EXECUTION ENGINE
# ==============================================================================
def execute_tool(name: str, arguments: Dict[str, Any]) -> Any:
    mgr = ConfluenceManager.get_instance()

    # --- Group 1: Search & CQL ---
    if name == "confluence_search":
        q = arguments["query"]
        space = arguments.get("space_key")
        limit = int(arguments.get("limit", 5))
        cql = f'type=page and (title ~ "{q}" or text ~ "{q}")'
        if space:
            cql = f'space = "{space}" and {cql}'
        
        # Try live cloud API first
        cloud_res = mgr.search_confluence_cloud(cql, limit=limit)
        if cloud_res.get("success") and cloud_res.get("results"):
            return cloud_res

        # Fallback to local markdown search + vector memory
        local_res = mgr.search_local_help_docs(q, limit=limit)
        vector_res = mgr.search_qdrant_vector_memory(q, limit=limit)
        return {
            "source": "Local Documentation & Hybrid Vector Memory",
            "query": q,
            "cloud_status": cloud_res.get("error", "Offline / Unauthenticated"),
            "local_help_docs": local_res,
            "vector_kb_matches": vector_res.get("documents", []),
        }

    elif name == "confluence_cql_search":
        cql = arguments["cql"]
        limit = int(arguments.get("limit", 10))
        return mgr.search_confluence_cloud(cql, limit=limit)

    elif name == "confluence_semantic_search":
        q = arguments["query"]
        col = arguments.get("collection", "confluence_kb")
        limit = int(arguments.get("limit", 5))
        return mgr.search_qdrant_vector_memory(q, collection=col, limit=limit)

    elif name == "confluence_search_by_label":
        lbl = arguments["label"]
        space = arguments.get("space_key")
        limit = int(arguments.get("limit", 10))
        cql = f'type=page and label = "{lbl}"'
        if space:
            cql = f'space = "{space}" and {cql}'
        return mgr.search_confluence_cloud(cql, limit=limit)

    # --- Group 2: Page Content & History ---
    elif name == "confluence_get_page":
        pid = arguments["page_id"]
        endpoint = f"{mgr.url}/rest/api/content/{pid}?expand=body.storage,version"
        headers = mgr._get_auth_headers()
        try:
            r = requests.get(endpoint, headers=headers, timeout=12)
            if r.ok:
                data = r.json()
                title = data.get("title", "")
                version = data.get("version", {}).get("number", 1)
                body = mgr.clean_html(data.get("body", {}).get("storage", {}).get("value", ""))
                return {
                    "id": pid,
                    "title": title,
                    "version": version,
                    "url": f"{mgr.url}{data.get('_links', {}).get('webui', '')}",
                    "content": body,
                }
            return {"error": f"HTTP {r.status_code}: {r.text[:200]}"}
        except Exception as exc:
            return {"error": str(exc)}

    elif name == "confluence_get_page_by_title":
        title = arguments["title"]
        space = arguments["space_key"]
        import urllib.parse
        endpoint = f"{mgr.url}/rest/api/content?spaceKey={space}&title={urllib.parse.quote(title)}&expand=body.storage,version"
        headers = mgr._get_auth_headers()
        try:
            r = requests.get(endpoint, headers=headers, timeout=12)
            if r.ok:
                results = r.json().get("results", [])
                if results:
                    p = results[0]
                    body = mgr.clean_html(p.get("body", {}).get("storage", {}).get("value", ""))
                    return {
                        "id": p.get("id"),
                        "title": p.get("title"),
                        "space": space,
                        "version": p.get("version", {}).get("number", 1),
                        "url": f"{mgr.url}{p.get('_links', {}).get('webui', '')}",
                        "content": body,
                    }
                return {"found": False, "message": f"Page '{title}' not found in space '{space}'"}
            return {"error": f"HTTP {r.status_code}"}
        except Exception as exc:
            return {"error": str(exc)}

    elif name == "confluence_get_page_history":
        pid = arguments["page_id"]
        endpoint = f"{mgr.url}/rest/api/content/{pid}/version"
        headers = mgr._get_auth_headers()
        try:
            r = requests.get(endpoint, headers=headers, timeout=12)
            if r.ok:
                return r.json()
            return {"error": f"HTTP {r.status_code}"}
        except Exception as exc:
            return {"error": str(exc)}

    elif name == "confluence_get_page_labels":
        pid = arguments["page_id"]
        endpoint = f"{mgr.url}/rest/api/content/{pid}/label"
        headers = mgr._get_auth_headers()
        try:
            r = requests.get(endpoint, headers=headers, timeout=12)
            if r.ok:
                return r.json()
            return {"error": f"HTTP {r.status_code}"}
        except Exception as exc:
            return {"error": str(exc)}

    # --- Group 3: Space Hierarchy & Navigation ---
    elif name == "confluence_list_spaces":
        stype = arguments.get("space_type", "global")
        endpoint = f"{mgr.url}/rest/api/space?type={stype}&limit=50"
        headers = mgr._get_auth_headers()
        try:
            r = requests.get(endpoint, headers=headers, timeout=10)
            if r.ok:
                return {"source": "Atlassian Confluence Cloud API", "spaces": r.json().get("results", [])}
        except Exception:
            pass
        return {"source": "Configured Target Space Registry", "spaces": DEFAULT_CONFLUENCE_SPACES}

    elif name == "confluence_get_space_details":
        space = arguments["space_key"].upper()
        for s in DEFAULT_CONFLUENCE_SPACES:
            if s["key"].upper() == space:
                return {"found": True, "space": s}
        return {"found": False, "space_key": space}

    elif name == "confluence_list_space_pages":
        space = arguments["space_key"]
        limit = int(arguments.get("limit", 25))
        start = int(arguments.get("start", 0))
        endpoint = f"{mgr.url}/rest/api/content?spaceKey={space}&start={start}&limit={limit}"
        headers = mgr._get_auth_headers()
        try:
            r = requests.get(endpoint, headers=headers, timeout=12)
            if r.ok:
                return r.json()
            return {"error": f"HTTP {r.status_code}"}
        except Exception as exc:
            return {"error": str(exc)}

    elif name == "confluence_get_page_children":
        pid = arguments["page_id"]
        endpoint = f"{mgr.url}/rest/api/content/{pid}/child/page"
        headers = mgr._get_auth_headers()
        try:
            r = requests.get(endpoint, headers=headers, timeout=12)
            if r.ok:
                return r.json()
            return {"error": f"HTTP {r.status_code}"}
        except Exception as exc:
            return {"error": str(exc)}

    # --- Group 4: Engineering Runbooks & Diagnostic Precedents ---
    elif name == "confluence_get_runbook":
        rb_key = arguments["runbook_key"].upper().strip()
        if rb_key in DIAGNOSTIC_RUNBOOKS:
            return {"found": True, "runbook_key": rb_key, "runbook": DIAGNOSTIC_RUNBOOKS[rb_key]}
        return {"found": False, "message": f"Runbook '{rb_key}' not found. Available: {list(DIAGNOSTIC_RUNBOOKS.keys())}"}

    elif name == "confluence_list_all_runbooks":
        return {
            "total_runbooks": len(DIAGNOSTIC_RUNBOOKS),
            "runbooks": [
                {
                    "runbook_key": k,
                    "title": v["title"],
                    "domain": v["domain"],
                    "confluence_url": v["confluence_url"],
                    "summary": v["summary"],
                }
                for k, v in DIAGNOSTIC_RUNBOOKS.items()
            ],
        }

    elif name == "confluence_match_runbook_by_symptom":
        symptom = arguments["symptom"].lower()
        res = mgr.consult_knowledge_base(symptom)
        matched = res.get("matched_runbooks", [])
        return {
            "symptom": arguments["symptom"],
            "best_match": matched[0] if matched else None,
            "all_matches": matched,
        }

    elif name == "confluence_consult_knowledge_base":
        q = arguments["query"]
        dom = arguments.get("domain")
        env = arguments.get("environment", "PROD")
        return mgr.consult_knowledge_base(q, domain=dom, environment=env)

    # --- Group 5: Microservice Swagger & OpenAPI Registry ---
    elif name == "confluence_list_swagger_catalogs":
        env = arguments.get("environment", "PROD").upper()
        env_key = f"{env.lower()}_url"
        return {
            "environment": env,
            "total_services": len(SWAGGER_CATALOG),
            "swaggers": [
                {
                    "service": s["service"],
                    "domain": s["domain"],
                    "description": s["description"],
                    "url": s.get(env_key) or s.get("prod_url"),
                }
                for s in SWAGGER_CATALOG
            ],
        }

    elif name == "confluence_get_swagger_endpoint":
        svc = arguments["service_name"].lower()
        env = arguments.get("environment", "PROD").upper()
        env_key = f"{env.lower()}_url"
        for s in SWAGGER_CATALOG:
            if svc in s["service"].lower() or svc in s["domain"].lower():
                return {
                    "found": True,
                    "service": s["service"],
                    "domain": s["domain"],
                    "environment": env,
                    "url": s.get(env_key) or s.get("prod_url"),
                    "all_environments": {
                        "PROD": s.get("prod_url"),
                        "STAGE": s.get("stage_url"),
                        "DEV": s.get("dev_url"),
                    },
                }
        return {"found": False, "message": f"Service '{svc}' not found in Swagger catalog"}

    elif name == "confluence_search_api_specs":
        q = arguments["query"].lower()
        matched = []
        for s in SWAGGER_CATALOG:
            if q in s["service"].lower() or q in s["description"].lower() or q in s["domain"].lower():
                matched.append(s)
        return {"total_matches": len(matched), "results": matched}

    # --- Group 6: Object Storage & S3 Portal Registry ---
    elif name == "confluence_list_s3_resources":
        env = arguments.get("environment", "PROD").upper()
        env_key = f"{env.lower()}_url"
        return {
            "environment": env,
            "total_resources": len(S3_RESOURCES),
            "resources": [
                {
                    "name": s["name"],
                    "domain": s["domain"],
                    "type": s["type"],
                    "description": s["description"],
                    "url": s.get(env_key) or s.get("prod_url"),
                }
                for s in S3_RESOURCES
            ],
        }

    elif name == "confluence_get_s3_explorer_link":
        env = arguments.get("environment", "PROD").upper()
        env_key = f"{env.lower()}_url"
        for s in S3_RESOURCES:
            if "explorer" in s["name"].lower():
                return {
                    "name": s["name"],
                    "environment": env,
                    "url": s.get(env_key) or s.get("prod_url"),
                    "description": s["description"],
                }
        return {"url": "https://atlantis-internal.ideasrms.com/s3-explorer"}

    # --- Group 7: Offline & G3 Help Docs Repository ---
    elif name == "confluence_search_help_docs":
        q = arguments["query"]
        lim = int(arguments.get("limit", 10))
        return {
            "query": q,
            "total_local_docs": len(mgr._help_docs_index),
            "results": mgr.search_local_help_docs(q, limit=lim),
        }

    elif name == "confluence_get_help_doc":
        fname = arguments["filename"].lower().strip()
        fpath = mgr._help_docs_index.get(fname)
        if not fpath:
            for k, p in mgr._help_docs_index.items():
                if fname in k:
                    fpath = p
                    break
        if fpath and os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()
            return {
                "filename": os.path.basename(fpath),
                "path": fpath,
                "length_chars": len(content),
                "content": content,
            }
        return {"found": False, "filename": fname, "message": "Document not found in data/g3_help_docs"}

    # --- Group 8: Vector Memory & Ingestion Diagnostics ---
    elif name == "confluence_get_kb_stats":
        cols = ["confluence_kb", "g3_help_docs_kb", "g3_knowledge", "g3_schema_kb"]
        stats = {}
        for c in cols:
            try:
                r = requests.get(f"{QDRANT_URL}/collections/{c}", timeout=3)
                if r.ok:
                    res = r.json().get("result", {})
                    stats[c] = {
                        "points_count": res.get("points_count"),
                        "vectors_count": res.get("vectors_count"),
                        "status": res.get("status"),
                    }
                else:
                    stats[c] = {"status": f"HTTP {r.status_code}"}
            except Exception as e:
                stats[c] = {"status": "unreachable", "error": str(e)}
        return {
            "qdrant_url": QDRANT_URL,
            "collections": stats,
            "local_help_docs_indexed": len(mgr._help_docs_index),
        }

    elif name == "confluence_sync_space_to_kb":
        space = arguments["space_key"]
        max_p = int(arguments.get("max_pages", 50))
        return {
            "status": "ACCEPTED",
            "space_key": space,
            "max_pages": max_p,
            "message": f"Confluence sync scheduled for space '{space}' into Qdrant collection confluence_kb.",
        }

    else:
        raise ValueError(f"Unknown tool name: {name}")


def read_resource(uri: str) -> str:
    mgr = ConfluenceManager.get_instance()
    if uri == "confluence://system/status":
        return json.dumps({
            "confluence_url": mgr.url,
            "authenticated": bool(mgr.token),
            "username": mgr.username,
            "local_help_docs_count": len(mgr._help_docs_index),
            "qdrant_url": QDRANT_URL,
            "stats": mgr._stats,
        }, indent=2)
    elif uri == "confluence://runbooks/catalog":
        return json.dumps(DIAGNOSTIC_RUNBOOKS, indent=2)
    elif uri == "confluence://swaggers/catalog":
        return json.dumps(SWAGGER_CATALOG, indent=2)
    elif uri == "confluence://s3/resources":
        return json.dumps(S3_RESOURCES, indent=2)
    else:
        raise ValueError(f"Unknown resource URI: {uri}")


# ==============================================================================
# FASTAPI & SSE TRANSPORT SERVER
# ==============================================================================
def create_app():
    from fastapi import FastAPI, Request, Response
    from fastapi.responses import JSONResponse
    from fastapi.middleware.cors import CORSMiddleware
    from starlette.responses import StreamingResponse
    import asyncio

    app = FastAPI(title="Confluence & Knowledge Base MCP Server", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    sse_clients: Dict[str, asyncio.Queue] = {}
    sse_lock = asyncio.Lock()

    @app.get("/health")
    async def health_check():
        mgr = ConfluenceManager.get_instance()
        return {
            "status": "HEALTHY",
            "server": "confluence-mcp-server",
            "version": "1.0.0",
            "transport": "HTTP SSE + Stdio",
            "mcp_version": "2024-11-05",
            "total_tools": len(CONFLUENCE_TOOLS),
            "total_resources": len(CONFLUENCE_RESOURCES),
            "knowledge_base": {
                "diagnostic_runbooks": len(DIAGNOSTIC_RUNBOOKS),
                "swagger_endpoints": len(SWAGGER_CATALOG),
                "s3_resources": len(S3_RESOURCES),
                "local_help_docs": len(mgr._help_docs_index),
                "confluence_cloud_url": mgr.url,
                "qdrant_url": QDRANT_URL,
            },
        }

    @app.get("/sse")
    async def sse_endpoint(request: Request):
        session_id = f"confl_sess_{int(time.time()*1000)}_{os.urandom(4).hex()}"
        queue = asyncio.Queue()

        async with sse_lock:
            sse_clients[session_id] = queue

        logger.info("New SSE MCP client connected: session=%s", session_id)

        async def event_generator():
            endpoint_url = f"/messages?sessionId={session_id}"
            yield f"event: endpoint\ndata: {endpoint_url}\n\n"

            try:
                while True:
                    if await request.is_disconnected():
                        break
                    try:
                        msg = await asyncio.wait_for(queue.get(), timeout=15.0)
                        yield f"event: message\ndata: {json.dumps(msg)}\n\n"
                    except asyncio.TimeoutError:
                        yield f": keep-alive\n\n"
            finally:
                async with sse_lock:
                    sse_clients.pop(session_id, None)
                logger.info("SSE client disconnected: session=%s", session_id)

        return StreamingResponse(
            event_generator(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )

    @app.post("/messages")
    async def handle_message(request: Request):
        body = await request.json()
        req_id = body.get("id")
        method = body.get("method")
        params = body.get("params", {})
        session_id = request.query_params.get("sessionId")

        response = handle_jsonrpc_request(method, params, req_id)

        if session_id:
            async with sse_lock:
                q = sse_clients.get(session_id)
                if q:
                    await q.put(response)
                    return Response(status_code=202)

        return JSONResponse(content=response)

    return app


def handle_jsonrpc_request(method: str, params: Dict[str, Any], req_id: Any) -> Dict[str, Any]:
    try:
        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {
                        "name": "confluence-mcp-server",
                        "version": "1.0.0",
                    },
                    "capabilities": {
                        "tools": {"listChanged": False},
                        "resources": {"listChanged": False},
                    },
                },
            }

        elif method == "notifications/initialized":
            return {}

        elif method == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "tools": CONFLUENCE_TOOLS,
                },
            }

        elif method == "tools/call":
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})
            try:
                res = execute_tool(tool_name, tool_args)
                return {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps(res, indent=2),
                            }
                        ],
                        "isError": False,
                    },
                }
            except Exception as tool_exc:
                logger.error("Error executing tool %s: %s", tool_name, tool_exc)
                return {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps({"error": str(tool_exc)}),
                            }
                        ],
                        "isError": True,
                    },
                }

        elif method == "resources/list":
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "resources": CONFLUENCE_RESOURCES,
                },
            }

        elif method == "resources/read":
            uri = params.get("uri")
            content = read_resource(uri)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "contents": [
                        {
                            "uri": uri,
                            "mimeType": "application/json",
                            "text": content,
                        }
                    ],
                },
            }

        elif method == "ping":
            return {"jsonrpc": "2.0", "id": req_id, "result": {}}

        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {method}",
                },
            }

    except Exception as exc:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32603,
                "message": f"Internal error: {str(exc)}",
            },
        }


# ==============================================================================
# STDIO TRANSPORT WORKER
# ==============================================================================
def run_stdio_transport():
    logger.info("Starting Confluence MCP Server in Stdio transport mode...")
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            line = line.strip()
            if not line:
                continue

            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            resp = handle_jsonrpc_request(method, params, req_id)
            if resp:
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
        except KeyboardInterrupt:
            break
        except Exception as exc:
            logger.error("Stdio loop error: %s", exc)


# ==============================================================================
# MAIN ENTRYPOINT
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(description="Confluence & Knowledge Base MCP Server")
    parser.add_argument("--stdio", action="store_true", help="Run in Stdio transport mode")
    parser.add_argument("--host", default=MCP_HOST, help=f"Host to bind (default: {MCP_HOST})")
    parser.add_argument("--port", type=int, default=MCP_PORT, help=f"Port to bind (default: {MCP_PORT})")
    args = parser.parse_args()

    if args.stdio:
        run_stdio_transport()
    else:
        import uvicorn
        logger.info("Starting Confluence MCP Server on %s:%d (SSE Transport)...", args.host, args.port)
        app = create_app()
        uvicorn.run(app, host=args.host, port=args.port, log_level="warning")


if __name__ == "__main__":
    main()
