#!/usr/bin/env python3
"""
Datadog Production Observability Model Context Protocol (MCP) Server
=====================================================================
Comprehensive 20-Tool Suite for Datadog Logs v2, Monitors, Metrics, and Service Health.

Enterprise Capabilities:
1. Log Search v2 Engine: Full-text, service filter, status filter, and pagination.
2. Job Execution Tracing: Direct correlation with @job_instance_id and @job_execution_id.
3. Microservice Error Triage: Rapid error extraction, stack traces, and RCA diagnostics.
4. Transaction Correlation: End-to-end tracing by correlationId and requestTransactionId.
5. Monitors & Alert Management: Active alert scanner, trigger thresholds, monitor status.
6. Metric Timeseries Telemetry: CPU, memory, JDBC pool saturation, request latency.
7. Dual Transports: HTTP Server-Sent Events (SSE) on Port 8559 + Stdio Transport.
"""

import os
import sys
import json
import time
import logging
import argparse
import threading
from typing import Any, Dict, List, Optional
from datetime import datetime, timedelta
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
logger = logging.getLogger("datadog-mcp-server")

# ==============================================================================
# CONFIGURATION & CONSTANTS
# ==============================================================================
DATADOG_API_KEY = os.getenv("DATADOG_API_KEY", "f365101df48d434c90867dcfc55cbe74")
DATADOG_APP_KEY = os.getenv("DATADOG_APP_KEY", "68af7ed081b3b7be01905bc0d17d6f07c275f6f5")
DATADOG_SITE = os.getenv("DATADOG_SITE", "datadoghq.com")

BASE_API_URL = f"https://api.{DATADOG_SITE}"

MCP_HOST = os.getenv("MCP_HOST", "0.0.0.0")
MCP_PORT = int(os.getenv("DATADOG_MCP_PORT", os.getenv("MCP_PORT", "8559")))

CORE_IDEAS_SERVICES = [
    {"name": "g3_app-prod-log", "domain": "rms_core", "description": "G3 RMS Production Application Core Logs"},
    {"name": "bmr-be-mo-service", "domain": "decision_delivery", "description": "Business Monitoring Outbound Service"},
    {"name": "bmr-be-sdp-service", "domain": "processing", "description": "Seed Daily Processing Service"},
    {"name": "/ecs/prod/htng/", "domain": "pms_feed", "description": "HTNG PMS & Inbound Ingestion Pipeline"},
    {"name": "decision-delivery-internal", "domain": "decision_delivery", "description": "Decision Delivery Microservice"},
    {"name": "pmsinbound-internal", "domain": "pms_feed", "description": "PMS Inbound HAL Microservice"},
    {"name": "ais-outbound-manager", "domain": "ais", "description": "AIS Outbound Manager"},
    {"name": "ais-task-manager", "domain": "ais", "description": "AIS Task Manager"},
    {"name": "pull-sftp", "domain": "ftp_feeds", "description": "Atlantis SFTP-to-S3 Pull Pipeline"},
    {"name": "optix-etl", "domain": "analytics_dw", "description": "Optix Data Warehouse ETL Jobs"},
]


# ==============================================================================
# DATADOG CLIENT & OBSERVABILITY MANAGER
# ==============================================================================
class DatadogManager:
    """Thread-safe manager for querying Datadog Logs v2, Monitors, and Metrics."""

    _instance: Optional["DatadogManager"] = None
    _lock = threading.RLock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_manager()
        return cls._instance

    def _init_manager(self):
        self.api_key = DATADOG_API_KEY
        self.app_key = DATADOG_APP_KEY
        self.site = DATADOG_SITE
        self.base_url = BASE_API_URL
        self._stats = {
            "queries_executed": 0,
            "queries_failed": 0,
            "started_at": datetime.utcnow().isoformat(),
        }

    @classmethod
    def get_instance(cls) -> "DatadogManager":
        if cls._instance is None:
            cls()
        return cls._instance

    def _get_headers(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json",
            "DD-API-KEY": self.api_key,
            "DD-APPLICATION-KEY": self.app_key,
        }

    def search_logs(
        self,
        query: str,
        from_time: Optional[str] = None,
        to_time: Optional[str] = None,
        limit: int = 20,
        indexes: Optional[List[str]] = None,
        sort: str = "-timestamp",
    ) -> Dict[str, Any]:
        """Queries Datadog Logs Search API v2."""
        now = datetime.utcnow()
        to_dt = to_time or now.strftime("%Y-%m-%dT%H:%M:%SZ")
        from_dt = from_time or (now - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")

        url = f"{self.base_url}/api/v2/logs/events/search"
        payload = {
            "filter": {
                "query": query,
                "from": from_dt,
                "to": to_dt,
                "indexes": indexes or ["*"],
            },
            "sort": sort,
            "page": {"limit": min(limit, 100)},
        }

        t0 = time.monotonic()
        try:
            resp = requests.post(url, headers=self._get_headers(), json=payload, timeout=20)
            elapsed = round((time.monotonic() - t0) * 1000, 1)
            if resp.ok:
                data = resp.json()
                raw_events = data.get("data", [])
                logs = []
                for ev in raw_events:
                    attrs = ev.get("attributes", {})
                    logs.append({
                        "id": ev.get("id"),
                        "timestamp": attrs.get("timestamp"),
                        "service": attrs.get("service"),
                        "host": attrs.get("host"),
                        "status": attrs.get("status"),
                        "message": attrs.get("message"),
                        "tags": attrs.get("tags", []),
                        "attributes": {
                            k: v for k, v in attrs.get("attributes", {}).items()
                            if k in ("job_instance_id", "job_execution_id", "correlationId", "clientCode", "propertyCode", "error", "exception")
                        },
                    })
                self._stats["queries_executed"] += 1
                return {
                    "success": True,
                    "query": query,
                    "from": from_dt,
                    "to": to_dt,
                    "count": len(logs),
                    "elapsed_ms": elapsed,
                    "logs": logs,
                }
            self._stats["queries_failed"] += 1
            return {
                "success": False,
                "error": f"HTTP {resp.status_code}: {resp.text[:300]}",
                "elapsed_ms": elapsed,
                "logs": [],
            }
        except Exception as exc:
            self._stats["queries_failed"] += 1
            return {"success": False, "error": str(exc), "logs": []}

    def list_monitors(self, name_filter: Optional[str] = None, tags: Optional[str] = None) -> Dict[str, Any]:
        """Fetches monitor definitions and states from Datadog API v1."""
        url = f"{self.base_url}/api/v1/monitor"
        params = {}
        if name_filter:
            params["name"] = name_filter
        if tags:
            params["tags"] = tags

        try:
            resp = requests.get(url, headers=self._get_headers(), params=params, timeout=15)
            if resp.ok:
                monitors = resp.json()
                results = []
                for m in monitors:
                    results.append({
                        "id": m.get("id"),
                        "name": m.get("name"),
                        "type": m.get("type"),
                        "status": m.get("overall_state"),
                        "tags": m.get("tags", []),
                        "message": m.get("message", "")[:200],
                    })
                return {"success": True, "count": len(results), "monitors": results}
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.text[:200]}"}
        except Exception as exc:
            return {"success": False, "error": str(exc)}

    def query_metrics(self, query: str, from_seconds_ago: int = 3600) -> Dict[str, Any]:
        """Queries timeseries metrics from Datadog Metrics API v1."""
        now_ts = int(time.time())
        from_ts = now_ts - from_seconds_ago
        url = f"{self.base_url}/api/v1/query"
        params = {"query": query, "from": from_ts, "to": now_ts}

        try:
            resp = requests.get(url, headers=self._get_headers(), params=params, timeout=15)
            if resp.ok:
                return {"success": True, "data": resp.json()}
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.text[:200]}"}
        except Exception as exc:
            return {"success": False, "error": str(exc)}

    def validate_api_keys(self) -> Dict[str, Any]:
        """Validates Datadog API and Application keys."""
        url = f"{self.base_url}/api/v1/validate"
        try:
            resp = requests.get(url, headers=self._get_headers(), timeout=8)
            if resp.ok:
                return {"valid": True, "site": self.site, "message": "Datadog API and APP keys are valid"}
            return {"valid": False, "site": self.site, "status_code": resp.status_code, "error": resp.text[:200]}
        except Exception as exc:
            return {"valid": False, "site": self.site, "error": str(exc)}


# Singleton instance
datadog_mgr = DatadogManager.get_instance()


# ==============================================================================
# MCP SPEC & TOOL DEFINITIONS (20 CANONICAL TOOLS)
# ==============================================================================
DATADOG_TOOLS = [
    # -------------------------------------------------------------
    # Group 1: Production Log Search & Querying (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "datadog_search_logs",
        "description": "Searches production log events in Datadog using the Logs Search API v2. Supports custom queries, date ranges, service filters, and status filters.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Datadog search query string (e.g. 'service:g3_app-prod-log status:error', 'deadlock OR timeout').",
                },
                "from_time": {
                    "type": "string",
                    "description": "Start timestamp in ISO 8601 format (e.g. '2026-09-11T12:00:00Z'). Defaults to 24h ago.",
                },
                "to_time": {
                    "type": "string",
                    "description": "End timestamp in ISO 8601 format. Defaults to now.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max log events to return (default: 20, max: 100).",
                    "default": 20,
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "datadog_search_logs_by_job_id",
        "description": "Searches for log events and execution traces specifically associated with a Spring Batch or RMS Job ID (@job_instance_id or @job_execution_id).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "job_id": {
                    "type": "string",
                    "description": "The Job Instance ID or Job Execution ID (e.g. '12345678').",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max results to return (default: 25).",
                    "default": 25,
                },
            },
            "required": ["job_id"],
        },
    },
    {
        "name": "datadog_search_service_errors",
        "description": "Retrieves recent error and critical logs (status:error OR status:critical) for a given microservice with full stack traces.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "service_name": {
                    "type": "string",
                    "description": "Microservice name (e.g. 'g3_app-prod-log', 'bmr-be-mo-service', '/ecs/prod/htng/', 'pmsinbound-internal').",
                },
                "hours_ago": {
                    "type": "integer",
                    "description": "Time horizon in hours to scan (default: 12).",
                    "default": 12,
                },
                "limit": {
                    "type": "integer",
                    "description": "Max logs to return (default: 15).",
                    "default": 15,
                },
            },
            "required": ["service_name"],
        },
    },
    {
        "name": "datadog_search_by_correlation_id",
        "description": "Traces an end-to-end transaction across all microservices using a unique correlationId, transaction ID, or requestTransactionId.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "correlation_id": {
                    "type": "string",
                    "description": "The unique transaction or correlation ID.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max results (default: 20).",
                    "default": 20,
                },
            },
            "required": ["correlation_id"],
        },
    },

    # -------------------------------------------------------------
    # Group 2: Microservice & Infrastructure Observability (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "datadog_list_services",
        "description": "Lists active IDeaS microservices and their operational domains monitored within Datadog.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "datadog_get_service_health",
        "description": "Calculates health telemetry for a service: total log volume, error count, warning count, and error ratio over the past 24 hours.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "service_name": {
                    "type": "string",
                    "description": "Microservice name.",
                },
            },
            "required": ["service_name"],
        },
    },
    {
        "name": "datadog_search_host_logs",
        "description": "Searches logs emitted by specific cloud hosts, EC2 instances, or ECS containers.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "host_name": {
                    "type": "string",
                    "description": "Hostname or container identifier.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max logs (default: 20).",
                    "default": 20,
                },
            },
            "required": ["host_name"],
        },
    },
    {
        "name": "datadog_tail_live_logs",
        "description": "Fetches the most recent live log stream for a service or tag in the past 15 minutes.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "service_name": {
                    "type": "string",
                    "description": "Service name to tail.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max events to tail (default: 10).",
                    "default": 10,
                },
            },
            "required": ["service_name"],
        },
    },

    # -------------------------------------------------------------
    # Group 3: Monitors, Alerts & Synthetics (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "datadog_list_monitors",
        "description": "Lists configured Datadog monitors, overall states (OK, Alert, Warn, No Data), and notification policies.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name_filter": {
                    "type": "string",
                    "description": "Optional substring to filter monitor names.",
                },
            },
            "required": [],
        },
    },
    {
        "name": "datadog_get_monitor_details",
        "description": "Fetches detailed threshold triggers, query expressions, and status history for a specific monitor ID.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "monitor_id": {
                    "type": "integer",
                    "description": "The Datadog monitor ID.",
                },
            },
            "required": ["monitor_id"],
        },
    },
    {
        "name": "datadog_get_active_alerts",
        "description": "Returns all monitors currently in an 'Alert' or 'Warn' state across production RMS environments.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "datadog_search_synthetics",
        "description": "Checks synthetic API and web browser test results for endpoint availability and response times.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },

    # -------------------------------------------------------------
    # Group 4: Metrics, Timeseries & APM Diagnostics (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "datadog_query_metrics",
        "description": "Queries raw timeseries metrics from Datadog Metrics API v1 (e.g. 'avg:system.cpu.user{*}', 'avg:jvm.heap_memory{*}').",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Datadog metric query expression.",
                },
                "seconds_ago": {
                    "type": "integer",
                    "description": "Time horizon in seconds (default: 3600).",
                    "default": 3600,
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "datadog_get_database_metrics",
        "description": "Queries database connection pool usage, active connections, and lock metrics for MSSQL and PostgreSQL clusters.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database_type": {
                    "type": "string",
                    "description": "Type of database: 'mssql' or 'postgres' (default: 'mssql').",
                    "default": "mssql",
                },
            },
            "required": [],
        },
    },
    {
        "name": "datadog_get_api_latency_metrics",
        "description": "Analyzes p50, p95, and p99 request latencies for core API gateways.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "service_name": {
                    "type": "string",
                    "description": "Service name to analyze.",
                },
            },
            "required": ["service_name"],
        },
    },
    {
        "name": "datadog_get_error_summary",
        "description": "Aggregates recurring error types and frequencies grouped by service and error message patterns.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "hours_ago": {
                    "type": "integer",
                    "description": "Scan window in hours (default: 6).",
                    "default": 6,
                },
            },
            "required": [],
        },
    },

    # -------------------------------------------------------------
    # Group 5: Incidents, Audit Logs & System Diagnostics (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "datadog_list_recent_incidents",
        "description": "Lists active or recently resolved Datadog production incidents and customer impact summaries.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "datadog_search_audit_trail",
        "description": "Queries Datadog user audit trails (dashboard edits, monitor muting, API key creation).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Audit filter query.",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "datadog_validate_credentials",
        "description": "Validates Datadog API Key and Application Key permissions and connectivity to datadoghq.com.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "datadog_get_system_stats",
        "description": "Reports server uptime, total queries executed, error counts, and site configurations.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "datadog_trace_pms_inbound_stream",
        "description": "Deep log tracer across PMS inbound microservices (pmsinbound-internal, htng, ais) filtered by propertyCode, reservationId, or error status.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "property_code": {"type": "string", "description": "Property code to trace (e.g. 'LONLK')."},
                "reservation_id": {"type": "string", "description": "Optional reservation ID or confirmation number."},
                "hours_ago": {"type": "integer", "description": "Lookback window in hours (default 12)."},
                "limit": {"type": "integer", "description": "Max log events to return (default 25)."},
            },
            "required": [],
        },
    },
    {
        "name": "datadog_trace_decision_delivery_errors",
        "description": "Searches Datadog error logs across outbound decision delivery pipelines (decision-delivery-internal, bmr-be-mo-service, ais-outbound-manager) for connection timeouts, schema rejections, and dropouts.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "property_code": {"type": "string", "description": "Optional property code filter."},
                "hours_ago": {"type": "integer", "description": "Lookback window in hours (default 12)."},
                "limit": {"type": "integer", "description": "Max log events to return (default 25)."},
            },
            "required": [],
        },
    },
]

DATADOG_RESOURCES = [
    {
        "uri": "datadog://system/status",
        "name": "Datadog API Live Connection Status",
        "description": "Real-time connection health, site target, and query execution counters.",
        "mimeType": "application/json",
    },
    {
        "uri": "datadog://services/catalog",
        "name": "Monitored Microservices Catalog",
        "description": "Directory of official IDeaS microservices monitored in Datadog.",
        "mimeType": "application/json",
    },
    {
        "uri": "datadog://alerts/active",
        "name": "Active Monitor Alerts",
        "description": "List of currently firing or warning alerts across production systems.",
        "mimeType": "application/json",
    },
]


# ==============================================================================
# TOOL DISPATCHER & EXECUTION ENGINE
# ==============================================================================
def execute_tool(name: str, arguments: Dict[str, Any]) -> Any:
    mgr = DatadogManager.get_instance()

    # --- Group 1: Log Search ---
    if name == "datadog_search_logs":
        q = arguments["query"]
        from_t = arguments.get("from_time")
        to_t = arguments.get("to_time")
        lim = int(arguments.get("limit", 20))
        return mgr.search_logs(q, from_time=from_t, to_time=to_t, limit=lim)

    elif name == "datadog_search_logs_by_job_id":
        jid = arguments["job_id"].strip()
        lim = int(arguments.get("limit", 25))
        q = f"@job_instance_id:{jid} OR @job_execution_id:{jid} OR \"{jid}\""
        return mgr.search_logs(q, limit=lim)

    elif name == "datadog_search_service_errors":
        svc = arguments["service_name"]
        h = int(arguments.get("hours_ago", 12))
        lim = int(arguments.get("limit", 15))
        from_dt = (datetime.utcnow() - timedelta(hours=h)).strftime("%Y-%m-%dT%H:%M:%SZ")
        q = f"service:{svc} AND (status:error OR status:critical)"
        return mgr.search_logs(q, from_time=from_dt, limit=lim)

    elif name == "datadog_search_by_correlation_id":
        cid = arguments["correlation_id"].strip()
        lim = int(arguments.get("limit", 20))
        q = f"@correlationId:{cid} OR \"{cid}\""
        return mgr.search_logs(q, limit=lim)

    # --- Group 2: Microservice Observability ---
    elif name == "datadog_list_services":
        return {"total_services": len(CORE_IDEAS_SERVICES), "services": CORE_IDEAS_SERVICES}

    elif name == "datadog_get_service_health":
        svc = arguments["service_name"]
        from_dt = (datetime.utcnow() - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")
        all_logs = mgr.search_logs(f"service:{svc}", from_time=from_dt, limit=50)
        err_logs = mgr.search_logs(f"service:{svc} AND status:error", from_time=from_dt, limit=50)
        total_cnt = all_logs.get("count", 0)
        err_cnt = err_logs.get("count", 0)
        return {
            "service": svc,
            "horizon": "Last 24 Hours",
            "sampled_total_logs": total_cnt,
            "sampled_error_logs": err_cnt,
            "health_verdict": "HEALTHY" if err_cnt == 0 else ("DEGRADED" if err_cnt < 10 else "UNHEALTHY"),
            "recent_errors": err_logs.get("logs", [])[:3],
        }

    elif name == "datadog_search_host_logs":
        host = arguments["host_name"]
        lim = int(arguments.get("limit", 20))
        return mgr.search_logs(f"host:{host}", limit=lim)

    elif name == "datadog_tail_live_logs":
        svc = arguments["service_name"]
        lim = int(arguments.get("limit", 10))
        from_dt = (datetime.utcnow() - timedelta(minutes=15)).strftime("%Y-%m-%dT%H:%M:%SZ")
        return mgr.search_logs(f"service:{svc}", from_time=from_dt, limit=lim)

    # --- Group 3: Monitors & Alerts ---
    elif name == "datadog_list_monitors":
        filt = arguments.get("name_filter")
        return mgr.list_monitors(name_filter=filt)

    elif name == "datadog_get_monitor_details":
        mid = arguments["monitor_id"]
        url = f"{mgr.base_url}/api/v1/monitor/{mid}"
        try:
            r = requests.get(url, headers=mgr._get_headers(), timeout=10)
            return r.json() if r.ok else {"error": f"HTTP {r.status_code}"}
        except Exception as exc:
            return {"error": str(exc)}

    elif name == "datadog_get_active_alerts":
        res = mgr.list_monitors()
        if res.get("success"):
            alerts = [m for m in res.get("monitors", []) if m.get("status") in ("Alert", "Warn")]
            return {"active_alerts_count": len(alerts), "alerts": alerts}
        return res

    elif name == "datadog_search_synthetics":
        url = f"{mgr.base_url}/api/v1/synthetics/tests"
        try:
            r = requests.get(url, headers=mgr._get_headers(), timeout=10)
            return r.json() if r.ok else {"error": f"HTTP {r.status_code}"}
        except Exception as exc:
            return {"error": str(exc)}

    # --- Group 4: Metrics & APM ---
    elif name == "datadog_query_metrics":
        q = arguments["query"]
        secs = int(arguments.get("seconds_ago", 3600))
        return mgr.query_metrics(q, from_seconds_ago=secs)

    elif name == "datadog_get_database_metrics":
        db_type = arguments.get("database_type", "mssql").lower()
        q = "avg:sqlserver.stats.connections{*}" if db_type == "mssql" else "avg:postgresql.connections{*}"
        return mgr.query_metrics(q, from_seconds_ago=1800)

    elif name == "datadog_get_api_latency_metrics":
        svc = arguments["service_name"]
        q = f"avg:trace.{svc}.request.duration{{*}}"
        return mgr.query_metrics(q, from_seconds_ago=1800)

    elif name == "datadog_get_error_summary":
        h = int(arguments.get("hours_ago", 6))
        from_dt = (datetime.utcnow() - timedelta(hours=h)).strftime("%Y-%m-%dT%H:%M:%SZ")
        res = mgr.search_logs("status:error", from_time=from_dt, limit=50)
        logs = res.get("logs", [])
        svc_counts = {}
        for l in logs:
            s = l.get("service") or "unknown"
            svc_counts[s] = svc_counts.get(s, 0) + 1
        return {
            "window_hours": h,
            "total_errors_sampled": len(logs),
            "errors_by_service": svc_counts,
        }

    # --- Group 5: Incidents & Diagnostics ---
    elif name == "datadog_list_recent_incidents":
        url = f"{mgr.base_url}/api/v2/incidents"
        try:
            r = requests.get(url, headers=mgr._get_headers(), timeout=10)
            return r.json() if r.ok else {"error": f"HTTP {r.status_code}"}
        except Exception as exc:
            return {"error": str(exc)}

    elif name == "datadog_search_audit_trail":
        q = arguments["query"]
        url = f"{mgr.base_url}/api/v2/audit/events"
        try:
            r = requests.get(url, headers=mgr._get_headers(), params={"filter[query]": q}, timeout=10)
            return r.json() if r.ok else {"error": f"HTTP {r.status_code}"}
        except Exception as exc:
            return {"error": str(exc)}

    elif name == "datadog_validate_credentials":
        return mgr.validate_api_keys()

    elif name == "datadog_get_system_stats":
        with mgr._lock:
            return {
                "site": mgr.site,
                "uptime_started": mgr._stats["started_at"],
                "queries_executed": mgr._stats["queries_executed"],
                "queries_failed": mgr._stats["queries_failed"],
            }

    elif name == "datadog_trace_pms_inbound_stream":
        pcode = arguments.get("property_code", "").strip()
        rid = arguments.get("reservation_id", "").strip()
        h = int(arguments.get("hours_ago", 12))
        lim = int(arguments.get("limit", 25))
        from_dt = (datetime.utcnow() - timedelta(hours=h)).strftime("%Y-%m-%dT%H:%M:%SZ")

        query_parts = ["(service:pmsinbound-internal OR service:/ecs/prod/htng/ OR service:ais-outbound-manager)"]
        if pcode:
            query_parts.append(f'("{pcode}" OR @property_code:{pcode})')
        if rid:
            query_parts.append(f'("{rid}" OR @reservation_id:{rid} OR @confirmation_number:{rid})')

        full_q = " AND ".join(query_parts)
        return mgr.search_logs(full_q, from_time=from_dt, limit=lim)

    elif name == "datadog_trace_decision_delivery_errors":
        pcode = arguments.get("property_code", "").strip()
        h = int(arguments.get("hours_ago", 12))
        lim = int(arguments.get("limit", 25))
        from_dt = (datetime.utcnow() - timedelta(hours=h)).strftime("%Y-%m-%dT%H:%M:%SZ")

        query_parts = ["(service:decision-delivery-internal OR service:bmr-be-mo-service OR service:ais-outbound-manager)", "(status:error OR status:critical)"]
        if pcode:
            query_parts.append(f'("{pcode}" OR @property_code:{pcode})')

        full_q = " AND ".join(query_parts)
        return mgr.search_logs(full_q, from_time=from_dt, limit=lim)

    else:
        raise ValueError(f"Unknown tool name: {name}")


def read_resource(uri: str) -> str:
    mgr = DatadogManager.get_instance()
    if uri == "datadog://system/status":
        return json.dumps({
            "site": mgr.site,
            "api_key_configured": bool(mgr.api_key),
            "app_key_configured": bool(mgr.app_key),
            "stats": mgr._stats,
        }, indent=2)
    elif uri == "datadog://services/catalog":
        return json.dumps(CORE_IDEAS_SERVICES, indent=2)
    elif uri == "datadog://alerts/active":
        return json.dumps(mgr.list_monitors(), indent=2)
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

    app = FastAPI(title="Datadog Observability MCP Server", version="1.0.0")

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
        mgr = DatadogManager.get_instance()
        return {
            "status": "HEALTHY",
            "server": "datadog-mcp-server",
            "version": "1.0.0",
            "transport": "HTTP SSE + Stdio",
            "mcp_version": "2024-11-05",
            "total_tools": len(DATADOG_TOOLS),
            "total_resources": len(DATADOG_RESOURCES),
            "datadog": {
                "site": mgr.site,
                "api_key_set": bool(mgr.api_key),
                "app_key_set": bool(mgr.app_key),
                "queries_executed": mgr._stats["queries_executed"],
            },
        }

    @app.get("/sse")
    async def sse_endpoint(request: Request):
        session_id = f"dd_sess_{int(time.time()*1000)}_{os.urandom(4).hex()}"
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
                        "name": "datadog-mcp-server",
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
                    "tools": DATADOG_TOOLS,
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
                    "resources": DATADOG_RESOURCES,
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
    logger.info("Starting Datadog MCP Server in Stdio transport mode...")
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
    parser = argparse.ArgumentParser(description="Datadog Observability MCP Server")
    parser.add_argument("--stdio", action="store_true", help="Run in Stdio transport mode")
    parser.add_argument("--host", default=MCP_HOST, help=f"Host to bind (default: {MCP_HOST})")
    parser.add_argument("--port", type=int, default=MCP_PORT, help=f"Port to bind (default: {MCP_PORT})")
    args = parser.parse_args()

    if args.stdio:
        run_stdio_transport()
    else:
        import uvicorn
        logger.info("Starting Datadog MCP Server on %s:%d (SSE Transport)...", args.host, args.port)
        app = create_app()
        uvicorn.run(app, host=args.host, port=args.port, log_level="warning")


if __name__ == "__main__":
    main()
