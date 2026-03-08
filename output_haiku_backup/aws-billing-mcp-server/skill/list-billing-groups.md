---
name: list-billing-groups
description: Retrieves a list of billing groups from AWS Billing Conductor.

This tool retrieve billing groups for a given billing period.
If no billing period is provided, the current billing period is used.

The tool returns information about:
- Billing group ARN, name, and description
- Billing group type (STANDARD or TRANSFER_BILLING)
- Billing group status (ACTIVE, PRIMARY_ACCOUNT_MISSING, or PENDING)
- Primary account ID
- Computation preference (pricing plan ARN)
- Account grouping settings (auto-associate, responsibility transfer ARN)
- Group size (number of member accounts)
- Creation and last modified timestamps

You can filter billing groups by:
- ARNs: Filter by specific billing group ARNs
- Names: Filter by billing group name (supports STARTS_WITH search)
- Statuses: Filter by status (ACTIVE, PRIMARY_ACCOUNT_MISSING, PENDING)
- Billing group types: Filter by type (STANDARD, TRANSFER_BILLING)
- Primary account IDs: Filter by primary account ID
- Pricing plan: Filter by pricing plan ARN
- Auto-associate: Filter by auto-associate setting
- Responsibility transfer ARNs: Filter by responsibility transfer ARNs

The tool paginates through results up to max_pages pages (default 10).
If more results are available after reaching the page limit, a next_token is returned.
Pass the next_token back to this tool to continue fetching from where you left off.

Example 1: {"billing_period": "2025-01"}
Example 2 (with filter): {"filters": "{"Statuses": ["ACTIVE"], "BillingGroupTypes": ["STANDARD"]}", "billing_period": "2025-01"}
---

# List-Billing-Groups

Retrieves a list of billing groups from AWS Billing Conductor.

This tool retrieve billing groups for a given billing period.
If no billing period is provided, the current billing period is used.

The tool returns information about:
- Billing group ARN, name, and description
- Billing group type (STANDARD or TRANSFER_BILLING)
- Billing group status (ACTIVE, PRIMARY_ACCOUNT_MISSING, or PENDING)
- Primary account ID
- Computation preference (pricing plan ARN)
- Account grouping settings (auto-associate, responsibility transfer ARN)
- Group size (number of member accounts)
- Creation and last modified timestamps

You can filter billing groups by:
- ARNs: Filter by specific billing group ARNs
- Names: Filter by billing group name (supports STARTS_WITH search)
- Statuses: Filter by status (ACTIVE, PRIMARY_ACCOUNT_MISSING, PENDING)
- Billing group types: Filter by type (STANDARD, TRANSFER_BILLING)
- Primary account IDs: Filter by primary account ID
- Pricing plan: Filter by pricing plan ARN
- Auto-associate: Filter by auto-associate setting
- Responsibility transfer ARNs: Filter by responsibility transfer ARNs

The tool paginates through results up to max_pages pages (default 10).
If more results are available after reaching the page limit, a next_token is returned.
Pass the next_token back to this tool to continue fetching from where you left off.

Example 1: {"billing_period": "2025-01"}
Example 2 (with filter): {"filters": "{"Statuses": ["ACTIVE"], "BillingGroupTypes": ["STANDARD"]}", "billing_period": "2025-01"}

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `billing_period` | string | No |  |
| `filters` | string | No |  |
| `max_pages` | integer | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws billingconductor list-billing-groups --billing-period <billing_period> --filters <filters> --max-results <max_pages> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('billingconductor')
response = client.list_billing_groups(
    BillingPeriod=billing_period,
    Filters=filters,
    MaxResults=max_pages,
    NextToken=next_token,
)
```
