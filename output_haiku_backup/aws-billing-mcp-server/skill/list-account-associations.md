---
name: list-account-associations
description: Lists linked accounts associated with the payer account from AWS Billing Conductor.

This tool retrieve linked accounts for a given billing period.
If no billing period is provided, the current billing period is used.

The tool returns information about each linked account:
- Account ID
- Account name
- Account email
- Billing group ARN (if associated to a billing group)

You can filter account associations by:
- AccountId: Filter by a specific AWS account ID
- AccountIds: Filter by a list of AWS account IDs (up to 30)
- Association: Filter by association status:
  - MONITORED: linked accounts associated to billing groups
  - UNMONITORED: linked accounts not associated to billing groups
  - Billing Group ARN: linked accounts associated to a specific billing group

The tool paginates through results up to max_pages pages (default 10).
If more results are available after reaching the page limit, a next_token is returned.
Pass the next_token back to this tool to continue fetching from where you left off.

Example 1: {"billing_period": "2025-01"}
Example 2 (monitored only): {"filters": "{"Association": "MONITORED"}", "billing_period": "2025-01"}
Example 3 (by account IDs): {"filters": "{"AccountIds": ["123456789012", "234567890123"]}"}
---

# List-Account-Associations

Lists linked accounts associated with the payer account from AWS Billing Conductor.

This tool retrieve linked accounts for a given billing period.
If no billing period is provided, the current billing period is used.

The tool returns information about each linked account:
- Account ID
- Account name
- Account email
- Billing group ARN (if associated to a billing group)

You can filter account associations by:
- AccountId: Filter by a specific AWS account ID
- AccountIds: Filter by a list of AWS account IDs (up to 30)
- Association: Filter by association status:
  - MONITORED: linked accounts associated to billing groups
  - UNMONITORED: linked accounts not associated to billing groups
  - Billing Group ARN: linked accounts associated to a specific billing group

The tool paginates through results up to max_pages pages (default 10).
If more results are available after reaching the page limit, a next_token is returned.
Pass the next_token back to this tool to continue fetching from where you left off.

Example 1: {"billing_period": "2025-01"}
Example 2 (monitored only): {"filters": "{"Association": "MONITORED"}", "billing_period": "2025-01"}
Example 3 (by account IDs): {"filters": "{"AccountIds": ["123456789012", "234567890123"]}"}

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `billing_period` | string | No |  |
| `filters` | string | No |  |
| `max_pages` | integer | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws billingconductor list-account-associations --billing-period <billing_period> --filters <filters> --max-results <max_pages> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('billingconductor')
response = client.list_account_associations(
    BillingPeriod=billing_period,
    Filters=filters,
    MaxResults=max_pages,
    NextToken=next_token,
)
```
