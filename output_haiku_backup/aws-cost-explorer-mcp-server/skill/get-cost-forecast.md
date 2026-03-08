---
name: get-cost-forecast
description: Retrieve AWS cost forecasts based on historical usage patterns.

    This tool generates cost forecasts for future periods using AWS Cost Explorer's machine learning models.
    Forecasts are based on your historical usage patterns and can help with budget planning and cost optimization.

    Important granularity limits:
    - DAILY forecasts: Maximum 3 months into the future
    - MONTHLY forecasts: Maximum 12 months into the future

    Note: The forecast start date must be equal to or no later than the current date, while the end date
    must be in the future. AWS automatically uses available historical data to generate forecasts.
    Forecasts return total costs and cannot be grouped by dimensions like services or regions.

    Example: Get monthly cost forecast for EC2 services for next quarter
        await get_cost_forecast(
            ctx=context,
            date_range={
                "start_date": "2025-06-19",  # Today or earlier
                "end_date": "2025-09-30"     # Future date
            },
            granularity="MONTHLY",
            filter_expression={
                "Dimensions": {
                    "Key": "SERVICE",
                    "Values": ["Amazon Elastic Compute Cloud - Compute"],
                    "MatchOptions": ["EQUALS"]
                }
            },
            metric="UNBLENDED_COST",
            prediction_interval_level=80
        )

    Args:
        ctx: MCP context
        date_range: The forecast period dates in YYYY-MM-DD format (start_date <= today, end_date > today)
        granularity: The granularity at which forecast data is aggregated (DAILY, MONTHLY)
        filter_expression: Filter criteria as a Python dictionary
        metric: Cost metric to forecast (UNBLENDED_COST, AMORTIZED_COST, etc.)
        prediction_interval_level: Confidence level for prediction intervals (80 or 95)

    Returns:
        Dictionary containing forecast data with confidence intervals and metadata
    
---

# Get Cost Forecast

Retrieve AWS cost forecasts based on historical usage patterns.

    This tool generates cost forecasts for future periods using AWS Cost Explorer's machine learning models.
    Forecasts are based on your historical usage patterns and can help with budget planning and cost optimization.

    Important granularity limits:
    - DAILY forecasts: Maximum 3 months into the future
    - MONTHLY forecasts: Maximum 12 months into the future

    Note: The forecast start date must be equal to or no later than the current date, while the end date
    must be in the future. AWS automatically uses available historical data to generate forecasts.
    Forecasts return total costs and cannot be grouped by dimensions like services or regions.

    Example: Get monthly cost forecast for EC2 services for next quarter
        await get_cost_forecast(
            ctx=context,
            date_range={
                "start_date": "2025-06-19",  # Today or earlier
                "end_date": "2025-09-30"     # Future date
            },
            granularity="MONTHLY",
            filter_expression={
                "Dimensions": {
                    "Key": "SERVICE",
                    "Values": ["Amazon Elastic Compute Cloud - Compute"],
                    "MatchOptions": ["EQUALS"]
                }
            },
            metric="UNBLENDED_COST",
            prediction_interval_level=80
        )

    Args:
        ctx: MCP context
        date_range: The forecast period dates in YYYY-MM-DD format (start_date <= today, end_date > today)
        granularity: The granularity at which forecast data is aggregated (DAILY, MONTHLY)
        filter_expression: Filter criteria as a Python dictionary
        metric: Cost metric to forecast (UNBLENDED_COST, AMORTIZED_COST, etc.)
        prediction_interval_level: Confidence level for prediction intervals (80 or 95)

    Returns:
        Dictionary containing forecast data with confidence intervals and metadata
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `date_range` | string | Yes |  |
| `granularity` | string | No | The granularity at which forecast data is aggregated. Valid values are DAILY and MONTHLY. DAILY forecasts support up to 3 months, MONTHLY forecasts support up to 12 months. If not provided, defaults to MONTHLY. |
| `filter_expression` | string | No | Filter criteria as a Python dictionary to narrow down AWS cost forecasts. Supports filtering by Dimensions (SERVICE, REGION, etc.), Tags, or CostCategories. You can use logical operators (And, Or, Not) for complex filters. Same format as get_cost_and_usage filter_expression. |
| `metric` | string | No | The metric to forecast. Valid values are AMORTIZED_COST,BLENDED_COST,NET_AMORTIZED_COST,NET_UNBLENDED_COST,UNBLENDED_COST. Note: UsageQuantity forecasting is not supported by AWS Cost Explorer. |
| `prediction_interval_level` | integer | No | The confidence level for the forecast prediction interval. Valid values are 80 and 95. Higher values provide wider confidence ranges. |

## AWS CLI

```bash
aws ce get-cost-forecast --time-period <date_range> --granularity <granularity> --filter <filter_expression> --metric <metric> --prediction-interval-level <prediction_interval_level>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_cost_forecast(
    TimePeriod=date_range,
    Granularity=granularity,
    Filter=filter_expression,
    Metric=metric,
    PredictionIntervalLevel=prediction_interval_level,
)
```
