---
name: query-sampled-traces
description: SECONDARY TRACE TOOL - Query AWS X-Ray traces (5% sampled data) for trace investigation.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the query_sampled_traces tool in the cloudwatch-applicationsignals-mcp-server instead.

    ⚠️ **IMPORTANT: Consider using audit_slos() with auditors="all" instead for comprehensive root cause analysis**

    **RECOMMENDED WORKFLOW FOR OPERATION DISCOVERY:**
    1. **Use `get_service_detail(service_name)` FIRST** to discover operations from metric dimensions
    2. **Use audit_slos() with auditors="all"** for comprehensive root cause analysis (PREFERRED)
    3. Only use this tool if you need specific trace filtering that other tools don't provide

    **RECOMMENDED WORKFLOW FOR SLO BREACH INVESTIGATION:**
    1. Use get_slo() to understand SLO configuration
    2. **Use audit_slos() with auditors="all"** for comprehensive root cause analysis (PREFERRED)
    3. Only use this tool if you need specific trace filtering that audit_slos() doesn't provide

    **WHY audit_slos() IS PREFERRED:**
    - **Comprehensive analysis**: Combines traces, logs, metrics, and dependencies
    - **Actionable recommendations**: Provides specific steps to resolve issues
    - **Integrated findings**: Correlates multiple data sources for better insights
    - **Much more effective** than individual trace analysis

    **WHY get_service_detail() IS PREFERRED FOR OPERATION DISCOVERY:**
    - **Direct operation discovery**: Operations are available in metric dimensions
    - **More reliable**: Uses Application Signals service metadata instead of sampling
    - **Comprehensive**: Shows all operations, not just those in sampled traces

    ⚠️ **LIMITATIONS OF THIS TOOL:**
    - Uses X-Ray's **5% sampled trace data** - may miss critical errors
    - **Limited context** compared to comprehensive audit tools
    - **No integrated analysis** with logs, metrics, or dependencies
    - **May miss operations** due to sampling - use get_service_detail() for complete operation discovery
    - For 100% trace visibility, enable Transaction Search and use search_transaction_spans()

    **Use this tool only when:**
    - You need specific X-Ray filter expressions not available in audit tools
    - You're doing exploratory trace analysis outside of SLO breach investigation
    - You need raw trace data for custom analysis
    - **After using get_service_detail() for operation discovery**

    **For operation discovery, use get_service_detail() instead:**
    ```
    get_service_detail(service_name='your-service-name')
    ```

    **For SLO breach root cause analysis, use audit_slos() instead:**
    ```
    audit_slos(
        slo_targets='[{"Type":"slo","Data":{"Slo":{"SloName":"your-slo-name"}}}]', auditors='all'
    )
    ```

    Common filter expressions (if you must use this tool):
    - 'service("service-name"){fault = true}': Find all traces with faults (5xx errors) for a service
    - 'service("service-name")': Filter by specific service
    - 'duration > 5': Find slow requests (over 5 seconds)
    - 'http.status = 500': Find specific HTTP status codes
    - 'annotation[aws.local.operation]="GET /owners/*/lastname"': Filter by specific operation (from metric dimensions)
    - 'annotation[aws.remote.operation]="ListOwners"': Filter by remote operation name
    - Combine filters: 'service("api"){fault = true} AND annotation[aws.local.operation]="POST /visits"'

    Returns JSON with trace summaries including:
    - Trace ID for detailed investigation
    - Duration and response time
    - Error/fault/throttle status
    - HTTP information (method, status, URL)
    - Service interactions
    - User information if available
    - Exception root causes (ErrorRootCauses, FaultRootCauses, ResponseTimeRootCauses)

    **RECOMMENDATION: Use get_service_detail() for operation discovery and audit_slos() with auditors="all" for comprehensive root cause analysis instead of this tool.**

    Returns:
        JSON string containing trace summaries with error status, duration, and service details
    
---

# Query Sampled Traces

SECONDARY TRACE TOOL - Query AWS X-Ray traces (5% sampled data) for trace investigation.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the query_sampled_traces tool in the cloudwatch-applicationsignals-mcp-server instead.

    ⚠️ **IMPORTANT: Consider using audit_slos() with auditors="all" instead for comprehensive root cause analysis**

    **RECOMMENDED WORKFLOW FOR OPERATION DISCOVERY:**
    1. **Use `get_service_detail(service_name)` FIRST** to discover operations from metric dimensions
    2. **Use audit_slos() with auditors="all"** for comprehensive root cause analysis (PREFERRED)
    3. Only use this tool if you need specific trace filtering that other tools don't provide

    **RECOMMENDED WORKFLOW FOR SLO BREACH INVESTIGATION:**
    1. Use get_slo() to understand SLO configuration
    2. **Use audit_slos() with auditors="all"** for comprehensive root cause analysis (PREFERRED)
    3. Only use this tool if you need specific trace filtering that audit_slos() doesn't provide

    **WHY audit_slos() IS PREFERRED:**
    - **Comprehensive analysis**: Combines traces, logs, metrics, and dependencies
    - **Actionable recommendations**: Provides specific steps to resolve issues
    - **Integrated findings**: Correlates multiple data sources for better insights
    - **Much more effective** than individual trace analysis

    **WHY get_service_detail() IS PREFERRED FOR OPERATION DISCOVERY:**
    - **Direct operation discovery**: Operations are available in metric dimensions
    - **More reliable**: Uses Application Signals service metadata instead of sampling
    - **Comprehensive**: Shows all operations, not just those in sampled traces

    ⚠️ **LIMITATIONS OF THIS TOOL:**
    - Uses X-Ray's **5% sampled trace data** - may miss critical errors
    - **Limited context** compared to comprehensive audit tools
    - **No integrated analysis** with logs, metrics, or dependencies
    - **May miss operations** due to sampling - use get_service_detail() for complete operation discovery
    - For 100% trace visibility, enable Transaction Search and use search_transaction_spans()

    **Use this tool only when:**
    - You need specific X-Ray filter expressions not available in audit tools
    - You're doing exploratory trace analysis outside of SLO breach investigation
    - You need raw trace data for custom analysis
    - **After using get_service_detail() for operation discovery**

    **For operation discovery, use get_service_detail() instead:**
    ```
    get_service_detail(service_name='your-service-name')
    ```

    **For SLO breach root cause analysis, use audit_slos() instead:**
    ```
    audit_slos(
        slo_targets='[{"Type":"slo","Data":{"Slo":{"SloName":"your-slo-name"}}}]', auditors='all'
    )
    ```

    Common filter expressions (if you must use this tool):
    - 'service("service-name"){fault = true}': Find all traces with faults (5xx errors) for a service
    - 'service("service-name")': Filter by specific service
    - 'duration > 5': Find slow requests (over 5 seconds)
    - 'http.status = 500': Find specific HTTP status codes
    - 'annotation[aws.local.operation]="GET /owners/*/lastname"': Filter by specific operation (from metric dimensions)
    - 'annotation[aws.remote.operation]="ListOwners"': Filter by remote operation name
    - Combine filters: 'service("api"){fault = true} AND annotation[aws.local.operation]="POST /visits"'

    Returns JSON with trace summaries including:
    - Trace ID for detailed investigation
    - Duration and response time
    - Error/fault/throttle status
    - HTTP information (method, status, URL)
    - Service interactions
    - User information if available
    - Exception root causes (ErrorRootCauses, FaultRootCauses, ResponseTimeRootCauses)

    **RECOMMENDATION: Use get_service_detail() for operation discovery and audit_slos() with auditors="all" for comprehensive root cause analysis instead of this tool.**

    Returns:
        JSON string containing trace summaries with error status, duration, and service details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `start_time` | string | No | Start time in ISO format (e.g., "2024-01-01T00:00:00Z"). Defaults to 3 hours ago |
| `end_time` | string | No | End time in ISO format (e.g., "2024-01-01T01:00:00Z"). Defaults to current time |
| `filter_expression` | string | No | X-Ray filter expression to narrow results (e.g., service("service-name"){fault = true}) |
| `region` | string | No | AWS region (defaults to AWS_REGION environment variable) |

## AWS CLI

```bash
aws xray get-trace-summaries --start-time <start_time> --end-time <end_time> --filter-expression <filter_expression>
```

## boto3

```python
import boto3

client = boto3.client('xray')
response = client.get_trace_summaries(
    StartTime=start_time,
    EndTime=end_time,
    FilterExpression=filter_expression,
)
```
