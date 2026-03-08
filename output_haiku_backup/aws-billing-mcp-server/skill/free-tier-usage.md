---
name: free-tier-usage
description: Retrieves AWS Free Tier usage information using the Free Tier Usage API.

This tool provides insights into your AWS Free Tier usage across services:

1. get_free_tier_usage: Shows your current Free Tier usage across AWS services
   - Helps identify where you are approaching Free Tier limits
   - Shows actual usage against Free Tier allocations
   - Supports filtering by service, region, or usage type
   - Possible Dimensions values are: 'SERVICE'|'OPERATION'|'USAGE_TYPE'|'REGION'|'FREE_TIER_TYPE'|'DESCRIPTION'|'USAGE_PERCENTAGE'
   - Possible MatchOptions are: 'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'GREATER_THAN_OR_EQUAL'
   
---

# Free-Tier-Usage

Retrieves AWS Free Tier usage information using the Free Tier Usage API.

This tool provides insights into your AWS Free Tier usage across services:

1. get_free_tier_usage: Shows your current Free Tier usage across AWS services
   - Helps identify where you are approaching Free Tier limits
   - Shows actual usage against Free Tier allocations
   - Supports filtering by service, region, or usage type
   - Possible Dimensions values are: 'SERVICE'|'OPERATION'|'USAGE_TYPE'|'REGION'|'FREE_TIER_TYPE'|'DESCRIPTION'|'USAGE_PERCENTAGE'
   - Possible MatchOptions are: 'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'GREATER_THAN_OR_EQUAL'
   

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | No |  |
| `filter` | string | No |  |
| `max_results` | string | No |  |

## AWS CLI

```bash
aws ce get-free-tier-usage --operation <operation> --filter <filter> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_free_tier_usage(
    Operation=operation,
    Filter=filter,
    MaxResults=max_results,
)
```
