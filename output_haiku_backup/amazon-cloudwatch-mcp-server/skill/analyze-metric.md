---
name: analyze-metric
description: Analyzes CloudWatch metric data to determine seasonality, trend, data density and statistical properties.

        This tool provides RAW DATA ONLY about historical metric data and performs analysis including:
        - Seasonality detection
        - Trend analysis
        - Data density and publishing period
        - Advanced statistical measures (min/max/median, std dev, noise)

        Usage: Use this tool to get objective metric analysis data.

        Args:
            ctx: The MCP context object for error handling and logging.
            namespace: The metric namespace (e.g., "AWS/EC2", "AWS/Lambda")
            metric_name: The name of the metric (e.g., "CPUUtilization", "Duration")
            dimensions: List of dimensions with name and value pairs
            region: AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.
            profile_name: AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.
            statistic: The statistic to use for metric analysis. For guidance on choosing the correct statistic, refer to the get_recommended_metric_alarms tool.

        Returns:
            Dict[str, Any]: Analysis results including:
                - message: Status message indicating success or reason for empty result
                - seasonality_seconds: Detected seasonality period in seconds
                - trend: Trend direction (INCREASING, DECREASING, or NONE)
                - statistics: Statistical measures (std_deviation, variance, etc.)
                - data_quality: Data density and publishing period information

        Example:
            analysis = await analyze_metric(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                dimensions=[
                    Dimension(name="InstanceId", value="i-1234567890abcdef0")
                ]
            )
            print(f"Status: {analysis['message']}")
            print(f"Seasonality: {analysis['seasonality_seconds']} seconds")
            print(f"Trend: {analysis['trend']}")
        
---

# Analyze Metric

Analyzes CloudWatch metric data to determine seasonality, trend, data density and statistical properties.

        This tool provides RAW DATA ONLY about historical metric data and performs analysis including:
        - Seasonality detection
        - Trend analysis
        - Data density and publishing period
        - Advanced statistical measures (min/max/median, std dev, noise)

        Usage: Use this tool to get objective metric analysis data.

        Args:
            ctx: The MCP context object for error handling and logging.
            namespace: The metric namespace (e.g., "AWS/EC2", "AWS/Lambda")
            metric_name: The name of the metric (e.g., "CPUUtilization", "Duration")
            dimensions: List of dimensions with name and value pairs
            region: AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.
            profile_name: AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.
            statistic: The statistic to use for metric analysis. For guidance on choosing the correct statistic, refer to the get_recommended_metric_alarms tool.

        Returns:
            Dict[str, Any]: Analysis results including:
                - message: Status message indicating success or reason for empty result
                - seasonality_seconds: Detected seasonality period in seconds
                - trend: Trend direction (INCREASING, DECREASING, or NONE)
                - statistics: Statistical measures (std_deviation, variance, etc.)
                - data_quality: Data density and publishing period information

        Example:
            analysis = await analyze_metric(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                dimensions=[
                    Dimension(name="InstanceId", value="i-1234567890abcdef0")
                ]
            )
            print(f"Status: {analysis['message']}")
            print(f"Seasonality: {analysis['seasonality_seconds']} seconds")
            print(f"Trend: {analysis['trend']}")
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `namespace` | string | Yes | The namespace of the metric (e.g., 'AWS/EC2', 'AWS/Lambda') |
| `metric_name` | string | Yes | The name of the metric (e.g., 'CPUUtilization', 'Duration') |
| `dimensions` | array | No | List of dimensions that identify the metric, each with name and value |
| `region` | string | No | AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set. |
| `profile_name` | string | No | AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain. |
| `statistic` | string | No | The statistic to use for the metric analysis |

## AWS CLI

```bash
aws cloudwatch get-metric-statistics --namespace <namespace> --metric-name <metric_name> --dimensions <dimensions> --statistics <statistic> --region <region> --profile <profile_name>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.get_metric_statistics(
    Namespace=namespace,
    MetricName=metric_name,
    Dimensions=dimensions,
    Statistics=statistic,
)
```
