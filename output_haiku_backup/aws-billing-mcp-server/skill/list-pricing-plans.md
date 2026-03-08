---
name: list-pricing-plans
description: Retrieves a list of pricing plans from AWS Billing Conductor.

This tool retrieve pricing plans for a given billing period.
If no billing period is provided, the current billing period is used.

The tool returns information about:
- Pricing plan ARN, name, and description
- Number of associated pricing rules (size)
- Creation and last modified timestamps

You can filter pricing plans by:
- Arns: Filter by specific pricing plan ARNs

Example 1: {"billing_period": "2025-01"}
Example 2: {"filters": "{"Arns": ["arn:aws:billingconductor::123456789012:pricingplan/abc"]}", "billing_period": "2025-01"}
---

# List-Pricing-Plans

Retrieves a list of pricing plans from AWS Billing Conductor.

This tool retrieve pricing plans for a given billing period.
If no billing period is provided, the current billing period is used.

The tool returns information about:
- Pricing plan ARN, name, and description
- Number of associated pricing rules (size)
- Creation and last modified timestamps

You can filter pricing plans by:
- Arns: Filter by specific pricing plan ARNs

Example 1: {"billing_period": "2025-01"}
Example 2: {"filters": "{"Arns": ["arn:aws:billingconductor::123456789012:pricingplan/abc"]}", "billing_period": "2025-01"}

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `billing_period` | string | No |  |
| `filters` | string | No |  |
| `max_pages` | integer | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws billingconductor list-pricing-plans --billing-period <billing_period> --filters <filters> --max-results <max_pages> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('billingconductor')
response = client.list_pricing_plans(
    BillingPeriod=billing_period,
    Filters=filters,
    MaxResults=max_pages,
    NextToken=next_token,
)
```
