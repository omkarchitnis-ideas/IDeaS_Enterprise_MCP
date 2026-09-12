#!/usr/bin/env python3
"""
IDeaS UPS & FDS Enterprise Model Context Protocol (MCP) Server
==============================================================
Definitive 30-Tool Suite for Unified Property Service (UPS), User Identity Service (UIS),
FDS Platform APIs, and Cloud Enterprise Datafeed (CEDF).

Enterprise Capabilities:
1. Dynamic M2M OAuth2 Token Lifecycle: Automatic grant generation, caching, and 401 retry.
2. Comprehensive Property Resolution: Unified ID lookup, multi-criteria search, appConfig,
   vendorMappings (RateGain, Rubicon, OTA Insight, TravelClick), channels (Booking, Expedia, GDS),
   and nearby geo-spatial radius queries.
3. Client & Tenant Management: Directory lookup (1,280+ clients), Optix product licensing
   entitlement checks (417 clients), and client custom attributes.
4. Product & Environment Infrastructure: 42+ active environments across G3, Elevate, CentralRMS,
   RevPlan, Optix, BMR, RDL, EDF, with cluster base URL resolution.
5. Cloud Enterprise Datafeed (CEDF): Feed configurations and client upload enablement checks.
6. Identity & Access Management (UIS / FDS): User profile lookups, account status, lockout,
   SAML 2.0 / Okta SSO certificate health, Cognito pools, and 6-point IAM access diagnostics.
7. Dual Transports: HTTP Server-Sent Events (SSE) on Port 8560 + Stdio Transport.
"""

import os
import sys
import json
import time
import logging
import argparse
import threading
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone
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
logger = logging.getLogger("ups-mcp-server")

# ==============================================================================
# CONFIGURATION & CONSTANTS
# ==============================================================================
FDS_BASE_URL = os.getenv("FDS_BASE_URL", "https://fds.ideasrms.com").rstrip("/")
CEDF_BASE_URL = os.getenv("CEDF_BASE_URL", "https://cedf.ideasrms.com").rstrip("/")
HAL_BASE_URL = os.getenv("HAL_BASE_URL", "https://integration-setting-internal.ideasrms.com").rstrip("/")

DEFAULT_M2M_TOKEN_URL = (
    f"{FDS_BASE_URL}/api/uis/internal_m2m/oauth2/token"
    "?grant_type=client_credentials&scope=com.ideas.casper%2FideasApiClient"
)
DEFAULT_M2M_BASIC_AUTH = os.getenv(
    "FDS_M2M_BASIC_AUTH",
    "Basic MjU0NGVyaG02OGttNDdzbWRsODVmcjQyNnA6ZTd0bnRiZWQ3Y2R0b3F1bmdxZjdldWEybG9wZ3NuZnI5MTVqNzdmYnU1MXIyMmFhdHBk",
)
DEFAULT_M2M_COOKIE = os.getenv("FDS_M2M_COOKIE", "XSRF-TOKEN=3ee197d6-8d66-475d-84de-fe56eeb1f00b")

MCP_HOST = os.getenv("MCP_HOST", "0.0.0.0")
MCP_PORT = int(os.getenv("UPS_MCP_PORT", os.getenv("MCP_PORT", "8560")))

# ==============================================================================
# TOKEN LIFECYCLE MANAGER
# ==============================================================================
class UpsAuthManager:
    """Manages M2M OAuth2 bearer tokens with automatic caching and proactive refresh."""

    _instance: Optional["UpsAuthManager"] = None
    _lock = threading.Lock()

    def __init__(self):
        self._cached_token: Optional[str] = None
        self._token_expiry: float = 0.0
        self._renewals_count: int = 0
        self._last_refresh_time: Optional[str] = None
        self._last_error: Optional[str] = None

    @classmethod
    def get_instance(cls) -> "UpsAuthManager":
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
            return cls._instance

    def get_bearer_token(self, force_refresh: bool = False) -> str:
        """Returns a valid Bearer token, refreshing if expired or forced."""
        now = time.time()
        if not force_refresh and self._cached_token and now < self._token_expiry:
            return self._cached_token

        with self._lock:
            if not force_refresh and self._cached_token and now < self._token_expiry:
                return self._cached_token

            logger.info("Requesting fresh M2M Bearer token from FDS UIS OAuth2 endpoint...")
            headers = {
                "Authorization": DEFAULT_M2M_BASIC_AUTH,
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": DEFAULT_M2M_COOKIE,
            }
            try:
                resp = requests.post(DEFAULT_M2M_TOKEN_URL, headers=headers, timeout=12)
                if resp.ok:
                    data = resp.json()
                    token = data.get("access_token")
                    expires_in = int(data.get("expires_in", 3600))
                    if token:
                        self._cached_token = token
                        # Cache token with 5-minute safety margin
                        self._token_expiry = now + max(60, expires_in - 300)
                        self._renewals_count += 1
                        self._last_refresh_time = datetime.now(timezone.utc).isoformat()
                        self._last_error = None
                        logger.info("Successfully acquired and cached fresh M2M token (TTL: %ds)", expires_in)
                        return token
                self._last_error = f"HTTP {resp.status_code}: {resp.text[:200]}"
                logger.warning("FDS M2M token grant failed (HTTP %s): %s", resp.status_code, resp.text[:200])
            except Exception as exc:
                self._last_error = str(exc)
                logger.error("Network error while acquiring FDS M2M token: %s", exc)

            # Fallback to configured static environment token if available
            fallback = os.getenv("UPS_BEARER_TOKEN", "")
            if fallback:
                logger.warning("Using fallback UPS_BEARER_TOKEN from environment.")
                return fallback

            if self._cached_token:
                logger.warning("Using existing cached token despite expiration due to refresh failure.")
                return self._cached_token

            raise RuntimeError(f"Failed to obtain M2M Bearer token from FDS: {self._last_error}")

    def get_auth_headers(self, force_refresh: bool = False) -> Dict[str, str]:
        """Returns standard authorization headers with Bearer token."""
        token = self.get_bearer_token(force_refresh=force_refresh)
        return {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def get_telemetry(self) -> Dict[str, Any]:
        """Returns token telemetry and health stats."""
        if not self._cached_token:
            try:
                self.get_bearer_token()
            except Exception:
                pass
        now = time.time()
        ttl_sec = max(0, int(self._token_expiry - now)) if self._cached_token else 0
        return {
            "has_token": bool(self._cached_token),
            "ttl_seconds": ttl_sec,
            "ttl_minutes": round(ttl_sec / 60, 1),
            "is_valid": ttl_sec > 30,
            "renewals_count": self._renewals_count,
            "last_refresh_time": self._last_refresh_time,
            "last_error": self._last_error,
        }


AUTH_MGR = UpsAuthManager.get_instance()

# ==============================================================================
# HTTP HELPER WITH AUTOMATIC RETRY & TIMING
# ==============================================================================
def execute_api_call(
    method: str,
    url: str,
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Any] = None,
    timeout: int = 25,
    retry_on_401: bool = True,
) -> Dict[str, Any]:
    """Executes an HTTP call against FDS / UPS with M2M auth and 401 retry."""
    t0 = time.monotonic()
    req_headers = AUTH_MGR.get_auth_headers()
    if headers:
        req_headers.update(headers)

    try:
        resp = requests.request(
            method=method,
            url=url,
            headers=req_headers,
            params=params,
            json=json_body,
            timeout=timeout,
        )
        elapsed_ms = round((time.monotonic() - t0) * 1000, 2)

        # Retry once on 401 Unauthorized with fresh token
        if resp.status_code == 401 and retry_on_401:
            logger.warning("FDS API returned 401 Unauthorized for %s. Renewing token and retrying...", url)
            req_headers = AUTH_MGR.get_auth_headers(force_refresh=True)
            if headers:
                req_headers.update(headers)
            t1 = time.monotonic()
            resp = requests.request(
                method=method,
                url=url,
                headers=req_headers,
                params=params,
                json=json_body,
                timeout=timeout,
            )
            elapsed_ms = round((time.monotonic() - t1) * 1000, 2)

        if resp.status_code in (200, 201, 206):
            try:
                data = resp.json()
            except Exception:
                data = resp.text
            return {
                "success": True,
                "status_code": resp.status_code,
                "elapsed_ms": elapsed_ms,
                "data": data,
            }
        elif resp.status_code == 204:
            return {
                "success": True,
                "status_code": 204,
                "elapsed_ms": elapsed_ms,
                "data": [],
                "message": "No content found",
            }
        elif resp.status_code == 404:
            return {
                "success": False,
                "status_code": 404,
                "elapsed_ms": elapsed_ms,
                "error": "Entity or resource not found",
                "data": None,
            }
        else:
            return {
                "success": False,
                "status_code": resp.status_code,
                "elapsed_ms": elapsed_ms,
                "error": resp.text[:500],
            }
    except Exception as exc:
        elapsed_ms = round((time.monotonic() - t0) * 1000, 2)
        logger.error("HTTP request exception for %s: %s", url, exc)
        return {
            "success": False,
            "status_code": 500,
            "elapsed_ms": elapsed_ms,
            "error": str(exc),
        }


# Global memory caches
OPTIX_CLIENTS_CACHE: Optional[List[Dict[str, Any]]] = None
OPTIX_CLIENTS_EXPIRY: float = 0.0
CEDF_CONFIG_CACHE: Optional[List[Dict[str, Any]]] = None
CEDF_CONFIG_EXPIRY: float = 0.0

# ==============================================================================
# CANONICAL TOOL DEFINITIONS (30 TOOLS)
# ==============================================================================
UPS_TOOLS = [
    # --------------------------------------------------------------------------
    # 1. Authentication & Token Lifecycle
    # --------------------------------------------------------------------------
    {
        "name": "ups_get_auth_status",
        "description": "Returns the active status of the FDS M2M OAuth2 token, including TTL in seconds, renewals count, and endpoint connectivity.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "ups_refresh_token",
        "description": "Forces an immediate refresh of the FDS M2M OAuth2 Bearer token from the UIS OAuth2 service.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    # --------------------------------------------------------------------------
    # 2. Property Search & Details
    # --------------------------------------------------------------------------
    {
        "name": "ups_get_property_by_id",
        "description": "Retrieves comprehensive property details from UPS by unifiedId (name, chains, address, coordinates, hotelCapacity, salesforceAccountId, appConfig, vendorMappings, channels).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "unified_id": {
                    "type": "string",
                    "description": "The unique UUID of the property in UPS (e.g. '02677f76-50ea-4f28-8ab7-6235d8ce6e42').",
                },
            },
            "required": ["unified_id"],
        },
    },
    {
        "name": "ups_search_properties",
        "description": "Performs advanced search across 100,000+ enterprise properties using application configuration filters (clientCode, propertyCode, pmsPropertyId), chain code, postal code, or name.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "client_code": {
                    "type": "string",
                    "description": "Optional client organization code (e.g. 'HILTON', 'CHOICE', 'WYNDHAM').",
                },
                "property_code": {
                    "type": "string",
                    "description": "Optional internal PMS or IDeaS property code (e.g. 'LONLK', 'MEXCH', '0001').",
                },
                "pms_property_id": {
                    "type": "string",
                    "description": "Optional external PMS property code or ID.",
                },
                "parent_chain_code": {
                    "type": "string",
                    "description": "Optional parent chain code (e.g. 'WY', 'HL', 'CH').",
                },
                "postal_code": {
                    "type": "string",
                    "description": "Optional postal or ZIP code.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of properties to return (default: 20, max: 100).",
                    "default": 20,
                },
                "offset": {
                    "type": "integer",
                    "description": "Record offset for pagination (default: 0).",
                    "default": 0,
                },
                "sort_field": {
                    "type": "string",
                    "description": "Field to sort by: 'name', 'countryCode', 'state', 'city', 'parentChainCode', 'unifiedId'.",
                    "default": "name",
                },
                "sort_direction": {
                    "type": "string",
                    "description": "'ASC' or 'DESC' (default: 'ASC').",
                    "default": "ASC",
                },
            },
            "required": [],
        },
    },
    {
        "name": "ups_get_property_app_config",
        "description": "Extracts the application-specific configuration object for a property (e.g. 'g3', 'centralrms', 'elevate', 'revplan'), returning tenantDBHost, tenantDBName, hostUrl, and propertyCode.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "unified_id": {
                    "type": "string",
                    "description": "The unique UUID of the property in UPS.",
                },
                "app_name": {
                    "type": "string",
                    "description": "Application name to filter (e.g. 'g3', 'centralrms', 'elevate', 'revplan'). If omitted, returns all application configs.",
                },
            },
            "required": ["unified_id"],
        },
    },
    {
        "name": "ups_get_property_vendor_mappings",
        "description": "Extracts competitive rate shopping vendor mappings for a property (RateGain, Rubicon, OTA Insight, TravelClick, etc.).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "unified_id": {
                    "type": "string",
                    "description": "The unique UUID of the property in UPS.",
                },
            },
            "required": ["unified_id"],
        },
    },
    {
        "name": "ups_get_property_channels",
        "description": "Retrieves distribution and OTA channels configured for a property (Booking.com, Expedia, GDS, Sabre, Ctrip, etc.).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "unified_id": {
                    "type": "string",
                    "description": "The unique UUID of the property in UPS.",
                },
            },
            "required": ["unified_id"],
        },
    },
    {
        "name": "ups_get_nearby_properties",
        "description": "Finds competitor or sister properties within a specified radius (in meters or kilometers) of a target property using geo-coordinates.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "unified_id": {
                    "type": "string",
                    "description": "The target property's UUID.",
                },
                "radius_km": {
                    "type": "number",
                    "description": "Search radius in kilometers (default: 25.0 km).",
                    "default": 25.0,
                },
                "max_num_properties": {
                    "type": "integer",
                    "description": "Maximum number of nearby properties to return (default: 50).",
                    "default": 50,
                },
                "include_str": {
                    "type": "boolean",
                    "description": "Whether to include STR (Smith Travel Research) benchmark properties (default: true).",
                    "default": True,
                },
            },
            "required": ["unified_id"],
        },
    },
    {
        "name": "ups_get_property_custom_attributes",
        "description": "Retrieves business custom attributes defined on a property (e.g. RDRM, Management Type, Brand Code, Number of Rooms, Property Owner, Open Status).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "unified_id": {
                    "type": "string",
                    "description": "The unique UUID of the property in UPS.",
                },
            },
            "required": ["unified_id"],
        },
    },
    {
        "name": "ups_get_recent_property_audits",
        "description": "Fetches property UUIDs modified, created, or audited across the platform within the last 24 hours.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    # --------------------------------------------------------------------------
    # 3. Clients & Tenant Organizations
    # --------------------------------------------------------------------------
    {
        "name": "ups_list_clients",
        "description": "Lists enterprise clients from the UPS directory (1,280+ clients) with optional search filter and pagination.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "search": {
                    "type": "string",
                    "description": "Optional filter text matching clientCode or clientName (case-insensitive).",
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of clients to return (default: 50).",
                    "default": 50,
                },
                "offset": {
                    "type": "integer",
                    "description": "Offset index for pagination (default: 0).",
                    "default": 0,
                },
            },
            "required": [],
        },
    },
    {
        "name": "ups_get_client_by_code",
        "description": "Fetches client organization metadata by clientCode or clientId (e.g. 'HILTON', 'JENKINS', 'CHOICE').",
        "inputSchema": {
            "type": "object",
            "properties": {
                "client_id_or_code": {
                    "type": "string",
                    "description": "The client code or UUID (e.g. 'JENKINS' or 'be6cb2b0-72e2-49de-9f2e-d2ffb7e9fce0').",
                },
            },
            "required": ["client_id_or_code"],
        },
    },
    {
        "name": "ups_get_client_product_environments",
        "description": "Lists active product environments activated for a client organization by clientId.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "client_id": {
                    "type": "string",
                    "description": "The client UUID in UPS.",
                },
            },
            "required": ["client_id"],
        },
    },
    {
        "name": "ups_get_client_custom_attributes",
        "description": "Retrieves custom configuration attributes defined for a client organization by clientId.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "client_id": {
                    "type": "string",
                    "description": "The client UUID in UPS.",
                },
            },
            "required": ["client_id"],
        },
    },
    {
        "name": "ups_list_optix_clients",
        "description": "Fetches the full list of all 417 enterprise clients licensed for Optix product access with 1-hour caching.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "force_refresh": {
                    "type": "boolean",
                    "description": "Force fresh retrieval from FDS API bypassing cache (default: false).",
                    "default": False,
                },
            },
            "required": [],
        },
    },
    {
        "name": "ups_check_optix_client_access",
        "description": "Verifies whether a specific clientCode has active Optix product entitlement (required for SystemCEO role access).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "client_code": {
                    "type": "string",
                    "description": "The client code to check (e.g. 'JENKINS', 'WYNDHAM').",
                },
            },
            "required": ["client_code"],
        },
    },
    # --------------------------------------------------------------------------
    # 4. Products, Environments & Clusters
    # --------------------------------------------------------------------------
    {
        "name": "ups_list_products",
        "description": "Lists all available SAS IDeaS products (g3, elevate, centralrms, revplan, optix, smartspace, bmr, rdl, edf, processingdashboard).",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "ups_list_product_environments",
        "description": "Lists all 42+ active product environments with URLs, display names, and cluster tags (e.g. G3-PROD1, G3-PROD5, Elevate, CentralRMS).",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "ups_resolve_cluster_url",
        "description": "Resolves the live HTTPS base URL for a given productEnvironmentId or environment nameId.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "product_environment_id": {
                    "type": "string",
                    "description": "The productEnvironmentId UUID (e.g. 'cdf68eb7-b0d7-43d9-b2e3-d6e0cdc89249') or environment name (e.g. 'G3-PROD1').",
                },
            },
            "required": ["product_environment_id"],
        },
    },
    # --------------------------------------------------------------------------
    # 5. Cloud Enterprise Datafeed (CEDF)
    # --------------------------------------------------------------------------
    {
        "name": "cedf_get_clients_configuration",
        "description": "Retrieves the complete CEDF client configuration feed from cedf.ideasrms.com with 1-hour caching.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "force_refresh": {
                    "type": "boolean",
                    "description": "Force fresh retrieval from CEDF API (default: false).",
                    "default": False,
                },
            },
            "required": [],
        },
    },
    {
        "name": "cedf_check_client_upload_status",
        "description": "Verifies whether a client is configured in CEDF and whether 'isClientUploadEnabled' is True for a given source system and product.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "client_code": {
                    "type": "string",
                    "description": "The client code to check (e.g. 'WYNDHAM', 'HILTON').",
                },
                "source_system": {
                    "type": "string",
                    "description": "Source system (default: 'G3').",
                    "default": "G3",
                },
                "product": {
                    "type": "string",
                    "description": "Product code (default: 'OPTIX').",
                    "default": "OPTIX",
                },
            },
            "required": ["client_code"],
        },
    },
    # --------------------------------------------------------------------------
    # 6. Identity, IAM & Access Management (UIS / FDS)
    # --------------------------------------------------------------------------
    {
        "name": "uis_get_user_by_email",
        "description": "Fetches user identity profile, status (ACTIVE/LOCKED), MFA, and assigned roles from the UIS Identity Directory.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": "The user's corporate email address.",
                },
            },
            "required": ["email"],
        },
    },
    {
        "name": "uis_get_client_sso_config",
        "description": "Fetches SAML 2.0 / Okta / Azure AD Single Sign-On configuration, certificate validity, and IdP metadata for client organization.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "client_code": {
                    "type": "string",
                    "description": "The client organization code.",
                },
            },
            "required": ["client_code"],
        },
    },
    {
        "name": "uis_get_cognito_user_pool",
        "description": "Retrieves AWS Cognito user pool configuration for a given client code or organization.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "client_code": {
                    "type": "string",
                    "description": "The client organization code.",
                },
            },
            "required": ["client_code"],
        },
    },
    {
        "name": "uis_diagnose_user_access",
        "description": "Executes comprehensive 6-point IAM access evaluation (User Presence, Account Status, Lockout, Property Tenancy, Role Entitlement, SSO Certificate Health) with auto-remediation steps.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": "User email to evaluate.",
                },
                "property_code": {
                    "type": "string",
                    "description": "Optional property code to verify tenancy scope assignment.",
                },
                "client_code": {
                    "type": "string",
                    "description": "Optional client organization code.",
                },
                "required_role": {
                    "type": "string",
                    "description": "Required role to check (e.g. 'REVENUE_MANAGER', 'SYSTEMCEO', 'RMS_ADMIN').",
                    "default": "REVENUE_MANAGER",
                },
            },
            "required": ["email"],
        },
    },
    # --------------------------------------------------------------------------
    # 7. System Operations, Notices & Health
    # --------------------------------------------------------------------------
    {
        "name": "ups_list_announcements",
        "description": "Retrieves active operational announcements, scheduled maintenance notices, and platform updates defined in UPS.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "ups_resolve_property_to_cluster",
        "description": "High-level helper: directly resolves clientCode and propertyCode into its target G3 / Optix cluster URL, database host, database name, and salesforceAccountId in one unified response.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "client_code": {
                    "type": "string",
                    "description": "Client code (e.g. 'HILTON', 'WYNDHAM').",
                },
                "property_code": {
                    "type": "string",
                    "description": "Property code (e.g. 'LONLK', '0001').",
                },
            },
            "required": ["client_code", "property_code"],
        },
    },
    {
        "name": "ups_get_system_health",
        "description": "Executes health check and latency benchmarks across UPS, UIS, and CEDF APIs.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "ups_get_api_catalog",
        "description": "Returns a comprehensive catalog of all active UPS, UIS, and CEDF endpoints, Swagger documentations, and capabilities.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "ups_validate_m2m_credentials",
        "description": "Validates that FDS M2M OAuth2 client credentials can successfully issue tokens and authenticate against live endpoints.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    # --------------------------------------------------------------------------
    # 7. HAL Integration Settings & Microservice Diagnostics
    # --------------------------------------------------------------------------
    {
        "name": "fds_get_integration_property_configs",
        "description": "Queries Spring Data REST HAL integrationPropertyConfigs (PMS and decision delivery integration settings, deferred delivery, vendorId, priority, extended attributes) filtered by propertyCode, clientCode, or vendorId.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "property_code": {"type": "string", "description": "Property short code (e.g. 'CO027', 'LONLK')."},
                "client_code": {"type": "string", "description": "Client organization code (e.g. 'CHOICE', 'HILTON')."},
                "vendor_id": {"type": "string", "description": "Integration vendor ID (e.g. 'SkyTouch', 'OperaCloud')."},
                "page": {"type": "integer", "description": "Pagination page number (default 0)."},
                "size": {"type": "integer", "description": "Page size (default 20)."},
            },
            "required": [],
        },
    },
    {
        "name": "fds_get_vendor_configs",
        "description": "Queries Spring Data REST HAL vendorConfigs (vendor connection profiles, integrationType e.g. OXI_PMS / HTNG, credentials, validation channels, and priority).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "vendor_id": {"type": "string", "description": "Vendor identifier (e.g. 'smoke_test_vendor_OXI')."},
                "integration_type": {"type": "string", "description": "Integration protocol type (e.g. 'OXI_PMS', 'HTNG')."},
                "page": {"type": "integer", "description": "Pagination page number (default 0)."},
                "size": {"type": "integer", "description": "Page size (default 20)."},
            },
            "required": [],
        },
    },
    {
        "name": "fds_get_integration_setting_changelogs",
        "description": "Queries Spring Data REST HAL integrationSettingChangelogs to inspect historical audit changes to integration settings and configs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "page": {"type": "integer", "description": "Pagination page number (default 0)."},
                "size": {"type": "integer", "description": "Page size (default 20)."},
            },
            "required": [],
        },
    },
    {
        "name": "fds_get_mongo_operation_audits",
        "description": "Queries Spring Data REST HAL mongoOperationAudits for MongoDB operation traces, timestamps, and entity updates across integration settings.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "page": {"type": "integer", "description": "Pagination page number (default 0)."},
                "size": {"type": "integer", "description": "Page size (default 20)."},
            },
            "required": [],
        },
    },
    {
        "name": "fds_get_nucleus_integration_settings",
        "description": "Queries Spring Data REST HAL base integration settings (baseIntegrationConfigs / nucleusIntegrationSettings).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "page": {"type": "integer", "description": "Pagination page number (default 0)."},
                "size": {"type": "integer", "description": "Page size (default 20)."},
            },
            "required": [],
        },
    },
    {
        "name": "fds_probe_microservice_health",
        "description": "Actively probes the live health and connectivity of core IDeaS microservices (UPS, UIS, Integration Setting HAL, CEDF) using M2M OAuth2 tokens, returning latency and status.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "service_name": {"type": "string", "description": "Target service: 'ALL', 'UPS', 'UIS', 'HAL_SETTINGS', 'CEDF' (default 'ALL')."},
            },
            "required": [],
        },
    },
]

# ==============================================================================
# TOOL IMPLEMENTATIONS (DISPATCH ENGINE)
# ==============================================================================
def dispatch_ups_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Executes the requested UPS / FDS tool and returns structured result."""
    t0 = time.monotonic()

    # 1. ups_get_auth_status
    if tool_name == "ups_get_auth_status":
        telem = AUTH_MGR.get_telemetry()
        return {
            "status": "HEALTHY" if telem["is_valid"] else "DEGRADED",
            "telemetry": telem,
            "fds_base_url": FDS_BASE_URL,
            "cedf_base_url": CEDF_BASE_URL,
            "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
        }

    # 2. ups_refresh_token
    elif tool_name == "ups_refresh_token":
        try:
            token = AUTH_MGR.get_bearer_token(force_refresh=True)
            telem = AUTH_MGR.get_telemetry()
            return {
                "status": "SUCCESS",
                "message": "FDS M2M Bearer token successfully renewed.",
                "token_prefix": token[:20] + "...",
                "ttl_seconds": telem["ttl_seconds"],
                "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
            }
        except Exception as exc:
            return {"status": "ERROR", "error": str(exc), "elapsed_ms": round((time.monotonic() - t0) * 1000, 2)}

    # 3. ups_get_property_by_id
    elif tool_name == "ups_get_property_by_id":
        uid = arguments.get("unified_id", "").strip()
        if not uid:
            return {"status": "ERROR", "error": "unified_id is required"}
        url = f"{FDS_BASE_URL}/api/ups/v2/properties/{uid}"
        res = execute_api_call("GET", url)
        return res

    # 4. ups_search_properties
    elif tool_name == "ups_search_properties":
        limit = min(int(arguments.get("limit", 20)), 100)
        offset = max(int(arguments.get("offset", 0)), 0)
        sort_field = arguments.get("sort_field", "name")
        sort_dir = arguments.get("sort_direction", "ASC").upper()

        headers = {
            "X-Range": f"records={offset}-{offset + limit - 1}",
            "Sort": sort_field,
            "Direction": sort_dir,
        }

        body: Dict[str, Any] = {}
        client_code = arguments.get("client_code")
        property_code = arguments.get("property_code")
        pms_id = arguments.get("pms_property_id")
        parent_chain = arguments.get("parent_chain_code")
        postal_code = arguments.get("postal_code")

        if client_code or property_code or pms_id:
            restriction: Dict[str, str] = {}
            if client_code:
                restriction["clientCode"] = client_code.strip().upper()
            if property_code:
                restriction["propertyCode"] = property_code.strip().upper()
            if pms_id:
                restriction["pmsPropertyId"] = pms_id.strip()
            body["appConfigJsons"] = {"*": [restriction]}

        if parent_chain:
            body["parentChainCode"] = parent_chain.strip().upper()
        if postal_code:
            body["postalCode"] = postal_code.strip()

        url = f"{FDS_BASE_URL}/api/ups/v2/properties/search"
        res = execute_api_call("POST", url, headers=headers, json_body=body)
        if res.get("success") and isinstance(res.get("data"), list):
            res["count"] = len(res["data"])
            res["offset"] = offset
            res["limit"] = limit
        return res

    # 5. ups_get_property_app_config
    elif tool_name == "ups_get_property_app_config":
        uid = arguments.get("unified_id", "").strip()
        app_name = arguments.get("app_name", "").strip().lower()
        if not uid:
            return {"status": "ERROR", "error": "unified_id is required"}
        url = f"{FDS_BASE_URL}/api/ups/v2/properties/{uid}"
        res = execute_api_call("GET", url)
        if not res.get("success"):
            return res
        prop_data = res.get("data") or {}
        app_configs = prop_data.get("appConfigJson") or {}
        if app_name:
            target_config = app_configs.get(app_name)
            return {
                "success": True,
                "unified_id": uid,
                "property_name": prop_data.get("name"),
                "app_name": app_name,
                "config": target_config,
                "found": target_config is not None,
            }
        return {
            "success": True,
            "unified_id": uid,
            "property_name": prop_data.get("name"),
            "app_configs": app_configs,
        }

    # 6. ups_get_property_vendor_mappings
    elif tool_name == "ups_get_property_vendor_mappings":
        uid = arguments.get("unified_id", "").strip()
        if not uid:
            return {"status": "ERROR", "error": "unified_id is required"}
        url = f"{FDS_BASE_URL}/api/ups/v2/properties/{uid}"
        res = execute_api_call("GET", url)
        if not res.get("success"):
            return res
        prop_data = res.get("data") or {}
        mappings = prop_data.get("vendorMappings") or []
        return {
            "success": True,
            "unified_id": uid,
            "property_name": prop_data.get("name"),
            "vendor_mappings_count": len(mappings),
            "vendor_mappings": mappings,
        }

    # 7. ups_get_property_channels
    elif tool_name == "ups_get_property_channels":
        uid = arguments.get("unified_id", "").strip()
        if not uid:
            return {"status": "ERROR", "error": "unified_id is required"}
        url = f"{FDS_BASE_URL}/api/ups/v2/properties/{uid}"
        res = execute_api_call("GET", url)
        if not res.get("success"):
            return res
        prop_data = res.get("data") or {}
        channels = prop_data.get("channels") or []
        return {
            "success": True,
            "unified_id": uid,
            "property_name": prop_data.get("name"),
            "channels_count": len(channels),
            "channels": channels,
        }

    # 8. ups_get_nearby_properties
    elif tool_name == "ups_get_nearby_properties":
        uid = arguments.get("unified_id", "").strip()
        radius_km = float(arguments.get("radius_km", 25.0))
        radius_meters = int(radius_km * 1000)
        max_props = int(arguments.get("max_num_properties", 50))
        include_str = bool(arguments.get("include_str", True))

        if not uid:
            return {"status": "ERROR", "error": "unified_id is required"}

        url = f"{FDS_BASE_URL}/api/ups/v2/properties/{uid}/nearby_properties"
        params = {
            "radiusInMeters": radius_meters,
            "maxNumProperties": max_props,
            "includeSTR": str(include_str).lower(),
        }
        res = execute_api_call("GET", url, params=params)
        if res.get("success") and isinstance(res.get("data"), list):
            res["count"] = len(res["data"])
            res["radius_km"] = radius_km
        return res

    # 9. ups_get_property_custom_attributes
    elif tool_name == "ups_get_property_custom_attributes":
        uid = arguments.get("unified_id", "").strip()
        if not uid:
            return {"status": "ERROR", "error": "unified_id is required"}
        url = f"{FDS_BASE_URL}/api/ups/v2/properties/{uid}"
        res = execute_api_call("GET", url)
        if not res.get("success"):
            return res
        prop_data = res.get("data") or {}
        attrs = prop_data.get("customAttributesJson") or {}
        return {
            "success": True,
            "unified_id": uid,
            "property_name": prop_data.get("name"),
            "custom_attributes": attrs,
            "attributes_count": len(attrs),
        }

    # 10. ups_get_recent_property_audits
    elif tool_name == "ups_get_recent_property_audits":
        url = f"{FDS_BASE_URL}/api/ups/v1/property_audits/in_last_day"
        res = execute_api_call("GET", url)
        if res.get("success") and isinstance(res.get("data"), list):
            res["count"] = len(res["data"])
        return res

    # 11. ups_list_clients
    elif tool_name == "ups_list_clients":
        limit = min(int(arguments.get("limit", 50)), 500)
        offset = max(int(arguments.get("offset", 0)), 0)
        search_filter = arguments.get("search", "").strip().lower()

        url = f"{FDS_BASE_URL}/api/ups/v1/clients"
        res = execute_api_call("GET", url)
        if not res.get("success"):
            return res

        clients = res.get("data") or []
        if search_filter:
            clients = [
                c for c in clients
                if search_filter in str(c.get("clientCode", "")).lower()
                or search_filter in str(c.get("clientName", "")).lower()
            ]

        total_matches = len(clients)
        paginated = clients[offset: offset + limit]
        return {
            "success": True,
            "total_matches": total_matches,
            "limit": limit,
            "offset": offset,
            "count": len(paginated),
            "clients": paginated,
        }

    # 12. ups_get_client_by_code
    elif tool_name == "ups_get_client_by_code":
        code = arguments.get("client_id_or_code", "").strip()
        if not code:
            return {"status": "ERROR", "error": "client_id_or_code is required"}
        url = f"{FDS_BASE_URL}/api/ups/v2/clients/{code}"
        res = execute_api_call("GET", url)
        return res

    # 13. ups_get_client_product_environments
    elif tool_name == "ups_get_client_product_environments":
        cid = arguments.get("client_id", "").strip()
        if not cid:
            return {"status": "ERROR", "error": "client_id is required"}
        url = f"{FDS_BASE_URL}/api/ups/v1/clientProductEnvironments/byClient/{cid}"
        res = execute_api_call("GET", url)
        if res.get("success") and isinstance(res.get("data"), list):
            res["count"] = len(res["data"])
        return res

    # 14. ups_get_client_custom_attributes
    elif tool_name == "ups_get_client_custom_attributes":
        cid = arguments.get("client_id", "").strip()
        if not cid:
            return {"status": "ERROR", "error": "client_id is required"}
        url = f"{FDS_BASE_URL}/api/ups/v1/custom_attributes/{cid}"
        res = execute_api_call("GET", url)
        return res

    # 15. ups_list_optix_clients
    elif tool_name == "ups_list_optix_clients":
        global OPTIX_CLIENTS_CACHE, OPTIX_CLIENTS_EXPIRY
        force_refresh = bool(arguments.get("force_refresh", False))
        now = time.time()

        if not force_refresh and OPTIX_CLIENTS_CACHE and now < OPTIX_CLIENTS_EXPIRY:
            return {
                "success": True,
                "source": "memory_cache",
                "count": len(OPTIX_CLIENTS_CACHE),
                "clients": OPTIX_CLIENTS_CACHE,
            }

        url = f"{FDS_BASE_URL}/api/ups/v1/clients/byProductName/optix"
        res = execute_api_call("GET", url)
        if res.get("success") and isinstance(res.get("data"), list):
            OPTIX_CLIENTS_CACHE = res["data"]
            OPTIX_CLIENTS_EXPIRY = now + 3600
            return {
                "success": True,
                "source": "live_api",
                "count": len(OPTIX_CLIENTS_CACHE),
                "clients": OPTIX_CLIENTS_CACHE,
            }
        return res

    # 16. ups_check_optix_client_access
    elif tool_name == "ups_check_optix_client_access":
        code = arguments.get("client_code", "").strip().upper()
        if not code:
            return {"status": "ERROR", "error": "client_code is required"}

        # Get optix clients list
        optix_res = dispatch_ups_tool("ups_list_optix_clients", {})
        if not optix_res.get("success"):
            return {"passed": False, "reason": f"Unable to fetch Optix clients: {optix_res.get('error')}"}

        clients = optix_res.get("clients") or []
        match = next((c for c in clients if (c.get("clientCode") or "").strip().upper() == code), None)
        if match:
            return {
                "passed": True,
                "client_code": code,
                "client_id": match.get("clientId"),
                "client_name": match.get("clientName"),
                "reason": f"Optix Product access verified for User Role SystemCEO (Client '{code}' is entitled).",
            }
        return {
            "passed": False,
            "client_code": code,
            "reason": f"Optix Product access is NOT present for client '{code}'.",
        }

    # 17. ups_list_products
    elif tool_name == "ups_list_products":
        url = f"{FDS_BASE_URL}/api/ups/v1/products"
        res = execute_api_call("GET", url)
        if res.get("success") and isinstance(res.get("data"), list):
            res["count"] = len(res["data"])
        return res

    # 18. ups_list_product_environments
    elif tool_name == "ups_list_product_environments":
        url = f"{FDS_BASE_URL}/api/ups/v1/productEnvironments"
        res = execute_api_call("GET", url)
        if res.get("success") and isinstance(res.get("data"), list):
            res["count"] = len(res["data"])
        return res

    # 19. ups_resolve_cluster_url
    elif tool_name == "ups_resolve_cluster_url":
        target = arguments.get("product_environment_id", "").strip()
        if not target:
            return {"status": "ERROR", "error": "product_environment_id is required"}

        # If it looks like a UUID, call context url endpoint directly
        if len(target) == 36 and "-" in target:
            url = f"{FDS_BASE_URL}/api/ups/v1/context/url/{target}"
            res = execute_api_call("GET", url)
            return res

        # Otherwise search product environments
        envs_res = execute_api_call("GET", f"{FDS_BASE_URL}/api/ups/v1/productEnvironments")
        if envs_res.get("success") and isinstance(envs_res.get("data"), list):
            match = next((e for e in envs_res["data"] if str(e.get("nameId", "")).upper() == target.upper()), None)
            if match:
                return {
                    "success": True,
                    "product_environment_id": match.get("productEnvironmentId"),
                    "nameId": match.get("nameId"),
                    "displayName": match.get("displayName"),
                    "baseUrl": match.get("url"),
                }
        return {"success": False, "error": f"Product environment '{target}' not found"}

    # 20. cedf_get_clients_configuration
    elif tool_name == "cedf_get_clients_configuration":
        global CEDF_CONFIG_CACHE, CEDF_CONFIG_EXPIRY
        force_refresh = bool(arguments.get("force_refresh", False))
        now = time.time()

        if not force_refresh and CEDF_CONFIG_CACHE and now < CEDF_CONFIG_EXPIRY:
            return {
                "success": True,
                "source": "memory_cache",
                "groups_count": len(CEDF_CONFIG_CACHE),
                "data": CEDF_CONFIG_CACHE,
            }

        url = f"{CEDF_BASE_URL}/api/configuration/v1/clients"
        res = execute_api_call("GET", url)
        if res.get("success") and isinstance(res.get("data"), list):
            CEDF_CONFIG_CACHE = res["data"]
            CEDF_CONFIG_EXPIRY = now + 3600
            return {
                "success": True,
                "source": "live_api",
                "groups_count": len(CEDF_CONFIG_CACHE),
                "data": CEDF_CONFIG_CACHE,
            }
        return res

    # 21. cedf_check_client_upload_status
    elif tool_name == "cedf_check_client_upload_status":
        code = arguments.get("client_code", "").strip().upper()
        source_sys = arguments.get("source_system", "G3").strip().upper()
        product = arguments.get("product", "OPTIX").strip().upper()

        if not code:
            return {"status": "ERROR", "error": "client_code is required"}

        cedf_res = dispatch_ups_tool("cedf_get_clients_configuration", {})
        if not cedf_res.get("success"):
            return {"passed": False, "reason": f"Unable to fetch CEDF config: {cedf_res.get('error')}"}

        groups = cedf_res.get("data") or []
        for group in groups:
            g_source = str(group.get("sourceSystem", "")).upper()
            g_prod = str(group.get("product", "")).upper()
            if g_source == source_sys and g_prod == product:
                for c in group.get("clients", []):
                    if str(c.get("clientCode", "")).upper() == code:
                        upload_enabled = bool(c.get("isClientUploadEnabled"))
                        return {
                            "passed": upload_enabled,
                            "client_code": code,
                            "source_system": source_sys,
                            "product": product,
                            "is_client_upload_enabled": upload_enabled,
                            "created_date": c.get("createDateTime"),
                            "reason": (
                                f"Client '{code}' is registered in CEDF with upload enabled."
                                if upload_enabled
                                else f"Client '{code}' found in CEDF but isClientUploadEnabled is FALSE."
                            ),
                        }

        return {
            "passed": False,
            "client_code": code,
            "source_system": source_sys,
            "product": product,
            "is_client_upload_enabled": False,
            "reason": f"Client '{code}' is NOT configured in CEDF for {source_sys}/{product}.",
        }

    # 22. uis_get_user_by_email
    elif tool_name == "uis_get_user_by_email":
        email = arguments.get("email", "").strip().lower()
        if not email:
            return {"status": "ERROR", "error": "email is required"}
        url = f"{FDS_BASE_URL}/api/uis/identity/v1/users"
        res = execute_api_call("GET", url, params={"email": email})
        return res

    # 23. uis_get_client_sso_config
    elif tool_name == "uis_get_client_sso_config":
        code = arguments.get("client_code", "").strip().upper()
        if not code:
            return {"status": "ERROR", "error": "client_code is required"}
        url = f"{FDS_BASE_URL}/api/uis/identity/v1/sso/config/{code}"
        res = execute_api_call("GET", url)
        return res

    # 24. uis_get_cognito_user_pool
    elif tool_name == "uis_get_cognito_user_pool":
        code = arguments.get("client_code", "").strip().upper()
        if not code:
            return {"status": "ERROR", "error": "client_code is required"}
        url = f"{FDS_BASE_URL}/api/uis/cognitoUserPoolConfig/v1/byClientCode/{code}"
        res = execute_api_call("GET", url)
        return res

    # 25. uis_diagnose_user_access
    elif tool_name == "uis_diagnose_user_access":
        email = arguments.get("email", "").strip().lower()
        property_code = arguments.get("property_code", "").strip()
        client_code = arguments.get("client_code", "").strip().upper()
        required_role = arguments.get("required_role", "REVENUE_MANAGER").strip().upper()

        if not email:
            return {"status": "ERROR", "error": "email is required"}

        # 1. Fetch user identity
        user_res = execute_api_call("GET", f"{FDS_BASE_URL}/api/uis/identity/v1/users", params={"email": email})
        user_info = user_res.get("data") if user_res.get("success") else {}

        # 2. Fetch SSO config if client provided
        sso_info = {}
        if client_code:
            sso_res = execute_api_call("GET", f"{FDS_BASE_URL}/api/uis/identity/v1/sso/config/{client_code}")
            if sso_res.get("success"):
                sso_info = sso_res.get("data") or {}

        pcode_clean = property_code.zfill(4) if property_code else ""
        checks = []
        all_passed = True

        # Check 1: User presence
        found = bool(user_info) and user_res.get("status_code") == 200
        checks.append({
            "check": "User Directory Presence",
            "expected": "User Exists in UIS Identity",
            "actual": f"Found ({email})" if found else "User Not Found",
            "status": "PASS" if found else "FAIL",
        })
        if not found:
            all_passed = False

        # Check 2: Account Status
        status = str(user_info.get("status", "ACTIVE" if found else "NOT_FOUND")).upper()
        status_pass = found and status in ("ACTIVE", "ENABLED")
        checks.append({
            "check": "Account Lifecycle Status",
            "expected": "ACTIVE",
            "actual": status,
            "status": "PASS" if status_pass else "FAIL",
        })
        if not status_pass:
            all_passed = False

        # Check 3: Lockout Status
        is_locked = bool(user_info.get("is_locked", False))
        failed_attempts = user_info.get("failed_login_attempts", 0)
        lock_pass = not is_locked
        checks.append({
            "check": "Account Lockout Status",
            "expected": "UNLOCKED (0 failed logins)",
            "actual": f"LOCKED ({failed_attempts} failed attempts)" if is_locked else f"UNLOCKED ({failed_attempts} failed attempts)",
            "status": "PASS" if lock_pass else "FAIL",
        })
        if not lock_pass:
            all_passed = False

        # Check 4: Property Tenancy
        assigned_props = [str(p).strip().zfill(4) for p in user_info.get("assigned_properties", [])]
        prop_mapped = (pcode_clean in assigned_props) or ("ALL" in assigned_props) or not pcode_clean
        checks.append({
            "check": "Property Tenancy Assignment",
            "expected": f"Mapped to Property {pcode_clean}" if pcode_clean else "Global Chain Scope",
            "actual": f"Assigned ({', '.join(assigned_props) if assigned_props else 'None'})",
            "status": "PASS" if prop_mapped else "FAIL",
        })
        if not prop_mapped:
            all_passed = False

        # Check 5: Required Role
        user_roles = [str(r).strip().upper() for r in user_info.get("roles", [])]
        role_has = (required_role in user_roles) or ("RMS_ADMIN" in user_roles)
        checks.append({
            "check": f"Role Entitlement ({required_role})",
            "expected": required_role,
            "actual": ", ".join(user_roles) if user_roles else "No Roles Assigned",
            "status": "PASS" if role_has else "FAIL",
        })
        if not role_has:
            all_passed = False

        # Check 6: SSO Certificate
        if sso_info and sso_info.get("sso_enabled"):
            cert_status = sso_info.get("cert_status", "VALID")
            cert_days = sso_info.get("cert_expiry_days", 180)
            sso_pass = cert_status == "VALID" and cert_days > 15
            checks.append({
                "check": "SAML 2.0 / SSO Certificate",
                "expected": "Valid > 15 days",
                "actual": f"{sso_info.get('idp_type', 'SAML')} cert expires in {cert_days} days",
                "status": "PASS" if sso_pass else "FAIL",
            })
            if not sso_pass:
                all_passed = False
        else:
            checks.append({
                "check": "SAML 2.0 / SSO Certificate",
                "expected": "SAML SSO or Standard Org Auth",
                "actual": "Standard Org Authentication (SSO Not Enforced / Inactive)",
                "status": "PASS",
            })

        # Remediation list
        remediations = []
        if not found:
            remediations.append(f"Provision user '{email}' under client '{client_code}' in the UIS Identity console.")
        if not status_pass and found:
            remediations.append(f"Re-activate user account (current status: {status}).")
        if is_locked:
            remediations.append(f"Unlock user '{email}' and issue password reset.")
        if not prop_mapped and pcode_clean:
            remediations.append(f"Add property '{pcode_clean}' to user's assigned properties list.")
        if not role_has:
            remediations.append(f"Assign required role '{required_role}' to user profile.")

        return {
            "passed": all_passed,
            "email": email,
            "property_code": pcode_clean,
            "client_code": client_code,
            "required_role": required_role,
            "user_profile": user_info,
            "sso_config": sso_info,
            "checks": checks,
            "remediations": remediations,
            "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
        }

    # 26. ups_list_announcements
    elif tool_name == "ups_list_announcements":
        url = f"{FDS_BASE_URL}/api/ups/v1/announcements"
        res = execute_api_call("GET", url)
        if res.get("success") and isinstance(res.get("data"), list):
            res["count"] = len(res["data"])
        return res

    # 27. ups_resolve_property_to_cluster
    elif tool_name == "ups_resolve_property_to_cluster":
        client_code = arguments.get("client_code", "").strip().upper()
        prop_code = arguments.get("property_code", "").strip().upper()

        if not (client_code and prop_code):
            return {"status": "ERROR", "error": "Both client_code and property_code are required"}

        # Search UPS for property by appConfig
        search_res = dispatch_ups_tool("ups_search_properties", {
            "client_code": client_code,
            "property_code": prop_code,
            "limit": 5,
        })

        if not search_res.get("success") or not search_res.get("data"):
            return {
                "resolved": False,
                "client_code": client_code,
                "property_code": prop_code,
                "reason": "Property not found in UPS property registry.",
            }

        match = search_res["data"][0]
        app_configs = match.get("appConfigJson") or {}
        g3_cfg = app_configs.get("g3") or {}
        crms_cfg = app_configs.get("centralrms") or {}

        return {
            "resolved": True,
            "client_code": client_code,
            "property_code": prop_code,
            "unified_id": match.get("unifiedId"),
            "property_name": match.get("name"),
            "parent_chain": match.get("parentChainName"),
            "salesforce_account_id": match.get("salesforceAccountId"),
            "g3": {
                "tenant_db_host": g3_cfg.get("tenantDBHost"),
                "tenant_db_name": g3_cfg.get("tenantDBName"),
                "host_url": g3_cfg.get("hostUrl"),
                "pms_property_id": g3_cfg.get("pmsPropertyId"),
            },
            "centralrms": {
                "host_url": crms_cfg.get("hostUrl"),
            },
            "hotel_capacity": match.get("hotelCapacity"),
            "timezone": match.get("timezone"),
            "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
        }

    # 28. ups_get_system_health
    elif tool_name == "ups_get_system_health":
        health_report: Dict[str, Any] = {"status": "HEALTHY", "endpoints": {}}

        # Test UPS Products
        t_ups = time.monotonic()
        r_ups = execute_api_call("GET", f"{FDS_BASE_URL}/api/ups/v1/products", timeout=8)
        health_report["endpoints"]["ups_products"] = {
            "status": "UP" if r_ups.get("success") else "DOWN",
            "latency_ms": round((time.monotonic() - t_ups) * 1000, 2),
        }

        # Test CEDF
        t_cedf = time.monotonic()
        r_cedf = execute_api_call("GET", f"{CEDF_BASE_URL}/api/configuration/v1/clients", timeout=8)
        health_report["endpoints"]["cedf_config"] = {
            "status": "UP" if r_cedf.get("success") else "DOWN",
            "latency_ms": round((time.monotonic() - t_cedf) * 1000, 2),
        }

        # Token telemetry
        health_report["token_telemetry"] = AUTH_MGR.get_telemetry()
        health_report["elapsed_ms"] = round((time.monotonic() - t0) * 1000, 2)
        return health_report

    # 29. ups_get_api_catalog
    elif tool_name == "ups_get_api_catalog":
        return {
            "services": [
                {
                    "name": "Unified Property Service (UPS)",
                    "base_url": f"{FDS_BASE_URL}/api/ups",
                    "swagger_ui": f"{FDS_BASE_URL}/api/ups/swagger-ui/index.html",
                    "openapi_v3": f"{FDS_BASE_URL}/api/ups/v3/api-docs",
                    "core_entities": ["Properties", "Clients", "Products", "Environments", "Audits"],
                },
                {
                    "name": "User Identity Service (UIS)",
                    "base_url": f"{FDS_BASE_URL}/api/uis",
                    "swagger_ui": f"{FDS_BASE_URL}/api/uis/swagger-ui/index.html",
                    "openapi_v3": f"{FDS_BASE_URL}/api/uis/v3/api-docs",
                    "core_entities": ["Users", "Roles", "SSO Config", "Cognito User Pools"],
                },
                {
                    "name": "Cloud Enterprise Datafeed (CEDF)",
                    "base_url": f"{CEDF_BASE_URL}/api/configuration/v1",
                    "core_entities": ["Client Upload Configurations", "Feed Group Mappings"],
                },
            ],
            "total_canonical_tools": len(UPS_TOOLS),
            "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
        }

    # 30. ups_validate_m2m_credentials
    elif tool_name == "ups_validate_m2m_credentials":
        try:
            token = AUTH_MGR.get_bearer_token(force_refresh=True)
            test_res = execute_api_call("GET", f"{FDS_BASE_URL}/api/ups/v1/products", timeout=8)
            return {
                "valid": test_res.get("success", False),
                "message": "FDS M2M Credentials successfully issued valid Bearer token and queried products API.",
                "token_prefix": token[:25] + "...",
                "status_code": test_res.get("status_code"),
                "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
            }
        except Exception as exc:
            return {
                "valid": False,
                "message": f"FDS M2M credential validation failed: {exc}",
                "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
            }

    # 31. fds_get_integration_property_configs
    elif tool_name == "fds_get_integration_property_configs":
        page = int(arguments.get("page", 0))
        size = int(arguments.get("size", 20))
        pcode = arguments.get("property_code", "").strip().upper()
        ccode = arguments.get("client_code", "").strip().upper()
        vid = arguments.get("vendor_id", "").strip()

        params = {"page": page, "size": size}
        res = execute_api_call("GET", f"{HAL_BASE_URL}/integrationPropertyConfigs", params=params)
        if not res.get("success"):
            return res

        data = res.get("data", {})
        embedded = data.get("_embedded", {}) if isinstance(data, dict) else {}
        configs = embedded.get("integrationPropertyConfigs", [])

        # Client-side filtering if parameters are provided
        filtered = []
        for c in configs:
            if pcode and c.get("propertyCode", "").upper() != pcode:
                continue
            if ccode and c.get("clientCode", "").upper() != ccode:
                continue
            if vid and vid.lower() not in c.get("vendorId", "").lower():
                continue
            filtered.append(c)

        return {
            "success": True,
            "total_sampled": len(configs),
            "matched_count": len(filtered),
            "configs": filtered if (pcode or ccode or vid) else configs,
            "page_metadata": data.get("page", {}),
            "elapsed_ms": res.get("elapsed_ms"),
        }

    # 32. fds_get_vendor_configs
    elif tool_name == "fds_get_vendor_configs":
        vid = arguments.get("vendor_id", "").strip()
        itype = arguments.get("integration_type", "").strip()
        page = int(arguments.get("page", 0))
        size = int(arguments.get("size", 20))

        if vid:
            url = f"{HAL_BASE_URL}/vendorConfigs/search/findByVendorId"
            res = execute_api_call("GET", url, params={"vendorId": vid})
        elif itype:
            url = f"{HAL_BASE_URL}/vendorConfigs/search/findByIntegrationType"
            res = execute_api_call("GET", url, params={"integrationType": itype, "page": page, "size": size})
        else:
            url = f"{HAL_BASE_URL}/vendorConfigs"
            res = execute_api_call("GET", url, params={"page": page, "size": size})
        return res

    # 33. fds_get_integration_setting_changelogs
    elif tool_name == "fds_get_integration_setting_changelogs":
        page = int(arguments.get("page", 0))
        size = int(arguments.get("size", 20))
        return execute_api_call("GET", f"{HAL_BASE_URL}/integrationSettingChangelogs", params={"page": page, "size": size})

    # 34. fds_get_mongo_operation_audits
    elif tool_name == "fds_get_mongo_operation_audits":
        page = int(arguments.get("page", 0))
        size = int(arguments.get("size", 20))
        return execute_api_call("GET", f"{HAL_BASE_URL}/mongoOperationAudits", params={"page": page, "size": size})

    # 35. fds_get_nucleus_integration_settings
    elif tool_name == "fds_get_nucleus_integration_settings":
        page = int(arguments.get("page", 0))
        size = int(arguments.get("size", 20))
        return execute_api_call("GET", f"{HAL_BASE_URL}/baseIntegrationConfigs", params={"page": page, "size": size})

    # 36. fds_probe_microservice_health
    elif tool_name == "fds_probe_microservice_health":
        target = arguments.get("service_name", "ALL").strip().upper()
        results: Dict[str, Any] = {}

        probes = {
            "UPS": f"{FDS_BASE_URL}/api/ups/v1/products",
            "UIS": f"{FDS_BASE_URL}/api/uis/v1/users?size=1",
            "HAL_SETTINGS": f"{HAL_BASE_URL}/",
            "CEDF": f"{CEDF_BASE_URL}/api/configuration/v1/clients",
        }

        for s_name, s_url in probes.items():
            if target not in ("ALL", s_name):
                continue
            t_probe = time.monotonic()
            r_probe = execute_api_call("GET", s_url, timeout=8)
            results[s_name] = {
                "status": "UP" if r_probe.get("success") else "DOWN",
                "status_code": r_probe.get("status_code"),
                "latency_ms": round((time.monotonic() - t_probe) * 1000, 2),
                "url": s_url,
            }

        return {
            "success": True,
            "overall_status": "UP" if all(v.get("status") == "UP" for v in results.values()) else "DEGRADED",
            "probed_services": results,
            "elapsed_ms": round((time.monotonic() - t0) * 1000, 2),
        }

    else:
        return {"status": "ERROR", "error": f"Tool '{tool_name}' not implemented"}


# ==============================================================================
# CANONICAL RESOURCES
# ==============================================================================
UPS_RESOURCES = [
    {
        "uri": "ups://system/status",
        "name": "UPS & FDS Operational Status",
        "description": "Live status of FDS M2M tokens, CEDF datafeed connectivity, and API health.",
        "mimeType": "application/json",
    },
    {
        "uri": "ups://products/catalog",
        "name": "SAS IDeaS Products & Active Environments",
        "description": "Master list of all IDeaS cloud products and 42+ active environments.",
        "mimeType": "application/json",
    },
    {
        "uri": "ups://announcements/active",
        "name": "Active Platform Announcements",
        "description": "Active operational and maintenance announcements defined in UPS.",
        "mimeType": "application/json",
    },
]

def read_ups_resource(uri: str) -> str:
    """Reads content for a specific ups:// resource URI."""
    if uri == "ups://system/status":
        status_data = dispatch_ups_tool("ups_get_system_health", {})
        return json.dumps(status_data, indent=2)
    elif uri == "ups://products/catalog":
        prod_data = dispatch_ups_tool("ups_list_products", {})
        envs_data = dispatch_ups_tool("ups_list_product_environments", {})
        return json.dumps({"products": prod_data, "environments": envs_data}, indent=2)
    elif uri == "ups://announcements/active":
        ann_data = dispatch_ups_tool("ups_list_announcements", {})
        return json.dumps(ann_data, indent=2)
    else:
        raise ValueError(f"Unknown resource URI: {uri}")


# ==============================================================================
# JSON-RPC 2.0 PROTOCOL HANDLER
# ==============================================================================
def handle_json_rpc(request: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Handles an incoming MCP JSON-RPC 2.0 request."""
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if not method:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid Request: method is required"}}

    # Notifications do not require responses
    if req_id is None and method.startswith("notifications/"):
        return None

    # MCP initialize
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {"listChanged": False},
                    "resources": {"subscribe": False, "listChanged": False},
                },
                "serverInfo": {
                    "name": "ups-mcp-server",
                    "version": "1.0.0",
                    "description": "IDeaS UPS, FDS, UIS & CEDF Enterprise MCP Server",
                },
            },
        }

    # Ping
    elif method == "ping":
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}

    # tools/list
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": UPS_TOOLS}}

    # tools/call
    elif method == "tools/call":
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        if not tool_name:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32602, "message": "Missing required parameter 'name'"},
            }

        try:
            tool_res = dispatch_ups_tool(tool_name, arguments)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(tool_res, indent=2),
                        }
                    ],
                    "isError": not tool_res.get("success", True) if isinstance(tool_res, dict) else False,
                },
            }
        except Exception as exc:
            logger.error("Error executing tool '%s': %s", tool_name, exc, exc_info=True)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps({"error": str(exc)})}],
                    "isError": True,
                },
            }

    # resources/list
    elif method == "resources/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"resources": UPS_RESOURCES}}

    # resources/read
    elif method == "resources/read":
        uri = params.get("uri")
        if not uri:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32602, "message": "Missing parameter 'uri'"},
            }
        try:
            content = read_ups_resource(uri)
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
                    ]
                },
            }
        except Exception as exc:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32000, "message": str(exc)},
            }

    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": -32601, "message": f"Method '{method}' not found"},
        }


# ==============================================================================
# FASTAPI SSE & HTTP SERVER
# ==============================================================================
def create_fastapi_app():
    import asyncio
    from fastapi import FastAPI, Request, Response
    from fastapi.responses import JSONResponse, StreamingResponse
    from fastapi.middleware.cors import CORSMiddleware

    app = FastAPI(
        title="IDeaS UPS & FDS MCP Server",
        description="Model Context Protocol server for UPS properties, UIS identity, and CEDF datafeed",
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _active_sessions: Dict[str, asyncio.Queue] = {}

    @app.get("/health")
    async def health_check():
        """Fast health check probe for Docker / Kubernetes."""
        telem = AUTH_MGR.get_telemetry()
        return {
            "status": "HEALTHY" if telem["is_valid"] else "DEGRADED",
            "server": "ups-mcp-server",
            "version": "1.0.0",
            "tools_count": len(UPS_TOOLS),
            "resources_count": len(UPS_RESOURCES),
            "m2m_token_valid": telem["is_valid"],
            "m2m_ttl_seconds": telem["ttl_seconds"],
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    @app.get("/sse")
    async def sse_endpoint(request: Request):
        """MCP Server-Sent Events handshake endpoint."""
        session_id = f"ups_sess_{int(time.time()*1000)}_{os.urandom(4).hex()}"
        queue: asyncio.Queue = asyncio.Queue()
        _active_sessions[session_id] = queue

        async def event_generator():
            try:
                endpoint_url = f"/messages?sessionId={session_id}"
                yield f"event: endpoint\ndata: {endpoint_url}\n\n"
                logger.info("SSE client connected: session=%s", session_id)

                while True:
                    if await request.is_disconnected():
                        logger.info("SSE client disconnected: session=%s", session_id)
                        break

                    try:
                        message = await asyncio.wait_for(queue.get(), timeout=15.0)
                        yield f"event: message\ndata: {json.dumps(message)}\n\n"
                    except asyncio.TimeoutError:
                        yield ": keepalive\n\n"
            finally:
                _active_sessions.pop(session_id, None)

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
    async def messages_endpoint(request: Request):
        """Receives JSON-RPC messages and routes responses through SSE queue."""
        session_id = request.query_params.get("sessionId")
        if not session_id or session_id not in _active_sessions:
            return JSONResponse(status_code=400, content={"error": "Invalid or expired sessionId"})

        try:
            payload = await request.json()
        except Exception as exc:
            return JSONResponse(status_code=400, content={"error": f"Invalid JSON payload: {exc}"})

        response = handle_json_rpc(payload)
        if response:
            await _active_sessions[session_id].put(response)

        return Response(status_code=202)

    return app


# ==============================================================================
# STDIO TRANSPORT (FOR DIRECT CLI / CLAUDE DESKTOP INTEGRATION)
# ==============================================================================
def run_stdio_transport():
    """Runs the MCP server over standard input/output (Stdio)."""
    logger.info("Starting UPS MCP Server in STDIO mode...")
    sys.stderr.write("IDeaS UPS & FDS MCP Server (Stdio Transport) Ready.\n")
    sys.stderr.flush()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_json_rpc(req)
            if resp is not None:
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
        except json.JSONDecodeError as exc:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": f"Parse error: {exc}"},
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()
        except Exception as exc:
            logger.error("Stdio handler unexpected error: %s", exc)


# ==============================================================================
# MAIN ENTRYPOINT
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(description="IDeaS UPS & FDS MCP Server")
    parser.add_argument("--stdio", action="store_true", help="Run with Stdio transport instead of SSE")
    parser.add_argument("--host", default=MCP_HOST, help=f"Host to bind (default: {MCP_HOST})")
    parser.add_argument("--port", type=int, default=MCP_PORT, help=f"Port to bind (default: {MCP_PORT})")
    args = parser.parse_args()

    if args.stdio:
        run_stdio_transport()
    else:
        import uvicorn
        logger.info("Starting UPS & FDS MCP Server on http://%s:%d (SSE Transport)", args.host, args.port)
        logger.info("Registered %d Canonical Tools and %d Resources", len(UPS_TOOLS), len(UPS_RESOURCES))
        app = create_fastapi_app()
        uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
