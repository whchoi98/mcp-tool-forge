---
name: get-cost-and-usage
description: Retrieve AWS cost and usage data.

    This tool retrieves AWS cost and usage data for AWS services during a specified billing period,
    with optional filtering and grouping. It dynamically generates cost reports tailored to specific needs
    by specifying parameters such as granularity, billing period dates, and filter criteria.

    Note: The end_date is treated as inclusive in this tool, meaning if you specify an end_date of
    "2025-01-31", the results will include data for January 31st. This differs from the AWS Cost Explorer
    API which treats end_date as exclusive.

    IMPORTANT: When using UsageQuantity metric, AWS aggregates usage numbers without considering units.
    This makes results meaningless when different usage types have different units (e.g., EC2 compute hours
    vs data transfer GB). For meaningful UsageQuantity results, you MUST be very specific with filtering, including USAGE_TYPE or USAGE_TYPE_GROUP.

    Example: Get monthly costs for EC2 and S3 services in us-east-1 for May 2025
        await get_cost_and_usage(
            ctx=context,
            date_range={
                "start_date": "2025-05-01",
                "end_date": "2025-05-31"
            },
            granularity="MONTHLY",
            group_by={"Type": "DIMENSION", "Key": "SERVICE"},
            filter_expression={
                "And": [
                    {
                        "Dimensions": {
                            "Key": "SERVICE",
                            "Values": ["Amazon Elastic Compute Cloud - Compute", "Amazon Simple Storage Service"],
                            "MatchOptions": ["EQUALS"]
                        }
                    },
                    {
                        "Dimensions": {
                            "Key": "REGION",
                            "Values": ["us-east-1"],
                            "MatchOptions": ["EQUALS"]
                        }
                    }
                ]
            },
            metric="UnblendedCost"
        )

    Example: Get meaningful UsageQuantity for specific EC2 instance usage
        await get_cost_and_usage(
            ctx=context,
            {
            "date_range": {
                "start_date": "2025-05-01",
                "end_date": "2025-05-31"
            },
            "filter_expression": {
                "And": [
                {
                    "Dimensions": {
                    "Values": [
                        "Amazon Elastic Compute Cloud - Compute"
                    ],
                    "Key": "SERVICE",
                    "MatchOptions": [
                        "EQUALS"
                    ]
                    }
                },
                {
                    "Dimensions": {
                    "Values": [
                        "EC2: Running Hours"
                    ],
                    "Key": "USAGE_TYPE_GROUP",
                    "MatchOptions": [
                        "EQUALS"
                    ]
                    }
                }
                ]
            },
            "metric": "UsageQuantity",
            "group_by": "USAGE_TYPE",
            "granularity": "MONTHLY"
            }

    Args:
        ctx: MCP context
        date_range: The billing period start and end dates in YYYY-MM-DD format (end date is inclusive)
        granularity: The granularity at which cost data is aggregated (DAILY, MONTHLY, HOURLY)
        group_by: Either a dictionary with Type and Key, or simply a string key to group by
        filter_expression: Filter criteria as a Python dictionary
        metric: Cost metric to use (UnblendedCost, BlendedCost, etc.)

    Returns:
        Dictionary containing cost report data grouped according to the specified parameters
    
---

# Get Cost And Usage

Retrieve AWS cost and usage data.

    This tool retrieves AWS cost and usage data for AWS services during a specified billing period,
    with optional filtering and grouping. It dynamically generates cost reports tailored to specific needs
    by specifying parameters such as granularity, billing period dates, and filter criteria.

    Note: The end_date is treated as inclusive in this tool, meaning if you specify an end_date of
    "2025-01-31", the results will include data for January 31st. This differs from the AWS Cost Explorer
    API which treats end_date as exclusive.

    IMPORTANT: When using UsageQuantity metric, AWS aggregates usage numbers without considering units.
    This makes results meaningless when different usage types have different units (e.g., EC2 compute hours
    vs data transfer GB). For meaningful UsageQuantity results, you MUST be very specific with filtering, including USAGE_TYPE or USAGE_TYPE_GROUP.

    Example: Get monthly costs for EC2 and S3 services in us-east-1 for May 2025
        await get_cost_and_usage(
            ctx=context,
            date_range={
                "start_date": "2025-05-01",
                "end_date": "2025-05-31"
            },
            granularity="MONTHLY",
            group_by={"Type": "DIMENSION", "Key": "SERVICE"},
            filter_expression={
                "And": [
                    {
                        "Dimensions": {
                            "Key": "SERVICE",
                            "Values": ["Amazon Elastic Compute Cloud - Compute", "Amazon Simple Storage Service"],
                            "MatchOptions": ["EQUALS"]
                        }
                    },
                    {
                        "Dimensions": {
                            "Key": "REGION",
                            "Values": ["us-east-1"],
                            "MatchOptions": ["EQUALS"]
                        }
                    }
                ]
            },
            metric="UnblendedCost"
        )

    Example: Get meaningful UsageQuantity for specific EC2 instance usage
        await get_cost_and_usage(
            ctx=context,
            {
            "date_range": {
                "start_date": "2025-05-01",
                "end_date": "2025-05-31"
            },
            "filter_expression": {
                "And": [
                {
                    "Dimensions": {
                    "Values": [
                        "Amazon Elastic Compute Cloud - Compute"
                    ],
                    "Key": "SERVICE",
                    "MatchOptions": [
                        "EQUALS"
                    ]
                    }
                },
                {
                    "Dimensions": {
                    "Values": [
                        "EC2: Running Hours"
                    ],
                    "Key": "USAGE_TYPE_GROUP",
                    "MatchOptions": [
                        "EQUALS"
                    ]
                    }
                }
                ]
            },
            "metric": "UsageQuantity",
            "group_by": "USAGE_TYPE",
            "granularity": "MONTHLY"
            }

    Args:
        ctx: MCP context
        date_range: The billing period start and end dates in YYYY-MM-DD format (end date is inclusive)
        granularity: The granularity at which cost data is aggregated (DAILY, MONTHLY, HOURLY)
        group_by: Either a dictionary with Type and Key, or simply a string key to group by
        filter_expression: Filter criteria as a Python dictionary
        metric: Cost metric to use (UnblendedCost, BlendedCost, etc.)

    Returns:
        Dictionary containing cost report data grouped according to the specified parameters
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `date_range` | string | Yes |  |
| `granularity` | string | No | The granularity at which cost data is aggregated. Valid values are DAILY, MONTHLY, HOURLY. If not provided, defaults to MONTHLY. |
| `group_by` | string | No | Either a dictionary with Type and Key for grouping costs, or simply a string key to group by (which will default to DIMENSION type). Example dictionary: {'Type': 'DIMENSION', 'Key': 'SERVICE'}. Example string: 'SERVICE'. |
| `filter_expression` | string | No | Filter criteria as a Python dictionary to narrow down AWS costs. Supports filtering by Dimensions (SERVICE, REGION, etc.), Tags, or CostCategories. You can use logical operators (And, Or, Not) for complex filters. MatchOptions validation: For Dimensions, valid values are ['EQUALS', 'CASE_SENSITIVE']. For Tags and CostCategories, valid values are ['EQUALS', 'ABSENT', 'CASE_SENSITIVE'] (defaults to EQUALS and CASE_SENSITIVE). Examples: 1) Simple service filter: {'Dimensions': {'Key': 'SERVICE', 'Values': ['Amazon Elastic Compute Cloud - Compute', 'Amazon Simple Storage Service'], 'MatchOptions': ['EQUALS']}}. 2) Region filter: {'Dimensions': {'Key': 'REGION', 'Values': ['us-east-1'], 'MatchOptions': ['EQUALS']}}. 3) Combined filter: {'And': [{'Dimensions': {'Key': 'SERVICE', 'Values': ['Amazon Elastic Compute Cloud - Compute'], 'MatchOptions': ['EQUALS']}}, {'Dimensions': {'Key': 'REGION', 'Values': ['us-east-1'], 'MatchOptions': ['EQUALS']}}]}. |
| `metric` | string | No | The metric to return in the query. Valid values are AmortizedCost, BlendedCost, NetAmortizedCost, NetUnblendedCost, UnblendedCost, UsageQuantity. IMPORTANT: For UsageQuantity, the service aggregates usage numbers without considering units, making results meaningless when mixing different unit types (e.g., compute hours + data transfer GB). To get meaningful UsageQuantity metrics, you MUST filter by USAGE_TYPE or group by USAGE_TYPE/USAGE_TYPE_GROUP to ensure consistent units. |

## AWS CLI

```bash
aws ce get-cost-and-usage --time-period <date_range> --granularity <granularity> --group-by <group_by> --filter <filter_expression> --metrics <metric>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_cost_and_usage(
    TimePeriod=date_range,
    Granularity=granularity,
    GroupBy=group_by,
    Filter=filter_expression,
    Metrics=metric,
)
```
