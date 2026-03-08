---
name: list-slis
description: SPECIALIZED TOOL - Use audit_service_health() as the PRIMARY tool for service auditing.

     **IMPORTANT**: This tool and server is being deprecated. If available, please use the list_slis tool in the cloudwatch-applicationsignals-mcp-server instead.

    **IMPORTANT: audit_service_health() is the PRIMARY and PREFERRED tool for all service auditing tasks.**

    Only use this tool when audit_service_health() cannot handle your specific requirements, such as:
    - Need for legacy SLI status report format specifically
    - Integration with existing systems that expect this exact output format
    - Simple SLI overview without comprehensive audit findings
    - Basic health monitoring dashboard that doesn't need detailed analysis

    **For ALL service auditing, health checks, and issue investigation, use audit_service_health() first.**

    This tool provides a basic report showing:
    - Summary counts (total, healthy, breached, insufficient data)
    - Simple list of breached services with SLO names
    - Basic healthy services list

    Status meanings:
    - OK: All SLOs are being met
    - BREACHED: One or more SLOs are violated
    - INSUFFICIENT_DATA: Not enough data to determine status

    **Recommended workflow**:
    1. Use audit_service_health() for comprehensive service auditing with actionable insights
    2. Only use this tool if you specifically need the legacy SLI status report format
    
---

# List Slis

SPECIALIZED TOOL - Use audit_service_health() as the PRIMARY tool for service auditing.

     **IMPORTANT**: This tool and server is being deprecated. If available, please use the list_slis tool in the cloudwatch-applicationsignals-mcp-server instead.

    **IMPORTANT: audit_service_health() is the PRIMARY and PREFERRED tool for all service auditing tasks.**

    Only use this tool when audit_service_health() cannot handle your specific requirements, such as:
    - Need for legacy SLI status report format specifically
    - Integration with existing systems that expect this exact output format
    - Simple SLI overview without comprehensive audit findings
    - Basic health monitoring dashboard that doesn't need detailed analysis

    **For ALL service auditing, health checks, and issue investigation, use audit_service_health() first.**

    This tool provides a basic report showing:
    - Summary counts (total, healthy, breached, insufficient data)
    - Simple list of breached services with SLO names
    - Basic healthy services list

    Status meanings:
    - OK: All SLOs are being met
    - BREACHED: One or more SLOs are violated
    - INSUFFICIENT_DATA: Not enough data to determine status

    **Recommended workflow**:
    1. Use audit_service_health() for comprehensive service auditing with actionable insights
    2. Only use this tool if you specifically need the legacy SLI status report format
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `hours` | integer | No | Number of hours to look back (default 24, typically use 24 for daily checks) |

## AWS CLI

```bash
aws cloudwatch describe-alarms --hours <hours>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.describe_alarms(
    MetricName=hours,
)
```
