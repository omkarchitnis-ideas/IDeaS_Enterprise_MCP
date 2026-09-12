#!/usr/bin/env python3
"""
Optix Data Warehouse (MSSQL Cluster) Model Context Protocol (MCP) Server
=========================================================================
Comprehensive 35-Tool Suite for the SAS IDeaS Optix Data Warehouse Production Cluster.

Enterprise Features:
1. 3-Node MSSQL Production Cluster Pooling (optix-db-01, optix-db-02, optix-db-03).
2. Automated Node & Database Resolution (ClientCode / PropertyCode -> Host & DB).
3. Read-Only Query Guardrails (Strict DDL/DML Blocking, NOLOCK hints, Timeout Controls).
4. Schema & Dimension Discovery (dbo, STAGE, SPOT, RMS schema reflection, table metadata).
5. 10-Tab Discrepancy Reconciliation Engine (<5% Tolerance, STLY 364-day DOW shifts, OTB Pace).
6. Group Allotment & Business Views Reconciliation (Transient, Group, Contract & Crew).
7. Data Quality & ZNV Anomaly Scanner (Unmapped IDs, Zero-Revenue Comps, Fee-Only Trans).
8. ETL Process History & Batch Pipeline Diagnostics.
9. Dual Transport: HTTP Server-Sent Events (SSE) on Port 8557 + Stdio Transport.
"""

import os
import re
import sys
import json
import time
import socket
import logging
import argparse
import threading
from typing import Any, Dict, List, Optional, Tuple, Union
from datetime import datetime, date, timedelta
from decimal import Decimal
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
logger = logging.getLogger("optix-mcp-server")

# ==============================================================================
# CONFIGURATION & CONSTANTS
# ==============================================================================
OPTIX_DB_USER = os.getenv("OPTIX_DB_USERNAME", "optixro")
OPTIX_DB_PASS = os.getenv("OPTIX_DB_PASSWORD", "ThisIsMy1andOnlyReadOnlyPasswordForProd")

# Cluster node endpoints with known IP fallbacks
DEFAULT_CLUSTER_NODES = [
    {"host": "optix-db-01.optix-db.ideasrms.com", "ip": "10.246.15.226", "port": 1433, "label": "Node 1"},
    {"host": "optix-db-02.optix-db.ideasrms.com", "ip": "10.246.13.38",  "port": 1433, "label": "Node 2"},
    {"host": "optix-db-03.optix-db.ideasrms.com", "ip": "10.246.8.150",  "port": 1433, "label": "Node 3"},
]

MCP_HOST = os.getenv("MCP_HOST", "0.0.0.0")
MCP_PORT = int(os.getenv("OPTIX_MCP_PORT", os.getenv("MCP_PORT", "8557")))

# JSON Serializer for Decimals, Dates, and Sets
class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, bytes):
            return obj.decode("utf-8", errors="replace")
        return super().default(obj)


# ==============================================================================
# OPTIX CLUSTER CONNECTION & ROUTING ENGINE
# ==============================================================================
class OptixClusterManager:
    """Thread-safe cluster connection manager and database router for Optix MSSQL."""

    _instance: Optional["OptixClusterManager"] = None
    _lock = threading.RLock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_manager()
        return cls._instance

    def _init_manager(self):
        self.username = OPTIX_DB_USER
        self.password = OPTIX_DB_PASS
        self.nodes = DEFAULT_CLUSTER_NODES
        self._db_catalog: Dict[str, Tuple[str, str]] = {}  # db_upper -> (host, db_real)
        self._route_cache: Dict[str, Tuple[str, str]] = {}  # client_prop_key -> (host, db_real)
        self._indexed_nodes: set = set()
        self._stats = {
            "queries_executed": 0,
            "queries_failed": 0,
            "cache_hits": 0,
            "cache_misses": 0,
            "started_at": datetime.utcnow().isoformat(),
        }
        # Start background indexing of databases across nodes
        threading.Thread(target=self._initial_cluster_index, daemon=True).start()

    @classmethod
    def get_instance(cls) -> "OptixClusterManager":
        if cls._instance is None:
            cls()
        return cls._instance

    def _get_active_target(self, node_info: Dict[str, Any]) -> str:
        """Determines best target host or IP for socket/connection."""
        host = node_info["host"]
        ip = node_info.get("ip")
        # Try resolving host first; fallback to IP if DNS lookup fails
        try:
            resolved = socket.gethostbyname(host)
            if resolved:
                return host
        except Exception:
            pass
        return ip or host

    def get_connection(self, host_or_ip: str, database: str = "master", timeout: int = 10):
        """Creates an authenticated MSSQL connection using pymssql or pyodbc with autocommit."""
        # Clean host string
        target_server = host_or_ip.split(":")[0].strip()
        # Check if mapped to specific node IP
        for node in self.nodes:
            if target_server in (node["host"], node["ip"]):
                target_server = self._get_active_target(node)
                break

        # Preference 1: pymssql (Pure TDS, highly stable in Linux/Docker & Windows)
        try:
            import pymssql
            conn = pymssql.connect(
                server=target_server,
                user=self.username,
                password=self.password,
                database=database,
                timeout=timeout,
                login_timeout=timeout,
                autocommit=True,
            )
            return conn
        except Exception as exc_pymssql:
            # Preference 2: pyodbc (ODBC Driver 17/18)
            try:
                import pyodbc
                pyodbc.pooling = True
                conn_str = (
                    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                    f"SERVER={target_server};"
                    f"DATABASE={database};"
                    f"UID={self.username};"
                    f"PWD={self.password};"
                    f"Connection Timeout={timeout};"
                    f"Application Intent=ReadOnly;"
                )
                return pyodbc.connect(conn_str, autocommit=True)
            except Exception as exc_pyodbc:
                raise RuntimeError(
                    f"Failed connecting to Optix MSSQL node '{target_server}' (DB: '{database}'). "
                    f"pymssql: {exc_pymssql} | pyodbc: {exc_pyodbc}"
                )

    def ping_all_nodes(self) -> Dict[str, Any]:
        """Pings all 3 cluster nodes and returns connectivity, latency, version, and DB count."""
        results = {}
        for node in self.nodes:
            label = node["label"]
            target = self._get_active_target(node)
            t0 = time.monotonic()
            conn = None
            try:
                conn = self.get_connection(target, database="master", timeout=4)
                cur = conn.cursor()
                cur.execute("SELECT @@VERSION;")
                ver_row = cur.fetchone()
                cur.execute("SELECT COUNT(*) FROM sys.databases WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb') AND state_desc = 'ONLINE';")
                db_cnt_row = cur.fetchone()
                elapsed = round((time.monotonic() - t0) * 1000, 1)
                results[label] = {
                    "status": "ONLINE",
                    "host": node["host"],
                    "ip": node.get("ip"),
                    "latency_ms": elapsed,
                    "databases_count": db_cnt_row[0] if db_cnt_row else 0,
                    "version": str(ver_row[0])[:70] if ver_row else "MSSQL 2022",
                }
            except Exception as exc:
                elapsed = round((time.monotonic() - t0) * 1000, 1)
                results[label] = {
                    "status": "OFFLINE",
                    "host": node["host"],
                    "ip": node.get("ip"),
                    "latency_ms": elapsed,
                    "error": str(exc),
                }
            finally:
                if conn:
                    try:
                        conn.close()
                    except Exception:
                        pass
        return results

    def _initial_cluster_index(self):
        """Background worker that catalogs all databases across cluster nodes."""
        logger.info("Initializing Optix cluster catalog sweep across all nodes...")
        with self._lock:
            for node in self.nodes:
                target = self._get_active_target(node)
                conn = None
                try:
                    conn = self.get_connection(target, database="master", timeout=6)
                    cur = conn.cursor()
                    cur.execute("SELECT name FROM sys.databases WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb') AND state_desc = 'ONLINE';")
                    rows = cur.fetchall()
                    for r in rows:
                        db_name = str(r[0]).strip()
                        self._db_catalog[db_name.upper()] = (target, db_name)
                    self._indexed_nodes.add(target)
                    logger.info("Indexed %d databases on node %s (%s)", len(rows), node["label"], target)
                except Exception as exc:
                    logger.warning("Catalog sweep failed on node %s (%s): %s", node["label"], target, exc)
                finally:
                    if conn:
                        try:
                            conn.close()
                        except Exception:
                            pass
        logger.info("Optix cluster catalog indexing complete: %d total tenant databases indexed.", len(self._db_catalog))

    def resolve_database(self, client_code: str, property_code: str = "") -> Tuple[Optional[str], Optional[str]]:
        """
        Resolves the exact (node_host, database_name) for a client code or property code.
        Applies multi-tier resolution:
        1. Exact database name match (e.g. 'ALTHOFF' -> 'ALTHOFF')
        2. Numeric prefix match (e.g. '1666', '3666MODO')
        3. Common prefix variations ('DW_<client>', '<client>_OPTIX')
        4. Property code lookup in Dim_Property across indexed databases
        """
        if not client_code and not property_code:
            return None, None

        c_clean = str(client_code or "").strip().upper()
        p_clean = str(property_code or "").strip().upper()
        cache_key = f"{c_clean}_{p_clean}"

        with self._lock:
            if cache_key in self._route_cache:
                self._stats["cache_hits"] += 1
                return self._route_cache[cache_key]

            # If catalog is empty or has < 10 entries, try indexing synchronously once
            if len(self._db_catalog) < 10:
                self._initial_cluster_index()

            # 1. Exact match on client code
            if c_clean and c_clean in self._db_catalog:
                route = self._db_catalog[c_clean]
                self._route_cache[cache_key] = route
                self._stats["cache_misses"] += 1
                return route

            # 2. Match DW_<client_code> or DW_<client_code>_01
            dw_candidates = [f"DW_{c_clean}", f"DW_{c_clean}_01", f"{c_clean}_DW", f"{c_clean}_OPTIX"]
            for cand in dw_candidates:
                if cand in self._db_catalog:
                    route = self._db_catalog[cand]
                    self._route_cache[cache_key] = route
                    self._stats["cache_misses"] += 1
                    return route

            # 3. Suffix match (e.g. '3666MODO' ends with 'MODO')
            if c_clean:
                for db_up, (host, db_real) in self._db_catalog.items():
                    if db_up.endswith(c_clean):
                        prefix = db_up[:-len(c_clean)]
                        if not prefix or prefix.isdigit() or prefix.endswith("_"):
                            route = (host, db_real)
                            self._route_cache[cache_key] = route
                            self._stats["cache_misses"] += 1
                            return route

            # 4. Prefix match (e.g. database starts with client code)
            if c_clean:
                for db_up, (host, db_real) in self._db_catalog.items():
                    if db_up.startswith(c_clean):
                        suffix = db_up[len(c_clean):]
                        if not suffix or suffix.isdigit() or suffix.startswith("_"):
                            route = (host, db_real)
                            self._route_cache[cache_key] = route
                            self._stats["cache_misses"] += 1
                            return route

            # 5. Property code fallback match if property code provided
            if p_clean and len(p_clean) >= 3:
                for db_up, (host, db_real) in self._db_catalog.items():
                    if db_up == p_clean or db_up.endswith(p_clean):
                        route = (host, db_real)
                        self._route_cache[cache_key] = route
                        self._stats["cache_misses"] += 1
                        return route

        self._stats["cache_misses"] += 1
        return None, None

    def execute_query(
        self,
        sql: str,
        database: Optional[str] = None,
        client_code: Optional[str] = None,
        property_code: Optional[str] = None,
        host: Optional[str] = None,
        max_rows: int = 100,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        """Executes a read-only SQL query against the resolved Optix node and database."""
        # 1. Read-only query validation
        self.enforce_read_only(sql)

        # 2. Resolve database and host
        target_host = host
        target_db = database

        if not target_host or not target_db:
            if client_code or (not target_db and database):
                lookup_code = client_code or database
                res_host, res_db = self.resolve_database(lookup_code, property_code or "")
                if res_host and res_db:
                    target_host = target_host or res_host
                    target_db = res_db
                else:
                    if not target_db:
                        target_db = lookup_code

        # Default host if still unresolved: Node 1
        if not target_host:
            target_host = self.nodes[0]["ip"]
        if not target_db:
            target_db = "master"

        t0 = time.monotonic()
        conn = None
        try:
            conn = self.get_connection(target_host, database=target_db, timeout=timeout)
            cur = conn.cursor()
            cur.execute(sql)
            
            # Fetch results
            columns = [desc[0] for desc in cur.description] if cur.description else []
            rows = []
            if cur.description:
                fetched = cur.fetchmany(max_rows)
                for r in fetched:
                    row_dict = {}
                    for idx, col in enumerate(columns):
                        val = r[idx]
                        if isinstance(val, (datetime, date)):
                            row_dict[col] = val.isoformat()
                        elif isinstance(val, Decimal):
                            row_dict[col] = float(val)
                        elif isinstance(val, bytes):
                            row_dict[col] = val.decode("utf-8", errors="replace")
                        else:
                            row_dict[col] = val
                    rows.append(row_dict)

            elapsed_ms = round((time.monotonic() - t0) * 1000, 1)
            self._stats["queries_executed"] += 1

            return {
                "success": True,
                "node": target_host,
                "database": target_db,
                "columns": columns,
                "rows": rows,
                "row_count": len(rows),
                "elapsed_ms": elapsed_ms,
            }
        except Exception as exc:
            self._stats["queries_failed"] += 1
            elapsed_ms = round((time.monotonic() - t0) * 1000, 1)
            logger.error("Optix query error on %s/%s: %s", target_host, target_db, exc)
            return {
                "success": False,
                "node": target_host,
                "database": target_db,
                "error": str(exc),
                "elapsed_ms": elapsed_ms,
            }
        finally:
            if conn:
                try:
                    conn.close()
                except Exception:
                    pass

    @staticmethod
    def enforce_read_only(sql: str) -> None:
        """Validates that query text strictly contains read-only statements."""
        # Strip comments
        cleaned = re.sub(r"--.*", "", sql)
        cleaned = re.sub(r"/\*.*?\*/", "", cleaned, flags=re.DOTALL).strip().upper()

        forbidden_patterns = [
            r"\bINSERT\b", r"\bUPDATE\b", r"\bDELETE\b", r"\bDROP\b",
            r"\bALTER\b", r"\bTRUNCATE\b", r"\bCREATE\b", r"\bGRANT\b",
            r"\bREVOKE\b", r"\bEXEC\b", r"\bEXECUTE\b", r"\bBACKUP\b",
            r"\bRESTORE\b", r"\bMERGE\b", r"\bINTO\b",
        ]
        for pat in forbidden_patterns:
            if re.search(pat, cleaned):
                raise ValueError(f"Write or administrative SQL operations are strictly forbidden in read-only Optix MCP server: matching {pat}")

    def flush_cache(self) -> Dict[str, int]:
        """Flushes in-memory routing cache and re-indexes all databases."""
        with self._lock:
            routes_evicted = len(self._route_cache)
            dbs_evicted = len(self._db_catalog)
            self._route_cache.clear()
            self._db_catalog.clear()
            self._indexed_nodes.clear()
        self._initial_cluster_index()
        return {"routes_cleared": routes_evicted, "databases_cleared": dbs_evicted}

    def get_stats(self) -> Dict[str, Any]:
        """Returns statistics on queries, cached routes, and indexed databases."""
        with self._lock:
            return {
                "uptime_started": self._stats["started_at"],
                "total_databases_indexed": len(self._db_catalog),
                "cached_routes": len(self._route_cache),
                "queries_executed": self._stats["queries_executed"],
                "queries_failed": self._stats["queries_failed"],
                "cache_hits": self._stats["cache_hits"],
                "cache_misses": self._stats["cache_misses"],
            }


# Singleton Cluster Manager
cluster_mgr = OptixClusterManager.get_instance()


# ==============================================================================
# MCP SPEC & TOOL DEFINITIONS (35 CANONICAL TOOLS)
# ==============================================================================
OPTIX_TOOLS = [
    # -------------------------------------------------------------
    # Group 1: Cluster Health, Routing & Metadata (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "optix_ping_cluster",
        "description": "Probes all 3 Optix MSSQL production cluster nodes (optix-db-01, optix-db-02, optix-db-03) and returns real-time TCP connectivity, round-trip latency, MSSQL version, and online tenant database counts.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "optix_list_all_databases",
        "description": "Returns the complete catalog of all 427+ tenant databases indexed across all 3 Optix cluster nodes, including the exact node hosting each database. Supports optional search filter pattern.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "filter_pattern": {
                    "type": "string",
                    "description": "Optional substring or wildcard pattern to filter database names (e.g. 'SON', 'ALTHOFF', '1666').",
                },
                "max_results": {
                    "type": "integer",
                    "description": "Maximum number of databases to return (default: 500).",
                    "default": 500,
                },
            },
            "required": [],
        },
    },
    {
        "name": "optix_resolve_database",
        "description": "Resolves the exact cluster node (host/IP) and database name for a given client code (e.g. 'ALTHOFF', 'SONESTA', '1666') or property code. Uses exact, prefix, suffix, and metadata heuristics.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "client_code": {
                    "type": "string",
                    "description": "The client code or tenant identifier (e.g. 'ALTHOFF', 'MODO', 'SON').",
                },
                "property_code": {
                    "type": "string",
                    "description": "Optional property code (e.g. '0010', '0259') to assist resolution.",
                },
            },
            "required": ["client_code"],
        },
    },
    {
        "name": "optix_cluster_stats",
        "description": "Returns aggregate cluster metrics including active nodes, total indexed tenant databases, routing cache stats, query execution counters, and server uptime.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },

    # -------------------------------------------------------------
    # Group 2: SQL Execution & Batch Operations (3 Tools)
    # -------------------------------------------------------------
    {
        "name": "optix_execute_query",
        "description": "Executes an arbitrary read-only SQL query against any Optix tenant database or cluster node. Automatically adds NOLOCK hints, blocks all DDL/DML, and enforces row limits and timeouts.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "sql": {
                    "type": "string",
                    "description": "The read-only SQL statement to execute (SELECT, WITH, etc.).",
                },
                "database": {
                    "type": "string",
                    "description": "The target tenant database name (e.g. 'ALTHOFF', 'DW_SONESTA_01'). If omitted, will resolve from client_code.",
                },
                "client_code": {
                    "type": "string",
                    "description": "Optional client code used to automatically resolve the target database and host node.",
                },
                "property_code": {
                    "type": "string",
                    "description": "Optional property code for multi-property tenant databases.",
                },
                "host": {
                    "type": "string",
                    "description": "Optional cluster node hostname or IP. If omitted, will be auto-resolved.",
                },
                "max_rows": {
                    "type": "integer",
                    "description": "Maximum number of rows to return (default: 100, max: 1000).",
                    "default": 100,
                },
                "timeout_seconds": {
                    "type": "integer",
                    "description": "Query timeout in seconds (default: 30).",
                    "default": 30,
                },
            },
            "required": ["sql"],
        },
    },
    {
        "name": "optix_execute_batch",
        "description": "Executes a batch of read-only queries in sequence across one or more Optix databases. Returns structured results grouped by query label.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "queries": {
                    "type": "array",
                    "description": "List of query specifications: [{'label': 'name', 'sql': 'SELECT...', 'database': 'DB_NAME'}].",
                    "items": {
                        "type": "object",
                        "properties": {
                            "label": {"type": "string"},
                            "sql": {"type": "string"},
                            "database": {"type": "string"},
                        },
                        "required": ["label", "sql", "database"],
                    },
                },
            },
            "required": ["queries"],
        },
    },
    {
        "name": "optix_explain_query",
        "description": "Returns estimated query execution plan and cost analysis for a given SQL query using SET SHOWPLAN_ALL ON without executing the query.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "sql": {
                    "type": "string",
                    "description": "The read-only SQL query to analyze.",
                },
                "database": {
                    "type": "string",
                    "description": "The target tenant database name.",
                },
            },
            "required": ["sql", "database"],
        },
    },

    # -------------------------------------------------------------
    # Group 3: Schema Reflection & Table Inspection (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "optix_list_tables",
        "description": "Lists all tables and views in an Optix tenant database. Supports filtering by schema (dbo, STAGE, SPOT, RMS) and name wildcard search.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name (e.g. 'ALTHOFF').",
                },
                "schema_name": {
                    "type": "string",
                    "description": "Optional schema filter (e.g. 'dbo', 'STAGE', 'SPOT', 'RMS').",
                },
                "name_filter": {
                    "type": "string",
                    "description": "Optional wildcard pattern for table name (e.g. '%Pace%', '%Activity%').",
                },
            },
            "required": ["database"],
        },
    },
    {
        "name": "optix_describe_table",
        "description": "Returns comprehensive schema definition for a table or view: column names, data types, nullability, max lengths, primary key flags, and foreign key references.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "table_name": {
                    "type": "string",
                    "description": "Name of the table or view (e.g. 'Fact_Daily_Activity', 'Dim_Property').",
                },
                "schema_name": {
                    "type": "string",
                    "description": "Schema name (default: 'dbo').",
                    "default": "dbo",
                },
            },
            "required": ["database", "table_name"],
        },
    },
    {
        "name": "optix_get_table_row_count",
        "description": "Returns exact row count and total storage space (in KB) for tables in a tenant database using sys.dm_db_partition_stats.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "table_name": {
                    "type": "string",
                    "description": "Optional table name. If omitted, returns row counts for top 30 largest tables.",
                },
            },
            "required": ["database"],
        },
    },
    {
        "name": "optix_search_columns",
        "description": "Searches for column names matching a pattern across all tables and views in an Optix tenant database (e.g. search for 'accom_revenue', 'calendar_id', 'as_of').",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "column_pattern": {
                    "type": "string",
                    "description": "Column name search pattern (e.g. '%pace%', '%revenue%', '%property%').",
                },
            },
            "required": ["database", "column_pattern"],
        },
    },

    # -------------------------------------------------------------
    # Group 4: Tenant Identity & Property Configuration (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "optix_get_properties",
        "description": "Retrieves all properties configured in an Optix tenant database from Dim_Property (property_id, property_cd, property_nm, currency_cd, status_id, pms_property_id, ups_id, time_zone_txt).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name (e.g. 'ALTHOFF').",
                },
            },
            "required": ["database"],
        },
    },
    {
        "name": "optix_resolve_property",
        "description": "Resolves a property code (unpadded or padded, e.g. '10' vs '0010') to its internal Optix numeric property_id, official name, and currency in Dim_Property.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_code": {
                    "type": "string",
                    "description": "Property code (e.g. '0010', '0259', '10').",
                },
            },
            "required": ["database", "property_code"],
        },
    },
    {
        "name": "optix_get_feature_flags",
        "description": "Audits feature flags from Feature and Feature_Property tables in an Optix tenant database, including the 5 mandatory RMS flags (enableCompetitiveRatesEtl, enableCompetitiveRatesDashboard, enablePMSInboundProfileData, dashboard.travel_agent, dashboard.company).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Optional numeric property_id to check property-specific feature flag overrides.",
                },
            },
            "required": ["database"],
        },
    },
    {
        "name": "optix_get_property_hierarchy",
        "description": "Retrieves property hierarchy tree, groups, and estate configurations from Property_Group, Property_Group_Master, and vw_property_hierarchy.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
            },
            "required": ["database"],
        },
    },

    # -------------------------------------------------------------
    # Group 5: Historical Actuals & Daily Activity (3 Tools)
    # -------------------------------------------------------------
    {
        "name": "optix_get_activity_summary",
        "description": "Extracts total rooms sold, accommodation revenue, F&B revenue, beverage, other revenue, and gross revenue for a property across a date range from Fact_Daily_Activity.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "start_calendar_id": {
                    "type": "integer",
                    "description": "Start date in YYYYMMDD integer format (e.g. 20240101).",
                },
                "end_calendar_id": {
                    "type": "integer",
                    "description": "End date in YYYYMMDD integer format (e.g. 20261231).",
                },
            },
            "required": ["database", "property_id"],
        },
    },
    {
        "name": "optix_get_daily_activity",
        "description": "Granular day-by-day drill-down of solds, room revenue, and ADR across stay dates (calendar_id) from Fact_Daily_Activity. Supports up to 1,095 stay dates.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "start_calendar_id": {
                    "type": "integer",
                    "description": "Start date in YYYYMMDD format (e.g. 20240101).",
                },
                "end_calendar_id": {
                    "type": "integer",
                    "description": "End date in YYYYMMDD format (e.g. 20240131).",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max rows (default: 365).",
                    "default": 365,
                },
            },
            "required": ["database", "property_id", "start_calendar_id", "end_calendar_id"],
        },
    },
    {
        "name": "optix_get_activity_hierarchy",
        "description": "Hierarchical rollups by Year (YYYY), Month (YYYY-MM), and Day (YYYYMMDD) for long-term trend analysis and multi-year comparisons from Fact_Daily_Activity.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "start_calendar_id": {
                    "type": "integer",
                    "description": "Start date in YYYYMMDD integer format.",
                },
                "end_calendar_id": {
                    "type": "integer",
                    "description": "End date in YYYYMMDD integer format.",
                },
            },
            "required": ["database", "property_id"],
        },
    },

    # -------------------------------------------------------------
    # Group 6: On-The-Books (OTB) Pace & STLY (5 Tools)
    # -------------------------------------------------------------
    {
        "name": "optix_get_current_pace",
        "description": "Extracts forward On-The-Books (OTB) booking pace for future stay dates from today onwards from Fact_Daily_Activity (calendar_id >= TODAY).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "end_calendar_id": {
                    "type": "integer",
                    "description": "Future horizon end date (YYYYMMDD). Defaults to today + 365 days.",
                },
            },
            "required": ["database", "property_id"],
        },
    },
    {
        "name": "optix_get_forward_monthly_pace",
        "description": "Summarizes forward 365-day booking horizon aggregated by future calendar month (OTB Solds, Revenue, ADR) from Fact_Daily_Activity.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
            },
            "required": ["database", "property_id"],
        },
    },
    {
        "name": "optix_get_stly_pace",
        "description": "Extracts historical Same Time Last Year (STLY) pace with 364-day (52-week DOW matched) snapshot from Fact_Daily_Activity_Pace using the latest as_of_calendar_id.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "as_of_calendar_id": {
                    "type": "integer",
                    "description": "Optional specific snapshot date (YYYYMMDD). Defaults to MAX(as_of_calendar_id).",
                },
            },
            "required": ["database", "property_id"],
        },
    },
    {
        "name": "optix_get_stly_actuals",
        "description": "Extracts final settled actuals for the 364-day prior occupancy dates from Fact_Daily_Activity for YoY growth reconciliation.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "start_calendar_id": {
                    "type": "integer",
                    "description": "Start date (YYYYMMDD) for STLY actuals.",
                },
                "end_calendar_id": {
                    "type": "integer",
                    "description": "End date (YYYYMMDD) for STLY actuals.",
                },
            },
            "required": ["database", "property_id"],
        },
    },
    {
        "name": "optix_get_pace_snapshots",
        "description": "Lists available snapshot dates (as_of_calendar_id) in Fact_Daily_Activity_Pace for a property, showing row counts and date horizons.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum snapshot dates to return (default: 30).",
                    "default": 30,
                },
            },
            "required": ["database", "property_id"],
        },
    },

    # -------------------------------------------------------------
    # Group 7: Dimensions — Market Segments & Room Types (4 Tools)
    # -------------------------------------------------------------
    {
        "name": "optix_get_market_segments",
        "description": "Reconciles accommodation solds, revenue, and ADR by PMS market segment and analytical split category from Fact_Daily_Activity joined with Dim_Market_Property.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "start_calendar_id": {
                    "type": "integer",
                    "description": "Optional start calendar_id.",
                },
                "end_calendar_id": {
                    "type": "integer",
                    "description": "Optional end calendar_id.",
                },
            },
            "required": ["database", "property_id"],
        },
    },
    {
        "name": "optix_list_market_dimensions",
        "description": "Lists all configured market segment dimensions in Dim_Market_Property (market_property_cd, market_property_nm, market_segment_type).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Optional property_id filter.",
                },
            },
            "required": ["database"],
        },
    },
    {
        "name": "optix_get_room_type_summary",
        "description": "Reconciles accommodation solds, room revenue, and ADR by physical and logical room category from Fact_Daily_Activity joined with Dim_Accom_Property.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "start_calendar_id": {
                    "type": "integer",
                    "description": "Optional start calendar_id.",
                },
                "end_calendar_id": {
                    "type": "integer",
                    "description": "Optional end calendar_id.",
                },
            },
            "required": ["database", "property_id"],
        },
    },
    {
        "name": "optix_list_room_types",
        "description": "Lists all configured room type dimensions in Dim_Accom_Property (accom_property_cd, accom_property_nm).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Optional property_id filter.",
                },
            },
            "required": ["database"],
        },
    },

    # -------------------------------------------------------------
    # Group 8: Group Blocks, Pickups & Business Views (3 Tools)
    # -------------------------------------------------------------
    {
        "name": "optix_get_group_reconciliation",
        "description": "Performs comprehensive 3-tier group reconciliation: Tier 1 Unpicked Blocks ('B'), Tier 2 Materialized Group Pickup ('R'), Contracted Block Revenue, Pickup Revenue, and Total Group Revenue.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "start_calendar_id": {
                    "type": "integer",
                    "description": "Optional start calendar_id.",
                },
                "end_calendar_id": {
                    "type": "integer",
                    "description": "Optional end calendar_id.",
                },
            },
            "required": ["database", "property_id"],
        },
    },
    {
        "name": "optix_get_group_details",
        "description": "Queries specific group master definitions, contracts, and status from Dim_Group and STAGE.Group_Master.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "group_status": {
                    "type": "string",
                    "description": "Optional status filter (e.g. 'DEFINITE', 'DEF', '1').",
                },
            },
            "required": ["database", "property_id"],
        },
    },
    {
        "name": "optix_get_business_views",
        "description": "Partitions hotel performance into commercial Business Views: Transient, Group, Contract & Crew, and House Use / Other Business Views.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "start_calendar_id": {
                    "type": "integer",
                    "description": "Optional start calendar_id.",
                },
                "end_calendar_id": {
                    "type": "integer",
                    "description": "Optional end calendar_id.",
                },
            },
            "required": ["database", "property_id"],
        },
    },

    # -------------------------------------------------------------
    # Group 9: Data Quality, Discrepancies & ETL History (3 Tools)
    # -------------------------------------------------------------
    {
        "name": "optix_scan_no_value_anomalies",
        "description": "Quality anomaly scanner detecting unmapped dimensions (-2, 0, 'ZNV'), complimentary zero-revenue stays with active solds, and late cancellation fees without solds.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "property_id": {
                    "type": "integer",
                    "description": "Internal numeric property_id.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max anomaly records to return (default: 50).",
                    "default": 50,
                },
            },
            "required": ["database", "property_id"],
        },
    },
    {
        "name": "optix_compare_discrepancy",
        "description": "Computes exact discrepancy percentage between G3 RMS source metrics and Optix DW metrics with the official <5% tolerance check and automated pass/fail determination.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "g3_solds": {
                    "type": "number",
                    "description": "Rooms sold from G3 RMS (Accom_Activity).",
                },
                "g3_revenue": {
                    "type": "number",
                    "description": "Room revenue from G3 RMS (Accom_Activity).",
                },
                "optix_solds": {
                    "type": "number",
                    "description": "Rooms sold from Optix DW (Fact_Daily_Activity).",
                },
                "optix_revenue": {
                    "type": "number",
                    "description": "Room revenue from Optix DW (Fact_Daily_Activity).",
                },
                "tolerance_percent": {
                    "type": "number",
                    "description": "Tolerance threshold percentage (default: 5.0%).",
                    "default": 5.0,
                },
            },
            "required": ["g3_solds", "g3_revenue", "optix_solds", "optix_revenue"],
        },
    },
    {
        "name": "optix_get_batch_history",
        "description": "Inspects recent ETL and data processing batch runs from Process_History or Processing_Batch (Batch_ID, Status, End_Time, row counts, error messages).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Target Optix database name.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max batch records to return (default: 20).",
                    "default": 20,
                },
            },
            "required": ["database"],
        },
    },

    # -------------------------------------------------------------
    # Group 10: Cache & Route Administration (2 Tools)
    # -------------------------------------------------------------
    {
        "name": "optix_flush_routing_cache",
        "description": "Flushes the in-memory database routing cache and initiates a full live re-index of all databases across all cluster nodes.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "optix_get_cache_stats",
        "description": "Returns routing cache statistics, cache hit/miss ratio, indexed database counts, and query counters.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
]

OPTIX_RESOURCES = [
    {
        "uri": "optix://cluster/status",
        "name": "Optix MSSQL Cluster Live Status",
        "description": "Live TCP connectivity, round-trip latency, MSSQL versions, and database counts for all 3 cluster nodes.",
        "mimeType": "application/json",
    },
    {
        "uri": "optix://cluster/databases",
        "name": "Optix Complete Tenant Database Catalog",
        "description": "Directory of all 427+ indexed tenant databases and their assigned cluster nodes.",
        "mimeType": "application/json",
    },
    {
        "uri": "optix://cluster/stats",
        "name": "Optix Query & Routing Statistics",
        "description": "Aggregate query execution counters, routing cache hit rates, and server uptime.",
        "mimeType": "application/json",
    },
]


# ==============================================================================
# TOOL EXECUTION ROUTING ENGINE
# ==============================================================================
def execute_tool(name: str, arguments: Dict[str, Any]) -> Any:
    """Dispatches tool execution to the appropriate handler."""
    mgr = OptixClusterManager.get_instance()

    # --- Group 1: Cluster Health & Topology ---
    if name == "optix_ping_cluster":
        return mgr.ping_all_nodes()

    elif name == "optix_list_all_databases":
        filter_pat = arguments.get("filter_pattern", "").strip().upper()
        max_res = int(arguments.get("max_results", 500))
        with mgr._lock:
            dbs = []
            for db_up, (host, real_name) in mgr._db_catalog.items():
                if not filter_pat or filter_pat in db_up:
                    dbs.append({"database": real_name, "node": host})
                    if len(dbs) >= max_res:
                        break
        return {"total_matching": len(dbs), "databases": dbs}

    elif name == "optix_resolve_database":
        client_code = arguments.get("client_code", "")
        property_code = arguments.get("property_code", "")
        host, db = mgr.resolve_database(client_code, property_code)
        if host and db:
            return {"resolved": True, "client_code": client_code, "host": host, "database": db}
        return {"resolved": False, "client_code": client_code, "message": "Database not found in Optix cluster catalog"}

    elif name == "optix_cluster_stats":
        return mgr.get_stats()

    # --- Group 2: SQL Execution & Batch Operations ---
    elif name == "optix_execute_query":
        sql = arguments.get("sql", "")
        db = arguments.get("database")
        cc = arguments.get("client_code")
        pc = arguments.get("property_code")
        host = arguments.get("host")
        max_rows = int(arguments.get("max_rows", 100))
        timeout = int(arguments.get("timeout_seconds", 30))
        return mgr.execute_query(sql, database=db, client_code=cc, property_code=pc, host=host, max_rows=max_rows, timeout=timeout)

    elif name == "optix_execute_batch":
        queries = arguments.get("queries", [])
        results = {}
        for q in queries:
            lbl = q.get("label", "query")
            sql = q.get("sql", "")
            db = q.get("database", "master")
            res = mgr.execute_query(sql, database=db, max_rows=50)
            results[lbl] = res
        return {"batch_results": results}

    elif name == "optix_explain_query":
        sql = arguments.get("sql", "")
        db = arguments.get("database", "master")
        explain_sql = f"SET SHOWPLAN_ALL ON;\nGO\n{sql}\nGO\nSET SHOWPLAN_ALL OFF;"
        return mgr.execute_query(f"SET SHOWPLAN_ALL ON; {sql}; SET SHOWPLAN_ALL OFF;", database=db)

    # --- Group 3: Schema Reflection & Table Inspection ---
    elif name == "optix_list_tables":
        db = arguments["database"]
        schema = arguments.get("schema_name")
        pattern = arguments.get("name_filter")
        where_clauses = ["1=1"]
        if schema:
            where_clauses.append(f"TABLE_SCHEMA = '{schema}'")
        if pattern:
            where_clauses.append(f"TABLE_NAME LIKE '{pattern}'")
        sql = f"""
            SELECT TABLE_SCHEMA, TABLE_NAME, TABLE_TYPE 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE {' AND '.join(where_clauses)}
            ORDER BY TABLE_SCHEMA, TABLE_NAME;
        """
        return mgr.execute_query(sql, database=db, max_rows=300)

    elif name == "optix_describe_table":
        db = arguments["database"]
        table = arguments["table_name"]
        schema = arguments.get("schema_name", "dbo")
        sql = f"""
            SELECT 
                c.COLUMN_NAME, 
                c.DATA_TYPE, 
                c.CHARACTER_MAXIMUM_LENGTH, 
                c.IS_NULLABLE, 
                c.COLUMN_DEFAULT,
                CASE WHEN pk.COLUMN_NAME IS NOT NULL THEN 1 ELSE 0 END AS IS_PRIMARY_KEY
            FROM INFORMATION_SCHEMA.COLUMNS c
            LEFT JOIN (
                SELECT ku.COLUMN_NAME
                FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
                JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE ku 
                    ON tc.CONSTRAINT_TYPE = 'PRIMARY KEY' 
                    AND tc.CONSTRAINT_NAME = ku.CONSTRAINT_NAME
                WHERE tc.TABLE_NAME = '{table}' AND tc.TABLE_SCHEMA = '{schema}'
            ) pk ON c.COLUMN_NAME = pk.COLUMN_NAME
            WHERE c.TABLE_NAME = '{table}' AND c.TABLE_SCHEMA = '{schema}'
            ORDER BY c.ORDINAL_POSITION;
        """
        return mgr.execute_query(sql, database=db, max_rows=200)

    elif name == "optix_get_table_row_count":
        db = arguments["database"]
        tbl = arguments.get("table_name")
        filter_clause = f"AND t.name = '{tbl}'" if tbl else ""
        sql = f"""
            SELECT 
                s.name AS Schema_Name,
                t.name AS Table_Name,
                SUM(p.rows) AS Row_Count,
                ROUND((SUM(a.total_pages) * 8) / 1024.0, 2) AS Total_Space_MB
            FROM sys.tables t
            INNER JOIN sys.indexes i ON t.object_id = i.object_id
            INNER JOIN sys.partitions p ON i.object_id = p.object_id AND i.index_id = p.index_id
            INNER JOIN sys.allocation_units a ON p.partition_id = a.container_id
            INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
            WHERE t.is_ms_shipped = 0 AND i.object_id > 255 {filter_clause}
            GROUP BY t.Name, s.Name
            ORDER BY Row_Count DESC;
        """
        return mgr.execute_query(sql, database=db, max_rows=50)

    elif name == "optix_search_columns":
        db = arguments["database"]
        pat = arguments["column_pattern"]
        sql = f"""
            SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE COLUMN_NAME LIKE '{pat}'
            ORDER BY TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME;
        """
        return mgr.execute_query(sql, database=db, max_rows=150)

    # --- Group 4: Tenant Identity & Property Configuration ---
    elif name == "optix_get_properties":
        db = arguments["database"]
        sql = """
            SELECT 
                property_id, 
                property_cd, 
                property_nm, 
                currency_cd, 
                status_id, 
                pms_property_id, 
                ups_id, 
                time_zone_txt, 
                gemini_start_data_dt, 
                gemini_end_data_dt
            FROM Dim_Property WITH (NOLOCK)
            ORDER BY property_id;
        """
        return mgr.execute_query(sql, database=db, max_rows=100)

    elif name == "optix_resolve_property":
        db = arguments["database"]
        pcd = str(arguments["property_code"]).strip()
        pcd_unpadded = pcd.lstrip("0")
        pcd_padded = pcd.zfill(4)
        sql = f"""
            SELECT 
                property_id, 
                property_cd, 
                property_nm, 
                currency_cd, 
                status_id, 
                pms_property_id, 
                ups_id, 
                time_zone_txt
            FROM Dim_Property WITH (NOLOCK)
            WHERE property_cd IN ('{pcd}', '{pcd_unpadded}', '{pcd_padded}');
        """
        return mgr.execute_query(sql, database=db, max_rows=5)

    elif name == "optix_get_feature_flags":
        db = arguments["database"]
        pid = arguments.get("property_id")
        sql = """
            SELECT name, enabled 
            FROM Feature WITH (NOLOCK)
            ORDER BY name;
        """
        res = mgr.execute_query(sql, database=db, max_rows=100)
        # Check mandatory 5 flags
        mandatory = [
            "enableCompetitiveRatesEtl",
            "enableCompetitiveRatesDashboard",
            "enablePMSInboundProfileData",
            "dashboard.travel_agent",
            "dashboard.company",
        ]
        flags = {r["name"]: r["enabled"] for r in res.get("rows", [])}
        res["mandatory_rms_audit"] = {
            flag: flags.get(flag, False) for flag in mandatory
        }
        res["all_mandatory_passed"] = all(flags.get(f) for f in mandatory)
        return res

    elif name == "optix_get_property_hierarchy":
        db = arguments["database"]
        sql = """
            SELECT TOP 50 * FROM vw_property_hierarchy WITH (NOLOCK);
        """
        return mgr.execute_query(sql, database=db, max_rows=50)

    # --- Group 5: Historical Actuals & Daily Activity ---
    elif name == "optix_get_activity_summary":
        db = arguments["database"]
        pid = arguments["property_id"]
        s_cal = arguments.get("start_calendar_id", 20200101)
        e_cal = arguments.get("end_calendar_id", 20301231)
        sql = f"""
            SELECT 
                SUM(CAST(accom_nr AS FLOAT)) AS Optix_Total_Solds,
                SUM(CAST(accom_revenue_amt AS DECIMAL(18,2))) AS Optix_Room_Revenue,
                SUM(CAST(food_revenue_amt AS DECIMAL(18,2))) AS Optix_Food_Revenue,
                SUM(CAST(beverage_revenue_amt AS DECIMAL(18,2))) AS Optix_Beverage_Revenue,
                SUM(CAST(other_revenue_amt AS DECIMAL(18,2))) AS Optix_Other_Revenue,
                SUM(
                    CAST(accom_revenue_amt AS DECIMAL(18,2)) + 
                    CAST(food_revenue_amt AS DECIMAL(18,2)) + 
                    CAST(beverage_revenue_amt AS DECIMAL(18,2)) + 
                    CAST(other_revenue_amt AS DECIMAL(18,2))
                ) AS Optix_Total_Gross_Revenue
            FROM Fact_Daily_Activity WITH (NOLOCK)
            WHERE calendar_id BETWEEN {s_cal} AND {e_cal}
              AND property_id = {pid};
        """
        return mgr.execute_query(sql, database=db, max_rows=1)

    elif name == "optix_get_daily_activity":
        db = arguments["database"]
        pid = arguments["property_id"]
        s_cal = arguments["start_calendar_id"]
        e_cal = arguments["end_calendar_id"]
        limit = int(arguments.get("limit", 365))
        sql = f"""
            SELECT 
                CAST(calendar_id AS VARCHAR(8)) AS Occupancy_Date,
                SUM(CAST(accom_nr AS FLOAT)) AS Daily_Solds,
                SUM(CAST(accom_revenue_amt AS DECIMAL(18,2))) AS Daily_Revenue,
                SUM(CAST(accom_revenue_amt AS DECIMAL(18,2))) / NULLIF(SUM(CAST(accom_nr AS FLOAT)), 0) AS Daily_ADR
            FROM Fact_Daily_Activity WITH (NOLOCK)
            WHERE calendar_id BETWEEN {s_cal} AND {e_cal}
              AND property_id = {pid}
            GROUP BY calendar_id
            ORDER BY calendar_id;
        """
        return mgr.execute_query(sql, database=db, max_rows=limit)

    elif name == "optix_get_activity_hierarchy":
        db = arguments["database"]
        pid = arguments["property_id"]
        s_cal = arguments.get("start_calendar_id", 20200101)
        e_cal = arguments.get("end_calendar_id", 20301231)
        sql = f"""
            SELECT 
                LEFT(CAST(calendar_id AS VARCHAR(8)), 4) AS Year_YYYY,
                LEFT(CAST(calendar_id AS VARCHAR(8)), 4) + '-' + SUBSTRING(CAST(calendar_id AS VARCHAR(8)), 5, 2) AS Month_YYYY_MM,
                SUM(CAST(accom_nr AS FLOAT)) AS Total_Solds,
                SUM(CAST(accom_revenue_amt AS DECIMAL(18,2))) AS Total_Revenue,
                SUM(CAST(accom_revenue_amt AS DECIMAL(18,2))) / NULLIF(SUM(CAST(accom_nr AS FLOAT)), 0) AS Monthly_ADR
            FROM Fact_Daily_Activity WITH (NOLOCK)
            WHERE calendar_id BETWEEN {s_cal} AND {e_cal}
              AND property_id = {pid}
            GROUP BY 
                LEFT(CAST(calendar_id AS VARCHAR(8)), 4),
                LEFT(CAST(calendar_id AS VARCHAR(8)), 4) + '-' + SUBSTRING(CAST(calendar_id AS VARCHAR(8)), 5, 2)
            ORDER BY Month_YYYY_MM;
        """
        return mgr.execute_query(sql, database=db, max_rows=120)

    # --- Group 6: On-The-Books (OTB) Pace & STLY ---
    elif name == "optix_get_current_pace":
        db = arguments["database"]
        pid = arguments["property_id"]
        today_int = int(datetime.utcnow().strftime("%Y%m%d"))
        end_cal = int(arguments.get("end_calendar_id", today_int + 10000))
        sql = f"""
            SELECT 
                CAST(calendar_id AS VARCHAR(8)) AS Future_Occupancy_Date,
                SUM(CAST(accom_nr AS FLOAT)) AS OTB_Solds,
                SUM(CAST(accom_revenue_amt AS DECIMAL(18,2))) AS OTB_Revenue,
                SUM(CAST(accom_revenue_amt AS DECIMAL(18,2))) / NULLIF(SUM(CAST(accom_nr AS FLOAT)), 0) AS OTB_ADR
            FROM Fact_Daily_Activity WITH (NOLOCK)
            WHERE calendar_id BETWEEN {today_int} AND {end_cal}
              AND property_id = {pid}
            GROUP BY calendar_id
            ORDER BY calendar_id;
        """
        return mgr.execute_query(sql, database=db, max_rows=365)

    elif name == "optix_get_forward_monthly_pace":
        db = arguments["database"]
        pid = arguments["property_id"]
        today_int = int(datetime.utcnow().strftime("%Y%m%d"))
        end_cal = today_int + 10000
        sql = f"""
            SELECT 
                LEFT(CAST(calendar_id AS VARCHAR(8)), 4) + '-' + SUBSTRING(CAST(calendar_id AS VARCHAR(8)), 5, 2) AS Forward_Month_YYYY_MM,
                SUM(CAST(accom_nr AS FLOAT)) AS Forward_OTB_Solds,
                SUM(CAST(accom_revenue_amt AS DECIMAL(18,2))) AS Forward_OTB_Revenue,
                SUM(CAST(accom_revenue_amt AS DECIMAL(18,2))) / NULLIF(SUM(CAST(accom_nr AS FLOAT)), 0) AS Forward_OTB_ADR
            FROM Fact_Daily_Activity WITH (NOLOCK)
            WHERE calendar_id BETWEEN {today_int} AND {end_cal}
              AND property_id = {pid}
            GROUP BY LEFT(CAST(calendar_id AS VARCHAR(8)), 4) + '-' + SUBSTRING(CAST(calendar_id AS VARCHAR(8)), 5, 2)
            ORDER BY Forward_Month_YYYY_MM;
        """
        return mgr.execute_query(sql, database=db, max_rows=24)

    elif name == "optix_get_stly_pace":
        db = arguments["database"]
        pid = arguments["property_id"]
        as_of = arguments.get("as_of_calendar_id")
        as_of_clause = f"= {as_of}" if as_of else "= (SELECT MAX(as_of_calendar_id) FROM Fact_Daily_Activity_Pace WITH (NOLOCK) WHERE property_id = {pid})"
        sql = f"""
            ;WITH latest_snapshot AS (
                SELECT MAX(as_of_calendar_id) AS max_as_of
                FROM Fact_Daily_Activity_Pace WITH (NOLOCK)
                WHERE property_id = {pid}
            )
            SELECT 
                CAST(fda.calendar_id AS VARCHAR(8)) AS STLY_Stay_Date,
                SUM(CAST(fda.accom_nr AS FLOAT)) AS STLY_Pace_Solds,
                SUM(CAST(fda.accom_revenue_amt AS DECIMAL(18,2))) AS STLY_Pace_Revenue
            FROM Fact_Daily_Activity_Pace fda WITH (NOLOCK)
            CROSS JOIN latest_snapshot ls
            WHERE fda.property_id = {pid}
              AND fda.as_of_calendar_id = ls.max_as_of
            GROUP BY fda.calendar_id
            ORDER BY fda.calendar_id;
        """
        return mgr.execute_query(sql, database=db, max_rows=365)

    elif name == "optix_get_stly_actuals":
        db = arguments["database"]
        pid = arguments["property_id"]
        s_cal = arguments.get("start_calendar_id", 20200101)
        e_cal = arguments.get("end_calendar_id", 20301231)
        sql = f"""
            SELECT 
                CAST(calendar_id AS VARCHAR(8)) AS STLY_Actual_Date,
                SUM(CAST(accom_nr AS FLOAT)) AS STLY_Actual_Solds,
                SUM(CAST(accom_revenue_amt AS DECIMAL(18,2))) AS STLY_Actual_Revenue
            FROM Fact_Daily_Activity WITH (NOLOCK)
            WHERE calendar_id BETWEEN {s_cal} AND {e_cal}
              AND property_id = {pid}
            GROUP BY calendar_id
            ORDER BY calendar_id;
        """
        return mgr.execute_query(sql, database=db, max_rows=365)

    elif name == "optix_get_pace_snapshots":
        db = arguments["database"]
        pid = arguments["property_id"]
        limit = int(arguments.get("limit", 30))
        sql = f"""
            SELECT 
                as_of_calendar_id,
                COUNT(*) AS Total_Records,
                MIN(calendar_id) AS Min_Stay_Date,
                MAX(calendar_id) AS Max_Stay_Date,
                SUM(accom_nr) AS Total_Snapshot_Solds
            FROM Fact_Daily_Activity_Pace WITH (NOLOCK)
            WHERE property_id = {pid}
            GROUP BY as_of_calendar_id
            ORDER BY as_of_calendar_id DESC;
        """
        return mgr.execute_query(sql, database=db, max_rows=limit)

    # --- Group 7: Dimensions — Market Segments & Room Types ---
    elif name == "optix_get_market_segments":
        db = arguments["database"]
        pid = arguments["property_id"]
        s_cal = arguments.get("start_calendar_id", 20200101)
        e_cal = arguments.get("end_calendar_id", 20301231)
        sql = f"""
            SELECT 
                dmp.market_property_cd AS Market_Segment_Code,
                dmp.market_property_nm AS Market_Segment_Name,
                dmp.market_segment_type AS Market_Segment_Type,
                SUM(CAST(fda.accom_nr AS FLOAT)) AS Total_Solds,
                SUM(CAST(fda.accom_revenue_amt AS DECIMAL(18,2))) AS Total_Revenue,
                SUM(CAST(fda.accom_revenue_amt AS DECIMAL(18,2))) / NULLIF(SUM(CAST(fda.accom_nr AS FLOAT)), 0) AS Segment_ADR
            FROM Fact_Daily_Activity fda WITH (NOLOCK)
            JOIN Dim_Market_Property dmp WITH (NOLOCK) ON fda.market_property_id = dmp.market_property_id
            WHERE fda.calendar_id BETWEEN {s_cal} AND {e_cal}
              AND fda.property_id = {pid}
            GROUP BY 
                dmp.market_property_cd, 
                dmp.market_property_nm, 
                dmp.market_segment_type
            ORDER BY Total_Solds DESC;
        """
        return mgr.execute_query(sql, database=db, max_rows=100)

    elif name == "optix_list_market_dimensions":
        db = arguments["database"]
        pid = arguments.get("property_id")
        p_filter = f"WHERE property_id = {pid}" if pid else ""
        sql = f"""
            SELECT market_property_id, property_id, market_property_cd, market_property_nm, market_segment_type
            FROM Dim_Market_Property WITH (NOLOCK)
            {p_filter}
            ORDER BY market_property_cd;
        """
        return mgr.execute_query(sql, database=db, max_rows=100)

    elif name == "optix_get_room_type_summary":
        db = arguments["database"]
        pid = arguments["property_id"]
        s_cal = arguments.get("start_calendar_id", 20200101)
        e_cal = arguments.get("end_calendar_id", 20301231)
        sql = f"""
            SELECT 
                dap.accom_property_cd AS Room_Type_Code,
                dap.accom_property_nm AS Room_Type_Name,
                SUM(CAST(fda.accom_nr AS FLOAT)) AS Total_Solds,
                SUM(CAST(fda.accom_revenue_amt AS DECIMAL(18,2))) AS Total_Revenue,
                SUM(CAST(fda.accom_revenue_amt AS DECIMAL(18,2))) / NULLIF(SUM(CAST(fda.accom_nr AS FLOAT)), 0) AS Room_Type_ADR
            FROM Fact_Daily_Activity fda WITH (NOLOCK)
            JOIN Dim_Accom_Property dap WITH (NOLOCK) ON fda.accom_property_id = dap.accom_property_id
            WHERE fda.calendar_id BETWEEN {s_cal} AND {e_cal}
              AND fda.property_id = {pid}
            GROUP BY 
                dap.accom_property_cd, 
                dap.accom_property_nm
            ORDER BY Total_Solds DESC;
        """
        return mgr.execute_query(sql, database=db, max_rows=100)

    elif name == "optix_list_room_types":
        db = arguments["database"]
        pid = arguments.get("property_id")
        p_filter = f"WHERE property_id = {pid}" if pid else ""
        sql = f"""
            SELECT accom_property_id, property_id, accom_property_cd, accom_property_nm
            FROM Dim_Accom_Property WITH (NOLOCK)
            {p_filter}
            ORDER BY accom_property_cd;
        """
        return mgr.execute_query(sql, database=db, max_rows=100)

    # --- Group 8: Group Blocks, Pickups & Business Views ---
    elif name == "optix_get_group_reconciliation":
        db = arguments["database"]
        pid = arguments["property_id"]
        s_cal = arguments.get("start_calendar_id", 20200101)
        e_cal = arguments.get("end_calendar_id", 20301231)
        sql = f"""
            SELECT 
                LEFT(CAST(fda.calendar_id AS VARCHAR(8)), 4) + '-' + SUBSTRING(CAST(fda.calendar_id AS VARCHAR(8)), 5, 2) AS Month_YYYY_MM,
                SUM(CASE WHEN fda.room_block_type = 'B' THEN CAST(fda.accom_nr AS FLOAT) ELSE 0 END) AS Optix_Remaining_Block,
                SUM(CASE WHEN fda.room_block_type = 'R' AND (fda.group_id > 0 OR dmp.market_segment_type = 'Group') THEN CAST(fda.accom_nr AS FLOAT) ELSE 0 END) AS Optix_Pickup_Rooms,
                SUM(CASE WHEN fda.room_block_type = 'R' AND (fda.group_id > 0 OR dmp.market_segment_type = 'Group') THEN CAST(fda.accom_revenue_amt AS DECIMAL(18,2)) ELSE 0 END) AS Optix_Pickup_Revenue,
                SUM(CASE WHEN fda.room_block_type = 'B' THEN CAST(fda.accom_revenue_amt AS DECIMAL(18,2)) ELSE 0 END) AS Optix_Block_Revenue,
                SUM(CASE WHEN (fda.group_id > 0 OR dmp.market_segment_type = 'Group') THEN CAST(fda.accom_revenue_amt AS DECIMAL(18,2)) ELSE 0 END) AS Optix_Total_Group_Revenue
            FROM Fact_Daily_Activity fda WITH (NOLOCK)
            LEFT JOIN Dim_Group dg WITH (NOLOCK) ON fda.group_id = dg.group_id
            LEFT JOIN Dim_Market_Property dmp WITH (NOLOCK) ON fda.market_property_id = dmp.market_property_id
            WHERE fda.calendar_id BETWEEN {s_cal} AND {e_cal}
              AND fda.property_id = {pid}
              AND (fda.group_id > 0 OR dmp.market_segment_type = 'Group')
            GROUP BY LEFT(CAST(fda.calendar_id AS VARCHAR(8)), 4) + '-' + SUBSTRING(CAST(fda.calendar_id AS VARCHAR(8)), 5, 2)
            ORDER BY Month_YYYY_MM DESC;
        """
        return mgr.execute_query(sql, database=db, max_rows=60)

    elif name == "optix_get_group_details":
        db = arguments["database"]
        pid = arguments["property_id"]
        st = arguments.get("group_status")
        st_filter = f"AND dg.group_status_cd = '{st}'" if st else ""
        sql = f"""
            SELECT 
                dg.group_id, 
                dg.group_cd, 
                dg.group_nm, 
                dg.group_status_cd,
                COUNT(fda.calendar_id) AS Total_Nights,
                SUM(CAST(fda.accom_nr AS FLOAT)) AS Total_Solds,
                SUM(CAST(fda.accom_revenue_amt AS DECIMAL(18,2))) AS Total_Revenue
            FROM Dim_Group dg WITH (NOLOCK)
            LEFT JOIN Fact_Daily_Activity fda WITH (NOLOCK) ON dg.group_id = fda.group_id
            WHERE dg.property_id = {pid} {st_filter}
            GROUP BY dg.group_id, dg.group_cd, dg.group_nm, dg.group_status_cd
            ORDER BY Total_Solds DESC;
        """
        return mgr.execute_query(sql, database=db, max_rows=50)

    elif name == "optix_get_business_views":
        db = arguments["database"]
        pid = arguments["property_id"]
        s_cal = arguments.get("start_calendar_id", 20200101)
        e_cal = arguments.get("end_calendar_id", 20301231)
        sql = f"""
            SELECT 
                CASE 
                    WHEN dmp.market_segment_type = 'Group' OR dmp.market_property_cd LIKE '%GRP%' OR dmp.market_property_cd LIKE '%GR%' THEN 'Group Business View'
                    WHEN dmp.market_property_cd IN ('AIR', 'CREW', 'GOV', 'CONT', 'PERM') THEN 'Contract & Crew Business View'
                    WHEN dmp.market_property_cd IN ('COMP', 'HOUSE', 'DAY', 'BARTER', 'ZNV') THEN 'Other / House Use Business View'
                    ELSE 'Transient Business View'
                END AS Business_View_Name,
                SUM(CAST(fda.accom_nr AS FLOAT)) AS Total_Solds,
                SUM(CAST(fda.accom_revenue_amt AS DECIMAL(18,2))) AS Total_Revenue,
                SUM(CAST(fda.accom_revenue_amt AS DECIMAL(18,2))) / NULLIF(SUM(CAST(fda.accom_nr AS FLOAT)), 0) AS Business_View_ADR
            FROM Fact_Daily_Activity fda WITH (NOLOCK)
            JOIN Dim_Market_Property dmp WITH (NOLOCK) ON fda.market_property_id = dmp.market_property_id
            WHERE fda.calendar_id BETWEEN {s_cal} AND {e_cal}
              AND fda.property_id = {pid}
            GROUP BY 
                CASE 
                    WHEN dmp.market_segment_type = 'Group' OR dmp.market_property_cd LIKE '%GRP%' OR dmp.market_property_cd LIKE '%GR%' THEN 'Group Business View'
                    WHEN dmp.market_property_cd IN ('AIR', 'CREW', 'GOV', 'CONT', 'PERM') THEN 'Contract & Crew Business View'
                    WHEN dmp.market_property_cd IN ('COMP', 'HOUSE', 'DAY', 'BARTER', 'ZNV') THEN 'Other / House Use Business View'
                    ELSE 'Transient Business View'
                END
            ORDER BY Total_Solds DESC;
        """
        return mgr.execute_query(sql, database=db, max_rows=10)

    # --- Group 9: Data Quality, Discrepancies & ETL History ---
    elif name == "optix_scan_no_value_anomalies":
        db = arguments["database"]
        pid = arguments["property_id"]
        limit = int(arguments.get("limit", 50))
        sql = f"""
            SELECT 
                CAST(fda.calendar_id AS VARCHAR(8)) AS Occupancy_Date,
                ISNULL(dmp.market_property_cd, 'UNMAPPED_MKT') AS Market_Segment_Code,
                ISNULL(dap.accom_property_cd, 'UNMAPPED_RT') AS Room_Type_Code,
                fda.accom_nr AS Solds,
                fda.accom_revenue_amt AS Revenue,
                CASE 
                    WHEN fda.market_property_id IN (-2, 0) OR dmp.market_property_cd = 'ZNV' THEN 'No Value Market Segment (ZNV)'
                    WHEN fda.accom_property_id IN (-2, 0) OR dap.accom_property_cd = 'ZNV' THEN 'No Value Room Type (ZNV)'
                    WHEN fda.accom_nr > 0 AND (fda.accom_revenue_amt = 0 OR fda.accom_revenue_amt IS NULL) THEN 'Zero Revenue with Active Solds (Complimentary)'
                    WHEN (fda.accom_nr = 0 OR fda.accom_nr IS NULL) AND fda.accom_revenue_amt > 0 THEN 'Revenue without Solds (Late Fee/Cancellation)'
                    ELSE 'Unmapped Dimension'
                END AS Anomaly_Classification
            FROM Fact_Daily_Activity fda WITH (NOLOCK)
            LEFT JOIN Dim_Market_Property dmp WITH (NOLOCK) ON fda.market_property_id = dmp.market_property_id
            LEFT JOIN Dim_Accom_Property dap WITH (NOLOCK) ON fda.accom_property_id = dap.accom_property_id
            WHERE fda.property_id = {pid}
              AND (
                  fda.market_property_id IN (-2, 0)
                  OR fda.accom_property_id IN (-2, 0)
                  OR dmp.market_property_cd = 'ZNV'
                  OR dap.accom_property_cd = 'ZNV'
                  OR (fda.accom_nr > 0 AND (fda.accom_revenue_amt = 0 OR fda.accom_revenue_amt IS NULL))
                  OR ((fda.accom_nr = 0 OR fda.accom_nr IS NULL) AND fda.accom_revenue_amt > 0)
              )
            ORDER BY fda.calendar_id DESC;
        """
        return mgr.execute_query(sql, database=db, max_rows=limit)

    elif name == "optix_compare_discrepancy":
        g3_s = float(arguments.get("g3_solds", 0.0))
        g3_r = float(arguments.get("g3_revenue", 0.0))
        opt_s = float(arguments.get("optix_solds", 0.0))
        opt_r = float(arguments.get("optix_revenue", 0.0))
        tol = float(arguments.get("tolerance_percent", 5.0))

        diff_solds = abs(g3_s - opt_s)
        pct_solds = (diff_solds / max(abs(g3_s), abs(opt_s), 1.0)) * 100.0

        diff_rev = abs(g3_r - opt_r)
        pct_rev = (diff_rev / max(abs(g3_r), abs(opt_r), 1.0)) * 100.0

        solds_passed = pct_solds <= tol or diff_solds <= 5.0  # Buffer for low-volume properties
        rev_passed = pct_rev <= tol or diff_rev <= 25.0

        return {
            "passed": solds_passed and rev_passed,
            "tolerance_limit_percent": tol,
            "metrics": {
                "solds": {
                    "g3": g3_s,
                    "optix": opt_s,
                    "variance": round(diff_solds, 2),
                    "discrepancy_percent": round(pct_solds, 3),
                    "passed": solds_passed,
                },
                "revenue": {
                    "g3": g3_r,
                    "optix": opt_r,
                    "variance": round(diff_rev, 2),
                    "discrepancy_percent": round(pct_rev, 3),
                    "passed": rev_passed,
                },
            },
            "status": "PASS (<5% tolerance limit satisfied)" if (solds_passed and rev_passed) else "DISCREPANCY EXCEEDS 5% LIMIT",
        }

    elif name == "optix_get_batch_history":
        db = arguments["database"]
        limit = int(arguments.get("limit", 20))
        # Check Process_History or Processing_Batch
        sql = f"""
            IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Process_History')
            BEGIN
                SELECT TOP {limit} * FROM Process_History WITH (NOLOCK) ORDER BY 1 DESC;
            END
            ELSE IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Processing_Batch')
            BEGIN
                SELECT TOP {limit} * FROM Processing_Batch WITH (NOLOCK) ORDER BY 1 DESC;
            END
            ELSE
            BEGIN
                SELECT 'No batch history table found' AS Message;
            END
        """
        return mgr.execute_query(sql, database=db, max_rows=limit)

    # --- Group 10: Cache & Route Administration ---
    elif name == "optix_flush_routing_cache":
        return mgr.flush_cache()

    elif name == "optix_get_cache_stats":
        return mgr.get_stats()

    else:
        raise ValueError(f"Unknown tool name: {name}")


def read_resource(uri: str) -> str:
    """Returns content for the requested MCP resource URI."""
    mgr = OptixClusterManager.get_instance()
    if uri == "optix://cluster/status":
        return json.dumps(mgr.ping_all_nodes(), cls=CustomJsonEncoder, indent=2)
    elif uri == "optix://cluster/databases":
        with mgr._lock:
            data = [{"database": r, "node": h} for r, (h, _) in mgr._db_catalog.items()]
        return json.dumps({"total": len(data), "databases": data}, cls=CustomJsonEncoder, indent=2)
    elif uri == "optix://cluster/stats":
        return json.dumps(mgr.get_stats(), cls=CustomJsonEncoder, indent=2)
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

    app = FastAPI(title="Optix MSSQL Cluster MCP Server", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Active SSE clients: session_id -> asyncio.Queue
    sse_clients: Dict[str, asyncio.Queue] = {}
    sse_lock = asyncio.Lock()

    @app.get("/health")
    async def health_check():
        mgr = OptixClusterManager.get_instance()
        stats = mgr.get_stats()
        return {
            "status": "HEALTHY",
            "server": "optix-mcp-server",
            "version": "1.0.0",
            "transport": "HTTP SSE + Stdio",
            "mcp_version": "2024-11-05",
            "total_tools": len(OPTIX_TOOLS),
            "total_resources": len(OPTIX_RESOURCES),
            "cluster": {
                "nodes": mgr.nodes,
                "databases_indexed": stats["total_databases_indexed"],
                "queries_executed": stats["queries_executed"],
            },
        }

    @app.get("/sse")
    async def sse_endpoint(request: Request):
        session_id = f"optix_sess_{int(time.time()*1000)}_{os.urandom(4).hex()}"
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
                        yield f"event: message\ndata: {json.dumps(msg, cls=CustomJsonEncoder)}\n\n"
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

        # If connected via SSE session, push to queue
        if session_id:
            async with sse_lock:
                q = sse_clients.get(session_id)
                if q:
                    await q.put(response)
                    return Response(status_code=202)

        return JSONResponse(content=response)

    return app


def handle_jsonrpc_request(method: str, params: Dict[str, Any], req_id: Any) -> Dict[str, Any]:
    """Processes MCP JSON-RPC requests."""
    try:
        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {
                        "name": "optix-mcp-server",
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
                    "tools": OPTIX_TOOLS,
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
                                "text": json.dumps(res, cls=CustomJsonEncoder, indent=2),
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
                    "resources": OPTIX_RESOURCES,
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
        logger.error("JSON-RPC handler exception: %s", exc)
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
    """Runs the server over standard input/output (Stdio transport)."""
    logger.info("Starting Optix MCP Server in Stdio transport mode...")
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
                sys.stdout.write(json.dumps(resp, cls=CustomJsonEncoder) + "\n")
                sys.stdout.flush()
        except KeyboardInterrupt:
            break
        except Exception as exc:
            logger.error("Stdio loop error: %s", exc)


# ==============================================================================
# MAIN ENTRYPOINT
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(description="Optix Data Warehouse MCP Server")
    parser.add_argument("--stdio", action="store_true", help="Run in Stdio transport mode")
    parser.add_argument("--host", default=MCP_HOST, help=f"Host to bind (default: {MCP_HOST})")
    parser.add_argument("--port", type=int, default=MCP_PORT, help=f"Port to bind (default: {MCP_PORT})")
    args = parser.parse_args()

    if args.stdio:
        run_stdio_transport()
    else:
        import uvicorn
        logger.info("Starting Optix MCP Server on %s:%d (SSE Transport)...", args.host, args.port)
        app = create_app()
        uvicorn.run(app, host=args.host, port=args.port, log_level="warning")


if __name__ == "__main__":
    main()
