#!/usr/bin/env python3
"""
SAS IDeaS Master Enterprise Unified Super-MCP Verification Suite
================================================================
Comprehensive verification testing:
1. HTTP Health check (/health on port 8550)
2. SSE Transport handshake (/sse)
3. Total tools verification (All 168 canonical tools)
4. Domain 1 (SFDC): sfdc_search_cases
5. Domain 2 (CMA): cma_search_chains
6. Domain 3 (Optix DB): optix_list_databases
7. Domain 4 (Confluence): confluence_list_runbooks
8. Domain 5 (Datadog): datadog_validate_credentials
9. Domain 6 (UPS/FDS): ups_validate_m2m_credentials
10. Unified Platform Resource (enterprise://platform/status)
11. Unified Tools Catalog Resource (enterprise://tools/catalog)
"""

import sys
import json
import time
import asyncio
import requests

TARGET_URL = "http://localhost:8550"

def log_test(name: str, passed: bool, details: str = ""):
    status = "[PASS]" if passed else "[FAIL]"
    print(f"{status} {name}: {details}")

def main():
    print("=" * 80)
    print("SAS IDEAS MASTER ENTERPRISE UNIFIED SUPER-MCP VERIFICATION SUITE")
    print(f"Target: {TARGET_URL}")
    print("=" * 80)

    total_tests = 0
    passed_tests = 0

    # Test 1: /health
    total_tests += 1
    try:
        r = requests.get(f"{TARGET_URL}/health", timeout=10)
        data = r.json() if r.ok else {}
        passed = r.status_code == 200 and data.get("status") == "HEALTHY"
        if passed:
            passed_tests += 1
            tools = data.get("total_canonical_tools", 0)
            domains = data.get("domains", {})
            log_test(
                "Health Check Probe (/health)",
                True,
                f"Status: HEALTHY | Total Tools: {tools} | SFDC: {domains.get('sfdc',{}).get('tools')}, CMA: {domains.get('cma',{}).get('tools')}, Optix: {domains.get('optix',{}).get('tools')}, Conf: {domains.get('confluence',{}).get('tools')}, DD: {domains.get('datadog',{}).get('tools')}, UPS: {domains.get('ups_fds',{}).get('tools')}"
            )
        else:
            log_test("Health Check Probe (/health)", False, f"HTTP {r.status_code}: {r.text[:100]}")
    except Exception as e:
        log_test("Health Check Probe (/health)", False, f"Exception: {e}")
        print("Unified server not reachable at port 8550. Exiting test suite.")
        sys.exit(1)

    # Test 2: SSE handshake
    total_tests += 1
    session_endpoint = ""
    try:
        r = requests.get(f"{TARGET_URL}/sse", stream=True, timeout=10)
        for line in r.iter_lines():
            line_str = line.decode("utf-8")
            if line_str.startswith("data: /messages?sessionId="):
                session_endpoint = line_str.replace("data: ", "").strip()
                break
        passed = bool(session_endpoint)
        if passed:
            passed_tests += 1
            log_test("SSE Transport Handshake (/sse)", True, f"Session endpoint: {session_endpoint}")
        else:
            log_test("SSE Transport Handshake (/sse)", False, "Failed to capture sessionId")
    except Exception as e:
        log_test("SSE Transport Handshake (/sse)", False, f"Exception: {e}")

    # Import modules for in-process verification
    from unified_mcp_server import MASTER_TOOLS, MASTER_RESOURCES, dispatch_unified_tool, read_unified_resource

    # Test 3: Total Tool Registry Count
    total_tests += 1
    passed = len(MASTER_TOOLS) == 168 and len(MASTER_RESOURCES) >= 12
    if passed:
        passed_tests += 1
        log_test("Unified Tools & Resources Registry", True, f"Found {len(MASTER_TOOLS)} canonical tools, {len(MASTER_RESOURCES)} resources")
    else:
        log_test("Unified Tools & Resources Registry", False, f"Tools count: {len(MASTER_TOOLS)}")

    # Async helper for running dispatch_unified_tool
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Test 4: Domain 1 (SFDC) - sfdc_search_cases
    total_tests += 1
    try:
        r_sfdc = loop.run_until_complete(dispatch_unified_tool("sfdc_search_cases", {"limit": 2}))
        passed = r_sfdc.get("count", 0) > 0
        if passed:
            passed_tests += 1
            log_test("Domain 1: Salesforce (sfdc_search_cases)", True, f"Retrieved {r_sfdc.get('count')} cases from clone (Sample: {r_sfdc['cases'][0].get('case_number')})")
        else:
            log_test("Domain 1: Salesforce (sfdc_search_cases)", False, str(r_sfdc)[:100])
    except Exception as e:
        log_test("Domain 1: Salesforce (sfdc_search_cases)", False, str(e))

    # Test 5: Domain 2 (CMA) - cma_search_chains
    total_tests += 1
    try:
        r_cma = loop.run_until_complete(dispatch_unified_tool("cma_search_chains", {"keyword": "Hilton", "limit": 2}))
        results = r_cma.get("results") if isinstance(r_cma, dict) else []
        passed = bool(results)
        if passed:
            passed_tests += 1
            log_test("Domain 2: CMA Gateway (cma_search_chains)", True, f"Matched chains: {len(results)} (Sample: {results[0].get('identifier')})")
        else:
            log_test("Domain 2: CMA Gateway (cma_search_chains)", False, str(r_cma)[:100])
    except Exception as e:
        log_test("Domain 2: CMA Gateway (cma_search_chains)", False, str(e))

    # Test 6: Domain 3 (Optix DB) - optix_list_all_databases
    total_tests += 1
    try:
        r_optix = loop.run_until_complete(dispatch_unified_tool("optix_list_all_databases", {"limit": 5}))
        dbs = r_optix.get("databases", []) if isinstance(r_optix, dict) else []
        passed = bool(dbs)
        if passed:
            passed_tests += 1
            log_test("Domain 3: Optix DB Cluster (optix_list_all_databases)", True, f"Sampled {len(dbs)} DBs from {r_optix.get('total_matching')} cluster catalog")
        else:
            log_test("Domain 3: Optix DB Cluster (optix_list_all_databases)", False, str(r_optix)[:100])
    except Exception as e:
        log_test("Domain 3: Optix DB Cluster (optix_list_all_databases)", False, str(e))

    # Test 7: Domain 4 (Confluence) - confluence_list_all_runbooks
    total_tests += 1
    try:
        r_conf = loop.run_until_complete(dispatch_unified_tool("confluence_list_all_runbooks", {}))
        passed = r_conf.get("total_runbooks", 0) >= 7
        if passed:
            passed_tests += 1
            log_test("Domain 4: Confluence KB (confluence_list_all_runbooks)", True, f"Found {r_conf.get('total_runbooks')} engineering diagnostic runbooks")
        else:
            log_test("Domain 4: Confluence KB (confluence_list_all_runbooks)", False, str(r_conf)[:100])
    except Exception as e:
        log_test("Domain 4: Confluence KB (confluence_list_all_runbooks)", False, str(e))

    # Test 8: Domain 5 (Datadog) - datadog_validate_credentials
    total_tests += 1
    try:
        r_dd = loop.run_until_complete(dispatch_unified_tool("datadog_validate_credentials", {}))
        passed = r_dd.get("valid") is True
        if passed:
            passed_tests += 1
            log_test("Domain 5: Datadog Observability (datadog_validate_credentials)", True, f"Site: {r_dd.get('site')} | Message: {r_dd.get('message')}")
        else:
            log_test("Domain 5: Datadog Observability (datadog_validate_credentials)", False, str(r_dd)[:100])
    except Exception as e:
        log_test("Domain 5: Datadog Observability (datadog_validate_credentials)", False, str(e))

    # Test 9: Domain 6 (UPS/FDS) - ups_validate_m2m_credentials
    total_tests += 1
    try:
        r_ups = loop.run_until_complete(dispatch_unified_tool("ups_validate_m2m_credentials", {}))
        passed = r_ups.get("valid") is True
        if passed:
            passed_tests += 1
            log_test("Domain 6: UPS & FDS Platform (ups_validate_m2m_credentials)", True, f"Message: {r_ups.get('message')}")
        else:
            log_test("Domain 6: UPS & FDS Platform (ups_validate_m2m_credentials)", False, str(r_ups)[:100])
    except Exception as e:
        log_test("Domain 6: UPS & FDS Platform (ups_validate_m2m_credentials)", False, str(e))

    # Test 10: Resource: enterprise://platform/status
    total_tests += 1
    try:
        content_status = read_unified_resource("enterprise://platform/status")
        passed = "SAS IDeaS Enterprise Unified MCP Platform" in content_status
        if passed:
            passed_tests += 1
            log_test("Unified Resource (enterprise://platform/status)", True, f"Bytes: {len(content_status)}")
        else:
            log_test("Unified Resource (enterprise://platform/status)", False, content_status[:100])
    except Exception as e:
        log_test("Unified Resource (enterprise://platform/status)", False, str(e))

    # Test 11: Resource: enterprise://tools/catalog
    total_tests += 1
    try:
        content_catalog = read_unified_resource("enterprise://tools/catalog")
        passed = "total_tools" in content_catalog and "168" in content_catalog
        if passed:
            passed_tests += 1
            log_test("Unified Tools Catalog Resource (enterprise://tools/catalog)", True, f"Bytes: {len(content_catalog)}")
        else:
            log_test("Unified Tools Catalog Resource (enterprise://tools/catalog)", False, content_catalog[:100])
    except Exception as e:
        log_test("Unified Tools Catalog Resource (enterprise://tools/catalog)", False, str(e))

    print("=" * 80)
    print(f"VERIFICATION COMPLETE: {passed_tests}/{total_tests} Checks Passed.")
    print("=" * 80)

    if passed_tests == total_tests:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
