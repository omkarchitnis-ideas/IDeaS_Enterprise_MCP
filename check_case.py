import requests
from sfdc_mcp_server import query_pg, query_soql_middleware

# 1. Tables in PG
try:
    tables = query_pg("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    print("PG Tables:", [t['table_name'] for t in tables])
except Exception as e:
    print("PG Error:", e)

# 2. Check SOQL via middleware for 03379138
try:
    res = query_soql_middleware("SELECT Id, CaseNumber, Subject, Status, Account.Name FROM Case WHERE CaseNumber = '03379138'")
    print("SOQL Query result:", res)
except Exception as e:
    print("SOQL Error:", e)
