---
name: get-metric-statistics
description: Get CloudWatch metric statistics.

    Args:
        metric_name: The name of the metric
        start_time: The start time in ISO 8601 format
        end_time: The end time in ISO 8601 format
        period: The granularity, in seconds, of the returned data points
        dimensions: The dimensions to filter by
        statistics: The metric statistics to return
        extended_statistics: The percentile statistics to return
        unit: The unit for the metric

    Returns:
        Dict containing metric statistics
    
---

# Get-Metric-Statistics

Get CloudWatch metric statistics.

    Args:
        metric_name: The name of the metric
        start_time: The start time in ISO 8601 format
        end_time: The end time in ISO 8601 format
        period: The granularity, in seconds, of the returned data points
        dimensions: The dimensions to filter by
        statistics: The metric statistics to return
        extended_statistics: The percentile statistics to return
        unit: The unit for the metric

    Returns:
        Dict containing metric statistics
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `metric_name` | string | Yes |  |
| `start_time` | string | Yes |  |
| `end_time` | string | Yes |  |
| `period` | integer | Yes |  |
| `dimensions` | string | No |  |
| `statistics` | string | No |  |
| `extended_statistics` | string | No |  |
| `unit` | string | No |  |

## AWS CLI

```bash
aws cloudwatch get-metric-statistics --metric-name <metric_name> --start-time <start_time> --end-time <end_time> --period <period> --dimensions <dimensions> --statistics <statistics> --extended-statistics <extended_statistics> --unit <unit>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.get_metric_statistics(
    MetricName=metric_name,
    StartTime=start_time,
    EndTime=end_time,
    Period=period,
    Dimensions=dimensions,
    Statistics=statistics,
    ExtendedStatistics=extended_statistics,
    Unit=unit,
)
```
