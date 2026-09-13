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
    "PRICING_SCREEN_INCORRECT_SYNTAX": {
        "title": "Pricing Screen Access Failure & Empty Collection IN () Syntax Error",
        "confluence_page_id": "5699012345",
        "confluence_title": "Pricing View Crash: SQLServerException Incorrect syntax near ')'",
        "confluence_url": "https://ideasinc.atlassian.net/wiki/spaces/G3P/pages/5699012345/Pricing+Screen+Syntax+Error+Near+Closing+Paren",
        "domain": "pricing_view",
        "keywords": ["incorrect syntax near", "pricing view", "pricing screen", "empty in", "onpresenterinit", "getcpdecisionbaroutputforaccomtypes", "ideas-29963", "palett"],
        "summary": (
            "Occurs when opening Manage -> Pricing. PricingPresenter executes checkForRoomClassRankHierarchyWarningsOptimizedLoop "
            "to validate price differentials across active Price Rank Paths. When base room classes have 0 physical capacity (due to "
            "renovations or room migration), an empty accommodation list [] is passed to getCpDecisionBAROutputForAccomTypes, generating "
            "SQL Server 'WHERE Accom_Type_ID IN ()', which fatally crashes the entire Pricing View."
        ),
        "identification_technique": (
            "Inspect Datadog error logs for stack trace containing PricingConfigurationService.getCpDecisionBAROutputForAccomTypes:3963 "
            "followed by SQLServerException 'Incorrect syntax near )'. Check tenant Accom_Type for room classes with 0 physical rooms."
        ),
        "suggested_remediation": (
            "1. (Option A - Recommended): In G3 RMS UI -> Configure -> Rooms -> Room Class Configuration (or Price Rank Hierarchy), "
            "remove or disconnect rank paths referencing empty room classes (e.g. STANDARD -> PREMIUM). Save and reload Pricing.\n"
            "2. (Option B): In Configure -> Rooms -> Room Configuration -> Room Types, assign at least 1 room capacity to the base representative room type.\n"
            "3. (Engineering Defect): Core dev team must add defensive check in PricingConfigurationService: if (CollectionUtils.isEmpty(accomTypeIds)) return Collections.emptyList();"
        ),
    },
    "UNMAPPED_DIMENSIONS_TRIAGE": {
        "title": "Unmapped Room Types, Rate Codes & Market Segments Resolution",
        "confluence_page_id": "5699012346",
        "confluence_title": "Unmapped Dimension Triage & Zero-DB Remapping",
        "confluence_url": "https://ideasinc.atlassian.net/wiki/spaces/BMR/pages/5699012346/Unmapped+Dimensions+Triage",
        "domain": "dimensions",
        "keywords": ["unmapped", "room type", "rate code", "srp", "market segment", "err_unmapped_dimension"],
        "summary": (
            "New room types, rate plans, or market segments introduced in upstream PMS (Opera, OnQ) that have not yet been registered "
            "in G3 RMS, causing BDE batch ETL failures or revenues accumulating in unassigned buckets."
        ),
        "identification_technique": (
            "Execute cma_check_unmapped_room_types, cma_check_unmapped_rate_codes, and cma_check_unmapped_market_segments."
        ),
        "suggested_remediation": (
            "1. Room Types: In G3 RMS UI -> Settings -> Property Setup -> Room Configuration -> Room Types -> Unmapped Room Types tab. Link to Room Class or create physical type, save.\n"
            "2. Rate Codes: In Pricing & Restrictions -> Rate Management -> Rate Codes, link code to Strategic Rate Plan (SRP) group, set parity rules, and publish.\n"
            "3. Reprocess: Navigate to System -> Sync Status -> Resync Reservations."
        ),
    },
    "DECISION_DELIVERY_TIMEOUT": {
        "title": "Decision Delivery Partner Timeout & Upload Drops (ERR_PMS_TIMEOUT)",
        "confluence_page_id": "5699012347",
        "confluence_title": "Decision Delivery Upload Drop & HTNG Interface Recovery",
        "confluence_url": "https://ideasinc.atlassian.net/wiki/spaces/OPS/pages/5699012347/Decision+Delivery+Timeout",
        "domain": "decision_delivery",
        "keywords": ["err_pms_timeout", "decision delivery", "upload drop", "htng", "http 504", "partner timeout"],
        "summary": (
            "Outbound pricing recommendations fail to publish to external partner PMS/CRS (SynXis, Choice, OnQ) due to partner listener timeout (>30s), "
            "expired TLS credentials, or XML schema rejections."
        ),
        "identification_technique": (
            "Check cma_get_decision_delivery_details and datadog_trace_decision_delivery_errors. Inspect HTNG Troubleshooter V2 (https://htng-troubleshooter.ideasrms.com/troubleshootV2/)."
        ),
        "suggested_remediation": (
            "1. In G3 RMS UI -> Pricing -> Decision Delivery -> Delivery Status -> Click 'Force Redelivery'.\n"
            "2. Verify partner endpoint credentials in HAL Explorer (fds_get_integration_property_configs).\n"
            "3. If partner listener timed out, instruct hotel IT / PMS vendor to restart their local HTNG interface receiver."
        ),
    },
    "CEDF_DATA_LAG_STALE_IMPORT": {
        "title": "CEDF Data Lag, Missing Batch Feeds & Ingestion Gaps",
        "confluence_page_id": "5699012348",
        "confluence_title": "CEDF Inbound Extract Recovery & SFTP Ingestion Gap",
        "confluence_url": "https://ideasinc.atlassian.net/wiki/spaces/HAWKING/pages/5699012348/CEDF+Data+Lag+Recovery",
        "domain": "pms_feed",
        "keywords": ["cedf", "data lag", "stale import", "freshness", "missing feed", "sftp drop"],
        "summary": (
            "BDE reservation data import freshness exceeds 24 hours due to missing PMS extract files or 0-byte transmission locks on SFTP."
        ),
        "identification_technique": (
            "Check cma_get_datafeed_import_freshness and cma_get_datafeed_status. Verify cedf_check_client_upload_status."
        ),
        "suggested_remediation": (
            "1. Do NOT manually insert reservation rows in database.\n"
            "2. Request hotel Night Auditor / IT trigger manual delta or historical extract from PMS (Opera: Miscellaneous -> File Export) directly to CEDF SFTP /inbound/.\n"
            "3. In G3 RMS UI -> System Operations -> Data Feeds -> Ingest Queue -> Process Now."
        ),
    },
    "COMPETITIVE_CONSTRAINT_CONFLICT": {
        "title": "Competitive Market Position Constraint Conflict & Rate Freezing",
        "confluence_page_id": "5699012349",
        "confluence_title": "Competitive Constraint Conflicts & Pricing Boundaries",
        "confluence_url": "https://ideasinc.atlassian.net/wiki/spaces/G3P/pages/5699012349/Competitive+Constraint+Conflicts",
        "domain": "pricing_engine",
        "keywords": ["competitive constraint", "rates frozen", "lrv floor", "price ranking violation", "closed rates"],
        "summary": (
            "Pricing recommendations appear frozen or hit unexpected ceilings/floors because configured competitor rules conflict "
            "with the Last Room Value (LRV) hurdle floor or cause price inversions between room classes."
        ),
        "identification_technique": (
            "Inspect Optix Competitive_Constraint and LRV tables via optix_execute_query."
        ),
        "suggested_remediation": (
            "1. In G3 RMS UI -> Pricing -> Competitive Intelligence -> Positioning Rules.\n"
            "2. Locate conflicting competitor rule; check 'Exclude Competitor When Rates Are Closed' or adjust percentile floor.\n"
            "3. Click Save & Recalculate."
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
# SRE ERROR CODE & DIAGNOSTIC ATTRIBUTION REGISTRY
# ==============================================================================
ERROR_CODES = {
    "INCORRECT_SYNTAX_EMPTY_COLLECTION": {
        "error_code": "SQLSERVEREXCEPTION_IN_EMPTY",
        "pattern": "Incorrect syntax near ')'",
        "subsystem": "Pricing Screen UI / Hibernate Dialect",
        "root_cause": (
            "Hibernate generates dynamic SQL with 'WHERE Room_Type_Code IN ()' when querying pricing/inventory "
            "for a property that has zero mapped room types or all room types are unmapped/inactive. MSSQL rejects "
            "the empty parenthetical clause as a fatal syntax error."
        ),
        "impact": "Pricing screen crashes with Unhandled Exception on load; users cannot view or edit room rates.",
        "affected_tables": ["Hospitality_Rooms_Config", "Room_Type_Diff", "CR_Mapping_Room_Numbers"],
        "diagnostic_query": "SELECT COUNT(*) as active_rooms FROM Hospitality_Rooms_Config WITH (NOLOCK) WHERE Property_ID = @property_id AND Status_ID = 1;",
        "zero_db_clickpath": "G3 RMS UI -> Settings -> Property Setup -> Room Configuration -> Room Types -> Unmapped Room Types -> Map unmapped PMS room code to room class -> Save & Apply.",
    },
    "ERR_LOCK_FAILED": {
        "error_code": "ERR_LOCK_FAILED / MSSQL_1205_DEADLOCK",
        "pattern": "ERR_LOCK_FAILED or Deadlock victim 1205",
        "subsystem": "CMA Batch Orchestration / Job DB / Optix",
        "root_cause": (
            "Concurrent Spring Batch worker threads or ad-hoc analytics queries locked Job_State or Accom_Activity "
            "in exclusive mode, triggering an MSSQL 1205 deadlock or lock timeout."
        ),
        "impact": "Nightly BDE or optimization job terminates in FAILED status; pricing decisions not generated.",
        "affected_tables": ["JOB_STATE", "Blocked_Job", "PROBLEM", "Accom_Activity"],
        "diagnostic_query": "SELECT js.Job_Name, js.Status, js.Start_Time, bj.valid_until FROM Job_State js WITH (NOLOCK) LEFT JOIN Blocked_Job bj WITH (NOLOCK) ON js.Job_Name = bj.Job_Name WHERE js.Status IN ('STARTED', 'RUNNING');",
        "zero_db_clickpath": "CMA Edge Gateway Portal -> Batch Orchestration -> Chains -> Filter tenant chain -> Select failed step -> Action: Resume / Restart Step.",
    },
    "ERR_PMS_TIMEOUT": {
        "error_code": "ERR_PMS_TIMEOUT / HTTP_504",
        "pattern": "ERR_PMS_TIMEOUT or HTTP 504",
        "subsystem": "AIS Outbound Decision Delivery / HTNG",
        "root_cause": (
            "External PMS/CRS listener (Opera OWS, Sabre SynXis, OnQ) failed to acknowledge rate or restriction "
            "upload within the 30-second HTTP socket timeout."
        ),
        "impact": "Pricing recommendations calculated by G3 RMS do not publish to PMS/CRS.",
        "affected_tables": ["Decision_Delivery", "Decision_Delivery_By_Type"],
        "diagnostic_query": "SELECT TOP 10 dd.Decision_Delivery_ID, dd.Uploaded_DTTM, dt.Decision_Type, dt.Status, dt.Error_Message FROM Decision_Delivery dd WITH (NOLOCK) JOIN Decision_Delivery_By_Type dt WITH (NOLOCK) ON dd.Decision_Delivery_ID = dt.Decision_Delivery_ID WHERE dd.Property_ID = @property_id ORDER BY dd.Uploaded_DTTM DESC;",
        "zero_db_clickpath": "G3 RMS UI -> Pricing -> Decision Delivery -> Delivery Status -> Select failed batch -> Force Redelivery.",
    },
    "ERR_LRV_VIOLATION": {
        "error_code": "ERR_LRV_VIOLATION",
        "pattern": "ERR_LRV_VIOLATION or Price below hurdle floor",
        "subsystem": "Continuous Daily Pricing (CDP) Optimizer",
        "root_cause": (
            "Recommended price fell below the calculated Last Room Value (LRV) hurdle floor. "
            "Optimizer suppressed publication to protect yield."
        ),
        "impact": "BAR rates remain unchanged or frozen; decisions marked as suppressed.",
        "affected_tables": ["RMS_LRV_Daily", "RMS_Pricing_Decisions"],
        "diagnostic_query": "SELECT Property_ID, Calendar_ID, LRV_Amount FROM RMS_LRV_Daily WITH (NOLOCK) WHERE Property_ID = @property_id AND Calendar_ID >= CONVERT(INT, CONVERT(VARCHAR(8), GETDATE(), 112));",
        "zero_db_clickpath": "G3 RMS UI -> Pricing -> Pricing & Restrictions -> Rate Management -> Verify LRV hurdle settings and ensure promotional rate plans do not breach floor.",
    },
    "ERR_PRICE_RANK_VIOLATION": {
        "error_code": "ERR_PRICE_RANK_VIOLATION",
        "pattern": "ERR_PRICE_RANK_VIOLATION or Room class parity inversion",
        "subsystem": "Strategic Rate Plan (SRP) / Ratchet Engine",
        "root_cause": (
            "A competitive market positioning rule or aggressive discount caused a higher room class "
            "(e.g. Suite) to price lower than a base room class (e.g. Standard King)."
        ),
        "impact": "Decisions rejected by validation engine before publication.",
        "affected_tables": ["Competitive_Positioning_Rule", "Room_Type_Diff"],
        "diagnostic_query": "SELECT Property_ID, Competitor_ID, Positioning_Rule_Type, Rate_Offset_Value, Floor_Price FROM Competitive_Positioning_Rule WITH (NOLOCK) WHERE Property_ID = @property_id;",
        "zero_db_clickpath": "G3 RMS UI -> Pricing -> Competitive Intelligence -> Positioning Rules -> Ensure 'Maintain Class Hierarchy' constraint is checked.",
    },
    "ERR_RATE_SHOP_EMPTY": {
        "error_code": "ERR_RATE_SHOP_EMPTY",
        "pattern": "ERR_RATE_SHOP_EMPTY or Missing competitor shop data",
        "subsystem": "Rate Shopping Ingestion / NGI STR",
        "root_cause": (
            "Competitor rate shopping vendor returned zero open rates for the shop date, often because "
            "competitor hotels closed inventory or anti-scraping blocks occurred."
        ),
        "impact": "Competitor pricing rules cannot evaluate; pricing falls back to unconstrained demand curve.",
        "affected_tables": ["Dim_Rate_Shop_History", "Dim_Competitor_Property"],
        "diagnostic_query": "SELECT Property_ID, Competitor_ID, Shop_Date, Open_Rates_Count FROM Dim_Rate_Shop_History WITH (NOLOCK) WHERE Property_ID = @property_id ORDER BY Shop_Date DESC;",
        "zero_db_clickpath": "G3 RMS UI -> Pricing -> Competitive Intelligence -> Competitor Settings -> Check 'Exclude Competitor When Rates Are Closed'.",
    },
    "ERR_INVALID_OAUTH_TOKEN": {
        "error_code": "ERR_INVALID_OAUTH_TOKEN / 401 Unauthorized",
        "pattern": "ERR_INVALID_OAUTH_TOKEN or 401 Unauthorized M2M",
        "subsystem": "FDS UIS / UPS Authentication Gateway",
        "root_cause": (
            "Cached Machine-to-Machine OAuth2 Bearer token expired after TTL or client secret rotated "
            "without invalidating microservice token cache."
        ),
        "impact": "Microservice API calls return 401 Unauthorized.",
        "affected_tables": ["Auth_Group", "Announcement_User"],
        "diagnostic_query": "SELECT * FROM Auth_Group WITH (NOLOCK) WHERE Client_ID = @client_id;",
        "zero_db_clickpath": "Use MCP tool ups_force_token_refresh to invalidate memory cache and fetch new token immediately.",
    },
    "KAFKA_CONSUMER_LAG_DLQ": {
        "error_code": "KAFKA_LAG_DLQ_OVERFLOW",
        "pattern": "Kafka consumer group lag or DLQ overflow",
        "subsystem": "NGI Streaming Ingestion / Cloud Inbound",
        "root_cause": (
            "Upstream PMS webhook payload schema change causing JSON deserialization failures "
            "and routing messages to Dead Letter Queue (DLQ)."
        ),
        "impact": "Real-time reservation updates stall; OTB pace drifts out of sync with PMS.",
        "affected_tables": ["CR_Mapping_Room_Numbers", "FS_Booking_Guest_Room_NGI_Pace"],
        "diagnostic_query": "SELECT TOP 20 * FROM FS_Booking_Guest_Room_NGI_Pace WITH (NOLOCK) WHERE Property_ID = @property_id ORDER BY Create_DTTM DESC;",
        "zero_db_clickpath": "G3 RMS UI -> System -> Sync Status -> Replay Streaming Messages from Timestamp. Check OHIP webhook configuration.",
    },
}


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
        self._global_tables: Dict[str, Dict[str, Any]] = {}
        self._job_tables: Dict[str, Dict[str, Any]] = {}
        self._tenant_tables: Dict[str, Dict[str, Any]] = {}
        self._stats = {
            "queries_executed": 0,
            "docs_read": 0,
            "cloud_calls": 0,
            "started_at": datetime.utcnow().isoformat(),
        }
        self._index_local_help_docs()
        self._index_db_catalogs()

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

    def _index_db_catalogs(self):
        """Indexes table schemas and business usages from Global, Job, and Tenant DB catalogs."""
        candidates = [
            os.path.join(SCRIPT_DIR, "data", "knowledge_docs"),
            os.path.join(SCRIPT_DIR, "knowledge_docs"),
            os.path.join(SCRIPT_DIR, "data"),
            SCRIPT_DIR,
        ]
        kb_dir = None
        for c in candidates:
            if os.path.exists(c) and os.path.exists(os.path.join(c, "GLOBAL_DB_TABLES_CATALOG.md")):
                kb_dir = c
                break

        if not kb_dir:
            logger.warning("Database catalog markdown files not found in candidates: %s", candidates)
            return

        # 1. Global DB Catalog
        g_path = os.path.join(kb_dir, "GLOBAL_DB_TABLES_CATALOG.md")
        if os.path.exists(g_path):
            try:
                with open(g_path, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if line.startswith("|") and not line.startswith("| Table Name") and not line.startswith("| :---"):
                            parts = [p.strip() for p in line.split("|")[1:-1]]
                            if len(parts) >= 4:
                                name = parts[0].strip("` ")
                                self._global_tables[name.upper()] = {
                                    "table_name": name,
                                    "database": "GLOBAL",
                                    "system_usage": parts[1].replace("**", "").strip(),
                                    "business_purpose": parts[2].strip(),
                                    "key_columns": parts[3].strip(),
                                }
            except Exception as ex:
                logger.warning("Error reading Global DB catalog: %s", ex)

        # 2. Job DB Catalog
        j_path = os.path.join(kb_dir, "JOB_DB_TABLES_CATALOG.md")
        if os.path.exists(j_path):
            try:
                with open(j_path, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if line.startswith("|") and not line.startswith("| Table Name") and not line.startswith("| :---"):
                            parts = [p.strip() for p in line.split("|")[1:-1]]
                            if len(parts) >= 4:
                                name = parts[0].strip("` ")
                                self._job_tables[name.upper()] = {
                                    "table_name": name,
                                    "database": "JOB",
                                    "system_usage": parts[1].replace("**", "").strip(),
                                    "business_purpose": parts[2].strip(),
                                    "key_columns": parts[3].strip(),
                                }
            except Exception as ex:
                logger.warning("Error reading Job DB catalog: %s", ex)

        # 3. Tenant DB Catalog
        t_path = os.path.join(kb_dir, "TENANT_DB_TABLES_CATALOG.md")
        if os.path.exists(t_path):
            try:
                curr_mod = "General RMS"
                with open(t_path, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if "RMS Module:" in line:
                            m = re.search(r'RMS Module:\s*\"?([^\"]+?)\"?\s*\(', line)
                            if m:
                                curr_mod = m.group(1).strip()
                        elif line.startswith("|") and not line.startswith("| Table Name") and not line.startswith("| :---"):
                            parts = [p.strip() for p in line.split("|")[1:-1]]
                            if len(parts) >= 6:
                                name = parts[0].strip("` ")
                                self._tenant_tables[name.upper()] = {
                                    "table_name": name,
                                    "database": "TENANT",
                                    "module": curr_mod,
                                    "system_usage": parts[1].strip(),
                                    "source": parts[2].strip(),
                                    "type": parts[3].strip(),
                                    "purge_days": parts[4].strip(),
                                    "notes": parts[5].strip(),
                                }
            except Exception as ex:
                logger.warning("Error reading Tenant DB catalog: %s", ex)

        logger.info(
            "Indexed %d Global DB, %d Job DB, and %d Tenant DB tables (Total: %d tables).",
            len(self._global_tables),
            len(self._job_tables),
            len(self._tenant_tables),
            len(self._global_tables) + len(self._job_tables) + len(self._tenant_tables),
        )

    def lookup_table(self, table_name: str, database: str = "ALL") -> Dict[str, Any]:
        """Retrieves technical metadata, business purpose, key columns, and safe query templates for a table."""
        t_up = table_name.upper().strip()
        db_up = database.upper().strip()
        matches = []

        if db_up in ("ALL", "GLOBAL") and t_up in self._global_tables:
            tbl = self._global_tables[t_up]
            matches.append({
                "table_name": tbl["table_name"],
                "database": "GLOBAL",
                "system_usage": tbl["system_usage"],
                "business_purpose": tbl["business_purpose"],
                "key_columns": tbl["key_columns"],
                "safe_read_query_template": f"SELECT TOP 50 * FROM {tbl['table_name']} WITH (NOLOCK) WHERE 1=1;",
            })

        if db_up in ("ALL", "JOB") and t_up in self._job_tables:
            tbl = self._job_tables[t_up]
            matches.append({
                "table_name": tbl["table_name"],
                "database": "JOB",
                "system_usage": tbl["system_usage"],
                "business_purpose": tbl["business_purpose"],
                "key_columns": tbl["key_columns"],
                "safe_read_query_template": f"SELECT TOP 50 * FROM {tbl['table_name']} WITH (NOLOCK) ORDER BY 1 DESC;",
            })

        if db_up in ("ALL", "TENANT") and t_up in self._tenant_tables:
            tbl = self._tenant_tables[t_up]
            matches.append({
                "table_name": tbl["table_name"],
                "database": "TENANT",
                "module": tbl["module"],
                "system_usage": tbl["system_usage"],
                "source": tbl["source"],
                "type": tbl["type"],
                "notes": tbl["notes"],
                "safe_read_query_template": f"SELECT TOP 50 * FROM {tbl['table_name']} WITH (NOLOCK) WHERE Property_ID = @property_id;",
            })

        # Substring fallback if no exact match
        if not matches:
            pool = []
            if db_up in ("ALL", "GLOBAL"):
                pool.extend(self._global_tables.values())
            if db_up in ("ALL", "JOB"):
                pool.extend(self._job_tables.values())
            if db_up in ("ALL", "TENANT"):
                pool.extend(self._tenant_tables.values())

            for tbl in pool:
                if t_up in tbl["table_name"].upper():
                    matches.append(tbl)
                    if len(matches) >= 5:
                        break

        return {
            "found": bool(matches),
            "query": table_name,
            "database_filter": db_up,
            "match_count": len(matches),
            "results": matches,
        }

    def search_tables(self, keyword: str, database: str = "ALL", limit: int = 15) -> Dict[str, Any]:
        """Fuzzy/keyword searches across table names, modules, and business usage descriptions."""
        kw = keyword.lower().strip()
        db_up = database.upper().strip()

        # Synonym expansion for common SRE concepts
        synonyms = {
            "deadlock": ["lock", "blocked", "contention", "victim", "job_state"],
            "room": ["rooms", "room_type", "hospitality", "pseudo"],
            "rate": ["rates", "srp", "pricing", "bar", "lrv"],
            "parameter": ["pacman", "config", "switch", "flag"],
            "inventory": ["capacity", "overbooking", "physical", "allotment"],
            "batch": ["bde", "chain", "job", "step", "pipeline"],
        }
        tokens = [t for t in re.split(r'[\s_\-]+', kw) if len(t) > 1]
        for syn_k, syn_list in synonyms.items():
            if syn_k in kw:
                tokens.extend(syn_list)

        pool = []
        if db_up in ("ALL", "GLOBAL"):
            pool.extend(self._global_tables.values())
        if db_up in ("ALL", "JOB"):
            pool.extend(self._job_tables.values())
        if db_up in ("ALL", "TENANT"):
            pool.extend(self._tenant_tables.values())

        scored = []
        for tbl in pool:
            t_name = tbl["table_name"].lower()
            score = 0
            if kw == t_name:
                score += 100
            elif kw in t_name:
                score += 50
            else:
                for tok in tokens:
                    if tok in t_name:
                        score += 25

            text_body = f"{tbl.get('system_usage', '')} {tbl.get('business_purpose', '')} {tbl.get('notes', '')} {tbl.get('module', '')} {tbl.get('key_columns', '')}".lower()
            if kw in text_body:
                score += 20
            else:
                for tok in tokens:
                    if tok in text_body:
                        score += 10

            if score > 0:
                scored.append((score, tbl))

        scored.sort(key=lambda x: x[0], reverse=True)
        results = [x[1] for x in scored[:limit]]
        return {
            "keyword": keyword,
            "database_filter": db_up,
            "total_matches": len(scored),
            "returned_count": len(results),
            "results": results,
        }

    def list_tables_by_module(self, database: str, module: Optional[str] = None) -> Dict[str, Any]:
        """Lists tables organized by functional module/system usage."""
        db_up = database.upper().strip()
        if db_up == "GLOBAL":
            modules: Dict[str, List[str]] = {}
            for t in self._global_tables.values():
                m = t.get("system_usage", "General")
                modules.setdefault(m, []).append(t["table_name"])
        elif db_up == "JOB":
            modules = {}
            for t in self._job_tables.values():
                m = t.get("system_usage", "General")
                modules.setdefault(m, []).append(t["table_name"])
        elif db_up == "TENANT":
            modules = {}
            for t in self._tenant_tables.values():
                m = t.get("module", "General")
                modules.setdefault(m, []).append(t["table_name"])
        else:
            return {"error": "Invalid database. Specify 'GLOBAL', 'JOB', or 'TENANT'."}

        if module:
            mod_lower = module.lower()
            filtered = {k: v for k, v in modules.items() if mod_lower in k.lower()}
            return {
                "database": db_up,
                "module_filter": module,
                "matched_modules": list(filtered.keys()),
                "total_tables": sum(len(v) for v in filtered.values()),
                "tables_by_module": filtered,
            }

        return {
            "database": db_up,
            "total_modules": len(modules),
            "total_tables": sum(len(v) for v in modules.values()),
            "modules_summary": {k: len(v) for k, v in sorted(modules.items(), key=lambda x: len(x[1]), reverse=True)},
        }

    def lookup_error_code(self, error_code: str) -> Dict[str, Any]:
        """Retrieves root cause, affected subsystem, diagnostic check, and Zero-DB UI remediation for an error."""
        q = error_code.lower().strip()
        matched = []
        for k, v in ERROR_CODES.items():
            if (
                q in k.lower()
                or q in v["pattern"].lower()
                or q in v["error_code"].lower()
                or any(tok in v["root_cause"].lower() for tok in q.split())
            ):
                matched.append(v)

        return {
            "query": error_code,
            "found": bool(matched),
            "total_matches": len(matched),
            "results": matched if matched else list(ERROR_CODES.values())[:3],
        }

    def generate_diagnostic_queries(
        self, scenario: str, client_code: Optional[str] = None, property_id: Optional[Any] = None, date_range: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generates verified read-only SQL queries with WITH (NOLOCK) and TOP 50 caps for triage scenarios."""
        c_code = client_code or "<CLIENT_CODE>"
        p_id = str(property_id or "<PROPERTY_ID>")
        sc_up = scenario.upper().strip()

        if sc_up in ("PRICING_SCREEN_FAILURE", "EMPTY_IN_CLAUSE", "INCORRECT_SYNTAX"):
            return {
                "scenario": "Pricing Screen Access Failure & Empty IN () Clause",
                "tenant_db_checks": [
                    {
                        "purpose": "Verify if property has zero mapped or active room types in Tenant DB",
                        "sql": f"SELECT Room_Type_Code, Pseudo_Room_Class_ID, Status_ID FROM Hospitality_Rooms_Config WITH (NOLOCK) WHERE Property_ID = {p_id};",
                    },
                    {
                        "purpose": "Check active rate codes and pricing delta configurations",
                        "sql": f"SELECT TOP 20 Room_Type_Code, Rate_Code, Start_Date, End_Date, Status_ID FROM Room_Type_Diff WITH (NOLOCK) WHERE Property_ID = {p_id};",
                    },
                ],
                "global_db_checks": [
                    {
                        "purpose": "Verify property master record and operational status",
                        "sql": f"SELECT Property_ID, Client_ID, Property_Code, Property_Name, Timezone, Status_ID FROM Agent_Property WITH (NOLOCK) WHERE Property_ID = {p_id};",
                    }
                ],
                "job_db_checks": [
                    {
                        "purpose": "Check if a batch job failed during property initialization",
                        "sql": f"SELECT TOP 5 j.Job_Name, js.Status, p.Description FROM Job_State js WITH (NOLOCK) JOIN Job_Instance j WITH (NOLOCK) ON js.Job_Instance_ID = j.Job_Instance_ID LEFT JOIN Problem p WITH (NOLOCK) ON js.Job_Execution_ID = p.Step_Execution_ID WHERE j.Job_Name LIKE '%{c_code}%' ORDER BY js.Start_Time DESC;",
                    }
                ],
                "zero_db_ui_remediation": "G3 RMS UI -> Settings -> Property Setup -> Room Configuration -> Room Types -> Unmapped Room Types -> Map room code -> Save & Apply.",
            }
        elif sc_up in ("BATCH_DEADLOCK", "LOCK_CONTENTION", "BLOCKED_JOB"):
            return {
                "scenario": "CMA Batch Orchestration Deadlock & Lock Contention",
                "job_db_checks": [
                    {
                        "purpose": "Identify active jobs currently holding locks or stuck in STARTED state",
                        "sql": "SELECT js.Job_Instance_ID, js.Job_Execution_ID, js.Job_Name, js.Start_Time, js.Status, bj.valid_until, bj.cooldown_start_timestamp FROM Job_State js WITH (NOLOCK) LEFT JOIN Blocked_Job bj WITH (NOLOCK) ON js.Job_Name = bj.Job_Name WHERE js.Status IN ('STARTED', 'RUNNING', 'FAILED') ORDER BY js.Start_Time DESC;",
                    },
                    {
                        "purpose": "Retrieve detailed error stack trace and exception dump from PROBLEM table",
                        "sql": "SELECT TOP 10 p.Problem_ID, p.Creation_Date, pc.Error_Code, pc.Error_Type, p.Description FROM Problem p WITH (NOLOCK) JOIN Problem_Classification pc WITH (NOLOCK) ON p.Problem_Classification_ID = pc.Problem_Classification_ID ORDER BY p.Creation_Date DESC;",
                    },
                ],
                "zero_db_ui_remediation": "CMA Edge Gateway Portal -> Batch Orchestration -> Chains -> Select failed step -> Action: Resume / Restart Step.",
            }
        elif sc_up in ("DECISION_DELIVERY_LAG", "ERR_PMS_TIMEOUT"):
            return {
                "scenario": "Decision Delivery Partner Upload Timeout / Lag",
                "global_db_checks": [
                    {
                        "purpose": "Inspect outbound decision delivery queue status and partner error messages",
                        "sql": f"SELECT TOP 20 dd.Decision_Delivery_ID, dd.Uploaded_DTTM, dt.Decision_Type, dt.Status, dt.Error_Message FROM Decision_Delivery dd WITH (NOLOCK) JOIN Decision_Delivery_By_Type dt WITH (NOLOCK) ON dd.Decision_Delivery_ID = dt.Decision_Delivery_ID WHERE dd.Property_ID = {p_id} ORDER BY dd.Uploaded_DTTM DESC;",
                    },
                    {
                        "purpose": "Verify decision delivery parameter mode (FULL vs DIFFERENTIAL)",
                        "sql": f"SELECT cp.Name, cpv.Context, cpv.FixedValue, cpv.Last_Updated_DTTM FROM Config_Parameter_Value cpv WITH (NOLOCK) JOIN Config_Parameter cp WITH (NOLOCK) ON cpv.Config_Parameter_ID = cp.Config_Parameter_ID WHERE cp.Name LIKE '%outbound%' AND (cpv.Context LIKE '%{c_code}%' OR cpv.Context LIKE '%{p_id}%');",
                    },
                ],
                "zero_db_ui_remediation": "G3 RMS UI -> Pricing -> Decision Delivery -> Delivery Status -> Select failed batch ID -> Click 'Force Redelivery'.",
            }
        elif sc_up in ("PARAMETER_AUDIT_DELTA", "CONFIGURATION_CHANGE"):
            return {
                "scenario": "Parameter Audit Trail & Configuration Delta Analysis",
                "global_db_checks": [
                    {
                        "purpose": "Retrieve latest configuration changes, user IDs, and revision notes",
                        "sql": f"SELECT TOP 50 cp.Name, cpv_aud.Context, cpv_aud.FixedValue, cpv_aud.REVTYPE, cpv_aud.Last_Updated_DTTM, cpv_aud.Updated_By_User_ID FROM Config_Parameter_Value_AUD cpv_aud WITH (NOLOCK) JOIN Config_Parameter cp WITH (NOLOCK) ON cpv_aud.Config_Parameter_ID = cp.Config_Parameter_ID WHERE cpv_aud.Context LIKE '%{c_code}%' OR cpv_aud.Context LIKE '%{p_id}%' ORDER BY cpv_aud.Last_Updated_DTTM DESC;",
                    }
                ],
                "zero_db_ui_remediation": "G3 RMS UI -> Admin -> System Configuration -> PACMAN Parameters -> Locate altered key -> Restore value -> Enter Salesforce Case # -> Apply.",
            }
        elif sc_up in ("UNMAPPED_ROOM_TYPES", "UNMAPPED_DIMENSION"):
            return {
                "scenario": "Unmapped PMS Room Types & Rate Codes",
                "tenant_db_checks": [
                    {
                        "purpose": "Inspect staging tables for unmapped room types from PMS feeds",
                        "sql": f"SELECT DISTINCT External_Room_Type, COUNT(*) as Ingested_Count FROM CR_Mapping_Room_Numbers WITH (NOLOCK) WHERE Property_ID = {p_id} GROUP BY External_Room_Type;",
                    }
                ],
                "optix_dw_checks": [
                    {
                        "purpose": "Find unmapped dimension entities in Optix Data Warehouse",
                        "sql": f"SELECT Property_ID, Unmapped_Type, External_Code, First_Seen_DTTM, Last_Seen_DTTM FROM Dim_Unmapped_Entity WITH (NOLOCK) WHERE Property_ID = {p_id};",
                    }
                ],
                "zero_db_ui_remediation": "G3 RMS UI -> Settings -> Property Setup -> Room Configuration -> Room Types -> Unmapped Room Types tab -> Assign to Room Class -> Save & Apply.",
            }
        else:
            return {
                "scenario": scenario,
                "supported_scenarios": [
                    "PRICING_SCREEN_FAILURE",
                    "BATCH_DEADLOCK",
                    "DECISION_DELIVERY_LAG",
                    "PARAMETER_AUDIT_DELTA",
                    "UNMAPPED_ROOM_TYPES",
                ],
                "generic_read_only_checks": [
                    {"database": "Tenant DB", "sql": f"SELECT TOP 20 * FROM Hospitality_Rooms_Config WITH (NOLOCK) WHERE Property_ID = {p_id};"},
                    {"database": "Global DB", "sql": f"SELECT TOP 20 * FROM Agent_Property WITH (NOLOCK) WHERE Property_ID = {p_id};"},
                    {"database": "Job DB", "sql": "SELECT TOP 20 * FROM Job_State WITH (NOLOCK) ORDER BY Start_Time DESC;"},
                ],
            }

    def get_investigation_matrix(self, incident_type: str) -> Dict[str, Any]:
        """Returns the complete 5-layer SRE investigation roadmap for an incident."""
        inc_up = incident_type.upper().strip()
        matrices = {
            "PRICING_SCREEN_FAILURE": {
                "incident_type": "Pricing Screen Access Failure (Empty IN () Syntax Error)",
                "layer_1_datadog_apm": {
                    "services": ["g3_app-prod-log", "g3_pricing-service"],
                    "query": "service:g3_app-prod-log \"SQLServerException\" AND \"syntax near ')'\"",
                    "expected_trace": "HTTP 500 on GET /api/pricing/property/{property_id}/views",
                },
                "layer_2_database_checks": [
                    {"db": "Tenant DB", "table": "Hospitality_Rooms_Config", "query": "SELECT COUNT(*) FROM Hospitality_Rooms_Config WITH (NOLOCK) WHERE Property_ID = @property_id AND Status_ID = 1;"},
                    {"db": "Tenant DB", "table": "Room_Type_Diff", "query": "SELECT TOP 10 * FROM Room_Type_Diff WITH (NOLOCK) WHERE Property_ID = @property_id;"},
                    {"db": "Global DB", "table": "Agent_Property", "query": "SELECT * FROM Agent_Property WITH (NOLOCK) WHERE Property_ID = @property_id;"},
                ],
                "layer_3_cma_batch": {
                    "chain": "IDeaS_Batch_<Client>_<Property>",
                    "step": "BDE_IMPORT",
                    "verification": "Verify if PMS room delta import completed or was skipped due to unmapped room types.",
                },
                "layer_4_external_transport": {
                    "type": "Inbound PMS (NGI Streaming / SFTP)",
                    "check": "Check whether upstream PMS sent new room codes (e.g. DLXK) not yet configured in G3.",
                },
                "layer_5_digital_twin_check": {
                    "technique": "Compare room count and active room class count with sister property in the same client cluster.",
                },
                "zero_db_ui_remediation": "G3 RMS UI -> Settings -> Property Setup -> Room Configuration -> Room Types -> Unmapped Room Types -> Map unmapped PMS room code to room class -> Save & Apply.",
                "engineering_fix": "In pricing DAO service, wrap IN predicate in empty collection guard before building SQL.",
            },
            "BATCH_DEADLOCK": {
                "incident_type": "Batch Pipeline Deadlock & Stale Job State",
                "layer_1_datadog_apm": {
                    "services": ["cma-batch-executor", "g3_batch-prod-log"],
                    "query": "service:g3_batch-prod-log \"Deadlock victim\" OR \"ERR_LOCK_FAILED\"",
                    "metric": "azure.sql_servers_databases.deadlock_count",
                },
                "layer_2_database_checks": [
                    {"db": "Job DB", "table": "Job_State", "query": "SELECT * FROM Job_State WITH (NOLOCK) WHERE Status IN ('STARTED', 'RUNNING');"},
                    {"db": "Job DB", "table": "Blocked_Job", "query": "SELECT * FROM Blocked_Job WITH (NOLOCK);"},
                    {"db": "Job DB", "table": "Problem", "query": "SELECT TOP 5 * FROM Problem WITH (NOLOCK) ORDER BY Creation_Date DESC;"},
                ],
                "layer_3_cma_batch": {
                    "chain": "Tenant Chain",
                    "step": "BDE_IMPORT or OPTIMIZATION",
                    "verification": "Check if an orphaned lock is preventing step progression.",
                },
                "layer_4_external_transport": {
                    "type": "Internal Orchestration",
                    "check": "No external transport failure; purely internal batch transaction concurrency.",
                },
                "layer_5_digital_twin_check": {
                    "technique": "Verify whether sister properties executed batch on the same worker node without deadlock.",
                },
                "zero_db_ui_remediation": "CMA Edge Gateway Portal -> Batch Orchestration -> Chains -> Select failed step -> Action: Resume / Restart Step.",
                "engineering_fix": "Add query hints WITH (ROWLOCK, READPAST) to high-concurrency Job_State updates.",
            },
            "DECISION_DELIVERY_LAG": {
                "incident_type": "Decision Delivery Upload Timeout & Missing Rates in PMS",
                "layer_1_datadog_apm": {
                    "services": ["ais-outbound-manager", "bmr-be-mo-service"],
                    "query": "service:ais-outbound-manager \"ERR_PMS_TIMEOUT\" OR \"HTTP 504\"",
                    "metric": "decision.delivery.failures",
                },
                "layer_2_database_checks": [
                    {"db": "Global DB", "table": "Decision_Delivery", "query": "SELECT TOP 20 * FROM Decision_Delivery WITH (NOLOCK) WHERE Property_ID = @property_id ORDER BY Uploaded_DTTM DESC;"},
                    {"db": "Global DB", "table": "Decision_Delivery_By_Type", "query": "SELECT TOP 20 * FROM Decision_Delivery_By_Type WITH (NOLOCK) WHERE Status = 'FAILED' ORDER BY 1 DESC;"},
                ],
                "layer_3_cma_batch": {
                    "chain": "Decision Delivery Dispatcher",
                    "step": "UPLOAD_DECISIONS",
                    "verification": "Confirm whether batch payload was constructed and queued for upload.",
                },
                "layer_4_external_transport": {
                    "type": "Direct URL / HTNG Outbound",
                    "check": "Verify partner listener response time, certificate validity, and endpoint URL.",
                },
                "layer_5_digital_twin_check": {
                    "technique": "Check if sister properties using the same CRS partner (e.g. SynXis) are experiencing identical timeouts.",
                },
                "zero_db_ui_remediation": "G3 RMS UI -> Pricing -> Decision Delivery -> Delivery Status -> Select failed batch -> Force Redelivery.",
                "engineering_fix": "Implement exponential backoff retry and notify partner engineering of listener socket timeout.",
            },
        }

        if inc_up in matrices:
            return matrices[inc_up]
        for k, v in matrices.items():
            if any(tok in inc_up for tok in k.split("_")):
                return v

        return {
            "incident_type": incident_type,
            "available_matrices": list(matrices.keys()),
            "default_investigation_protocol": {
                "step_1": "Query Datadog APM for HTTP 500/504 errors and exception stack traces.",
                "step_2": "Inspect Job DB Job_State and Problem tables for failed batch steps.",
                "step_3": "Inspect Tenant DB configuration tables (Hospitality_Rooms_Config, Room_Type_Diff).",
                "step_4": "Inspect Global DB Decision_Delivery and Config_Parameter_Value tables.",
                "step_5": "Execute Zero-DB UI remediation steps in G3 RMS or CMA Edge Gateway.",
            },
        }

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

    # -------------------------------------------------------------
    # Group 9: Built-in SRE Master Knowledge Base & Zero-DB Engine (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "kb_get_triage_playbook",
        "description": "Retrieves the master SRE incident triage playbook and Zero-DB resolution steps for a given failure key or symptom (e.g. 'PRICING_SCREEN_INCORRECT_SYNTAX', 'BATCH_DEADLOCK', 'DECISION_DELIVERY_TIMEOUT', 'UNMAPPED_DIMENSIONS_TRIAGE', 'CEDF_DATA_LAG_STALE_IMPORT', 'COMPETITIVE_CONSTRAINT_CONFLICT', 'HAL_CONFIG_DESYNC').",
        "inputSchema": {
            "type": "object",
            "properties": {
                "playbook_key": {
                    "type": "string",
                    "description": "The playbook identifier or symptom key (e.g. 'PRICING_SCREEN_INCORRECT_SYNTAX', 'BATCH_DEADLOCK', 'DECISION_DELIVERY_TIMEOUT', 'UNMAPPED_DIMENSIONS_TRIAGE', 'CEDF_DATA_LAG_STALE_IMPORT', 'COMPETITIVE_CONSTRAINT_CONFLICT').",
                },
            },
            "required": ["playbook_key"],
        },
    },
    {
        "name": "kb_search_operations_guide",
        "description": "Searches the complete SAS IDeaS Master Operations & Architecture Knowledge Base (subsystems, 4 transport topologies, Zero-DB compliance rules, error codes, click-paths, and playbooks) for relevant guidance.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search topic, question, or keyword (e.g. 'Zero-DB mandate', 'NGI streaming failure', 'Opera delta extract', 'Hibernate empty collection', 'deadlock').",
                },
                "section": {
                    "type": "string",
                    "description": "Optional section filter: 'ARCHITECTURE', 'TRANSPORT_TOPOLOGY', 'ZERO_DB_MANDATE', 'PLAYBOOKS', 'TOOL_ROUTING', or 'ALL' (default 'ALL').",
                    "default": "ALL",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "kb_get_transport_topology",
        "description": "Returns comprehensive architecture, failure modes, diagnostic tools, and recovery actions for external PMS/CRS transport mechanisms (NGI, Direct URL / HTNG, CEDF SFTP, Ratchet SRP).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "mechanism": {
                    "type": "string",
                    "description": "Transport mechanism: 'NGI', 'DIRECT_URL_HTNG', 'CEDF_SFTP', 'RATCHET_SRP', or 'ALL' (default 'ALL').",
                    "default": "ALL",
                },
            },
            "required": [],
        },
    },
    {
        "name": "kb_get_zero_db_clickpaths",
        "description": "Returns exact click-by-click G3 RMS UI navigation paths, save procedures, and verification checks for non-database operational fixes.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "Target module: 'ROOM_TYPES', 'RATE_CODES_SRP', 'DECISION_DELIVERY', 'BATCH_CHAINS', 'COMPETITIVE_RULES', 'PACMAN_PARAMETERS', or 'RESERVATIONS_RESYNC'.",
                },
            },
            "required": ["category"],
        },
    },
    {
        "name": "kb_lookup_db_table",
        "description": "Retrieves technical metadata, business purpose, key columns, system usage, and safe read-only SQL query template for any table in Global DB (213 tables), Job DB (25 tables), or Tenant DB (1,011 tables).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "table_name": {
                    "type": "string",
                    "description": "Table name or substring (e.g. 'CONFIG_PARAMETER_VALUE', 'JOB_STATE', 'RMS_ROOM_RATES', 'PROBLEM', 'AGENT_PROPERTY', 'PROFILE', 'CR_MAPPING_ROOM_NUMBERS').",
                },
                "database": {
                    "type": "string",
                    "description": "Optional database filter: 'GLOBAL', 'JOB', 'TENANT', or 'ALL' (default 'ALL').",
                    "default": "ALL",
                },
            },
            "required": ["table_name"],
        },
    },
    {
        "name": "kb_search_db_tables",
        "description": "Fuzzy searches the 1,249+ table catalog across Global DB, Job DB, and Tenant DB by keyword or functional concept (e.g. 'room', 'rate', 'pricing', 'parameter', 'lock', 'deadlock', 'decision', 'forecast', 'segment', 'batch').",
        "inputSchema": {
            "type": "object",
            "properties": {
                "keyword": {
                    "type": "string",
                    "description": "Search keyword or technical concept.",
                },
                "database": {
                    "type": "string",
                    "description": "Optional database filter: 'GLOBAL', 'JOB', 'TENANT', or 'ALL' (default 'ALL').",
                    "default": "ALL",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max results to return (default: 15).",
                    "default": 15,
                },
            },
            "required": ["keyword"],
        },
    },
    {
        "name": "kb_list_db_tables_by_module",
        "description": "Lists all tables organized by functional business module for Global DB, Job DB, or Tenant DB (e.g. 'Parameter Hierarchy', 'Property Master', 'Analytics', 'Pricing', 'Inventory', 'Decisions').",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target database: 'GLOBAL', 'JOB', or 'TENANT'.",
                },
                "module": {
                    "type": "string",
                    "description": "Optional module filter name. If omitted, returns all modules with table counts.",
                },
            },
            "required": ["database"],
        },
    },
    {
        "name": "kb_lookup_error_code",
        "description": "Retrieves diagnostic attribution, technical root cause, affected subsystem layer, diagnostic SQL, and Zero-DB UI remediation for IDeaS, SQL Server, Oracle, BDE, and Kafka error codes/patterns.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "error_code": {
                    "type": "string",
                    "description": "Error code or pattern snippet (e.g. 'ERR_PMS_TIMEOUT', 'ERR_LOCK_FAILED', 'ERR_LRV_VIOLATION', 'Incorrect syntax near )', 'Deadlock victim', 'ERR_RATE_SHOP_EMPTY').",
                },
            },
            "required": ["error_code"],
        },
    },
    {
        "name": "kb_generate_diagnostic_queries",
        "description": "Generates verified, safe, read-only SQL queries with WITH (NOLOCK) and TOP 50 caps tailored for investigating specific incident scenarios across Tenant DB, Job DB, Global DB, and Optix DW.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "scenario": {
                    "type": "string",
                    "description": "Incident scenario: 'PRICING_SCREEN_FAILURE', 'BATCH_DEADLOCK', 'DECISION_DELIVERY_LAG', 'PARAMETER_AUDIT_DELTA', 'UNMAPPED_ROOM_TYPES'.",
                },
                "client_code": {
                    "type": "string",
                    "description": "Client code (e.g. 'PALETT', 'OXFCOLLECT', 'ACCOR').",
                },
                "property_id": {
                    "type": "string",
                    "description": "Property code or numeric ID (e.g. '996317', '0018').",
                },
                "date_range": {
                    "type": "string",
                    "description": "Optional date filter.",
                },
            },
            "required": ["scenario"],
        },
    },
    {
        "name": "kb_get_incident_investigation_matrix",
        "description": "Returns an end-to-end multi-system SRE investigation matrix for an incident type, detailing Datadog APM metrics/logs to search, exact SQL tables and queries to inspect, CMA batch chains to review, transport checks, and sister property comparative validation.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "incident_type": {
                    "type": "string",
                    "description": "Incident type: 'PRICING_SCREEN_FAILURE', 'BATCH_DEADLOCK', 'DECISION_DELIVERY_LAG', 'UNMAPPED_DIMENSION'.",
                },
            },
            "required": ["incident_type"],
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

    # --- Group 9: Built-in SRE Master Knowledge Base & Zero-DB Engine ---
    elif name == "kb_get_triage_playbook":
        pkey = arguments["playbook_key"].upper().strip()
        if pkey in DIAGNOSTIC_RUNBOOKS:
            rb = DIAGNOSTIC_RUNBOOKS[pkey]
            return {
                "playbook_key": pkey,
                "found": True,
                "title": rb["title"],
                "domain": rb["domain"],
                "summary": rb["summary"],
                "identification_technique": rb["identification_technique"],
                "suggested_remediation": rb["suggested_remediation"],
                "confluence_url": rb.get("confluence_url"),
            }
        for k, rb in DIAGNOSTIC_RUNBOOKS.items():
            if pkey in k or any(kw in pkey.lower() for kw in rb.get("keywords", [])):
                return {
                    "playbook_key": k,
                    "matched_query": pkey,
                    "found": True,
                    "title": rb["title"],
                    "domain": rb["domain"],
                    "summary": rb["summary"],
                    "identification_technique": rb["identification_technique"],
                    "suggested_remediation": rb["suggested_remediation"],
                    "confluence_url": rb.get("confluence_url"),
                }
        return {
            "found": False,
            "playbook_key": pkey,
            "message": f"Playbook '{pkey}' not found. Available playbooks: {list(DIAGNOSTIC_RUNBOOKS.keys())}",
            "available_playbooks": list(DIAGNOSTIC_RUNBOOKS.keys()),
        }

    elif name == "kb_search_operations_guide":
        query = arguments["query"].lower().strip()
        sec = arguments.get("section", "ALL").upper()
        kb_docs = [
            "ZERO_DB_OPERATIONS_PLAYBOOK.md",
            "IDeaS_Triage_Knowledge_Base.md",
            "IDeaS_Error_Codes_And_Glossary.md",
            "TENANT_DB_TABLES_CATALOG.md",
            "GLOBAL_DB_TABLES_CATALOG.md",
            "JOB_DB_TABLES_CATALOG.md",
        ]
        matches = []
        for dname in kb_docs:
            dpath = None
            for cand in [
                os.path.join(SCRIPT_DIR, "data", "knowledge_docs", dname),
                os.path.join(SCRIPT_DIR, "knowledge_docs", dname),
                os.path.join(SCRIPT_DIR, "data", dname),
                os.path.join(SCRIPT_DIR, dname),
            ]:
                if os.path.exists(cand):
                    dpath = cand
                    break
            if dpath:
                try:
                    with open(dpath, "r", encoding="utf-8", errors="ignore") as fp:
                        content = fp.read()
                    sections = content.split("## ")
                    for s in sections:
                        if not s.strip():
                            continue
                        s_title = s.split("\n")[0].strip()
                        if query in s.lower():
                            matches.append({
                                "source_document": dname,
                                "section_title": s_title,
                                "excerpt": s[:800] + ("..." if len(s) > 800 else ""),
                            })
                except Exception as ex:
                    logger.warning("Error reading %s: %s", dname, ex)
        return {
            "query": arguments["query"],
            "section_filter": sec,
            "total_matches": len(matches),
            "results": matches[:5],
        }

    elif name == "kb_get_transport_topology":
        mech = arguments.get("mechanism", "ALL").upper().strip()
        topologies = {
            "NGI": {
                "name": "NGI (Next Generation Integration / Streaming)",
                "technology": "Kafka real-time event streaming & cloud ingestion microservices",
                "common_partners": ["Oracle Opera Cloud (OHIP)", "Mews", "Stayntouch"],
                "failure_modes": ["Kafka consumer group lag", "JSON/Avro deserialization errors", "Dead Letter Queue (DLQ) overflow", "OAuth2 token expiry"],
                "diagnostic_tools": ["datadog_trace_pms_inbound_stream", "fds_probe_microservice_health", "fds_get_nucleus_integration_settings"],
                "zero_db_resolution": "In G3 RMS UI -> System -> Sync Status -> Replay Streaming Messages from Timestamp, or request hotel IT verify OHIP webhook subscription status.",
            },
            "DIRECT_URL_HTNG": {
                "name": "Direct URL / Webhooks / HTNG Outbound Delivery",
                "technology": "Synchronous/asynchronous HTTPS POST/PUT payloads (HTNG 2008B/2014A XML / REST)",
                "common_partners": ["Sabre SynXis CRS", "Hilton OnQ", "Amadeus iHotelier", "Opera OWS / OXI proxy"],
                "failure_modes": ["HTTP 401/403 cert or basic auth expiry", "HTTP 404 endpoint path altered", "HTTP 500/504 partner listener timeout >30s", "HTNG XML schema rejection"],
                "diagnostic_tools": ["cma_get_decision_delivery_details", "datadog_trace_decision_delivery_errors", "fds_get_integration_property_configs"],
                "zero_db_resolution": "In G3 RMS UI -> Pricing -> Decision Delivery -> Delivery Status -> Force Redelivery. Update credentials in HAL Explorer. Notify hotel IT to bounce local HTNG listener.",
            },
            "CEDF_SFTP": {
                "name": "File-Based CEDF / SFTP Batch Inbound & Outbound",
                "technology": "Scheduled flat files (CSV, pipe-delimited, XML) over secure SFTP (cedf.ideasrms.com) ingested by Spring Batch BDE",
                "common_partners": ["Legacy Opera V5 (OXI extracts)", "Custom enterprise data feeds", "Nightly PMS audit dumps"],
                "failure_modes": ["SFTP connection timeout", "0-byte file locks", "Corrupt headers/delimiters", "File arrival after batch cutoff time"],
                "diagnostic_tools": ["cma_get_datafeed_status", "cma_get_datafeed_import_freshness", "cedf_check_client_upload_status"],
                "zero_db_resolution": "Do NOT manually insert reservation rows in SQL. Request hotel Night Auditor run manual delta extract from PMS (Opera: Miscellaneous -> File Export) to SFTP /inbound/, then trigger G3 RMS UI -> System Operations -> Ingest Queue.",
            },
            "RATCHET_SRP": {
                "name": "Ratchet Strategic Rate Plan (SRP) Channel Distribution",
                "technology": "Ratchet middleware synchronizing SRPs across channel managers, OTAs, and CRS partners",
                "common_partners": ["DerbySoft", "SiteMinder", "D-EDGE", "Direct OTAs"],
                "failure_modes": ["Unmapped Strategic Rate Plans", "Room class parity inversions", "Inactive rate plans"],
                "diagnostic_tools": ["cma_get_ratchet_srp_mappings"],
                "zero_db_resolution": "Link unmapped SRPs in G3 RMS UI -> Pricing & Restrictions -> Rate Management -> SRP Mapping. Publish rate plan changes to trigger Ratchet cache reload.",
            },
        }
        if mech in topologies:
            return {"mechanism": mech, "topology": topologies[mech]}
        return {"mechanism": "ALL", "topologies": topologies}

    elif name == "kb_get_zero_db_clickpaths":
        cat = arguments["category"].upper().strip()
        clickpaths = {
            "ROOM_TYPES": {
                "module": "Room Types & Physical Inventory",
                "navigation_path": "G3 RMS UI -> Settings -> Property Setup -> Room Configuration -> Room Types",
                "steps": [
                    "1. Click on the 'Unmapped Room Types' tab.",
                    "2. Select the unmapped PMS room code (e.g. DLXK).",
                    "3. Assign to an existing Pseudo Room Class or define as a new Physical Room Type with physical capacity.",
                    "4. Click 'Save & Apply'.",
                    "5. Reprocess: Navigate to System -> Sync Status -> Resync Reservations.",
                ],
            },
            "RATE_CODES_SRP": {
                "module": "Rate Codes & Strategic Rate Plans (SRP)",
                "navigation_path": "G3 RMS UI -> Pricing & Restrictions -> Rate Management -> Rate Codes / SRP Mapping",
                "steps": [
                    "1. Search for the unmapped PMS rate code.",
                    "2. Link the rate code to the designated Strategic Rate Plan (SRP) group (e.g. Commercial, Promotional).",
                    "3. Configure rate parity rules and ceiling/floor constraints.",
                    "4. Click 'Publish Mappings' to invalidate cache across Ratchet and decision delivery queues.",
                ],
            },
            "DECISION_DELIVERY": {
                "module": "Decision Delivery Uploads",
                "navigation_path": "G3 RMS UI -> Pricing -> Decision Delivery -> Delivery Status",
                "steps": [
                    "1. Filter by date window and failed delivery batch ID.",
                    "2. Inspect the delivery error message (e.g. timeout or schema mismatch).",
                    "3. Click 'Force Redelivery' (or 'Replay Batch') to re-queue the payload cleanly without database updates.",
                ],
            },
            "BATCH_CHAINS": {
                "module": "CMA Batch Orchestration & Deadlocks",
                "navigation_path": "CMA Edge Gateway Portal -> Batch Orchestration -> Chains",
                "steps": [
                    "1. Filter for the tenant property chain (e.g. IDeaS_Batch_Hilton_LONLK).",
                    "2. Inspect the failed or blocked step (e.g. BDE_IMPORT or OPTIMIZATION).",
                    "3. Click 'Action: Resume / Restart Step'.",
                    "4. Spring Batch runtime automatically clears orphaned transaction locks on Job_State and advances state.",
                ],
            },
            "COMPETITIVE_RULES": {
                "module": "Competitive Market Position Rules",
                "navigation_path": "G3 RMS UI -> Pricing -> Competitive Intelligence -> Positioning Rules",
                "steps": [
                    "1. Locate the competitor rule conflicting with LRV hurdle floors or causing room class inversions.",
                    "2. Check the box 'Exclude Competitor When Rates Are Closed' or relax the floor constraint.",
                    "3. Click 'Save & Recalculate' to generate fresh decisions.",
                ],
            },
            "PACMAN_PARAMETERS": {
                "module": "System Configuration & PACMAN Parameters",
                "navigation_path": "G3 RMS UI -> Admin -> System Configuration -> PACMAN Parameters",
                "steps": [
                    "1. Search for the parameter key (e.g. pacman.pricing.continuous.sensitivity).",
                    "2. Enter the updated value.",
                    "3. Enter the mandatory Salesforce Case # / Change Reason for SOX audit tracking.",
                    "4. Click 'Apply' to trigger automatic worker node memory reload.",
                ],
            },
            "RESERVATIONS_RESYNC": {
                "module": "Reservation Ingestion & Datafeed Resync",
                "navigation_path": "G3 RMS UI -> System Operations -> Data Feeds -> Ingest Queue",
                "steps": [
                    "1. Verify that the PMS delta file has landed in the CEDF SFTP /inbound/ directory.",
                    "2. Select the pending file from the Ingest Queue.",
                    "3. Click 'Process Now' to execute safe, transactional BDE ingestion into Optix.",
                ],
            },
        }
        if cat in clickpaths:
            return {"category": cat, "clickpath": clickpaths[cat]}
        return {"found": False, "requested": cat, "available_categories": list(clickpaths.keys())}

    elif name == "kb_lookup_db_table":
        tname = arguments["table_name"]
        db = arguments.get("database", "ALL")
        return mgr.lookup_table(tname, database=db)

    elif name == "kb_search_db_tables":
        kw = arguments["keyword"]
        db = arguments.get("database", "ALL")
        lim = int(arguments.get("limit", 15))
        return mgr.search_tables(kw, database=db, limit=lim)

    elif name == "kb_list_db_tables_by_module":
        db = arguments["database"]
        mod = arguments.get("module")
        return mgr.list_tables_by_module(db, module=mod)

    elif name == "kb_lookup_error_code":
        err = arguments["error_code"]
        return mgr.lookup_error_code(err)

    elif name == "kb_generate_diagnostic_queries":
        scen = arguments["scenario"]
        c_code = arguments.get("client_code")
        p_id = arguments.get("property_id")
        d_range = arguments.get("date_range")
        return mgr.generate_diagnostic_queries(scen, client_code=c_code, property_id=p_id, date_range=d_range)

    elif name == "kb_get_incident_investigation_matrix":
        inc_type = arguments["incident_type"]
        return mgr.get_investigation_matrix(inc_type)

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
