---
name: query-service-metrics
description: Get CloudWatch metrics for a specific Application Signals service.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the query_service_metrics tool in the cloudwatch-applicationsignals-mcp-server instead.

    Use this tool to:
    - Analyze service performance (latency, throughput)
    - Check error rates and reliability
    - View trends over time
    - Get both standard statistics (Average, Max) and percentiles (p99, p95)

    Common metric names:
    - 'Latency': Response time in milliseconds
    - 'Error': Percentage of failed requests
    - 'Fault': Percentage of server errors (5xx)

    Returns:
    - Summary statistics (latest, average, min, max)
    - Recent data points with timestamps
    - Both standard and percentile values when available

    The tool automatically adjusts the granularity based on time range:
    - Up to 3 hours: 1-minute resolution
    - Up to 24 hours: 5-minute resolution
    - Over 24 hours: 1-hour resolution
    
---

# Query Service Metrics

Get CloudWatch metrics for a specific Application Signals service.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the query_service_metrics tool in the cloudwatch-applicationsignals-mcp-server instead.

    Use this tool to:
    - Analyze service performance (latency, throughput)
    - Check error rates and reliability
    - View trends over time
    - Get both standard statistics (Average, Max) and percentiles (p99, p95)

    Common metric names:
    - 'Latency': Response time in milliseconds
    - 'Error': Percentage of failed requests
    - 'Fault': Percentage of server errors (5xx)

    Returns:
    - Summary statistics (latest, average, min, max)
    - Recent data points with timestamps
    - Both standard and percentile values when available

    The tool automatically adjusts the granularity based on time range:
    - Up to 3 hours: 1-minute resolution
    - Up to 24 hours: 5-minute resolution
    - Over 24 hours: 1-hour resolution
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `service_name` | string | Yes | Name of the service to get metrics for (case-sensitive) |
| `metric_name` | string | Yes | Specific metric name (e.g., Latency, Error, Fault). Leave empty to list available metrics |
| `statistic` | string | No | Standard statistic type (Average, Sum, Maximum, Minimum, SampleCount) |
| `extended_statistic` | string | No | Extended statistic (p99, p95, p90, p50, etc) |
| `hours` | integer | No | Number of hours to look back (default 1, max 168 for 1 week) |

## AWS CLI

```bash
aws cloudwatch get-metric-statistics --namespace <AWS/ApplicationSignals> --metric-name <metric_name> --dimensions <Name=ServiceName,Value=service_name> --period <3600> --start-time <calculated_start_time> --end-time <current_time> --statistics <statistic> --extended-statistics <extended_statistic>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.get_metric_statistics(
    Namespace=AWS/ApplicationSignals,
    MetricName=metric_name,
    Dimensions=[{'Name': 'ServiceName', 'Value': 'service_name'}],
    Period=3600,
    StartTime=calculated_start_time,
    EndTime=current_time,
    Statistics=['statistic'],
    ExtendedStatistics=['extended_statistic'],
)
```
