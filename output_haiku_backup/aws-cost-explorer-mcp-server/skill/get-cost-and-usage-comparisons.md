---
name: get-cost-and-usage-comparisons
description: Compare AWS costs and usage between two time periods.

    This tool compares cost and usage data between a baseline period and a comparison period,
    providing percentage changes and absolute differences. Both periods must be exactly one month
    and start/end on the first day of a month. The tool also provides detailed cost drivers
    when available, showing what specific factors contributed to cost changes.

    Important requirements:
    - Both periods must be exactly one month duration
    - Dates must start and end on the first day of a month (e.g., 2025-01-01 to 2025-02-01)
    - Maximum lookback of 13 months (38 months if multi-year data enabled)
    - Start dates must be equal to or no later than current date

    Example: Compare January 2025 vs December 2024 EC2 costs
        await get_cost_and_usage_comparisons(
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
            group_by={"Type": "DIMENSION", "Key": "SERVICE"},
            filter_expression={
                "Dimensions": {
                    "Key": "SERVICE",
                    "Values": ["Amazon Elastic Compute Cloud - Compute"],
                    "MatchOptions": ["EQUALS"]
                }
            }
        )

    Args:
        ctx: MCP context
        baseline_date_range: The reference period for comparison (exactly one month)
        comparison_date_range: The comparison period (exactly one month)
        metric_for_comparison: Cost metric to compare (UnblendedCost, BlendedCost, etc.)
        group_by: Either a dictionary with Type and Key, or simply a string key to group by
        filter_expression: Filter criteria as a Python dictionary

    Returns:
        Dictionary containing comparison data with percentage changes, absolute differences,
        and detailed cost drivers when available
    
---

# Get Cost And Usage Comparisons

Compare AWS costs and usage between two time periods.

    This tool compares cost and usage data between a baseline period and a comparison period,
    providing percentage changes and absolute differences. Both periods must be exactly one month
    and start/end on the first day of a month. The tool also provides detailed cost drivers
    when available, showing what specific factors contributed to cost changes.

    Important requirements:
    - Both periods must be exactly one month duration
    - Dates must start and end on the first day of a month (e.g., 2025-01-01 to 2025-02-01)
    - Maximum lookback of 13 months (38 months if multi-year data enabled)
    - Start dates must be equal to or no later than current date

    Example: Compare January 2025 vs December 2024 EC2 costs
        await get_cost_and_usage_comparisons(
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
            group_by={"Type": "DIMENSION", "Key": "SERVICE"},
            filter_expression={
                "Dimensions": {
                    "Key": "SERVICE",
                    "Values": ["Amazon Elastic Compute Cloud - Compute"],
                    "MatchOptions": ["EQUALS"]
                }
            }
        )

    Args:
        ctx: MCP context
        baseline_date_range: The reference period for comparison (exactly one month)
        comparison_date_range: The comparison period (exactly one month)
        metric_for_comparison: Cost metric to compare (UnblendedCost, BlendedCost, etc.)
        group_by: Either a dictionary with Type and Key, or simply a string key to group by
        filter_expression: Filter criteria as a Python dictionary

    Returns:
        Dictionary containing comparison data with percentage changes, absolute differences,
        and detailed cost drivers when available
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `baseline_date_range` | string | Yes |  |
| `comparison_date_range` | string | Yes |  |
| `metric_for_comparison` | string | No | The cost and usage metric to compare. Valid values are AmortizedCost, BlendedCost, NetAmortizedCost, NetUnblendedCost, UnblendedCost, UsageQuantity. |
| `group_by` | string | No | Either a dictionary with Type and Key for grouping comparisons, or simply a string key to group by (which will default to DIMENSION type). Example dictionary: {'Type': 'DIMENSION', 'Key': 'SERVICE'}. Example string: 'SERVICE'. |
| `filter_expression` | string | No | Filter criteria as a Python dictionary to narrow down AWS cost comparisons. Supports filtering by Dimensions (SERVICE, REGION, etc.), Tags, or CostCategories. You can use logical operators (And, Or, Not) for complex filters. Same format as get_cost_and_usage filter_expression. |

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
    Metrics=metric_for_comparison,
    GroupBy=group_by,
    Filter=filter_expression,
)
```
