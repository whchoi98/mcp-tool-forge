---
name: get-metrics
description: Retrieves CloudWatch metrics from a deployed web application.

        Use this tool get metrics on error rates, latency, throttles, etc. of Lambda functions, API Gateways, or CloudFront distributions.
        This tool can help provide insights into anomalies and monitor operations, which can help with troubleshooting.

        Returns:
            Dict: Metrics retrieval result
        
---

# Get Metrics

Retrieves CloudWatch metrics from a deployed web application.

        Use this tool get metrics on error rates, latency, throttles, etc. of Lambda functions, API Gateways, or CloudFront distributions.
        This tool can help provide insights into anomalies and monitor operations, which can help with troubleshooting.

        Returns:
            Dict: Metrics retrieval result
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `project_name` | string | Yes | Project name |
| `start_time` | string | No | Start time for metrics (ISO 8601 format). Example: 2025-05-30T20:00:00Z |
| `end_time` | string | No | End time for metrics (ISO 8601 format). Example: 2025-05-30T21:00:00Z |
| `period` | string | No | Period for metrics in seconds |
| `resources` | string | No | Resources to get metrics for |
| `function_name` | string | No | Lambda function to get metrics for. Set this
                        parameter if resources parameter contains 'lambda' and the function name is not same as the project_name. Typically, SAM appends a random id suffix to function names.
                        Find the name from CFN stack output. If function_name is not specified, project_name is used as function name. |
| `distribution_id` | string | No | CloudFront distribution ID to get metrics for. Find the id from the CFN stack output.
                distribution_id required if the resources parameter list contains cloudfront. |
| `region` | string | No | AWS region to use (e.g., us-east-1) |
| `stage` | string | No | API Gateway stage |

## AWS CLI

```bash
aws cloudwatch get-metric-data --start-time <start_time> --end-time <end_time> --period <period> --metric-data-queries <resources>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.get_metric_data(
    StartTime=start_time,
    EndTime=end_time,
    Period=period,
    MetricDataQueries=resources,
)
```
