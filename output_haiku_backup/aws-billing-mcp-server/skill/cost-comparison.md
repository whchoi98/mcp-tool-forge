---
name: cost-comparison
description: Retrieves AWS cost comparisons between two one-month periods.

Do not use this tool except for comparing the costs of one month to the costs of another month. This tool should not be used for week-over-week or quarter-over-quarter (e.g., comparing Q2 vs. Q1) analysis.

USE THIS TOOL ONLY FOR:
- **Month-to-month cost variance analysis** (e.g., January vs February)
- **Root cause analysis** of cost changes between specific months
- **Detailed cost driver identification** (what exactly caused the cost change)
- **Service-level impact analysis** for month-over-month changes
- **Executive reporting** on monthly cost variances

STRICT LIMITATIONS:
- ONLY compares exactly one month to another month
- Both periods must start on 1st day of month, end on 1st day of next month
- Cannot compare weeks, quarters, or custom periods
- DO NOT USE for general cost analysis or flexible time periods

This tool supports two main operations:
1. getCostAndUsageComparisons: Compare costs between two time periods with flexible grouping and filtering
2. getCostComparisonDrivers: Identify key factors driving cost changes between two time periods

Both operations require:
- BaselineTimePeriod: Earlier time period for comparison (must be exactly one month)
- ComparisonTimePeriod: Later time period for comparison (must be exactly one month)
- MetricForComparison: The cost metric to compare (e.g., BlendedCost, UnblendedCost)

Supported metrics for comparison include:
- AmortizedCost: Costs with upfront and recurring reservation fees spread across the period
- BlendedCost: Average cost of all usage throughout the billing period
- NetAmortizedCost: Amortized cost after discounts
- NetUnblendedCost: Unblended cost after discounts
- NormalizedUsageAmount: Normalized usage amount
- UnblendedCost: Actual costs incurred during the specified period
- UsageQuantity: Usage amounts in their respective units

You can group results by dimensions such as:
- SERVICE: AWS service (e.g., Amazon EC2, Amazon S3)
- LINKED_ACCOUNT: Member accounts in an organization
- REGION: AWS Region
- USAGE_TYPE: Type of usage (e.g., BoxUsage:t2.micro)
- INSTANCE_TYPE: EC2 instance type (e.g., t2.micro, m5.large)
- PLATFORM: Operating system (e.g., Windows, Linux)
- TENANCY: Instance tenancy (e.g., shared, dedicated)
- RECORD_TYPE: Record type (e.g., Usage, Credit, Tax)
- LEGAL_ENTITY_NAME: AWS seller of record

Note:
- Time periods must start and end on the first day of a month, with a duration of exactly one month
- The getCostComparisonDrivers operation automatically includes SERVICE and USAGE_TYPE dimensions
- Data is available for the last 13 months, or up to 38 months if multi-year data is enabled
---

# Cost-Comparison

Retrieves AWS cost comparisons between two one-month periods.

Do not use this tool except for comparing the costs of one month to the costs of another month. This tool should not be used for week-over-week or quarter-over-quarter (e.g., comparing Q2 vs. Q1) analysis.

USE THIS TOOL ONLY FOR:
- **Month-to-month cost variance analysis** (e.g., January vs February)
- **Root cause analysis** of cost changes between specific months
- **Detailed cost driver identification** (what exactly caused the cost change)
- **Service-level impact analysis** for month-over-month changes
- **Executive reporting** on monthly cost variances

STRICT LIMITATIONS:
- ONLY compares exactly one month to another month
- Both periods must start on 1st day of month, end on 1st day of next month
- Cannot compare weeks, quarters, or custom periods
- DO NOT USE for general cost analysis or flexible time periods

This tool supports two main operations:
1. getCostAndUsageComparisons: Compare costs between two time periods with flexible grouping and filtering
2. getCostComparisonDrivers: Identify key factors driving cost changes between two time periods

Both operations require:
- BaselineTimePeriod: Earlier time period for comparison (must be exactly one month)
- ComparisonTimePeriod: Later time period for comparison (must be exactly one month)
- MetricForComparison: The cost metric to compare (e.g., BlendedCost, UnblendedCost)

Supported metrics for comparison include:
- AmortizedCost: Costs with upfront and recurring reservation fees spread across the period
- BlendedCost: Average cost of all usage throughout the billing period
- NetAmortizedCost: Amortized cost after discounts
- NetUnblendedCost: Unblended cost after discounts
- NormalizedUsageAmount: Normalized usage amount
- UnblendedCost: Actual costs incurred during the specified period
- UsageQuantity: Usage amounts in their respective units

You can group results by dimensions such as:
- SERVICE: AWS service (e.g., Amazon EC2, Amazon S3)
- LINKED_ACCOUNT: Member accounts in an organization
- REGION: AWS Region
- USAGE_TYPE: Type of usage (e.g., BoxUsage:t2.micro)
- INSTANCE_TYPE: EC2 instance type (e.g., t2.micro, m5.large)
- PLATFORM: Operating system (e.g., Windows, Linux)
- TENANCY: Instance tenancy (e.g., shared, dedicated)
- RECORD_TYPE: Record type (e.g., Usage, Credit, Tax)
- LEGAL_ENTITY_NAME: AWS seller of record

Note:
- Time periods must start and end on the first day of a month, with a duration of exactly one month
- The getCostComparisonDrivers operation automatically includes SERVICE and USAGE_TYPE dimensions
- Data is available for the last 13 months, or up to 38 months if multi-year data is enabled

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | Yes |  |
| `baseline_start_date` | string | Yes |  |
| `baseline_end_date` | string | Yes |  |
| `comparison_start_date` | string | Yes |  |
| `comparison_end_date` | string | Yes |  |
| `metric_for_comparison` | string | Yes |  |
| `group_by` | string | No |  |
| `filter` | string | No |  |
| `max_results` | string | No |  |
| `billing_view_arn` | string | No |  |

## AWS CLI

```bash
aws ce get-cost-and-usage --time-period <baseline_start_date> --metrics <metric_for_comparison> --granularity <MONTHLY> --group-by <group_by> --filter <filter> --max-results <max_results> --billing-view-arn <billing_view_arn>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_cost_and_usage(
    TimePeriod={'Start': 'baseline_start_date', 'End': 'baseline_end_date'},
    Metrics=['metric_for_comparison'],
    Granularity=MONTHLY,
    GroupBy=group_by,
    Filter=filter,
    MaxResults=max_results,
    BillingViewArn=billing_view_arn,
)
```
