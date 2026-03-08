---
name: list-custom-line-items
description: Retrieves a list of custom line items (FFLIs) from AWS Billing Conductor.

Custom line items let you allocate costs and discounts to designated AWS accounts within a
billing group. Common use cases include allocating support fees, shared service costs, managed
service fees, taxes, credits, and distributing RI/Savings Plans savings.

This tool retrieve custom line items for a given billing period.
If no billing period is provided, the current billing period is used.

The tool returns information about:
- Custom line item ARN, name, and description
- Account ID, billing group ARN
- Charge details (type: CREDIT or FEE, flat or percentage)
- Computation rule (CONSOLIDATED or ITEMIZED)
- Currency code, association size, product code
- Presentation details, creation and last modified timestamps

You can filter custom line items by:
- AccountIds: Filter by AWS account IDs (up to 30)
- Arns: Filter by specific custom line item ARNs (up to 100)
- BillingGroups: Filter by billing group ARNs (up to 100)
- Names: Filter by custom line item names (up to 100)

Example 1: {"billing_period": "2025-01"}
Example 2 (with filter): {"filters": "{"Names": ["MyCustomLineItem"]}", "billing_period": "2025-01"}
---

# List-Custom-Line-Items

Retrieves a list of custom line items (FFLIs) from AWS Billing Conductor.

Custom line items let you allocate costs and discounts to designated AWS accounts within a
billing group. Common use cases include allocating support fees, shared service costs, managed
service fees, taxes, credits, and distributing RI/Savings Plans savings.

This tool retrieve custom line items for a given billing period.
If no billing period is provided, the current billing period is used.

The tool returns information about:
- Custom line item ARN, name, and description
- Account ID, billing group ARN
- Charge details (type: CREDIT or FEE, flat or percentage)
- Computation rule (CONSOLIDATED or ITEMIZED)
- Currency code, association size, product code
- Presentation details, creation and last modified timestamps

You can filter custom line items by:
- AccountIds: Filter by AWS account IDs (up to 30)
- Arns: Filter by specific custom line item ARNs (up to 100)
- BillingGroups: Filter by billing group ARNs (up to 100)
- Names: Filter by custom line item names (up to 100)

Example 1: {"billing_period": "2025-01"}
Example 2 (with filter): {"filters": "{"Names": ["MyCustomLineItem"]}", "billing_period": "2025-01"}

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `billing_period` | string | No |  |
| `filters` | string | No |  |
| `max_pages` | integer | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws billingconductor list-custom-line-items --billing-period <billing_period> --filters <filters> --max-results <max_pages> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('billingconductor')
response = client.list_custom_line_items(
    BillingPeriod=billing_period,
    Filters=filters,
    MaxResults=max_pages,
    NextToken=next_token,
)
```
