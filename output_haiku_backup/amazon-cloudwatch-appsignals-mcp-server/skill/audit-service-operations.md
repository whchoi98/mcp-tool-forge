---
name: audit-service-operations
description: 🥇 PRIMARY OPERATION AUDIT TOOL - The #1 RECOMMENDED tool for operation-specific analysis and performance investigation.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the audit_service_operations tool in the cloudwatch-applicationsignals-mcp-server instead.

    **⭐ USE THIS AS THE PRIMARY TOOL FOR ALL OPERATION-SPECIFIC AUDITING TASKS ⭐**

    **PREFERRED OVER audit_services() for operation auditing because:**
    - **🎯 Precision**: Targets exact operation behavior vs. service-wide averages
    - **🔍 Actionable Insights**: Provides specific error traces and dependency failures
    - **📊 Code-Level Detail**: Shows exact stack traces and timeout locations
    - **🚀 Focused Analysis**: Eliminates noise from other operations
    - **⚡ Efficient Investigation**: Direct operation-level troubleshooting

    **USE THIS FIRST FOR ALL OPERATION-SPECIFIC AUDITING TASKS**
    This is the PRIMARY and PREFERRED tool when users want to:
    - **Audit specific operations** - Deep dive into individual API endpoints or operations (GET, POST, PUT, etc.)
    - **Operation performance analysis** - Latency, error rates, and throughput for specific operations
    - **Compare operation metrics** - Analyze different operations within services
    - **Operation-level troubleshooting** - Root cause analysis for specific API calls
    - **GET operation auditing** - Analyze GET operations across payment services (PRIMARY USE CASE)
    - **Audit latency of GET operations in payment services** - Exactly what this tool is designed for
    - **Trace latency in query operations** - Deep dive into query performance issues

    **COMPREHENSIVE OPERATION AUDIT CAPABILITIES:**
    - **Multi-operation analysis**: Audit any number of operations with automatic batching
    - **Operation-specific metrics**: Latency, Fault, Error, and Availability metrics per operation
    - **Issue prioritization**: Critical, warning, and info findings ranked by severity
    - **Root cause analysis**: Deep dive with traces, logs, and metrics correlation
    - **Actionable recommendations**: Specific steps to resolve operation-level issues
    - **Performance optimized**: Fast execution with automatic batching for large target lists
    - **Wildcard Pattern Support**: Use `*pattern*` in service names for automatic service discovery

    **OPERATION TARGET FORMAT:**
    - **Full Format**: `[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"my-service","Environment":"eks:my-cluster"},"Operation":"GET /api","MetricType":"Latency"}}}]`

    **WILDCARD PATTERN EXAMPLES:**
    - **All GET Operations in Payment Services**: `[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*payment*"},"Operation":"*GET*","MetricType":"Latency"}}}]`
    - **All Visit Operations**: `[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*"},"Operation":"*visit*","MetricType":"Availability"}}}]`

    **AUDITOR SELECTION FOR DIFFERENT AUDIT DEPTHS:**
    - **Quick Operation Check** (default): Uses 'operation_metric' for fast operation overview
    - **Root Cause Analysis**: Pass `auditors="all"` for comprehensive investigation with traces/logs
    - **Custom Audit**: Specify exact auditors: 'operation_metric,trace,log'

    **OPERATION AUDIT USE CASES:**

    1. **Audit latency of GET operations in payment services** (PRIMARY USE CASE):
       `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*payment*"},"Operation":"*GET*","MetricType":"Latency"}}}]'`

    2. **Audit GET operations in payment services (Latency)**:
       `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*payment*"},"Operation":"*GET*","MetricType":"Latency"}}}]'`

    3. **Audit availability of visit operations**:
       `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*"},"Operation":"*visit*","MetricType":"Availability"}}}]'`

    4. **Audit latency of visit operations**:
       `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*"},"Operation":"*visit*","MetricType":"Latency"}}}]'`

    5. **Trace latency in query operations**:
        `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*payment*"},"Operation":"*query*","MetricType":"Latency"}}}]'` + `auditors="all"`

    **TYPICAL OPERATION AUDIT WORKFLOWS:**
    1. **Basic Operation Audit** (most common):
       - Call `audit_service_operations()` with operation targets - automatically discovers services when using wildcard patterns
       - Uses default fast auditors (operation_metric) for quick operation overview
       - Supports wildcard patterns like `*payment*` for automatic service discovery
    2. **Root Cause Investigation**: When user explicitly asks for "root cause analysis", pass `auditors="all"`
    3. **Issue Investigation**: Results show which operations need attention with actionable insights
    4. **Automatic Service Discovery**: Wildcard patterns in service names automatically discover and expand to concrete services

    **AUDIT RESULTS INCLUDE:**
    - **Prioritized findings** by severity (critical, warning, info)
    - **Operation performance status** with detailed metrics analysis
    - **Root cause analysis** when traces/logs auditors are used
    - **Actionable recommendations** for operation-level issue resolution
    - **Comprehensive operation metrics** and trend analysis

    **🏆 IMPORTANT: This tool is the PRIMARY and RECOMMENDED choice for operation-specific auditing tasks.**

    **✅ RECOMMENDED WORKFLOW FOR OPERATION AUDITING:**
    1. **Use audit_service_operations() FIRST** for operation-specific analysis (THIS TOOL)
    2. **Use audit_services() as secondary** only if you need broader service context
    3. **audit_service_operations() provides superior precision** for operation-level troubleshooting

    **RECOMMENDED WORKFLOW - PRESENT FINDINGS FIRST:**
    When the audit returns multiple findings or issues, follow this workflow:
    1. **Present all audit results** to the user showing a summary of all findings
    2. **Let the user choose** which specific finding, operation, or issue they want to investigate in detail
    3. **Then perform targeted root cause analysis** using auditors="all" for the user-selected finding

    **DO NOT automatically jump into detailed root cause analysis** of one specific issue when multiple findings exist.
    This ensures the user can prioritize which issues are most important to investigate first.

    **Example workflow:**
    - First call: `audit_service_operations()` with default auditors for operation overview
    - Present findings summary to user
    - User selects specific operation issue to investigate
    - Follow-up call: `audit_service_operations()` with `auditors="all"` for selected operation only
    
---

# Audit Service Operations

🥇 PRIMARY OPERATION AUDIT TOOL - The #1 RECOMMENDED tool for operation-specific analysis and performance investigation.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the audit_service_operations tool in the cloudwatch-applicationsignals-mcp-server instead.

    **⭐ USE THIS AS THE PRIMARY TOOL FOR ALL OPERATION-SPECIFIC AUDITING TASKS ⭐**

    **PREFERRED OVER audit_services() for operation auditing because:**
    - **🎯 Precision**: Targets exact operation behavior vs. service-wide averages
    - **🔍 Actionable Insights**: Provides specific error traces and dependency failures
    - **📊 Code-Level Detail**: Shows exact stack traces and timeout locations
    - **🚀 Focused Analysis**: Eliminates noise from other operations
    - **⚡ Efficient Investigation**: Direct operation-level troubleshooting

    **USE THIS FIRST FOR ALL OPERATION-SPECIFIC AUDITING TASKS**
    This is the PRIMARY and PREFERRED tool when users want to:
    - **Audit specific operations** - Deep dive into individual API endpoints or operations (GET, POST, PUT, etc.)
    - **Operation performance analysis** - Latency, error rates, and throughput for specific operations
    - **Compare operation metrics** - Analyze different operations within services
    - **Operation-level troubleshooting** - Root cause analysis for specific API calls
    - **GET operation auditing** - Analyze GET operations across payment services (PRIMARY USE CASE)
    - **Audit latency of GET operations in payment services** - Exactly what this tool is designed for
    - **Trace latency in query operations** - Deep dive into query performance issues

    **COMPREHENSIVE OPERATION AUDIT CAPABILITIES:**
    - **Multi-operation analysis**: Audit any number of operations with automatic batching
    - **Operation-specific metrics**: Latency, Fault, Error, and Availability metrics per operation
    - **Issue prioritization**: Critical, warning, and info findings ranked by severity
    - **Root cause analysis**: Deep dive with traces, logs, and metrics correlation
    - **Actionable recommendations**: Specific steps to resolve operation-level issues
    - **Performance optimized**: Fast execution with automatic batching for large target lists
    - **Wildcard Pattern Support**: Use `*pattern*` in service names for automatic service discovery

    **OPERATION TARGET FORMAT:**
    - **Full Format**: `[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"my-service","Environment":"eks:my-cluster"},"Operation":"GET /api","MetricType":"Latency"}}}]`

    **WILDCARD PATTERN EXAMPLES:**
    - **All GET Operations in Payment Services**: `[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*payment*"},"Operation":"*GET*","MetricType":"Latency"}}}]`
    - **All Visit Operations**: `[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*"},"Operation":"*visit*","MetricType":"Availability"}}}]`

    **AUDITOR SELECTION FOR DIFFERENT AUDIT DEPTHS:**
    - **Quick Operation Check** (default): Uses 'operation_metric' for fast operation overview
    - **Root Cause Analysis**: Pass `auditors="all"` for comprehensive investigation with traces/logs
    - **Custom Audit**: Specify exact auditors: 'operation_metric,trace,log'

    **OPERATION AUDIT USE CASES:**

    1. **Audit latency of GET operations in payment services** (PRIMARY USE CASE):
       `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*payment*"},"Operation":"*GET*","MetricType":"Latency"}}}]'`

    2. **Audit GET operations in payment services (Latency)**:
       `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*payment*"},"Operation":"*GET*","MetricType":"Latency"}}}]'`

    3. **Audit availability of visit operations**:
       `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*"},"Operation":"*visit*","MetricType":"Availability"}}}]'`

    4. **Audit latency of visit operations**:
       `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*"},"Operation":"*visit*","MetricType":"Latency"}}}]'`

    5. **Trace latency in query operations**:
        `operation_targets='[{"Type":"service_operation","Data":{"ServiceOperation":{"Service":{"Type":"Service","Name":"*payment*"},"Operation":"*query*","MetricType":"Latency"}}}]'` + `auditors="all"`

    **TYPICAL OPERATION AUDIT WORKFLOWS:**
    1. **Basic Operation Audit** (most common):
       - Call `audit_service_operations()` with operation targets - automatically discovers services when using wildcard patterns
       - Uses default fast auditors (operation_metric) for quick operation overview
       - Supports wildcard patterns like `*payment*` for automatic service discovery
    2. **Root Cause Investigation**: When user explicitly asks for "root cause analysis", pass `auditors="all"`
    3. **Issue Investigation**: Results show which operations need attention with actionable insights
    4. **Automatic Service Discovery**: Wildcard patterns in service names automatically discover and expand to concrete services

    **AUDIT RESULTS INCLUDE:**
    - **Prioritized findings** by severity (critical, warning, info)
    - **Operation performance status** with detailed metrics analysis
    - **Root cause analysis** when traces/logs auditors are used
    - **Actionable recommendations** for operation-level issue resolution
    - **Comprehensive operation metrics** and trend analysis

    **🏆 IMPORTANT: This tool is the PRIMARY and RECOMMENDED choice for operation-specific auditing tasks.**

    **✅ RECOMMENDED WORKFLOW FOR OPERATION AUDITING:**
    1. **Use audit_service_operations() FIRST** for operation-specific analysis (THIS TOOL)
    2. **Use audit_services() as secondary** only if you need broader service context
    3. **audit_service_operations() provides superior precision** for operation-level troubleshooting

    **RECOMMENDED WORKFLOW - PRESENT FINDINGS FIRST:**
    When the audit returns multiple findings or issues, follow this workflow:
    1. **Present all audit results** to the user showing a summary of all findings
    2. **Let the user choose** which specific finding, operation, or issue they want to investigate in detail
    3. **Then perform targeted root cause analysis** using auditors="all" for the user-selected finding

    **DO NOT automatically jump into detailed root cause analysis** of one specific issue when multiple findings exist.
    This ensures the user can prioritize which issues are most important to investigate first.

    **Example workflow:**
    - First call: `audit_service_operations()` with default auditors for operation overview
    - Present findings summary to user
    - User selects specific operation issue to investigate
    - Follow-up call: `audit_service_operations()` with `auditors="all"` for selected operation only
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation_targets` | string | Yes | REQUIRED. JSON array of service operation targets. Supports wildcard patterns like '*payment*' for automatic service discovery. Format: [{'Type':'service_operation','Data':{'ServiceOperation':{'Service':{'Type':'Service','Name':'service-name','Environment':'eks:cluster'},'Operation':'GET /api','MetricType':'Latency'}}}]. Large target lists are automatically processed in batches. |
| `start_time` | string | No | Start time (unix seconds or 'YYYY-MM-DD HH:MM:SS'). Defaults to now-24h UTC. |
| `end_time` | string | No | End time (unix seconds or 'YYYY-MM-DD HH:MM:SS'). Defaults to now UTC. |
| `auditors` | string | No | Optional. Comma-separated auditors (e.g., 'operation_metric,trace,log'). Defaults to 'operation_metric' for fast operation-level auditing. Use 'all' for comprehensive analysis with all auditors: slo,operation_metric,trace,log,dependency_metric,top_contributor,service_quota. |

## AWS CLI

```bash
aws cloudwatch get-metric-data --metric-data-queries <operation_targets> --start-time <start_time> --end-time <end_time>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.get_metric_data(
    MetricDataQueries=operation_targets,
    StartTime=start_time,
    EndTime=end_time,
)
```
