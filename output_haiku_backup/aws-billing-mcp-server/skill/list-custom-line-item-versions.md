---
name: list-custom-line-item-versions
description: Retrieves a list of versions for a specific custom line item from AWS Billing Conductor.

This tool retrieve all versions of a custom line item.
If no billing period is provided, the current billing period is used.

The tool returns information about each version including charge details, computation rule,
billing periods, and timestamps.

You can filter versions by:
- BillingPeriodRange: Filter by start and/or end billing period

Example 1: {"arn": "arn:aws:billingconductor::123456789012:customlineitem/abcdef1234"}
Example 2: {"arn": "...", "filters": "{"BillingPeriodRange": {"StartBillingPeriod": "2025-01", "EndBillingPeriod": "2025-06"}}"}
---

# List-Custom-Line-Item-Versions

Retrieves a list of versions for a specific custom line item from AWS Billing Conductor.

This tool retrieve all versions of a custom line item.
If no billing period is provided, the current billing period is used.

The tool returns information about each version including charge details, computation rule,
billing periods, and timestamps.

You can filter versions by:
- BillingPeriodRange: Filter by start and/or end billing period

Example 1: {"arn": "arn:aws:billingconductor::123456789012:customlineitem/abcdef1234"}
Example 2: {"arn": "...", "filters": "{"BillingPeriodRange": {"StartBillingPeriod": "2025-01", "EndBillingPeriod": "2025-06"}}"}

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `arn` | string | Yes |  |
| `filters` | string | No |  |
| `max_pages` | integer | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws billingconductor list-custom-line-item-versions --arn <arn> --filters <filters> --max-results <max_pages> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('billingconductor')
response = client.list_custom_line_item_versions(
    Arn=arn,
    Filters=filters,
    MaxResults=max_pages,
    NextToken=next_token,
)
```
