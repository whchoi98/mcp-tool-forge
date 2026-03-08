---
name: list-billing-group-cost-reports
description: Retrieves a summary report of actual AWS charges and calculated AWS charges
based on the associated pricing plan of a billing group.

This tool retrieve cost reports for billing groups.
If no billing period is provided, the current billing period is used.

The tool returns cost report information for each billing group:
- Billing group ARN
- AWS cost (actual AWS charges)
- Proforma cost (hypothetical charges based on the associated pricing plan)
- Margin (billing group margin)
- Margin percentage (percentage of billing group margin)
- Currency (displayed currency)

You can filter cost reports by:
- BillingGroupArns: Filter by specific billing group ARNs (1 to 100 ARNs)

Example 1: {"billing_period": "2025-01"}
Example 2 (with filter): {"filters": "{"BillingGroupArns": ["arn:aws:billingconductor::123456789012:billinggroup/abc"]}", "billing_period": "2025-01"}
---

# List-Billing-Group-Cost-Reports

Retrieves a summary report of actual AWS charges and calculated AWS charges
based on the associated pricing plan of a billing group.

This tool retrieve cost reports for billing groups.
If no billing period is provided, the current billing period is used.

The tool returns cost report information for each billing group:
- Billing group ARN
- AWS cost (actual AWS charges)
- Proforma cost (hypothetical charges based on the associated pricing plan)
- Margin (billing group margin)
- Margin percentage (percentage of billing group margin)
- Currency (displayed currency)

You can filter cost reports by:
- BillingGroupArns: Filter by specific billing group ARNs (1 to 100 ARNs)

Example 1: {"billing_period": "2025-01"}
Example 2 (with filter): {"filters": "{"BillingGroupArns": ["arn:aws:billingconductor::123456789012:billinggroup/abc"]}", "billing_period": "2025-01"}

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `billing_period` | string | No |  |
| `filters` | string | No |  |
| `max_pages` | integer | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws ce get-cost-and-usage-with-resources --time-period <billing_period> --filter <filters> --max-results <max_pages> --next-page-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_cost_and_usage_with_resources(
    TimePeriod=billing_period,
    Filter=filters,
    MaxResults=max_pages,
    NextPageToken=next_token,
)
```
