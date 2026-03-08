---
name: get-cost-and-usage
description: Get cost and usage data for ElastiCache resources.

    This tool retrieves cost and usage data for ElastiCache resources with customizable
    time periods and granularity. It uses default configurations for:
    - Metrics: BlendedCost, UnblendedCost, UsageQuantity
    - Group By: SERVICE dimension and Environment tag
    - Filter: Filtered to Amazon ElastiCache service

    Args:
        request: The GetCostAndUsageRequest object containing:
            - time_period: Time period in YYYY-MM-DD/YYYY-MM-DD format
            - granularity: Data granularity (DAILY, MONTHLY, or HOURLY)

    Returns:
        Dict containing the cost and usage data.
    
---

# Get-Cost-And-Usage

Get cost and usage data for ElastiCache resources.

    This tool retrieves cost and usage data for ElastiCache resources with customizable
    time periods and granularity. It uses default configurations for:
    - Metrics: BlendedCost, UnblendedCost, UsageQuantity
    - Group By: SERVICE dimension and Environment tag
    - Filter: Filtered to Amazon ElastiCache service

    Args:
        request: The GetCostAndUsageRequest object containing:
            - time_period: Time period in YYYY-MM-DD/YYYY-MM-DD format
            - granularity: Data granularity (DAILY, MONTHLY, or HOURLY)

    Returns:
        Dict containing the cost and usage data.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | string | Yes |  |

## AWS CLI

```bash
aws ce get-cost-and-usage --time-period <request>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_cost_and_usage(
    TimePeriod=request,
)
```
