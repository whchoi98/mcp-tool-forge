---
name: sp-performance
description: Tool that retrieves AWS Savings Plans coverage and utilization data using the Cost Explorer API.

This tool provides insights into your Savings Plans usage patterns through three main operations:

1. get_savings_plans_coverage: Shows how much of your eligible usage is covered by Savings Plans
2. get_savings_plans_utilization: Shows overall utilization metrics for your Savings Plans
3. get_savings_plans_utilization_details: Shows detailed per-Savings Plan utilization
---

# Sp-Performance

Tool that retrieves AWS Savings Plans coverage and utilization data using the Cost Explorer API.

This tool provides insights into your Savings Plans usage patterns through three main operations:

1. get_savings_plans_coverage: Shows how much of your eligible usage is covered by Savings Plans
2. get_savings_plans_utilization: Shows overall utilization metrics for your Savings Plans
3. get_savings_plans_utilization_details: Shows detailed per-Savings Plan utilization

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | Yes |  |
| `start_date` | string | No |  |
| `end_date` | string | No |  |
| `granularity` | string | No |  |
| `metrics` | string | No |  |
| `group_by` | string | No |  |
| `filter` | string | No |  |
| `max_results` | string | No |  |

## AWS CLI

```bash
aws ce get-savings-plans-coverage --time-period <start_date> --granularity <granularity> --filter <filter> --metrics <metrics> --group-by <group_by> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_savings_plans_coverage(
    TimePeriod=start_date,
    Granularity=granularity,
    Filter=filter,
    Metrics=metrics,
    GroupBy=group_by,
    MaxResults=max_results,
)
```
