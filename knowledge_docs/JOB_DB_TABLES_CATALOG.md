# IDeaS G3 · Job Database Complete Table & Detailed Usage Guide
## 25 Tables in JOB Database with Functional Business Usage & System Roles

The Job database coordinates and audits all background scheduled batch jobs, BDE daily optimization runs, SDB synthetic history builds, datafeed ingestions, and failure problem diagnosis.

---

| Table Name | System Usage | Business Purpose & Operational Role | Key Columns |
| :--- | :--- | :--- | :--- |
| Blocked_Job | **Job Concurrency Lock** | Prevents duplicate concurrent runs of the same job on the same property; manages cooldown start/end timestamps. | Blocked_Job_Id, Job_Name, valid_until, cooldown_start_timestamp... |
| DAILY_JOB_STATISTICS | **Job Performance Metrics** | Aggregates daily performance statistics: total duration, execution counts, success rates, and average latency per job type. | DAILY_JOB_STATISTICS_ID, JOB_NAME, JOB_DATE, JOB_COUNT... |
| DAILY_STEP_STATISTICS | **Step Performance Metrics** | Aggregates daily sub-step runtimes to identify pipeline bottlenecks across BDE and CDP batch cycles. | DAILY_STEP_STATISTICS_ID, DAILY_JOB_STATISTICS_ID, STEP_NAME, STEP_COUNT... |
| DataDog_Proc_Audit | **Datadog Telemetry** | Logs stored procedure executions and telemetry sync checkpoints sent to Datadog for APM monitoring. | Stored_Procedure, Last_Executed_At |
| JOB_EXECUTION | **Job Lifecycle & State Log** | Tracks the live execution lifecycle: START_TIME, END_TIME, STATUS (COMPLETED, FAILED, RUNNING), EXIT_CODE, and EXIT_MESSAGE for each run. | JOB_EXECUTION_ID, VERSION, JOB_INSTANCE_ID, CREATE_TIME... |
| JOB_EXECUTION_CONTEXT | **Serialized Pipeline Context** | Holds the runtime memory context and checkpoint states so long-running SAS/SQL batch jobs can resume after interruptions. | JOB_EXECUTION_ID, SHORT_CONTEXT, SERIALIZED_CONTEXT |
| JOB_EXECUTION_PARAMS | **Runtime Parameters** | Stores key-value input parameters passed to a job execution (e.g. Property_ID, Client_ID, Forecast_Date, Force_Rebuild_Flag). | JOB_EXECUTION_ID, TYPE_CD, KEY_NAME, STRING_VAL... |
| JOB_EXECUTION_SEQ | **Sequence Generator** | Database sequence generator for unique Job Execution IDs. | ID |
| JOB_INSTANCE | **Job Instance Definition** | Stores the master record for every scheduled or ad-hoc job execution instance (e.g. RevertSDBToStandardJob, NightlyBDE, SDBBuild). Links to job keys and unique run instances. | JOB_INSTANCE_ID, VERSION, JOB_NAME, JOB_KEY |
| JOB_INSTANCE_WORK_CONTEXT | **Property & Client Context** | Maps which specific Property_ID, Property_Code, Client_ID, and Client_Code a batch job instance was launched for. | JOB_INSTANCE_ID, CLIENT_ID, CLIENT_CODE, PROPERTY_ID... |
| JOB_NOTE | **Audit & Operator Notes** | Stores automated system notes or support engineer annotations regarding job executions and manual restarts. | JOB_NOTE_ID, JOB_INSTANCE_ID, CREATION_DATE, TEXT... |
| JOB_SEQ | **Sequence Generator** | Database sequence generator for unique Job Instance IDs. | ID |
| JOB_STATE | **Current Live Status** | Maintains the real-time execution state of all running background jobs, worker threads, and active pipeline triggers across the server cluster. | JOB_INSTANCE_ID, JOB_EXECUTION_ID, JOB_NAME, START_TIME... |
| PROBLEM | **Failure Diagnostics** | Captures detailed diagnostic error dumps, exception stack traces, and severity scores whenever a job step fails. | PROBLEM_ID, STEP_EXECUTION_ID, CREATION_DATE, DESCRIPTION... |
| PROBLEM_CLASSIFICATION | **Error Categorization** | Maps error codes (e.g. ERR_PMS_TIMEOUT, ERR_LOCK_FAILED, ERR_INVALID_SCHEMA) to root cause categories. | PROBLEM_CLASSIFICATION_ID, ERROR_CODE, ERROR_TYPE |
| PROBLEM_NOTE | **Troubleshooting Log** | Stores automated diagnostic triage findings and remediation notes recorded during job failure analysis. | PROBLEM_NOTE_ID, PROBLEM_ID, CREATION_DATE, TEXT... |
| Purge_Status | **Data Retention Tracking** | Tracks background data purge and cleanup jobs for old historical job logs. | Status_Time, Status_Message |
| SAS_STEP_EXECUTION | **SAS Analytics Step Tracking** | Tracks high-performance SAS analytics kernel execution times, memory usage, and mathematical solver completion timestamps. | STEP_EXECUTION_ID, START_TIME, END_TIME |
| SERIALIZABLE_JOB_EXECUTION_PARAM | **Serialized Parameters** | Stores complex or binary-serialized parameter sets passed to specialized analytical jobs. | SERIALIZABLE_JOB_EXECUTION_PARAM_ID, JOB_EXECUTION_ID, SERIALIZED_CONTEXT |
| STEP_EXECUTION | **Step-Level Execution Log** | Logs individual pipeline sub-steps (e.g. ExtractPMSData, RunOptimization, GenerateDecisions, UploadRates), step duration, and commit counts. | STEP_EXECUTION_ID, VERSION, STEP_NAME, JOB_EXECUTION_ID... |
| STEP_EXECUTION_CONTEXT | **Sub-Step State Data** | Stores serialized step execution variables and intermediate data metrics. | STEP_EXECUTION_ID, SHORT_CONTEXT, SERIALIZED_CONTEXT |
| STEP_EXECUTION_SEQ | **Sequence Generator** | Database sequence generator for unique Step Execution IDs. | ID |
| SUPPORT_BULLETIN | **Support Notification** | Broadcasts automated alert bulletins to support engineers when critical jobs fail for high-tier enterprise clients. | SUPPORT_BULLETIN_ID, BULLETIN_TEXT, PROPERTY_ID, ERROR_CODE... |
| dbmaintain_scripts | **Database Migration History** | Tracks executed DB maintain scripts, checksums, and execution timestamps. | file_name, file_last_modified_at, checksum, executed_at... |
| flyway_schema_history | **Schema Version Control** | Maintains Flyway database version control migration records, script names, and installed ranks. | installed_rank, version, description, type... |