---
name: list-resources-associated-to-custom-line-item
description: Lists the resources associated to a custom line item from AWS Billing Conductor.

This tool retrieve resources associated with a specific custom line item.
If no billing period is provided, the current billing period is used.

The tool returns information about each associated resource:
- Resource ARN (can be a billing group or custom line item)
- End billing period of the association
- Relationship type (PARENT or CHILD)

You can filter associated resources by:
- Relationship: Filter by relationship type ("PARENT" or "CHILD")

Example 1: {"arn": "arn:aws:billingconductor::123456789012:customlineitem/abcdef1234"}
Example 2: {"arn": "...", "filters": "{"Relationship": "CHILD"}", "billing_period": "2025-01"}
---

# List-Resources-Associated-To-Custom-Line-Item

Lists the resources associated to a custom line item from AWS Billing Conductor.

This tool retrieve resources associated with a specific custom line item.
If no billing period is provided, the current billing period is used.

The tool returns information about each associated resource:
- Resource ARN (can be a billing group or custom line item)
- End billing period of the association
- Relationship type (PARENT or CHILD)

You can filter associated resources by:
- Relationship: Filter by relationship type ("PARENT" or "CHILD")

Example 1: {"arn": "arn:aws:billingconductor::123456789012:customlineitem/abcdef1234"}
Example 2: {"arn": "...", "filters": "{"Relationship": "CHILD"}", "billing_period": "2025-01"}

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `arn` | string | Yes |  |
| `billing_period` | string | No |  |
| `filters` | string | No |  |
| `max_pages` | integer | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws billingconductor list-resources-associated-to-custom-line-item --arn <arn> --billing-period <billing_period> --filters <filters> --max-results <max_pages> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('billingconductor')
response = client.list_resources_associated_to_custom_line_item(
    Arn=arn,
    BillingPeriod=billing_period,
    Filters=filters,
    MaxResults=max_pages,
    NextToken=next_token,
)
```
