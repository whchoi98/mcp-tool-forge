---
name: bcm-pricing-calc
description: Allows working with workload estimates using the AWS Billing and Cost Management Pricing Calculator API.

IMPORTANT USAGE GUIDELINES:
- Always first check the rate preference setting for the authorized principal by calling the get_preferences operation.
- DO NOT state assumptions about Free Tier API

USE THIS TOOL FOR:
- Listing available **workload estimates** for the logged in account.
- **Filter list of available workload estimates** using name, status, created date, or expiration date.
- Get **details of a workload estimate**.
- Get the list of **services, usage type, operation, and usage amount** modeled within a workload estimate.
- Get **rate preferences** set for Pricing Calculator. These rate preferences denote what rate preferences can be used by each account type in your organization.

## OPERATIONS

1) list_workload_estimates - list of available workload estimates
   Required: operation="list_workload_estimates"
   Optional: created_after, created_before, expires_after, expires_before, status_filter, name_filter, name_match_option, next_token, max_results
   Returns: List of all workload estimates for the account.

2) get_workload_estimate - get details of a workload estimate
   Required: operation="get_workload_estimate", identifier
   Returns: Details of a specific workload estimate.

3) list_workload_estimate_usage - list of modeled usage lines within a workload estimate
   Required: operation="get_workload_estimate", identifier
   Optional: usage_account_id_filter, service_code_filter, usage_type_filter, operation_filter, location_filter, usage_group_filter, next_token, max_results
   Returns: List of usage associated with a workload estimate.

4) get_preferences - get the rate preferences available to an account
   Required: operation="get_preferences"
   Returns: Retrieves the current preferences for AWS Billing and Cost Management Pricing Calculator.

---

# Bcm-Pricing-Calc

Allows working with workload estimates using the AWS Billing and Cost Management Pricing Calculator API.

IMPORTANT USAGE GUIDELINES:
- Always first check the rate preference setting for the authorized principal by calling the get_preferences operation.
- DO NOT state assumptions about Free Tier API

USE THIS TOOL FOR:
- Listing available **workload estimates** for the logged in account.
- **Filter list of available workload estimates** using name, status, created date, or expiration date.
- Get **details of a workload estimate**.
- Get the list of **services, usage type, operation, and usage amount** modeled within a workload estimate.
- Get **rate preferences** set for Pricing Calculator. These rate preferences denote what rate preferences can be used by each account type in your organization.

## OPERATIONS

1) list_workload_estimates - list of available workload estimates
   Required: operation="list_workload_estimates"
   Optional: created_after, created_before, expires_after, expires_before, status_filter, name_filter, name_match_option, next_token, max_results
   Returns: List of all workload estimates for the account.

2) get_workload_estimate - get details of a workload estimate
   Required: operation="get_workload_estimate", identifier
   Returns: Details of a specific workload estimate.

3) list_workload_estimate_usage - list of modeled usage lines within a workload estimate
   Required: operation="get_workload_estimate", identifier
   Optional: usage_account_id_filter, service_code_filter, usage_type_filter, operation_filter, location_filter, usage_group_filter, next_token, max_results
   Returns: List of usage associated with a workload estimate.

4) get_preferences - get the rate preferences available to an account
   Required: operation="get_preferences"
   Returns: Retrieves the current preferences for AWS Billing and Cost Management Pricing Calculator.


## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | Yes |  |
| `identifier` | string | No |  |
| `created_after` | string | No |  |
| `created_before` | string | No |  |
| `expires_after` | string | No |  |
| `expires_before` | string | No |  |
| `status_filter` | string | No |  |
| `name_filter` | string | No |  |
| `name_match_option` | string | No |  |
| `usage_account_id_filter` | string | No |  |
| `service_code_filter` | string | No |  |
| `usage_type_filter` | string | No |  |
| `operation_filter` | string | No |  |
| `location_filter` | string | No |  |
| `usage_group_filter` | string | No |  |
| `next_token` | string | No |  |
| `max_results` | string | No |  |
| `max_pages` | string | No |  |

## AWS CLI

```bash
aws pricing get-products --service-code <service_code_filter> --usage-type <usage_type_filter> --location <location_filter> --next-token <next_token> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('pricing')
response = client.get_products(
    ServiceCode=service_code_filter,
    UsageType=usage_type_filter,
    Location=location_filter,
    NextToken=next_token,
    MaxResults=max_results,
)
```
