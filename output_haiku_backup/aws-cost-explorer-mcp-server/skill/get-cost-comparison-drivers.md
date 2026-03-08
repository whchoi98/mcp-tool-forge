---
name: get-cost-comparison-drivers
description: Analyze what drove cost changes between two time periods.

    This tool provides detailed analysis of the TOP 10 most significant cost drivers
    that caused changes between periods. AWS returns only the most impactful drivers
    to focus on the changes that matter most for cost optimization.

    The tool provides rich insights including:
    - Top 10 most significant cost drivers across all services (or filtered subset)
    - Specific usage types that drove changes (e.g., "BoxUsage:c5.large", "NatGateway-Hours")
    - Multiple driver types: usage changes, savings plan impacts, enterprise discounts, support fees
    - Both cost and usage quantity changes with units (hours, GB-months, etc.)
    - Context about what infrastructure components changed
    - Detailed breakdown of usage patterns vs pricing changes

    Can be used with or without filters:
    - Without filters: Shows top 10 cost drivers across ALL services
    - With filters: Shows top 10 cost drivers within the filtered scope
    - Multiple services: Can filter to multiple services and get top 10 within that scope

    Both periods must be exactly one month and start/end on the first day of a month.

    Important requirements:
    - Both periods must be exactly one month duration
    - Dates must start and end on the first day of a month (e.g., 2025-01-01 to 2025-02-01)
    - Maximum lookback of 13 months (38 months if multi-year data enabled)
    - Start dates must be equal to or no later than current date
    - Results limited to top 10 most significant drivers (no pagination)

    Example: Analyze top 10 cost drivers across all services
        await get_cost_comparison_drivers(
            ctx=context,
            baseline_date_range={
                "start_date": "2024-12-01",  # December 2024
                "end_date": "2025-01-01"
            },
            comparison_date_range={
                "start_date": "2025-01-01",  # January 2025
                "end_date": "2025-02-01"
            },
            metric_for_comparison="UnblendedCost",
            group_by={"Type": "DIMENSION", "Key": "SERVICE"}
            # No filter = top 10 drivers across all services
        )

    Example: Analyze top 10 cost drivers for specific services
        await get_cost_comparison_drivers(
            ctx=context,
            baseline_date_range={
                "start_date": "2024-12-01",
                "end_date": "2025-01-01"
            },
            comparison_date_range={
                "start_date": "2025-01-01",
                "end_date": "2025-02-01"
            },
            metric_for_comparison="UnblendedCost",
            group_by={"Type": "DIMENSION", "Key": "SERVICE"},
            filter_expression={
                "Dimensions": {
                    "Key": "SERVICE",
                    "Values": ["Amazon Elastic Compute Cloud - Compute", "Amazon Simple Storage Service"],
                    "MatchOptions": ["EQUALS"]
                }
            }
        )

    Args:
        ctx: MCP context
        baseline_date_range: The reference period for comparison (exactly one month)
        comparison_date_range: The comparison period (exactly one month)
        metric_for_comparison: Cost metric to analyze drivers for (UnblendedCost, BlendedCost, etc.)
        group_by: Either a dictionary with Type and Key, or simply a string key to group by
        filter_expression: Filter criteria as a Python dictionary

    Returns:
        with specific usage types, usage quantity changes, driver types (savings plans, discounts, usage changes, support fees), and contextual information
    
---

# Get Cost Comparison Drivers

Analyze what drove cost changes between two time periods.

    This tool provides detailed analysis of the TOP 10 most significant cost drivers
    that caused changes between periods. AWS returns only the most impactful drivers
    to focus on the changes that matter most for cost optimization.

    The tool provides rich insights including:
    - Top 10 most significant cost drivers across all services (or filtered subset)
    - Specific usage types that drove changes (e.g., "BoxUsage:c5.large", "NatGateway-Hours")
    - Multiple driver types: usage changes, savings plan impacts, enterprise discounts, support fees
    - Both cost and usage quantity changes with units (hours, GB-months, etc.)
    - Context about what infrastructure components changed
    - Detailed breakdown of usage patterns vs pricing changes

    Can be used with or without filters:
    - Without filters: Shows top 10 cost drivers across ALL services
    - With filters: Shows top 10 cost drivers within the filtered scope
    - Multiple services: Can filter to multiple services and get top 10 within that scope

    Both periods must be exactly one month and start/end on the first day of a month.

    Important requirements:
    - Both periods must be exactly one month duration
    - Dates must start and end on the first day of a month (e.g., 2025-01-01 to 2025-02-01)
    - Maximum lookback of 13 months (38 months if multi-year data enabled)
    - Start dates must be equal to or no later than current date
    - Results limited to top 10 most significant drivers (no pagination)

    Example: Analyze top 10 cost drivers across all services
        await get_cost_comparison_drivers(
            ctx=context,
            baseline_date_range={
                "start_date": "2024-12-01",  # December 2024
                "end_date": "2025-01-01"
            },
            comparison_date_range={
                "start_date": "2025-01-01",  # January 2025
                "end_date": "2025-02-01"
            },
            metric_for_comparison="UnblendedCost",
            group_by={"Type": "DIMENSION", "Key": "SERVICE"}
            # No filter = top 10 drivers across all services
        )

    Example: Analyze top 10 cost drivers for specific services
        await get_cost_comparison_drivers(
            ctx=context,
            baseline_date_range={
                "start_date": "2024-12-01",
                "end_date": "2025-01-01"
            },
            comparison_date_range={
                "start_date": "2025-01-01",
                "end_date": "2025-02-01"
            },
            metric_for_comparison="UnblendedCost",
            group_by={"Type": "DIMENSION", "Key": "SERVICE"},
            filter_expression={
                "Dimensions": {
                    "Key": "SERVICE",
                    "Values": ["Amazon Elastic Compute Cloud - Compute", "Amazon Simple Storage Service"],
                    "MatchOptions": ["EQUALS"]
                }
            }
        )

    Args:
        ctx: MCP context
        baseline_date_range: The reference period for comparison (exactly one month)
        comparison_date_range: The comparison period (exactly one month)
        metric_for_comparison: Cost metric to analyze drivers for (UnblendedCost, BlendedCost, etc.)
        group_by: Either a dictionary with Type and Key, or simply a string key to group by
        filter_expression: Filter criteria as a Python dictionary

    Returns:
        with specific usage types, usage quantity changes, driver types (savings plans, discounts, usage changes, support fees), and contextual information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `baseline_date_range` | string | Yes |  |
| `comparison_date_range` | string | Yes |  |
| `metric_for_comparison` | string | No | The cost and usage metric to analyze drivers for. Valid values are AmortizedCost, BlendedCost, NetAmortizedCost, NetUnblendedCost, UnblendedCost, UsageQuantity. |
| `group_by` | string | No | Either a dictionary with Type and Key for grouping driver analysis, or simply a string key to group by (which will default to DIMENSION type). Example dictionary: {'Type': 'DIMENSION', 'Key': 'SERVICE'}. Example string: 'SERVICE'. |
| `filter_expression` | string | No | Filter criteria as a Python dictionary to narrow down AWS cost driver analysis. Supports filtering by Dimensions (SERVICE, REGION, etc.), Tags, or CostCategories. You can use logical operators (And, Or, Not) for complex filters. Same format as get_cost_and_usage filter_expression. |

## AWS CLI

```bash
aws ce get-cost-and-usage --time-period <baseline_date_range> --metrics <metric_for_comparison> --group-by <group_by> --filter <filter_expression>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_cost_and_usage(
    TimePeriod={'Start': 'baseline_date_range', 'End': 'baseline_date_range'},
    Metrics=['metric_for_comparison'],
    GroupBy=group_by,
    Filter=filter_expression,
)
```
