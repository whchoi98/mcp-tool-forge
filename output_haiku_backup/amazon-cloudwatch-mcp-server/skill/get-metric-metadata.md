---
name: get-metric-metadata
description: Gets metadata for a CloudWatch metric including description, unit and recommended
        statistics that can be used for metric data retrieval.

        This tool retrieves comprehensive metadata about a specific CloudWatch metric
        identified by its namespace and metric name. Note: This function uses local metadata
        and does not make AWS API calls.

        Usage: Use this tool to get detailed information about CloudWatch metrics,
        including their descriptions, units, and recommended statistics to use.

        Args:
            ctx: The MCP context object for error handling and logging.
            namespace: The metric namespace (e.g., "AWS/EC2", "AWS/Lambda")
            metric_name: The name of the metric (e.g., "CPUUtilization", "Duration")

        Returns:
            Optional[MetricMetadata]: An object containing the metric's description,
                                     recommended statistics, and unit if found,
                                     None if no metadata is available.

        Example:
            result = await get_metric_metadata(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization"
            )
            if result:
                print(f"Description: {result.description}")
                print(f"Unit: {result.unit}")
                print(f"Recommended Statistics: {result.recommendedStatistics}")
        
---

# Get Metric Metadata

Gets metadata for a CloudWatch metric including description, unit and recommended
        statistics that can be used for metric data retrieval.

        This tool retrieves comprehensive metadata about a specific CloudWatch metric
        identified by its namespace and metric name. Note: This function uses local metadata
        and does not make AWS API calls.

        Usage: Use this tool to get detailed information about CloudWatch metrics,
        including their descriptions, units, and recommended statistics to use.

        Args:
            ctx: The MCP context object for error handling and logging.
            namespace: The metric namespace (e.g., "AWS/EC2", "AWS/Lambda")
            metric_name: The name of the metric (e.g., "CPUUtilization", "Duration")

        Returns:
            Optional[MetricMetadata]: An object containing the metric's description,
                                     recommended statistics, and unit if found,
                                     None if no metadata is available.

        Example:
            result = await get_metric_metadata(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization"
            )
            if result:
                print(f"Description: {result.description}")
                print(f"Unit: {result.unit}")
                print(f"Recommended Statistics: {result.recommendedStatistics}")
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `namespace` | string | Yes | The namespace of the metric (e.g., 'AWS/EC2', 'AWS/Lambda') |
| `metric_name` | string | Yes | The name of the metric (e.g., 'CPUUtilization', 'Duration') |

## AWS CLI

```bash
aws cloudwatch list-metrics --namespace <namespace> --metric-name <metric_name>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.list_metrics(
    Namespace=namespace,
    MetricName=metric_name,
)
```
