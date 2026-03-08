---
name: budgets
description: Retrieves AWS budget information using the AWS Budgets API.

This tool uses the DescribeBudgets API to retrieve all budgets for an account.

The API returns information about:
- Budget names, types, and time periods
- Budget limits (amount and unit)
- Current actual spend
- Forecasted spend
- Cost filters applied to budgets

With this information, you can determine which budgets have been exceeded or are projected to exceed their limits.

The tool automatically retrieves the AWS account ID of the calling identity or uses the provided account_id.
---

# Budgets

Retrieves AWS budget information using the AWS Budgets API.

This tool uses the DescribeBudgets API to retrieve all budgets for an account.

The API returns information about:
- Budget names, types, and time periods
- Budget limits (amount and unit)
- Current actual spend
- Forecasted spend
- Cost filters applied to budgets

With this information, you can determine which budgets have been exceeded or are projected to exceed their limits.

The tool automatically retrieves the AWS account ID of the calling identity or uses the provided account_id.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `budget_name` | string | No |  |
| `max_results` | integer | No |  |
| `account_id` | string | No |  |

## AWS CLI

```bash
aws budgets describe-budgets --account-id <account_id> --max-results <max_results> --budget-name <budget_name>
```

## boto3

```python
import boto3

client = boto3.client('budgets')
response = client.describe_budgets(
    AccountId=account_id,
    MaxResults=max_results,
    BudgetName=budget_name,
)
```
