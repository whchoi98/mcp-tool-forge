---
name: list-pricing-plans-for-rule
description: Lists the pricing plans associated with a specific pricing rule.

This tool retrieve pricing plans associated with a specific pricing rule
If no billing period is provided, the current billing period is used.

The tool returns information about:
- The billing period for which the pricing rule associations are listed.
- The optional pagination token to be used on subsequent calls.
- The ARN of the pricing rule for which associations are listed.
- The list containing pricing plans that are associated with the requested pricing rule.

Example: {"pricing_rule_arn": "arn:aws:billingconductor::123456789012:pricingrule/abc"}
---

# List-Pricing-Plans-For-Rule

Lists the pricing plans associated with a specific pricing rule.

This tool retrieve pricing plans associated with a specific pricing rule
If no billing period is provided, the current billing period is used.

The tool returns information about:
- The billing period for which the pricing rule associations are listed.
- The optional pagination token to be used on subsequent calls.
- The ARN of the pricing rule for which associations are listed.
- The list containing pricing plans that are associated with the requested pricing rule.

Example: {"pricing_rule_arn": "arn:aws:billingconductor::123456789012:pricingrule/abc"}

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pricing_rule_arn` | string | Yes |  |
| `billing_period` | string | No |  |
| `max_results` | string | No |  |
| `max_pages` | integer | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws billingconductor list-pricing-plans-associated-with-pricing-rule --pricing-rule-arn <pricing_rule_arn> --billing-period <billing_period> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('billingconductor')
response = client.list_pricing_plans_associated_with_pricing_rule(
    PricingRuleArn=pricing_rule_arn,
    BillingPeriod=billing_period,
    MaxResults=max_results,
    NextToken=next_token,
)
```
