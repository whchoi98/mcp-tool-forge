---
name: list-pricing-rules
description: Retrieves a list of pricing rules from AWS Billing Conductor.

This tool retrieve pricing rules for a given billing period.

The tool returns information about:
- Pricing rule ARN, name, and description
- Type (MARKUP, DISCOUNT, or TIERING)
- Scope (GLOBAL, SERVICE, BILLING_ENTITY, or SKU)
- Modifier percentage, associated pricing plan count
- Service, operation, usage type, billing entity
- Tiering configuration, creation and last modified timestamps

You can filter pricing rules by:
- Arns: Filter by specific pricing rule ARNs

Example 1: {"billing_period": "2025-01"}
Example 2: {"filters": "{"Arns": ["arn:aws:billingconductor::123456789012:pricingrule/abc"]}", "billing_period": "2025-01"}
---

# List-Pricing-Rules

Retrieves a list of pricing rules from AWS Billing Conductor.

This tool retrieve pricing rules for a given billing period.

The tool returns information about:
- Pricing rule ARN, name, and description
- Type (MARKUP, DISCOUNT, or TIERING)
- Scope (GLOBAL, SERVICE, BILLING_ENTITY, or SKU)
- Modifier percentage, associated pricing plan count
- Service, operation, usage type, billing entity
- Tiering configuration, creation and last modified timestamps

You can filter pricing rules by:
- Arns: Filter by specific pricing rule ARNs

Example 1: {"billing_period": "2025-01"}
Example 2: {"filters": "{"Arns": ["arn:aws:billingconductor::123456789012:pricingrule/abc"]}", "billing_period": "2025-01"}

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `billing_period` | string | No |  |
| `filters` | string | No |  |
| `max_pages` | integer | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws billingconductor list-pricing-rules --billing-period <billing_period> --filters <filters> --max-results <max_pages> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('billingconductor')
response = client.list_pricing_rules(
    BillingPeriod=billing_period,
    Filters=filters,
    MaxResults=max_pages,
    NextToken=next_token,
)
```
