---
name: get-slo
description: Get detailed information about a specific Service Level Objective (SLO).

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the get_slo tool in the cloudwatch-applicationsignals-mcp-server instead.

    **RECOMMENDED WORKFLOW AFTER USING THIS TOOL:**
    After getting SLO configuration details, use `audit_slos()` with `auditors="all"` for comprehensive root cause analysis:
    - `audit_slos(slo_targets='[{"Type":"slo","Data":{"Slo":{"SloName":"your-slo-name"}}}]', auditors="all")`
    - This provides deep root cause analysis with traces, logs, metrics, and dependencies
    - Much more comprehensive than using individual trace tools

    Use this tool to:
    - Get comprehensive SLO configuration details
    - Understand what metrics the SLO monitors
    - See threshold values and comparison operators
    - Extract operation names and key attributes for further investigation
    - Identify dependency configurations
    - Review attainment goals and burn rate settings

    Returns detailed information including:
    - SLO name, description, and metadata
    - Metric configuration (for period-based or request-based SLOs)
    - Key attributes and operation names
    - Metric type (LATENCY or AVAILABILITY)
    - Threshold values and comparison operators
    - Goal configuration (attainment percentage, time interval)
    - Burn rate configurations

    This tool is essential for:
    - Understanding SLO configuration before deep investigation
    - Getting the exact SLO name/ARN for use with audit_slos()
    - Identifying the metrics and thresholds being monitored
    - Planning comprehensive root cause analysis workflow

    **NEXT STEP: Use audit_slos() with auditors="all" for root cause analysis**
    
---

# Get Slo

Get detailed information about a specific Service Level Objective (SLO).

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the get_slo tool in the cloudwatch-applicationsignals-mcp-server instead.

    **RECOMMENDED WORKFLOW AFTER USING THIS TOOL:**
    After getting SLO configuration details, use `audit_slos()` with `auditors="all"` for comprehensive root cause analysis:
    - `audit_slos(slo_targets='[{"Type":"slo","Data":{"Slo":{"SloName":"your-slo-name"}}}]', auditors="all")`
    - This provides deep root cause analysis with traces, logs, metrics, and dependencies
    - Much more comprehensive than using individual trace tools

    Use this tool to:
    - Get comprehensive SLO configuration details
    - Understand what metrics the SLO monitors
    - See threshold values and comparison operators
    - Extract operation names and key attributes for further investigation
    - Identify dependency configurations
    - Review attainment goals and burn rate settings

    Returns detailed information including:
    - SLO name, description, and metadata
    - Metric configuration (for period-based or request-based SLOs)
    - Key attributes and operation names
    - Metric type (LATENCY or AVAILABILITY)
    - Threshold values and comparison operators
    - Goal configuration (attainment percentage, time interval)
    - Burn rate configurations

    This tool is essential for:
    - Understanding SLO configuration before deep investigation
    - Getting the exact SLO name/ARN for use with audit_slos()
    - Identifying the metrics and thresholds being monitored
    - Planning comprehensive root cause analysis workflow

    **NEXT STEP: Use audit_slos() with auditors="all" for root cause analysis**
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `slo_id` | string | Yes | The ARN or name of the SLO to retrieve |

## AWS CLI

```bash
aws cloudwatch get-service-level-objective --service-level-objective-id <slo_id>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.get_service_level_objective(
    ServiceLevelObjectiveId=slo_id,
)
```
