---
name: list-pricing-rules-for-plan
description: Lists the pricing rules associated with a specific pricing plan.

This tool retrieve pricing rules associated with a specific pricing plan
If no billing period is provided, the current billing period is used.

The tool returns information about:
- The billing period for which the pricing rule associations are listed.
- The optional pagination token to be used on subsequent calls.
- The ARN of the pricing plan for which associations are listed.
- A list containing pricing rules that are associated with the requested pricing plan

Example: {"pricing_plan_arn": "arn:aws:billingconductor::123456789012:pricingplan/abc"}
---

# List-Pricing-Rules-For-Plan

Lists the pricing rules associated with a specific pricing plan.

This tool retrieve pricing rules associated with a specific pricing plan
If no billing period is provided, the current billing period is used.

The tool returns information about:
- The billing period for which the pricing rule associations are listed.
- The optional pagination token to be used on subsequent calls.
- The ARN of the pricing plan for which associations are listed.
- A list containing pricing rules that are associated with the requested pricing plan

Example: {"pricing_plan_arn": "arn:aws:billingconductor::123456789012:pricingplan/abc"}

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pricing_plan_arn` | string | Yes |  |
| `billing_period` | string | No |  |
| `max_results` | string | No |  |
| `max_pages` | integer | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws billingconductor list-pricing-rules-associated-to-pricing-plan --pricing-plan-arn <pricing_plan_arn> --billing-period <billing_period> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('billingconductor')
response = client.list_pricing_rules_associated_to_pricing_plan(
    PricingPlanArn=pricing_plan_arn,
    BillingPeriod=billing_period,
    MaxResults=max_results,
    NextToken=next_token,
)
```
