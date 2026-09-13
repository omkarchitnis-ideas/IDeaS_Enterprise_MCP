# SAS IDeaS Enterprise Acronyms, Error Codes & Architectural Glossary

## 1. Core Enterprise Acronyms
- **RMS**: Revenue Management System (G3 RMS).
- **BAR**: Best Available Rate. The primary non-restricted pricing tier published to PMS/CRS.
- **LRV**: Last Room Value. The minimum expected revenue threshold below which G3 will refuse to sell a room.
- **BDE**: Business Data Exchange. The core batch ETL process that moves reservation transactions into analytical tables.
- **CDP**: Continuous Daily Pricing. Real-time pricing model calculating unconstrained demand curves.
- **SDB**: Synthetic Database. Historical reservation models used to seed newly onboarded properties lacking 2+ years of PMS history.
- **PMS**: Property Management System (e.g., Opera / OPMS, OnQ, FOLS, Fidelio, Galaxy).
- **HTNG**: Hospitality Technology Next Generation. The standard XML/REST messaging protocol for 2-way PMS rate uploads.
- **CMA**: Configuration & Management Application. The edge gateway orchestrating 19,496 Spring Batch workflow chains.
- **CEDF**: Corporate Enterprise Data Feed. Centralized data export pipeline delivering pricing and pace extracts.
- **FDS**: Forecast & Decision Service. Microservice layer delivering real-time pricing recommendations via OAuth2 M2M.
- **UPS**: User & Permission Service. IAM service managing authentication, role assignments, and client entitlements.

---

## 2. Common Error Codes & Triage Attribution

| Error Pattern | Root Cause Category | Diagnostic Action |
| :--- | :--- | :--- |
| `ERR_PMS_TIMEOUT` | **Network / Partner Endpoint** | PMS listener failed to acknowledge rate upload within 30s. Check firewall and partner connection status. |
| `ERR_LOCK_FAILED` | **Batch Concurrency Lock** | A previous step in `JOB_STATE` held a lock on `Accom_Activity`. Check `Blocked_Job` table. |
| `ERR_LRV_VIOLATION` | **Pricing Science Boundary** | Recommended price falls below the calculated LRV floor. Optimizer suppressed publication to prevent revenue loss. |
| `ERR_PRICE_RANK_VIOLATION`| **Configuration Conflict** | A Competitive Market Position Constraint caused higher room class to price lower than base room class. |
| `ERR_RATE_SHOP_EMPTY` | **External Rate Shop Stale** | Competitor rate shopping provider returned 0 open rates or only closed rates for the shop date. |
| `ERR_INVALID_OAUTH_TOKEN`| **M2M Authentication** | Bearer token expired or invalid client secret in FDS UIS. Force token refresh via `ups_force_token_refresh`. |

---

## 3. Top Troubleshooting Heuristics for Engineers
1. **Never Assume System Defect on Pricing Inquiries**: 90% of pricing decision cases in Salesforce are How-To or constraint expectation gaps (like Case #03379138). Check `Competitive_Constraint` and `LRV` before escalating.
2. **Always Check Rate Adjustments & Ignore Periods**: If a competitor rate looks wrong, check if a tax-inclusive adjustment or an active `Competitor_Ignore` window is distorting comparisons.
3. **Verify Data Delivery Heartbeats**: If rates haven't uploaded, inspect `cma_get_property_sync_status` and Datadog logs for the delivery worker.
