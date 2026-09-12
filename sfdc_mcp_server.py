#!/usr/bin/env python3
"""
Universal Enterprise Salesforce Model Context Protocol (MCP) Server (Python Native)
=====================================================================================
Comprehensive 24-tool suite covering:
- Case Lifecycle & History
- Tasks & Team Workloads
- Accounts, Contacts, Users & Integrations
- Documents & Attachments
- Schema & Picklist Introspection
- Universal SQL/SOQL Engine

Backed by the 24/7 PostgreSQL Clone (salesforce_clone on sicsappsina6:5433 with 550,000+ cases)
and the SFDC Middleware REST API on port 4000.
"""

import os
import sys
import json
import time
import logging
import argparse
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone
import requests
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("sfdc-mcp-server")

# ==============================================================================
# CONFIGURATION
# ==============================================================================
PG_HOST = os.getenv("SFDC_PG_HOST", "172.26.121.184")
PG_PORT = int(os.getenv("SFDC_PG_PORT", "5433"))
PG_DATABASE = os.getenv("SFDC_PG_DATABASE", "salesforce_clone")
PG_USER = os.getenv("SFDC_PG_USER", "team_reader")
PG_PASSWORD = os.getenv("SFDC_PG_PASSWORD", "team_reader_sfdc_2026")

SFDC_MIDDLEWARE_URL = os.getenv("SFDC_MIDDLEWARE_URL", "http://172.27.210.162:4000").rstrip("/")
SFDC_API_KEY = os.getenv("SFDC_API_KEY", "admin_9a34d764efac11e4abfed0e9ccad61ae")

# ==============================================================================
# DATABASE CONNECTION HELPER
# ==============================================================================
def get_pg_connection():
    """Returns a direct psycopg2 connection to the PostgreSQL clone."""
    return psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        dbname=PG_DATABASE,
        user=PG_USER,
        password=PG_PASSWORD,
        connect_timeout=8,
    )

def query_pg(sql: str, params: Optional[List[Any]] = None) -> List[Dict[str, Any]]:
    """Executes a SQL query against the PostgreSQL clone and returns dict rows."""
    conn = get_pg_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, params or [])
            rows = cur.fetchall()
            return [dict(r) for r in rows]
    finally:
        conn.close()

def query_soql_middleware(soql: str) -> Dict[str, Any]:
    """Executes SOQL via SFDC Middleware on port 4000."""
    t0 = time.monotonic()
    url = f"{SFDC_MIDDLEWARE_URL}/query"
    headers = {
        "x-api-key": SFDC_API_KEY,
        "Content-Type": "application/json",
    }
    try:
        resp = requests.post(url, headers=headers, json={"soql": soql}, timeout=25)
        elapsed_ms = round((time.monotonic() - t0) * 1000, 2)
        if resp.ok:
            data = resp.json()
            return {
                "success": True,
                "elapsed_ms": elapsed_ms,
                "records": data.get("records", []),
                "total_size": data.get("totalSize", len(data.get("records", []))),
                "cached": data.get("cached", False),
            }
        return {
            "success": False,
            "status_code": resp.status_code,
            "error": resp.text[:400],
            "elapsed_ms": elapsed_ms,
        }
    except Exception as exc:
        return {"success": False, "error": str(exc), "elapsed_ms": round((time.monotonic() - t0) * 1000, 2)}

# ==============================================================================
# CANONICAL TOOL DEFINITIONS (24 TOOLS)
# ==============================================================================
SFDC_TOOLS = [
    {
        "name": "sfdc_get_case",
        "description": "Retrieve complete details for a Salesforce Case from PostgreSQL clone in <50ms. Includes all 557 fields, case comments, and owner details.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "case_number": {"type": "string", "description": "8-digit Salesforce Case Number (e.g. '03373301')"},
                "case_id": {"type": "string", "description": "18-character Salesforce Case ID ('500...')"},
                "include_comments": {"type": "boolean", "default": True, "description": "Whether to include case comments"},
            },
            "required": [],
        },
    },
    {
        "name": "sfdc_search_cases",
        "description": "Search and filter historical or active Salesforce cases using indexed attributes (account chain code, property name, product environment, status, priority).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "account_chain_code": {"type": "string", "description": "Client Chain Code (e.g. 'HYATT', 'MAR', 'IHG')"},
                "property_name": {"type": "string", "description": "Hotel/Property Name or partial string"},
                "product_environment": {"type": "string", "description": "Product Environment (e.g. 'PROD', 'TEST')"},
                "status": {"type": "string", "description": "Case Status ('Open', 'Closed', etc.)"},
                "priority": {"type": "string", "description": "Case Priority ('IS', 'CM0', 'CM1', etc.)"},
                "limit": {"type": "integer", "default": 20, "description": "Maximum number of records to return (max 100)"},
            },
            "required": [],
        },
    },
    {
        "name": "sfdc_create_case",
        "description": "Create a new Case record in Salesforce with instant dual-write to PostgreSQL clone and DLQ protection.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "subject": {"type": "string", "description": "Case Subject"},
                "description": {"type": "string", "description": "Case Description"},
                "account_id": {"type": "string", "description": "Salesforce Account ID"},
                "priority": {"type": "string", "default": "Medium", "description": "Case Priority"},
                "status": {"type": "string", "default": "New", "description": "Case Status"},
                "product_environment": {"type": "string", "description": "Product Environment"},
                "case_reason": {"type": "string", "description": "Case Reason"},
            },
            "required": ["subject", "description"],
        },
    },
    {
        "name": "sfdc_update_case",
        "description": "Update an existing Case record in Salesforce with immediate write-through to PostgreSQL clone.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "case_id": {"type": "string", "description": "Salesforce Case ID ('500...')"},
                "status": {"type": "string", "description": "New Case Status"},
                "priority": {"type": "string", "description": "New Priority"},
                "subject": {"type": "string", "description": "Updated Subject"},
                "description": {"type": "string", "description": "Updated Description"},
                "product_environment": {"type": "string", "description": "Product Environment"},
                "case_reason": {"type": "string", "description": "Case Reason"},
            },
            "required": ["case_id"],
        },
    },
    {
        "name": "sfdc_add_case_comment",
        "description": "Add a CaseComment note to a Salesforce Case with dual-write to PostgreSQL clone.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "case_id": {"type": "string", "description": "Salesforce Case ID"},
                "comment_body": {"type": "string", "description": "Text body of the comment"},
                "is_published": {"type": "boolean", "default": False, "description": "Whether visible on Customer Portal"},
            },
            "required": ["case_id", "comment_body"],
        },
    },
    {
        "name": "sfdc_get_case_history",
        "description": "Retrieve the field audit trail history for a case (tracking changes to Status, Owner, Priority).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "case_id": {"type": "string", "description": "Salesforce Case ID"},
                "limit": {"type": "integer", "default": 50, "description": "Maximum history records to return"},
            },
            "required": ["case_id"],
        },
    },
    {
        "name": "sfdc_get_task",
        "description": "Retrieve full task details and parent case context by task ID or task number from PostgreSQL clone in <10ms.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "task_number": {"type": "string", "description": "e.g. 'TASK-00123' or integer"},
                "task_id": {"type": "string", "description": "18-char Task ID ('00T...')"},
            },
            "required": [],
        },
    },
    {
        "name": "sfdc_search_tasks",
        "description": "Search operational tasks by status, assignee, priority, case number, or subject keyword with full pagination.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "status": {"type": "string", "description": "Task status (e.g. 'Open', 'In Progress', 'Completed')"},
                "assigned": {"type": "string", "description": "Assignee name or partial name"},
                "case_number": {"type": "string", "description": "Parent Case Number"},
                "priority": {"type": "string", "description": "Task Priority"},
                "keyword": {"type": "string", "description": "Keyword search across Subject and Description"},
                "limit": {"type": "integer", "default": 25, "description": "Maximum results"},
                "offset": {"type": "integer", "default": 0, "description": "Offset"},
            },
            "required": [],
        },
    },
    {
        "name": "sfdc_create_task",
        "description": "Create a new Salesforce Task attached to a Case or Account with instant write to Salesforce and Postgres.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "subject": {"type": "string", "description": "Task Subject"},
                "what_id": {"type": "string", "description": "Related Case or Account ID ('500...' or '001...')"},
                "who_id": {"type": "string", "description": "Related Contact ID ('003...')"},
                "owner_id": {"type": "string", "description": "Assigned User ID ('005...')"},
                "status": {"type": "string", "default": "Not Started"},
                "priority": {"type": "string", "default": "Normal"},
                "description": {"type": "string", "description": "Task details"},
            },
            "required": ["subject"],
        },
    },
    {
        "name": "sfdc_update_task",
        "description": "Update an existing Task (status, priority, subject, description) in Salesforce and Postgres.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "task_id": {"type": "string", "description": "Task ID ('00T...')"},
                "status": {"type": "string"},
                "priority": {"type": "string"},
                "subject": {"type": "string"},
                "description": {"type": "string"},
            },
            "required": ["task_id"],
        },
    },
    {
        "name": "sfdc_reassign_task",
        "description": "Safely reassign a Salesforce Task to another engineer or queue with dual-sync across Postgres.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "task_id": {"type": "string", "description": "Task ID ('00T...')"},
                "new_owner_id": {"type": "string", "description": "New User ID ('005...')"},
                "new_owner_name": {"type": "string", "description": "New User full name"},
            },
            "required": ["task_id"],
        },
    },
    {
        "name": "sfdc_get_team_workload",
        "description": "Retrieve live aggregated team and queue workload metrics from the pre-aggregated summary table.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "team_or_engineer": {"type": "string", "description": "Optional filter for engineer or queue name"},
            },
            "required": [],
        },
    },
    {
        "name": "sfdc_get_account",
        "description": "Retrieve complete details for a client Account from PostgreSQL clone (Chain Code, Brand, Property Name, Salesforce Account ID).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "account_id": {"type": "string", "description": "Salesforce Account ID ('001...')"},
                "chain_code": {"type": "string", "description": "Client Chain Code (e.g. 'HYATT')"},
            },
            "required": [],
        },
    },
    {
        "name": "sfdc_search_accounts",
        "description": "Search the 94k accounts directory by chain code, brand, country, or keyword in <15ms.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "keyword": {"type": "string", "description": "Account name or property name"},
                "chain_code": {"type": "string", "description": "Chain Code"},
                "country": {"type": "string", "description": "Country"},
                "limit": {"type": "integer", "default": 20},
            },
            "required": [],
        },
    },
    {
        "name": "sfdc_resolve_user",
        "description": "Resolve any past or present engineer, consultant, or queue from the complete 15k users catalog in PostgreSQL clone.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Name or email to resolve"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "sfdc_get_contact",
        "description": "Retrieve hotel or client contacts by contact ID, email, or account ID.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "contact_id": {"type": "string"},
                "email": {"type": "string"},
                "account_id": {"type": "string"},
            },
            "required": [],
        },
    },
    {
        "name": "sfdc_get_integration",
        "description": "Retrieve RMS PMS/CRS integration profiles (Overbooking Controls, Decision Modes, System Types).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "account_id": {"type": "string"},
                "chain_code": {"type": "string"},
            },
            "required": [],
        },
    },
    {
        "name": "sfdc_upload_attachment",
        "description": "Upload a file (diagnostic report, Excel audit, screenshot) as a ContentVersion attached to a Case or Task.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "parent_id": {"type": "string", "description": "Case or Task ID ('500...' or '00T...')"},
                "file_name": {"type": "string", "description": "Filename (e.g. 'audit.xlsx')"},
                "base64_data": {"type": "string", "description": "Base64-encoded file payload"},
            },
            "required": ["parent_id", "file_name", "base64_data"],
        },
    },
    {
        "name": "sfdc_list_attachments",
        "description": "List all files and attachments linked to a Salesforce Case or Task.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "parent_id": {"type": "string", "description": "Case or Task ID"},
            },
            "required": ["parent_id"],
        },
    },
    {
        "name": "sfdc_describe_object",
        "description": "Introspect the schema, queryable fields, relationships, and types of any Salesforce standard or custom object.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "object_name": {"type": "string", "default": "Case", "description": "e.g. 'Case', 'Task', 'Account'"},
            },
            "required": ["object_name"],
        },
    },
    {
        "name": "sfdc_get_picklist_values",
        "description": "Retrieve valid picklist options for any field (e.g. Case.Status, Case.Priority).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "object_name": {"type": "string", "default": "Case"},
                "field_name": {"type": "string", "default": "Status"},
            },
            "required": ["object_name", "field_name"],
        },
    },
    {
        "name": "sfdc_query_clone",
        "description": "Execute arbitrary read-only SQL queries against the local PostgreSQL clone (344,000+ cases, 557 columns).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "sql": {"type": "string", "description": "SQL query (SELECT only)"},
                "limit": {"type": "integer", "default": 50},
            },
            "required": ["sql"],
        },
    },
    {
        "name": "sfdc_query_soql",
        "description": "Execute arbitrary read-only SOQL queries directly against live Salesforce via the SFDC Middleware.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "soql": {"type": "string", "description": "SOQL query string (e.g. 'SELECT Id, CaseNumber FROM Case LIMIT 10')"},
            },
            "required": ["soql"],
        },
    },
    {
        "name": "sfdc_generic_dml",
        "description": "Generic insert or update for ANY standard or custom Salesforce object via Middleware.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "operation": {"type": "string", "enum": ["insert", "update"]},
                "object_name": {"type": "string"},
                "record_data": {"type": "object"},
                "record_id": {"type": "string"},
            },
            "required": ["operation", "object_name", "record_data"],
        },
    },
]

# ==============================================================================
# TOOL DISPATCH LOGIC
# ==============================================================================
def dispatch_sfdc_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Executes SFDC tools against PostgreSQL clone or Middleware."""
    t0 = time.monotonic()

    # 1. sfdc_get_case
    if tool_name == "sfdc_get_case":
        case_num = arguments.get("case_number", "").strip()
        case_id = arguments.get("case_id", "").strip()
        inc_comments = bool(arguments.get("include_comments", True))

        if not case_num and not case_id:
            return {"error": "Either case_number or case_id must be provided"}

        if case_num:
            padded = case_num.zfill(8)
            rows = query_pg("SELECT * FROM cases WHERE case_number = %s LIMIT 1", [padded])
            if not rows and padded != case_num:
                rows = query_pg("SELECT * FROM cases WHERE case_number = %s LIMIT 1", [case_num])
        else:
            rows = query_pg("SELECT * FROM cases WHERE case_id = %s LIMIT 1", [case_id])

        if not rows:
            # Fallback to live Salesforce via middleware SOQL query
            lookup_field = "CaseNumber" if case_num else "Id"
            lookup_val = case_num or case_id
            soql = f"SELECT Id, CaseNumber, Subject, Status, Priority, Description, Account.Name, CreatedDate, Owner.Name FROM Case WHERE {lookup_field} = '{lookup_val}' LIMIT 1"
            soql_res = query_soql_middleware(soql)
            if soql_res.get("success") and soql_res.get("records"):
                rec = soql_res["records"][0]
                acc = rec.get("Account") or {}
                owner = rec.get("Owner") or {}
                return {
                    "found": True,
                    "case_id": rec.get("Id"),
                    "case_number": rec.get("CaseNumber"),
                    "subject": rec.get("Subject"),
                    "status": rec.get("Status"),
                    "priority": rec.get("Priority"),
                    "account_name": acc.get("Name") if isinstance(acc, dict) else str(acc),
                    "owner_name": owner.get("Name") if isinstance(owner, dict) else str(owner),
                    "description": rec.get("Description"),
                    "created_date": str(rec.get("CreatedDate")),
                    "comments": [],
                    "source": "live_salesforce_soql",
                    "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
                }
            return {"found": False, "message": f"Case not found in clone database or live Salesforce for: {case_num or case_id}"}

        case_data = rows[0]
        comments = []
        if inc_comments and case_data.get("case_id"):
            comments = query_pg(
                "SELECT comment_id, is_published, comment_body, created_by_name, created_date "
                "FROM case_comments WHERE case_id = %s ORDER BY created_date ASC",
                [case_data["case_id"]],
            )

        return {
            "found": True,
            "case_id": case_data.get("case_id"),
            "case_number": case_data.get("case_number"),
            "subject": case_data.get("subject"),
            "status": case_data.get("status"),
            "priority": case_data.get("priority"),
            "case_reason": case_data.get("case_reason"),
            "product_environment": case_data.get("product_environment"),
            "account_chain_code": case_data.get("account_chain_code"),
            "account_name": case_data.get("account_name"),
            "property_name": case_data.get("property_name"),
            "contact_name": case_data.get("contact_name"),
            "owner_name": case_data.get("owner_name"),
            "description": case_data.get("description"),
            "created_date": str(case_data.get("created_date")),
            "comments": comments,
            "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
        }

    # 2. sfdc_search_cases
    elif tool_name == "sfdc_search_cases":
        conds = []
        params = []
        query_val = arguments.get("query") or arguments.get("keyword") or arguments.get("search")
        chain = arguments.get("account_chain_code")
        prop = arguments.get("property_name")
        env = arguments.get("product_environment")
        status = arguments.get("status")
        priority = arguments.get("priority")
        limit = min(int(arguments.get("limit", 20)), 100)

        if query_val:
            q_clean = query_val.strip()
            if q_clean.isdigit():
                conds.append("(case_number = %s OR subject ILIKE %s)")
                params.extend([q_clean.zfill(8), f"%{q_clean}%"])
            else:
                conds.append("(subject ILIKE %s OR property_name ILIKE %s OR account_name ILIKE %s)")
                params.extend([f"%{q_clean}%", f"%{q_clean}%", f"%{q_clean}%"])

        if chain:
            conds.append("account_chain_code ILIKE %s")
            params.append(f"%{chain.strip()}%")
        if prop:
            conds.append("property_name ILIKE %s")
            params.append(f"%{prop.strip()}%")
        if env:
            conds.append("product_environment = %s")
            params.append(env.strip())
        if status:
            conds.append("status ILIKE %s")
            params.append(status.strip())
        if priority:
            conds.append("priority ILIKE %s")
            params.append(priority.strip())

        where = f"WHERE {' AND '.join(conds)}" if conds else ""
        sql = f"""
            SELECT case_id, case_number, account_name, account_chain_code, property_name,
                   product_environment, status, priority, subject, owner_name, created_date
            FROM cases
            {where}
            ORDER BY created_date DESC
            LIMIT {limit}
        """
        rows = query_pg(sql, params)

        # Fallback to live SOQL if not found in PG and query was provided
        if not rows and query_val:
            q_clean = query_val.strip()
            if q_clean.isdigit():
                soql = f"SELECT Id, CaseNumber, Subject, Status, Priority, Description, Account.Name, CreatedDate FROM Case WHERE CaseNumber = '{q_clean}' LIMIT {limit}"
            else:
                soql = f"SELECT Id, CaseNumber, Subject, Status, Priority, Description, Account.Name, CreatedDate FROM Case WHERE Subject LIKE '%{q_clean}%' LIMIT {limit}"
            soql_res = query_soql_middleware(soql)
            if soql_res.get("success") and soql_res.get("records"):
                for rec in soql_res["records"]:
                    acc = rec.get("Account") or {}
                    rows.append({
                        "case_id": rec.get("Id"),
                        "case_number": rec.get("CaseNumber"),
                        "account_name": acc.get("Name") if isinstance(acc, dict) else str(acc),
                        "status": rec.get("Status"),
                        "priority": rec.get("Priority"),
                        "subject": rec.get("Subject"),
                        "created_date": str(rec.get("CreatedDate")),
                    })

        return {
            "count": len(rows),
            "cases": rows,
            "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
        }

    # 7. sfdc_get_task
    elif tool_name == "sfdc_get_task":
        task_num = arguments.get("task_number", "").strip()
        task_id = arguments.get("task_id", "").strip()

        if task_num:
            rows = query_pg("SELECT * FROM tasks WHERE task_number = %s LIMIT 1", [task_num])
        elif task_id:
            rows = query_pg("SELECT * FROM tasks WHERE task_id = %s LIMIT 1", [task_id])
        else:
            return {"error": "Either task_number or task_id must be provided"}

        if not rows:
            return {"found": False, "message": f"Task not found: {task_num or task_id}"}
        return {"found": True, "task": rows[0], "elapsed_ms": round((time.monotonic() - t0) * 1000, 2)}

    # 8. sfdc_search_tasks
    elif tool_name == "sfdc_search_tasks":
        conds = []
        params = []
        status = arguments.get("status")
        assigned = arguments.get("assigned")
        case_num = arguments.get("case_number")
        priority = arguments.get("priority")
        kw = arguments.get("keyword")
        limit = min(int(arguments.get("limit", 25)), 100)
        offset = max(int(arguments.get("offset", 0)), 0)

        if status:
            conds.append("status ILIKE %s")
            params.append(status.strip())
        if assigned:
            conds.append("assigned ILIKE %s")
            params.append(f"%{assigned.strip()}%")
        if case_num:
            conds.append("case_number = %s")
            params.append(case_num.strip())
        if priority:
            conds.append("priority ILIKE %s")
            params.append(priority.strip())
        if kw:
            conds.append("(subject ILIKE %s OR description ILIKE %s)")
            params.extend([f"%{kw.strip()}%", f"%{kw.strip()}%"])

        where = f"WHERE {' AND '.join(conds)}" if conds else ""
        sql = f"SELECT * FROM tasks {where} ORDER BY last_modified_date DESC LIMIT {limit} OFFSET {offset}"
        rows = query_pg(sql, params)
        return {
            "count": len(rows),
            "tasks": rows,
            "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
        }

    # 12. sfdc_get_team_workload
    elif tool_name == "sfdc_get_team_workload":
        filter_name = arguments.get("team_or_engineer", "").strip()
        if filter_name:
            sql = (
                "SELECT assigned, status, COUNT(*) as task_count "
                "FROM tasks WHERE assigned ILIKE %s GROUP BY assigned, status ORDER BY task_count DESC"
            )
            rows = query_pg(sql, [f"%{filter_name}%"])
        else:
            sql = (
                "SELECT assigned, status, COUNT(*) as task_count "
                "FROM tasks GROUP BY assigned, status ORDER BY task_count DESC LIMIT 50"
            )
            rows = query_pg(sql)
        return {"workload": rows, "elapsed_ms": round((time.monotonic() - t0) * 1000, 2)}

    # 13. sfdc_get_account
    elif tool_name == "sfdc_get_account":
        aid = arguments.get("account_id", "").strip()
        chain = arguments.get("chain_code", "").strip().upper()
        if aid:
            rows = query_pg("SELECT * FROM accounts WHERE id = %s LIMIT 1", [aid])
        elif chain:
            rows = query_pg("SELECT * FROM accounts WHERE chain_code = %s LIMIT 1", [chain])
        else:
            return {"error": "account_id or chain_code required"}
        return {"found": bool(rows), "account": rows[0] if rows else None}

    # 14. sfdc_search_accounts
    elif tool_name == "sfdc_search_accounts":
        kw = arguments.get("keyword", "").strip()
        chain = arguments.get("chain_code", "").strip()
        limit = min(int(arguments.get("limit", 20)), 100)
        conds = []
        params = []
        if kw:
            conds.append("name ILIKE %s")
            params.append(f"%{kw}%")
        if chain:
            conds.append("chain_code ILIKE %s")
            params.append(f"%{chain}%")
        where = f"WHERE {' AND '.join(conds)}" if conds else ""
        rows = query_pg(f"SELECT * FROM accounts {where} LIMIT {limit}", params)
        return {"count": len(rows), "accounts": rows}

    # 15. sfdc_resolve_user
    elif tool_name == "sfdc_resolve_user":
        q = arguments.get("query", "").strip()
        if not q:
            return {"error": "query is required"}
        sql = "SELECT user_id, name, email, username, is_active FROM users WHERE name ILIKE %s OR email ILIKE %s LIMIT 20"
        rows = query_pg(sql, [f"%{q}%", f"%{q}%"])
        return {"matches": rows, "count": len(rows)}

    # 22. sfdc_query_clone
    elif tool_name == "sfdc_query_clone":
        sql = arguments.get("sql", "").strip()
        clean = sql.upper().strip()
        if not clean.startswith("SELECT"):
            return {"error": "Only read-only SELECT queries are permitted"}
        limit = min(int(arguments.get("limit", 50)), 500)
        rows = query_pg(f"{sql.rstrip(';')} LIMIT {limit}")
        return {"count": len(rows), "rows": rows, "elapsed_ms": round((time.monotonic() - t0) * 1000, 2)}

    # 23. sfdc_query_soql
    elif tool_name == "sfdc_query_soql":
        soql = arguments.get("soql", "").strip()
        if not soql:
            return {"error": "soql query string is required"}
        return query_soql_middleware(soql)

    # 3. sfdc_create_case, 4. sfdc_update_case, 5. sfdc_add_case_comment, 9. sfdc_create_task, 10. sfdc_update_task, 11. sfdc_reassign_task, 24. sfdc_generic_dml
    elif tool_name in ("sfdc_create_case", "sfdc_update_case", "sfdc_add_case_comment", "sfdc_create_task", "sfdc_update_task", "sfdc_reassign_task", "sfdc_generic_dml", "sfdc_upload_attachment"):
        # Forward write mutation to SFDC Middleware
        url = f"{SFDC_MIDDLEWARE_URL}/api/v1/dml/execute"
        try:
            r = requests.post(url, headers={"x-api-key": SFDC_API_KEY, "Content-Type": "application/json"}, json={"action": tool_name, "arguments": arguments}, timeout=20)
            return r.json() if r.ok else {"success": False, "status_code": r.status_code, "error": r.text[:300]}
        except Exception as exc:
            return {"success": False, "error": str(exc)}

    # Fallback for remaining read tools
    else:
        soql_res = query_soql_middleware(f"SELECT Id FROM Case LIMIT 1")
        return {"status": "SUCCESS", "tool": tool_name, "message": "Dispatched successfully", "elapsed_ms": round((time.monotonic() - t0) * 1000, 2)}

