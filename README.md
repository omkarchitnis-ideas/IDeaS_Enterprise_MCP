# SAS IDeaS Enterprise Master Unified Super-MCP Server

[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
[![MCP](https://img.shields.io/badge/MCP-1.0.0-purple.svg)](https://modelcontextprotocol.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)](https://fastapi.tiangolo.com/)
[![Tools](https://img.shields.io/badge/Canonical%20Tools-168-orange.svg)]()
[![Resources](https://img.shields.io/badge/Canonical%20Resources-15-teal.svg)]()

Production-grade **Model Context Protocol (MCP)** server consolidating all 6 SAS IDeaS mission-critical core systems into a single high-performance SSE (Server-Sent Events) daemon on port **8550**.

---

## 🏛️ Architecture Overview

```
                      +-----------------------------------+
                      |   AI Coding Agents / IDEs / LLMs  |
                      |  (Antigravity, Claude, Cursor)    |
                      +-----------------+-----------------+
                                        | SSE / JSON-RPC (Port 8550)
                                        v
+---------------------------------------------------------------------------------+
|                       SAS IDeaS Master Super-MCP Server                         |
|                           (unified_mcp_server.py)                              |
+--------+--------------+--------------+---------------+--------------+-----------+
         |              |              |               |              |
         v              v              v               v              v           v
   [Domain 1]     [Domain 2]     [Domain 3]      [Domain 4]     [Domain 5]  [Domain 6]
   Salesforce    CMA Gateway      Optix DW       Confluence       Datadog    UPS & FDS
   Enterprise    Edge Gateway   SQL Clusters     Knowledge &   Observability Platform
   Middleware    (19,496 chains) (420 DBs)      Vector Search   Telemetry   (OAuth2 M2M)
   (24 Tools)     (34 Tools)     (35 Tools)      (25 Tools)    (20 Tools)   (30 Tools)
```

---

## 🛠️ Canonical Tool Catalog (168 Tools)

The server exposes **168 unique, canonical tools** across 6 specialized enterprise domains:

### 1. Salesforce Enterprise Core (24 Tools)
- `sfdc_search_cases`, `sfdc_get_case_detail`, `sfdc_query_soql`, `sfdc_describe_object`
- `sfdc_get_account_detail`, `sfdc_get_contact_detail`, `sfdc_list_case_comments`
- `sfdc_add_case_comment`, `sfdc_update_case_status`, `sfdc_search_knowledge`
- `sfdc_get_article_detail`, `sfdc_list_open_escalations`, `sfdc_get_case_history`
- `sfdc_get_user_cases`, `sfdc_bulk_case_lookup`, `sfdc_export_cases_to_json`
- `sfdc_count_cases_by_status`, `sfdc_get_recent_modified_cases`, `sfdc_search_accounts`
- `sfdc_get_queue_cases`, `sfdc_get_case_attachments`, `sfdc_verify_client_access`
- `sfdc_health_check`, `sfdc_check_sync_status`

### 2. CMA Gateway (34 Tools)
- **Chain Management**: `cma_search_chains`, `cma_get_chain_details`, `cma_list_tenant_chains`, `cma_get_job_chains`, `cma_export_chain_catalog`
- **Client & Property**: `cma_get_client_info`, `cma_list_client_properties`, `cma_get_property_config`, `cma_search_properties`, `cma_get_active_properties`
- **Database Routing**: `cma_get_db_routing`, `cma_list_db_servers`, `cma_validate_db_connectivity`, `cma_get_connection_pool_stats`
- **Schema & Query**: `cma_execute_readonly_sql`, `cma_describe_table_schema`, `cma_list_tables`, `cma_get_table_row_count`, `cma_explain_query_plan`
- **System & Gateway**: `cma_get_gateway_health`, `cma_get_api_metrics`, `cma_list_active_sessions`, `cma_clear_gateway_cache`, `cma_verify_api_key`
- **Specialized Analytics**: `cma_get_audit_log`, `cma_get_tenant_quota`, `cma_get_ratchet_chains`, `cma_list_global_chains`, `cma_get_chain_execution_history`, `cma_get_property_sync_status`, `cma_check_tenant_lock`, `cma_get_system_time`, `cma_ping_gateway`, `cma_export_gateway_report`

### 3. Optix SQL Server Cluster (35 Tools)
- **Cluster Management**: `optix_list_cluster_nodes`, `optix_get_node_status`, `optix_list_all_databases`, `optix_search_database_catalog`, `optix_get_cluster_health_overview`
- **Database & Table Operations**: `optix_execute_query`, `optix_describe_table`, `optix_list_tables`, `optix_get_table_row_counts`, `optix_get_table_indexes`, `optix_get_foreign_keys`
- **Performance & Diagnostics**: `optix_get_running_queries`, `optix_get_blocking_queries`, `optix_get_expensive_queries`, `optix_get_index_fragmentation`, `optix_get_missing_index_recommendations`, `optix_get_database_size_stats`, `optix_get_buffer_cache_usage`
- **Tenant & Property Analytics**: `optix_lookup_tenant_database`, `optix_get_tenant_configuration`, `optix_get_client_revenue_summary`, `optix_get_property_performance_metrics`, `optix_export_query_results`
- **Maintenance & Monitoring**: `optix_check_backup_status`, `optix_get_sql_server_error_log`, `optix_get_tempdb_usage`, `optix_get_cpu_memory_usage`, `optix_check_connection_pool`, `optix_kill_query_session`, `optix_refresh_database_catalog`, `optix_get_cluster_capacity_forecast`, `optix_get_transaction_log_stats`, `optix_get_deadlock_reports`, `optix_validate_credentials`

### 4. Confluence & G3 Knowledge Base (25 Tools)
- **Search & Retrieval**: `confluence_search_kb`, `confluence_get_page_content`, `confluence_search_cql`, `confluence_list_space_pages`, `confluence_get_page_comments`
- **G3 Local Docs Engine**: `confluence_search_g3_docs`, `confluence_get_g3_doc_content`, `confluence_list_all_g3_docs`, `confluence_get_g3_feature_guide`, `confluence_list_all_runbooks`
- **Vector Engine (Qdrant)**: `confluence_semantic_search_docs`, `confluence_get_similar_articles`, `confluence_index_document`, `confluence_get_collection_stats`
- **Runbooks & Troubleshooting**: `confluence_get_escalation_runbook`, `confluence_get_troubleshooting_guide`, `confluence_get_release_notes`, `confluence_get_api_documentation`
- **Spaces & Analytics**: `confluence_list_spaces`, `confluence_get_space_details`, `confluence_get_recently_updated_pages`, `confluence_export_page_markdown`, `confluence_check_kb_sync_status`, `confluence_health_check`, `confluence_validate_credentials`

### 5. Datadog Observability & Telemetry (20 Tools)
- **Monitors & Alerts**: `datadog_list_monitors`, `datadog_get_monitor_details`, `datadog_get_active_alerts`, `datadog_mute_monitor`, `datadog_unmute_monitor`
- **Metrics & Performance**: `datadog_query_metrics`, `datadog_list_metric_names`, `datadog_get_service_latency_stats`, `datadog_get_error_rate_stats`
- **Logs & Traces**: `datadog_search_logs`, `datadog_get_log_details`, `datadog_search_traces`, `datadog_get_trace_details`
- **Services & Dashboards**: `datadog_list_services`, `datadog_get_service_health`, `datadog_list_dashboards`, `datadog_get_dashboard_details`
- **Events & Infrastructure**: `datadog_search_events`, `datadog_get_host_metrics`, `datadog_validate_credentials`

### 6. UPS & FDS Enterprise Platform (30 Tools)
- **FDS Product & Config**: `fds_list_products`, `fds_get_product_config`, `fds_search_tenants`, `fds_get_tenant_details`, `fds_get_tenant_deployments`, `fds_get_rate_management_config`, `fds_list_property_forecasts`, `fds_get_pricing_rules`, `fds_get_inventory_blocks`, `fds_export_tenant_configuration`
- **CEDF Data Feeds**: `cedf_list_extract_jobs`, `cedf_get_job_status`, `cedf_get_latest_delivery_log`, `cedf_trigger_resend_job`, `cedf_get_feed_schema`, `cedf_list_feed_partners`, `cedf_get_delivery_metrics`
- **UPS Security & Audit**: `ups_get_user_permissions`, `ups_list_role_assignments`, `ups_get_session_audit_log`, `ups_check_feature_flag`, `ups_list_api_tokens`, `ups_revoke_api_token`
- **M2M OAuth2 Token Management**: `ups_get_cached_bearer_token`, `ups_force_token_refresh`, `ups_validate_m2m_credentials`
- **Diagnostics & Health**: `fds_get_platform_health`, `cedf_get_gateway_health`, `ups_get_auth_service_status`, `ups_export_platform_telemetry`

---

## 📡 Canonical Resources (15 Resources)

Access URI-based enterprise context snapshots via `read_resource`:

- `enterprise://platform/status` - Live system-wide health and subsystem status
- `enterprise://tools/catalog` - Complete tool inventory schema
- `sfdc://cases/summary` - Salesforce cases overview and backfill status
- `cma://chains/summary` - Cached CMA chain topology
- `optix://cluster/overview` - 3-node SQL Server cluster catalog
- `confluence://runbooks/index` - Local G3 runbook index
- `datadog://alerts/summary` - Current active Datadog alerts
- `fds://tenants/overview` - FDS tenant and environment summary
- `enterprise://diagnostics/quickstart` - Quickstart diagnostic workflow
- ...and domain-specific telemetry streams.

---

## 🚀 Quickstart

### 1. Run via Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/omkarchitnis-ideas/IDeaS_Enterprise_MCP.git
cd IDeaS_Enterprise_MCP

# Copy configuration template and adjust secrets
cp .env.example .env

# Launch the Unified Super-MCP container
docker compose up -d
```

### 2. Run Standalone with Python

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
python unified_mcp_server.py --host 0.0.0.0 --port 8550
```

---

## 🔌 Connecting to AI Agents & IDEs

### SSE Endpoint Configuration

The Unified MCP Server provides a standard Server-Sent Events (SSE) interface:
- **SSE Transport URL**: `http://172.27.210.162:8550/sse` (or `http://localhost:8550/sse`)
- **Healthcheck Probe**: `http://localhost:8550/health`

### Claude Desktop / Cursor (`claude_desktop_config.json` / `mcp.json`)

```json
{
  "mcpServers": {
    "ideas-enterprise-mcp": {
      "url": "http://172.27.210.162:8550/sse"
    }
  }
}
```

### Python SDK (`mcp` library)

```python
from mcp.client.sse import sse_client
from mcp import ClientSession

async with sse_client("http://localhost:8550/sse") as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        tools = await session.list_tools()
        print(f"Loaded {len(tools.tools)} enterprise tools.")
```

---

## 🏢 Microsoft 365 Copilot & Copilot Studio Integration

This platform natively exposes **OpenAPI 3.0 REST endpoints** and pre-filtered domain specifications designed for **1-click import into Microsoft Copilot Studio** to power **Microsoft 365 Copilot** across Teams, Outlook, Word, and Excel.

### 1. OpenAPI Specification Endpoints

You can import either the full unified catalog or domain-tailored OpenAPI specs directly into Microsoft Copilot Studio:

| Endpoint URL | Target Copilot Action | Included Actions |
| :--- | :--- | :--- |
| `http://<host>:8550/openapi.json` | **Full Unified Enterprise Platform** | All 168 Actions |
| `http://<host>:8550/api/v1/openapi/sfdc.json` | **Salesforce Enterprise Actions** | 24 Salesforce Actions |
| `http://<host>:8550/api/v1/openapi/optix.json` | **Optix SQL DW Cluster Actions** | 35 Optix Actions |
| `http://<host>:8550/api/v1/openapi/cma.json` | **CMA Edge Gateway Actions** | 34 CMA Actions |
| `http://<host>:8550/api/v1/openapi/confluence.json` | **Confluence & G3 KB Actions** | 25 Knowledge Actions |
| `http://<host>:8550/api/v1/openapi/datadog.json` | **Datadog Observability Actions** | 20 Telemetry Actions |
| `http://<host>:8550/api/v1/openapi/ups.json` | **UPS & FDS Platform Actions** | 30 Platform Actions |

### 2. How to Connect to M365 Copilot

1. Open **[Microsoft Copilot Studio](https://copilotstudio.microsoft.com/)** with your organization account.
2. Select your custom Copilot or click **Actions** -> **Add an action**.
3. Choose **REST API / OpenAPI**.
4. Provide the OpenAPI URL (e.g. `https://<corporate-gateway>/api/v1/openapi/sfdc.json`).
5. Review the imported actions and select parameter mappings.
6. Click **Publish to Microsoft 365 Copilot**.
7. Users in **Microsoft Teams** can now mention `@Copilot` to query live Salesforce cases, Optix database booking curves, CMA chains, or Datadog alerts directly!

### 3. REST API Endpoints

- **Interactive Swagger Documentation**: `http://localhost:8550/docs`
- **List All Tools**: `GET /api/v1/tools`
- **Universal Tool Invocation**: `POST /api/v1/tools/call` with body `{"name": "...", "arguments": {...}}`
- **Direct Tool REST Routes**: `POST /api/v1/tools/{tool_name}` (e.g. `POST /api/v1/tools/sfdc_search_cases`)

---


## 🧪 Verification Suite

Run the full automated 11-suite verification against all 6 connected subsystems:

```bash
python verify_unified_mcp.py
```

Expected output:
```
================================================================================
SAS IDEAS MASTER ENTERPRISE UNIFIED SUPER-MCP VERIFICATION SUITE
Target: http://localhost:8550
================================================================================
[PASS] Health Check Probe (/health): Status: HEALTHY | Total Tools: 168
[PASS] SSE Transport Handshake (/sse): Session established
[PASS] Unified Tools & Resources Registry: Found 168 canonical tools, 15 resources
[PASS] Domain 1: Salesforce (sfdc_search_cases)
[PASS] Domain 2: CMA Gateway (cma_search_chains)
[PASS] Domain 3: Optix DB Cluster (optix_list_all_databases)
[PASS] Domain 4: Confluence KB (confluence_list_all_runbooks)
[PASS] Domain 5: Datadog Observability (datadog_validate_credentials)
[PASS] Domain 6: UPS & FDS Platform (ups_validate_m2m_credentials)
[PASS] Unified Resource (enterprise://platform/status)
[PASS] Unified Tools Catalog Resource (enterprise://tools/catalog)
================================================================================
VERIFICATION COMPLETE: 11/11 Checks Passed.
================================================================================
```

---

## 📄 License
Internal SAS IDeaS Enterprise Proprietary - All rights reserved.
