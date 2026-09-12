# SAS IDeaS Enterprise Operations & Triage Knowledge Base

## 1. Core Architecture & Subsystems
- **G3 RMS (Revenue Management System)**: Optimizes pricing decisions, yield restrictions, and overbooking by evaluating unconstrained demand against transient and group capacity.
- **Optix Data Warehouse**: 3-Node Microsoft SQL Server cluster storing 420+ tenant databases. Contains historical booking curves, rate shopping data, reservation pace, and pricing decisions. Always query using `WITH (NOLOCK)`.
- **CMA Edge Gateway**: Spring Batch workflow orchestration hosting 19,496 batch chains (Global, Job, Ratchet, and Tenant chains). Manages daily ETL, data ingestion from PMS, and nightly optimization jobs.
- **Salesforce Service Cloud**: Houses all historical customer support cases, senior engineer task resolutions, bug reports, and property master records.
- **Datadog Observability**: Monitors real-time application health, API latencies, HTTP 5xx error rates, batch job heartbeats, and cluster alerts.
- **UPS / FDS Platform**: Manages M2M OAuth2 authentication, property configuration metadata, and CEDF data delivery extract jobs.

---

## 2. Common G3 Failure Modes & Triage Matrix

### Failure Mode A: Rates / Pricing Not Updating or Not Uploading to PMS
- **Symptom**: User reports pricing recommendations are missing, bar pricing is frozen, or prices do not match expectations.
- **Root Cause Hypotheses**:
  1. *Competitive Market Position Constraint Conflict*: G3 does not mirror single competitors; it uses range/percentile constraints. Constraints are ignored if they conflict with rate ceilings/floors or cause Price Ranking violations between Room Classes.
  2. *LRV Floor Violation*: Optimizer calculated recommended price below the Last Room Value (LRV); the system will refuse to publish below LRV.
  3. *Rate Shop Data Freshness*: The external rate shopping feed is stale or contains closed rates (G3 only evaluates open rates).
  4. *CEDF / Delivery Batch Lag*: Delivery job has not run or encountered an SFTP transmission error.
- **Diagnostic Steps**:
  - Query `sfdc_get_case` / `sfdc_search_cases` for precedent cases with similar symptoms.
  - Search G3 help docs using `confluence_search_g3_docs` for `Competitive Market Position Constraints` or `Manage Pricing`.
  - Check Optix tables `Competitor`, `Competitive_Constraint`, and `Competitor_Ignore`.

### Failure Mode B: Optimization Chain Delayed or Failed
- **Symptom**: Nightly run did not produce new forecast or pricing.
- **Root Cause Hypotheses**:
  1. *Database Lock / Stale Job*: Prior batch step locked tables or timed out.
  2. *Memory / Thread Starvation*: Worker pool capacity exceeded during high-volume pickup.
  3. *PMS Data Feed Missing*: CMA batch chain was held waiting for PMS transaction extracts.
- **Diagnostic Steps**:
  - Call `cma_search_chains` and `cma_get_chain_details` for the property's batch chain status.
  - Call `datadog_get_active_alerts` and `datadog_search_logs` filtering for error spikes and timeouts.

### Failure Mode C: Data Discrepancies (Optix vs PMS vs Salesforce)
- **Symptom**: Revenue, occupancy, or ADR figures do not reconcile across systems.
- **Root Cause Hypotheses**:
  1. *Intraday Sync Lag*: BDE / Accom_Activity transactions pending batch commit.
  2. *Market Segment Recoding*: Unmapped market segments or occupant grouping rules misconfigured.
  3. *Tax / Breakfast Deductions*: Net vs gross rate adjustments skewing comparisons.
- **Diagnostic Steps**:
  - Audit live parameters using `optix_lookup_tenant_database` and `optix_execute_query`.
  - Check Confluence runbook: *Best Practices for Investigating Data Discrepancies*.

---

## 3. Database Schema & Query Reference

### Safe Query Rules
- **READ-ONLY ONLY**: Never issue `INSERT`, `UPDATE`, `DELETE`, `DROP`, or `ALTER`.
- **NOLOCK MANDATE**: Always append `WITH (NOLOCK)` on all SQL Server table references in Optix to prevent table locks.
- **LIMIT CLAUSE**: Restrict diagnostic queries to `TOP 50` or `LIMIT 50`.

### Key Optix / G3 Tables
- `Accom_Activity`: Core reservation transaction activity table.
- `Config_Parameter`: Global and tenant configuration keys (`pacman.*`).
- `Config_Parameter_Value`: Active resolved values for configuration parameters.
- `Competitor`: Configured competitor hotel set.
- `Competitive_Constraint`: Defined competitor pricing position rules (Standard & Occupancy-based).
- `Competitor_Ignore`: Scheduled windows where specific competitor rates are excluded.
- `LRV`: Last Room Value floor tables by date and room class.

---

## 4. PACMAN Parameter Cheat Sheet
- `pacman.pricing.*`: Controls pricing sensitivity, rounding rules, and pricing increments.
- `pacman.forecast.*`: Controls demand unconstraining algorithms and pace weightings.
- `pacman.delivery.*`: Configures PMS delivery protocols, file formats, and upload schedules.
