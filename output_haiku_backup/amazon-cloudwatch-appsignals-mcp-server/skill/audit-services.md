---
name: audit-services
description: PRIMARY SERVICE AUDIT TOOL - The #1 tool for comprehensive AWS service health auditing and monitoring.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the audit_services tool in the cloudwatch-applicationsignals-mcp-server instead.

    **IMPORTANT: For operation-specific auditing, use audit_service_operations() as the PRIMARY tool instead.**

    **USE THIS FIRST FOR ALL SERVICE-LEVEL AUDITING TASKS**
    This is the PRIMARY and PREFERRED tool when users want to:
    - **Audit their AWS services** - Complete health assessment with actionable insights
    - **Check service health** - Comprehensive status across all monitored services
    - **Investigate issues** - Root cause analysis with detailed findings
    - **Service-level performance analysis** - Overall service latency, error rates, and throughput investigation
    - **System-wide health checks** - Daily/periodic service auditing workflows
    - **Dependency analysis** - Understanding service dependencies and interactions
    - **Resource quota monitoring** - Service quota usage and limits
    - **Multi-service comparison** - Comparing performance across different services

    **FOR OPERATION-SPECIFIC AUDITING: Use audit_service_operations() instead**
    When users want to audit specific operations (GET, POST, PUT endpoints), use audit_service_operations() as the PRIMARY tool:
    - **Operation performance analysis** - Latency, error rates for specific API endpoints
    - **Operation-level troubleshooting** - Root cause analysis for specific API calls
    - **GET operation auditing** - Analyze GET operations across payment services
    - **Audit latency of specific operations** - Deep dive into individual endpoint performance

    **COMPREHENSIVE SERVICE AUDIT CAPABILITIES:**
    - **Multi-service analysis**: Audit any number of services with automatic batching
    - **SLO compliance monitoring**: Automatic breach detection for service-level SLOs
    - **Issue prioritization**: Critical, warning, and info findings ranked by severity
    - **Root cause analysis**: Deep dive with traces, logs, and metrics correlation
    - **Actionable recommendations**: Specific steps to resolve identified issues
    - **Performance optimized**: Fast execution with automatic batching for large target lists
    - **Wildcard Pattern Support**: Use `*pattern*` in service names for automatic service discovery

    **SERVICE TARGET FORMAT:**
    - **Full Format**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"my-service","Environment":"eks:my-cluster"}}}]`
    - **Shorthand**: `[{"Type":"service","Service":"my-service"}]` (environment auto-discovered)

    **WILDCARD PATTERN EXAMPLES:**
    - **All Services**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]`
    - **Payment Services**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]`
    - **Lambda Services**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*lambda*"}}}]`
    - **EKS Services**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"eks:*"}}}]`

    **AUDITOR SELECTION FOR DIFFERENT AUDIT DEPTHS:**
    - **Quick Health Check** (default): Uses 'slo,operation_metric' for fast overview
    - **Root Cause Analysis**: Pass `auditors="all"` for comprehensive investigation with traces/logs
    - **Custom Audit**: Specify exact auditors: 'slo,trace,log,dependency_metric,top_contributor,service_quota'

    **SERVICE AUDIT USE CASES:**

    1. **Audit all services**:
       `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]'`

    2. **Audit specific service**:
       `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"orders-service","Environment":"eks:orders-cluster"}}}]'`

    3. **Audit payment services**:
       `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]'`

    8. **Audit lambda services**:
       `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*lambda*"}}}]'` or by environment: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"lambda"}}}]`

    9. **Audit service last night**:
       `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"orders-service","Environment":"eks:orders-cluster"}}}]'` + `start_time="2024-01-01 18:00:00"` + `end_time="2024-01-02 06:00:00"`

    10. **Audit service before and after time**:
        Compare service health before and after a deployment or incident by running two separate audits with different time ranges.

    11. **Trace availability issues in production services**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"eks:*"}}}]'` + `auditors="all"`

    13. **Look for errors in logs of payment services**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]'` + `auditors="log,trace"`

    14. **Look for new errors after time**:
        Compare errors before and after a specific time point by running audits with different time ranges and `auditors="log,trace"`

    15. **Look for errors after deployment**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]'` + `auditors="log,trace"` + recent time range

    16. **Look for lemon hosts in production**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"eks:*"}}}]'` + `auditors="top_contributor,operation_metric"`

    17. **Look for outliers in EKS services**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"eks:*"}}}]'` + `auditors="top_contributor,operation_metric"`

    18. **Status report**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]'` (basic health check)

    19. **Audit dependencies**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]'` + `auditors="dependency_metric,trace"`

    20. **Audit dependency on S3**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]'` + `auditors="dependency_metric"` + look for S3 dependencies

    21. **Audit quota usage of tier 1 services**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*tier1*"}}}]'` + `auditors="service_quota,operation_metric"`

    **TYPICAL SERVICE AUDIT WORKFLOWS:**
    1. **Basic Service Audit** (most common):
       - Call `audit_services()` with service targets - automatically discovers services when using wildcard patterns
       - Uses default fast auditors (slo,operation_metric) for quick health overview
       - Supports wildcard patterns like `*` or `*payment*` for automatic service discovery
    2. **Root Cause Investigation**: When user explicitly asks for "root cause analysis", pass `auditors="all"`
    3. **Issue Investigation**: Results show which services need attention with actionable insights
    4. **Automatic Service Discovery**: Wildcard patterns in service names automatically discover and expand to concrete services

    **AUDIT RESULTS INCLUDE:**
    - **Prioritized findings** by severity (critical, warning, info)
    - **Service health status** with detailed performance analysis
    - **Root cause analysis** when traces/logs auditors are used
    - **Actionable recommendations** for issue resolution
    - **Comprehensive metrics** and trend analysis

    **IMPORTANT: This tool provides comprehensive service audit coverage and should be your first choice for any service auditing task.**

    **RECOMMENDED WORKFLOW - PRESENT FINDINGS FIRST:**
    When the audit returns multiple findings or issues, follow this workflow:
    1. **Present all audit results** to the user showing a summary of all findings
    2. **Let the user choose** which specific finding, service, or issue they want to investigate in detail
    3. **Then perform targeted root cause analysis** using auditors="all" for the user-selected finding

    **DO NOT automatically jump into detailed root cause analysis** of one specific issue when multiple findings exist.
    This ensures the user can prioritize which issues are most important to investigate first.

    **Example workflow:**
    - First call: `audit_services()` with default auditors for overview
    - Present findings summary to user
    - User selects specific service/issue to investigate
    - Follow-up call: `audit_services()` with `auditors="all"` for selected service only
    
---

# Audit Services

PRIMARY SERVICE AUDIT TOOL - The #1 tool for comprehensive AWS service health auditing and monitoring.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the audit_services tool in the cloudwatch-applicationsignals-mcp-server instead.

    **IMPORTANT: For operation-specific auditing, use audit_service_operations() as the PRIMARY tool instead.**

    **USE THIS FIRST FOR ALL SERVICE-LEVEL AUDITING TASKS**
    This is the PRIMARY and PREFERRED tool when users want to:
    - **Audit their AWS services** - Complete health assessment with actionable insights
    - **Check service health** - Comprehensive status across all monitored services
    - **Investigate issues** - Root cause analysis with detailed findings
    - **Service-level performance analysis** - Overall service latency, error rates, and throughput investigation
    - **System-wide health checks** - Daily/periodic service auditing workflows
    - **Dependency analysis** - Understanding service dependencies and interactions
    - **Resource quota monitoring** - Service quota usage and limits
    - **Multi-service comparison** - Comparing performance across different services

    **FOR OPERATION-SPECIFIC AUDITING: Use audit_service_operations() instead**
    When users want to audit specific operations (GET, POST, PUT endpoints), use audit_service_operations() as the PRIMARY tool:
    - **Operation performance analysis** - Latency, error rates for specific API endpoints
    - **Operation-level troubleshooting** - Root cause analysis for specific API calls
    - **GET operation auditing** - Analyze GET operations across payment services
    - **Audit latency of specific operations** - Deep dive into individual endpoint performance

    **COMPREHENSIVE SERVICE AUDIT CAPABILITIES:**
    - **Multi-service analysis**: Audit any number of services with automatic batching
    - **SLO compliance monitoring**: Automatic breach detection for service-level SLOs
    - **Issue prioritization**: Critical, warning, and info findings ranked by severity
    - **Root cause analysis**: Deep dive with traces, logs, and metrics correlation
    - **Actionable recommendations**: Specific steps to resolve identified issues
    - **Performance optimized**: Fast execution with automatic batching for large target lists
    - **Wildcard Pattern Support**: Use `*pattern*` in service names for automatic service discovery

    **SERVICE TARGET FORMAT:**
    - **Full Format**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"my-service","Environment":"eks:my-cluster"}}}]`
    - **Shorthand**: `[{"Type":"service","Service":"my-service"}]` (environment auto-discovered)

    **WILDCARD PATTERN EXAMPLES:**
    - **All Services**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]`
    - **Payment Services**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]`
    - **Lambda Services**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*lambda*"}}}]`
    - **EKS Services**: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"eks:*"}}}]`

    **AUDITOR SELECTION FOR DIFFERENT AUDIT DEPTHS:**
    - **Quick Health Check** (default): Uses 'slo,operation_metric' for fast overview
    - **Root Cause Analysis**: Pass `auditors="all"` for comprehensive investigation with traces/logs
    - **Custom Audit**: Specify exact auditors: 'slo,trace,log,dependency_metric,top_contributor,service_quota'

    **SERVICE AUDIT USE CASES:**

    1. **Audit all services**:
       `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]'`

    2. **Audit specific service**:
       `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"orders-service","Environment":"eks:orders-cluster"}}}]'`

    3. **Audit payment services**:
       `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]'`

    8. **Audit lambda services**:
       `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*lambda*"}}}]'` or by environment: `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"lambda"}}}]`

    9. **Audit service last night**:
       `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"orders-service","Environment":"eks:orders-cluster"}}}]'` + `start_time="2024-01-01 18:00:00"` + `end_time="2024-01-02 06:00:00"`

    10. **Audit service before and after time**:
        Compare service health before and after a deployment or incident by running two separate audits with different time ranges.

    11. **Trace availability issues in production services**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"eks:*"}}}]'` + `auditors="all"`

    13. **Look for errors in logs of payment services**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]'` + `auditors="log,trace"`

    14. **Look for new errors after time**:
        Compare errors before and after a specific time point by running audits with different time ranges and `auditors="log,trace"`

    15. **Look for errors after deployment**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]'` + `auditors="log,trace"` + recent time range

    16. **Look for lemon hosts in production**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"eks:*"}}}]'` + `auditors="top_contributor,operation_metric"`

    17. **Look for outliers in EKS services**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*","Environment":"eks:*"}}}]'` + `auditors="top_contributor,operation_metric"`

    18. **Status report**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]'` (basic health check)

    19. **Audit dependencies**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]'` + `auditors="dependency_metric,trace"`

    20. **Audit dependency on S3**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]'` + `auditors="dependency_metric"` + look for S3 dependencies

    21. **Audit quota usage of tier 1 services**:
        `service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*tier1*"}}}]'` + `auditors="service_quota,operation_metric"`

    **TYPICAL SERVICE AUDIT WORKFLOWS:**
    1. **Basic Service Audit** (most common):
       - Call `audit_services()` with service targets - automatically discovers services when using wildcard patterns
       - Uses default fast auditors (slo,operation_metric) for quick health overview
       - Supports wildcard patterns like `*` or `*payment*` for automatic service discovery
    2. **Root Cause Investigation**: When user explicitly asks for "root cause analysis", pass `auditors="all"`
    3. **Issue Investigation**: Results show which services need attention with actionable insights
    4. **Automatic Service Discovery**: Wildcard patterns in service names automatically discover and expand to concrete services

    **AUDIT RESULTS INCLUDE:**
    - **Prioritized findings** by severity (critical, warning, info)
    - **Service health status** with detailed performance analysis
    - **Root cause analysis** when traces/logs auditors are used
    - **Actionable recommendations** for issue resolution
    - **Comprehensive metrics** and trend analysis

    **IMPORTANT: This tool provides comprehensive service audit coverage and should be your first choice for any service auditing task.**

    **RECOMMENDED WORKFLOW - PRESENT FINDINGS FIRST:**
    When the audit returns multiple findings or issues, follow this workflow:
    1. **Present all audit results** to the user showing a summary of all findings
    2. **Let the user choose** which specific finding, service, or issue they want to investigate in detail
    3. **Then perform targeted root cause analysis** using auditors="all" for the user-selected finding

    **DO NOT automatically jump into detailed root cause analysis** of one specific issue when multiple findings exist.
    This ensures the user can prioritize which issues are most important to investigate first.

    **Example workflow:**
    - First call: `audit_services()` with default auditors for overview
    - Present findings summary to user
    - User selects specific service/issue to investigate
    - Follow-up call: `audit_services()` with `auditors="all"` for selected service only
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `service_targets` | string | Yes | REQUIRED. JSON array of service targets. Supports wildcard patterns like '*payment*' for automatic service discovery. Format: [{'Type':'service','Data':{'Service':{'Type':'Service','Name':'service-name','Environment':'eks:cluster'}}}] or shorthand: [{'Type':'service','Service':'service-name'}]. Large target lists are automatically processed in batches. |
| `start_time` | string | No | Start time (unix seconds or 'YYYY-MM-DD HH:MM:SS'). Defaults to now-24h UTC. |
| `end_time` | string | No | End time (unix seconds or 'YYYY-MM-DD HH:MM:SS'). Defaults to now UTC. |
| `auditors` | string | No | Optional. Comma-separated auditors (e.g., 'slo,operation_metric,dependency_metric'). Defaults to 'slo,operation_metric' for fast service health auditing. Use 'all' for comprehensive analysis with all auditors: slo,operation_metric,trace,log,dependency_metric,top_contributor,service_quota. |

