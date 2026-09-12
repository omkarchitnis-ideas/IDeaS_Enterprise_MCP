#!/usr/bin/env python3
"""
SAS IDeaS Enterprise MCP Authentication & Management Subsystem
============================================================
Handles SQLite-backed API Key lifecycle, rate limiting, domain toggles,
audit logging, and metrics aggregation for the Master MCP Gateway.
"""

import os
import time
import secrets
import sqlite3
import logging
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger("mcp-auth-manager")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
DB_PATH = os.getenv("MCP_DB_PATH", os.path.join(DATA_DIR, "mcp_management.db"))

DEFAULT_MASTER_KEY = os.getenv("MCP_MASTER_API_KEY", "mcp_copilot_prod_key_2026")
ADMIN_USERNAME = os.getenv("MCP_ADMIN_USER", "admin")
ADMIN_PASSWORD = os.getenv("MCP_ADMIN_PASSWORD", "ideas_mcp_admin_2026")

_RATE_LIMIT_BUCKETS: Dict[str, List[float]] = {}


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, timeout=10.0)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initializes the database schema and seeds initial data if empty."""
    conn = get_db_connection()
    try:
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS api_keys (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    key_value TEXT UNIQUE NOT NULL,
                    client_name TEXT NOT NULL,
                    description TEXT,
                    created_at TEXT NOT NULL,
                    last_used_at TEXT,
                    total_calls INTEGER DEFAULT 0,
                    rate_limit_rpm INTEGER DEFAULT 120,
                    is_active INTEGER DEFAULT 1
                );
            """)

            conn.execute("""
                CREATE TABLE IF NOT EXISTS audit_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    client_name TEXT NOT NULL,
                    api_key_prefix TEXT NOT NULL,
                    endpoint TEXT NOT NULL,
                    method TEXT NOT NULL,
                    tool_name TEXT,
                    domain TEXT,
                    status_code INTEGER NOT NULL,
                    execution_time_ms REAL NOT NULL,
                    error_message TEXT,
                    client_ip TEXT
                );
            """)

            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_audit_timestamp ON audit_logs(timestamp);
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_audit_tool ON audit_logs(tool_name);
            """)

            conn.execute("""
                CREATE TABLE IF NOT EXISTS domain_settings (
                    domain_name TEXT PRIMARY KEY,
                    is_enabled INTEGER DEFAULT 1,
                    display_name TEXT NOT NULL,
                    tool_count INTEGER DEFAULT 0,
                    description TEXT
                );
            """)

            # Seed default domains
            default_domains = [
                ("salesforce", 1, "Salesforce (SFDC)", 24, "Case management, audit trail, triage comments"),
                ("cma", 1, "CMA & Job DB", 34, "Batch execution history, SQL queries, blocked steps"),
                ("datadog", 1, "Datadog Telemetry", 20, "Live production log search, cluster monitors, error traces"),
                ("confluence", 1, "Confluence Runbooks", 25, "IDeaS SOPs, triage precedents, PACMAN parameters"),
                ("optix", 1, "Optix Analytics", 35, "Historical forecast accuracy, revenue metrics, booking data"),
                ("ups_fds", 1, "UPS & FDS Interfaces", 30, "Property PMS interfaces, data feed configurations"),
            ]
            for d_name, en, d_disp, count, desc in default_domains:
                conn.execute("""
                    INSERT OR IGNORE INTO domain_settings (domain_name, is_enabled, display_name, tool_count, description)
                    VALUES (?, ?, ?, ?, ?)
                """, (d_name, en, d_disp, count, desc))

            # Seed default master key if no keys exist
            cur = conn.execute("SELECT COUNT(*) as count FROM api_keys")
            if cur.fetchone()["count"] == 0:
                now_str = datetime.now(timezone.utc).isoformat()
                conn.execute("""
                    INSERT INTO api_keys (key_value, client_name, description, created_at, rate_limit_rpm, is_active)
                    VALUES (?, ?, ?, ?, ?, 1)
                """, (
                    DEFAULT_MASTER_KEY,
                    "Microsoft_Copilot_Studio_Prod",
                    "Primary Production Key for M365 Copilot Studio Agent",
                    now_str,
                    300
                ))
                logger.info("Seeded default production API key: %s (Client: Microsoft_Copilot_Studio_Prod)", DEFAULT_MASTER_KEY)

    finally:
        conn.close()


def verify_api_key(raw_key: str, client_ip: str = "127.0.0.1") -> Tuple[bool, Optional[str], Optional[Dict[str, Any]]]:
    """
    Validates the provided API key against the database, checks active status,
    updates last-used telemetry, and enforces sliding-window rate limiting.
    """
    if not raw_key:
        return False, "Missing API Key. Provide via 'x-api-key' header, 'Authorization: Bearer <key>', or '?apiKey=<key>'", None

    clean_key = raw_key.strip()
    conn = get_db_connection()
    try:
        cur = conn.execute("SELECT * FROM api_keys WHERE key_value = ?", (clean_key,))
        row = cur.fetchone()
        if not row:
            return False, "Invalid API Key.", None

        key_data = dict(row)
        if not key_data["is_active"]:
            return False, "API Key has been revoked or deactivated by an administrator.", key_data

        # Rate limiting (sliding 60-second window)
        rpm_limit = key_data.get("rate_limit_rpm") or 120
        now = time.monotonic()
        bucket = _RATE_LIMIT_BUCKETS.setdefault(clean_key, [])
        # Expire timestamps older than 60 seconds
        _RATE_LIMIT_BUCKETS[clean_key] = [t for t in bucket if now - t < 60.0]

        if len(_RATE_LIMIT_BUCKETS[clean_key]) >= rpm_limit:
            return False, f"Rate limit exceeded for client '{key_data['client_name']}' (Limit: {rpm_limit} req/min).", key_data

        _RATE_LIMIT_BUCKETS[clean_key].append(now)

        # Update last used timestamp and call count
        now_iso = datetime.now(timezone.utc).isoformat()
        with conn:
            conn.execute("""
                UPDATE api_keys
                SET last_used_at = ?, total_calls = total_calls + 1
                WHERE id = ?
            """, (now_iso, key_data["id"]))

        return True, None, key_data

    finally:
        conn.close()


def log_audit(
    client_name: str,
    api_key: str,
    endpoint: str,
    method: str,
    tool_name: Optional[str],
    domain: Optional[str],
    status_code: int,
    execution_time_ms: float,
    error_message: Optional[str] = None,
    client_ip: str = "127.0.0.1",
):
    """Logs an API/tool call into the audit log."""
    prefix = (api_key[:10] + "...") if len(api_key) > 10 else api_key
    now_iso = datetime.now(timezone.utc).isoformat()
    conn = get_db_connection()
    try:
        with conn:
            conn.execute("""
                INSERT INTO audit_logs (
                    timestamp, client_name, api_key_prefix, endpoint, method,
                    tool_name, domain, status_code, execution_time_ms, error_message, client_ip
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                now_iso, client_name, prefix, endpoint, method,
                tool_name, domain, status_code, round(execution_time_ms, 2), error_message, client_ip
            ))
    except Exception as exc:
        logger.error("Failed to write audit log: %s", exc)
    finally:
        conn.close()


def is_domain_enabled(domain_name: str) -> bool:
    """Checks if a domain is enabled in real-time."""
    conn = get_db_connection()
    try:
        cur = conn.execute("SELECT is_enabled FROM domain_settings WHERE domain_name = ?", (domain_name.lower(),))
        row = cur.fetchone()
        if row is not None:
            return bool(row["is_enabled"])
        return True
    finally:
        conn.close()


def toggle_domain(domain_name: str) -> bool:
    """Toggles domain active status. Returns new state."""
    conn = get_db_connection()
    try:
        with conn:
            cur = conn.execute("SELECT is_enabled FROM domain_settings WHERE domain_name = ?", (domain_name.lower(),))
            row = cur.fetchone()
            new_state = 0 if (row and row["is_enabled"]) else 1
            conn.execute("UPDATE domain_settings SET is_enabled = ? WHERE domain_name = ?", (new_state, domain_name.lower()))
            return bool(new_state)
    finally:
        conn.close()


def create_api_key(client_name: str, description: str = "", rate_limit_rpm: int = 120) -> str:
    """Generates and registers a new cryptographically secure API key."""
    token = secrets.token_urlsafe(24)
    key = f"mcp_{token}"
    now_iso = datetime.now(timezone.utc).isoformat()
    conn = get_db_connection()
    try:
        with conn:
            conn.execute("""
                INSERT INTO api_keys (key_value, client_name, description, created_at, rate_limit_rpm, is_active)
                VALUES (?, ?, ?, ?, ?, 1)
            """, (key, client_name.strip(), description.strip(), now_iso, rate_limit_rpm))
        return key
    finally:
        conn.close()


def toggle_api_key(key_id: int) -> bool:
    """Toggles an API key active/revoked status."""
    conn = get_db_connection()
    try:
        with conn:
            cur = conn.execute("SELECT is_active FROM api_keys WHERE id = ?", (key_id,))
            row = cur.fetchone()
            if not row:
                return False
            new_val = 0 if row["is_active"] else 1
            conn.execute("UPDATE api_keys SET is_active = ? WHERE id = ?", (new_val, key_id))
            return bool(new_val)
    finally:
        conn.close()


def delete_api_key(key_id: int) -> bool:
    """Deletes an API key from the database."""
    conn = get_db_connection()
    try:
        with conn:
            conn.execute("DELETE FROM api_keys WHERE id = ?", (key_id,))
            return True
    finally:
        conn.close()


def get_dashboard_metrics() -> Dict[str, Any]:
    """Gathers KPI analytics and logs for the admin dashboard."""
    conn = get_db_connection()
    try:
        # Total calls all-time
        cur = conn.execute("SELECT COUNT(*) as cnt, AVG(execution_time_ms) as avg_ms FROM audit_logs")
        r_all = cur.fetchone()
        total_calls = r_all["cnt"] or 0
        avg_latency = round(r_all["avg_ms"] or 0.0, 1)

        # Total calls last 24h
        cutoff_24h = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
        cur = conn.execute("SELECT COUNT(*) as cnt FROM audit_logs WHERE timestamp >= ?", (cutoff_24h,))
        calls_24h = cur.fetchone()["cnt"] or 0

        # Success vs error counts
        cur = conn.execute("SELECT COUNT(*) as cnt FROM audit_logs WHERE status_code >= 400")
        error_count = cur.fetchone()["cnt"] or 0
        success_rate = round(((total_calls - error_count) / total_calls * 100), 1) if total_calls > 0 else 100.0

        # Active keys
        cur = conn.execute("SELECT * FROM api_keys ORDER BY id DESC")
        keys = [dict(r) for r in cur.fetchall()]

        # Domain settings
        cur = conn.execute("SELECT * FROM domain_settings ORDER BY display_name ASC")
        domains = [dict(r) for r in cur.fetchall()]

        # Calls by domain (last 7 days)
        cur = conn.execute("""
            SELECT domain, COUNT(*) as cnt
            FROM audit_logs
            WHERE domain IS NOT NULL
            GROUP BY domain
            ORDER BY cnt DESC
        """)
        domain_counts = {r["domain"]: r["cnt"] for r in cur.fetchall()}

        # Recent 50 audit logs
        cur = conn.execute("SELECT * FROM audit_logs ORDER BY id DESC LIMIT 50")
        recent_logs = [dict(r) for r in cur.fetchall()]

        return {
            "total_calls": total_calls,
            "calls_24h": calls_24h,
            "avg_latency_ms": avg_latency,
            "success_rate": success_rate,
            "error_count": error_count,
            "keys": keys,
            "domains": domains,
            "domain_counts": domain_counts,
            "recent_logs": recent_logs,
        }
    finally:
        conn.close()


# Auto-initialize DB on import
init_db()
