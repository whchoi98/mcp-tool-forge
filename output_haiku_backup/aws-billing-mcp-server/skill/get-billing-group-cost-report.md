---
name: get-billing-group-cost-report
description: Retrieves the margin summary report for a specific billing group, which includes
the AWS cost and charged amount (pro forma cost) broken down by attributes such as AWS service
name or billing period.

This tool retrieve detailed cost reports for a
single billing group, optionally broken down by product name and/or billing period.

The tool returns margin summary report results for the billing group:
- Billing group ARN
- Attributes (key-value pairs for grouping, e.g., PRODUCT_NAME: "S3", BILLING_PERIOD: "Nov 2023")
- AWS cost (actual AWS charges)
- Proforma cost (hypothetical charges based on the associated pricing plan)
- Margin (billing group margin)
- Margin percentage (percentage of billing group margin)
- Currency (displayed currency)

You can customize the report by:
- BillingPeriodRange: JSON string specifying a time range (up to 12 months)
- GroupBy: JSON array string with values "PRODUCT_NAME" and/or "BILLING_PERIOD"

Example 1: {"arn": "arn:aws:billingconductor::123456789012:billinggroup/abc", "group_by": "["PRODUCT_NAME"]"}
Example 2: {"arn": "arn:aws:billingconductor::123456789012:billinggroup/abc", "group_by": "["PRODUCT_NAME", "BILLING_PERIOD"]", "billing_period_range": "{"InclusiveStartBillingPeriod": "2025-01", "ExclusiveEndBillingPeriod": "2025-07"}"}
---

# Get-Billing-Group-Cost-Report

Retrieves the margin summary report for a specific billing group, which includes
the AWS cost and charged amount (pro forma cost) broken down by attributes such as AWS service
name or billing period.

This tool retrieve detailed cost reports for a
single billing group, optionally broken down by product name and/or billing period.

The tool returns margin summary report results for the billing group:
- Billing group ARN
- Attributes (key-value pairs for grouping, e.g., PRODUCT_NAME: "S3", BILLING_PERIOD: "Nov 2023")
- AWS cost (actual AWS charges)
- Proforma cost (hypothetical charges based on the associated pricing plan)
- Margin (billing group margin)
- Margin percentage (percentage of billing group margin)
- Currency (displayed currency)

You can customize the report by:
- BillingPeriodRange: JSON string specifying a time range (up to 12 months)
- GroupBy: JSON array string with values "PRODUCT_NAME" and/or "BILLING_PERIOD"

Example 1: {"arn": "arn:aws:billingconductor::123456789012:billinggroup/abc", "group_by": "["PRODUCT_NAME"]"}
Example 2: {"arn": "arn:aws:billingconductor::123456789012:billinggroup/abc", "group_by": "["PRODUCT_NAME", "BILLING_PERIOD"]", "billing_period_range": "{"InclusiveStartBillingPeriod": "2025-01", "ExclusiveEndBillingPeriod": "2025-07"}"}

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `arn` | string | Yes |  |
| `billing_period_range` | string | No |  |
| `group_by` | string | No |  |
| `max_pages` | integer | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws ce get-cost-and-usage-with-resources --filter <arn> --granularity <billing_period_range> --group-by <group_by> --max-results <max_pages> --next-page-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_cost_and_usage_with_resources(
    Filter=arn,
    Granularity=billing_period_range,
    GroupBy=group_by,
    MaxResults=max_pages,
    NextPageToken=next_token,
)
```
