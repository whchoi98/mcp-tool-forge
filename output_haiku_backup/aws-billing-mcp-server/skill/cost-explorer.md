---
name: cost-explorer
description: Retrieves AWS cost and usage data using the Cost Explorer API.

IMPORTANT USAGE GUIDELINES:
- Use UnblendedCost metric by default (not BlendedCost) unless user specifies otherwise
- Exclude record_types 'Credit' and 'Refund' by default unless user requests inclusion
- Choose DAILY granularity for periods <3 months, MONTHLY for longer periods
- Start with high-level dimensions (SERVICE, LINKED_ACCOUNT) before detailed ones
- Always remember that the end_date is exclusive

USE THIS TOOL FOR:
- **Historical cost trends** and spending analysis (any time period)
- **Usage pattern analysis** over time
- **Cost breakdown** by service, account, region, or any dimension
- **Forecasting** future costs and usage
- **Resource-level cost analysis** (last 14 days)
- **Multi-dimensional cost analysis** with complex grouping

## OPERATIONS

1) getCostAndUsage — account-level historical cost/usage
   Required: operation="getCostAndUsage", start_date, end_date, granularity, metrics
   Optional: group_by, filter, next_token, max_pages
   Example: {"operation": "getCostAndUsage", "start_date": "2024-01-01", "end_date": "2024-02-01", "granularity": "DAILY", "metrics": ["UnblendedCost"], "group_by": "[{"Type": "DIMENSION", "Key": "SERVICE"}]"}

2. getCostAndUsageWithResources - Resource-level cost data (limited to last 14 days)
   Required: operation="getCostAndUsageWithResources", filter, granularity, start_date, end_date
   Optional: metrics, group_by
   Notes: RESOURCE_ID must be included in either filter OR group_by parameters. This operation is limited to past 14 days of data from current date. Hourly granularity is only available for EC2-Instances resource-level data. All other resource-level data is available at daily granularity.
   Example: {"operation": "getCostAndUsageWithResources", "start_date": "2025-08-07", "end_date": "2025-08-21", "granularity": "DAILY", "filter": "{"Dimensions": {"Key": "SERVICE", "Values": ["Amazon Elastic Compute Cloud - Compute"]}}", "group_by": "[{"Type": "DIMENSION", "Key": "RESOURCE_ID"}]"}
   Returns: Cost data with resource-level granularity

3. getDimensionValues - List of available values for specified dimension
   Required: operation="getDimensionValues", dimension, start_date, end_date
   Optional: context, search_string, filter, max_results
   Example: {"operation": "getDimensionValues", "dimension": "SERVICE", "start_date": "2024-01-01", "end_date": "2024-02-01"}
   Returns: List of values for specified dimension with automatic pagination

4. getCostForecast - Future cost projections
   Required: operation="getCostForecast", metric, granularity, start_date, end_date
   Optional: filter, prediction_interval_level
   Example: {"operation": "getCostForecast", "metric": "UNBLENDED_COST", "granularity": "MONTHLY", "start_date": "2025-08-22", "end_date": "2025-11-22"}
   Notes: metric value for this operation should be in all caps
   Returns: Cost forecast for specified time period and granularity

5. getUsageForecast - Future usage projections
   Required: operation="getUsageForecast", metric, granularity, start_date, end_date, filter
   Optional: prediction_interval_level
   Example 1: {"operation": "getUsageForecast", "metric": "USAGE_QUANTITY", "granularity": "MONTHLY", "start_date": "2025-08-22", "end_date": "2025-11-22", "filter": "{"Dimensions": {"Key": "USAGE_TYPE_GROUP", "Values": ["EC2-Instance"]}}"}
   Example 2: {"operation": "getUsageForecast", "metric": "USAGE_QUANTITY", "granularity": "MONTHLY", "start_date": "2025-08-22", "end_date": "2025-11-22", "filter": "{"And": [{"Dimensions": {"Key": "SERVICE", "Values": ["Amazon Elastic Compute Cloud - Compute"]}}, {"Dimensions": {"Key": "USAGE_TYPE", "Values": ["BoxUsage:p4de.24xlarge"]}}]}"}
   Example 3: {"operation": "getUsageForecast", "metric": "USAGE_QUANTITY", "granularity": "MONTHLY", "start_date": "2025-08-22", "end_date": "2025-11-22", "filter": "{"Dimensions": {"Key": "USAGE_TYPE", "Values": ["BoxUsage:p4de.24xlarge", "Reservation:p4de.24xlarge", "UnusedBox:p4de.24xlarge"]}}", "group_by": "[{"Type": "DIMENSION", "Key": "REGION"}]"}
   Notes: Valid values for metric is: USAGE_QUANTITY, NORMALIZED_USAGE_AMOUNT. Valid values for granularity is: DAILY, MONTHLY. Filter is REQUIRED and must specify USAGE_TYPE or USAGE_TYPE_GROUP to define what usage units to forecast.
   Returns: Usage forecast for specified time period and granularity

6. getTagsOrValues - Available cost allocation tags or values
   Required: operation="getTagsOrValues"
   Optional: start_date, end_date, search_string, next_token, max_pages
   Example 1: {"operation": "getTagsOrValues"}
   Example 2: {"operation": "getTagsOrValues", "tag_key": "Environment"}
   Returns: List of available cost allocation tags with automatic pagination. If tag values for a particular key are needed, pass the tag key as a parameter.

8. getCostCategories - Available cost categories
   Required: operation="getCostCategories", start_date, end_date
   Optional: search_string, next_token, max_pages
   Example: {"operation": "getCostCategories", "start_date": "2024-01-01", "end_date": "2024-08-01"}
   Returns: List of available cost categories with automatic pagination

9. getSavingsPlansUtilization - Savings Plans utilization data
   Required: operation="getSavingsPlansUtilization", start_date, end_date
   Optional: granularity, filter
   Example: {"operation": "getSavingsPlansUtilization", "granularity": "MONTHLY"}
   Notes: This operation supports only DAILY and MONTHLY granularity
   Returns: Savings Plans utilization for the specified time period

DIMENSION REFERENCE:
- AZ: The Availability Zone (e.g., us-east-1a)
- DATABASE_ENGINE: The Amazon RDS database (e.g., Aurora, MySQL)
- DEPLOYMENT_OPTION: RDS deployment scope (SingleAZ, MultiAZ)
- INSTANCE_TYPE: The EC2 instance type (e.g., m4.xlarge)
- INSTANCE_TYPE_FAMILY: Family of instances (e.g., Compute Optimized, Memory Optimized)
- LINKED_ACCOUNT: AWS member accounts
- OPERATING_SYSTEM: OS type (e.g., Windows, Linux)
- PLATFORM: EC2 operating system
- PURCHASE_TYPE: Reservation type (e.g., On-Demand, Reserved)
- REGION: AWS Region
- SERVICE: AWS service (e.g., Amazon DynamoDB)
- TAG: Cost allocation tag
- TENANCY: EC2 tenancy (shared, dedicated)
- USAGE_TYPE: Usage type (e.g., DataTransfer-In-Bytes)
- RECORD_TYPE: Charge types (e.g., RI fees, usage costs)
---

# Cost-Explorer

Retrieves AWS cost and usage data using the Cost Explorer API.

IMPORTANT USAGE GUIDELINES:
- Use UnblendedCost metric by default (not BlendedCost) unless user specifies otherwise
- Exclude record_types 'Credit' and 'Refund' by default unless user requests inclusion
- Choose DAILY granularity for periods <3 months, MONTHLY for longer periods
- Start with high-level dimensions (SERVICE, LINKED_ACCOUNT) before detailed ones
- Always remember that the end_date is exclusive

USE THIS TOOL FOR:
- **Historical cost trends** and spending analysis (any time period)
- **Usage pattern analysis** over time
- **Cost breakdown** by service, account, region, or any dimension
- **Forecasting** future costs and usage
- **Resource-level cost analysis** (last 14 days)
- **Multi-dimensional cost analysis** with complex grouping

## OPERATIONS

1) getCostAndUsage — account-level historical cost/usage
   Required: operation="getCostAndUsage", start_date, end_date, granularity, metrics
   Optional: group_by, filter, next_token, max_pages
   Example: {"operation": "getCostAndUsage", "start_date": "2024-01-01", "end_date": "2024-02-01", "granularity": "DAILY", "metrics": ["UnblendedCost"], "group_by": "[{"Type": "DIMENSION", "Key": "SERVICE"}]"}

2. getCostAndUsageWithResources - Resource-level cost data (limited to last 14 days)
   Required: operation="getCostAndUsageWithResources", filter, granularity, start_date, end_date
   Optional: metrics, group_by
   Notes: RESOURCE_ID must be included in either filter OR group_by parameters. This operation is limited to past 14 days of data from current date. Hourly granularity is only available for EC2-Instances resource-level data. All other resource-level data is available at daily granularity.
   Example: {"operation": "getCostAndUsageWithResources", "start_date": "2025-08-07", "end_date": "2025-08-21", "granularity": "DAILY", "filter": "{"Dimensions": {"Key": "SERVICE", "Values": ["Amazon Elastic Compute Cloud - Compute"]}}", "group_by": "[{"Type": "DIMENSION", "Key": "RESOURCE_ID"}]"}
   Returns: Cost data with resource-level granularity

3. getDimensionValues - List of available values for specified dimension
   Required: operation="getDimensionValues", dimension, start_date, end_date
   Optional: context, search_string, filter, max_results
   Example: {"operation": "getDimensionValues", "dimension": "SERVICE", "start_date": "2024-01-01", "end_date": "2024-02-01"}
   Returns: List of values for specified dimension with automatic pagination

4. getCostForecast - Future cost projections
   Required: operation="getCostForecast", metric, granularity, start_date, end_date
   Optional: filter, prediction_interval_level
   Example: {"operation": "getCostForecast", "metric": "UNBLENDED_COST", "granularity": "MONTHLY", "start_date": "2025-08-22", "end_date": "2025-11-22"}
   Notes: metric value for this operation should be in all caps
   Returns: Cost forecast for specified time period and granularity

5. getUsageForecast - Future usage projections
   Required: operation="getUsageForecast", metric, granularity, start_date, end_date, filter
   Optional: prediction_interval_level
   Example 1: {"operation": "getUsageForecast", "metric": "USAGE_QUANTITY", "granularity": "MONTHLY", "start_date": "2025-08-22", "end_date": "2025-11-22", "filter": "{"Dimensions": {"Key": "USAGE_TYPE_GROUP", "Values": ["EC2-Instance"]}}"}
   Example 2: {"operation": "getUsageForecast", "metric": "USAGE_QUANTITY", "granularity": "MONTHLY", "start_date": "2025-08-22", "end_date": "2025-11-22", "filter": "{"And": [{"Dimensions": {"Key": "SERVICE", "Values": ["Amazon Elastic Compute Cloud - Compute"]}}, {"Dimensions": {"Key": "USAGE_TYPE", "Values": ["BoxUsage:p4de.24xlarge"]}}]}"}
   Example 3: {"operation": "getUsageForecast", "metric": "USAGE_QUANTITY", "granularity": "MONTHLY", "start_date": "2025-08-22", "end_date": "2025-11-22", "filter": "{"Dimensions": {"Key": "USAGE_TYPE", "Values": ["BoxUsage:p4de.24xlarge", "Reservation:p4de.24xlarge", "UnusedBox:p4de.24xlarge"]}}", "group_by": "[{"Type": "DIMENSION", "Key": "REGION"}]"}
   Notes: Valid values for metric is: USAGE_QUANTITY, NORMALIZED_USAGE_AMOUNT. Valid values for granularity is: DAILY, MONTHLY. Filter is REQUIRED and must specify USAGE_TYPE or USAGE_TYPE_GROUP to define what usage units to forecast.
   Returns: Usage forecast for specified time period and granularity

6. getTagsOrValues - Available cost allocation tags or values
   Required: operation="getTagsOrValues"
   Optional: start_date, end_date, search_string, next_token, max_pages
   Example 1: {"operation": "getTagsOrValues"}
   Example 2: {"operation": "getTagsOrValues", "tag_key": "Environment"}
   Returns: List of available cost allocation tags with automatic pagination. If tag values for a particular key are needed, pass the tag key as a parameter.

8. getCostCategories - Available cost categories
   Required: operation="getCostCategories", start_date, end_date
   Optional: search_string, next_token, max_pages
   Example: {"operation": "getCostCategories", "start_date": "2024-01-01", "end_date": "2024-08-01"}
   Returns: List of available cost categories with automatic pagination

9. getSavingsPlansUtilization - Savings Plans utilization data
   Required: operation="getSavingsPlansUtilization", start_date, end_date
   Optional: granularity, filter
   Example: {"operation": "getSavingsPlansUtilization", "granularity": "MONTHLY"}
   Notes: This operation supports only DAILY and MONTHLY granularity
   Returns: Savings Plans utilization for the specified time period

DIMENSION REFERENCE:
- AZ: The Availability Zone (e.g., us-east-1a)
- DATABASE_ENGINE: The Amazon RDS database (e.g., Aurora, MySQL)
- DEPLOYMENT_OPTION: RDS deployment scope (SingleAZ, MultiAZ)
- INSTANCE_TYPE: The EC2 instance type (e.g., m4.xlarge)
- INSTANCE_TYPE_FAMILY: Family of instances (e.g., Compute Optimized, Memory Optimized)
- LINKED_ACCOUNT: AWS member accounts
- OPERATING_SYSTEM: OS type (e.g., Windows, Linux)
- PLATFORM: EC2 operating system
- PURCHASE_TYPE: Reservation type (e.g., On-Demand, Reserved)
- REGION: AWS Region
- SERVICE: AWS service (e.g., Amazon DynamoDB)
- TAG: Cost allocation tag
- TENANCY: EC2 tenancy (shared, dedicated)
- USAGE_TYPE: Usage type (e.g., DataTransfer-In-Bytes)
- RECORD_TYPE: Charge types (e.g., RI fees, usage costs)

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | Yes |  |
| `start_date` | string | No |  |
| `end_date` | string | No |  |
| `granularity` | string | No |  |
| `metrics` | string | No |  |
| `group_by` | string | No |  |
| `filter` | string | No |  |
| `dimension` | string | No |  |
| `search_string` | string | No |  |
| `max_results` | string | No |  |
| `next_token` | string | No |  |
| `max_pages` | string | No |  |
| `metric` | string | No |  |
| `prediction_interval_level` | integer | No |  |
| `tag_key` | string | No |  |
| `cost_category_name` | string | No |  |

## AWS CLI

```bash
aws ce get-cost-and-usage --start-date <start_date> --end-date <end_date> --granularity <granularity> --metrics <metrics> --group-by <group_by> --filter <filter> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_cost_and_usage(
    StartTime=start_date,
    EndTime=end_date,
    Granularity=granularity,
    Metrics=metrics,
    GroupBy=group_by,
    Filter=filter,
    NextToken=next_token,
)
```
