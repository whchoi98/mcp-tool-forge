---
name: get-cloudwatch-metrics
description: Get metrics from CloudWatch for a specific resource.

        This tool retrieves metrics from CloudWatch for Kubernetes resources in an EKS cluster,
        allowing you to monitor performance, resource utilization, and system health. It supports
        various resource types and metrics with flexible time ranges and aggregation options for
        monitoring CPU/memory usage, analyzing network traffic, and identifying performance bottlenecks.

        IMPORTANT: Use this tool instead of 'aws cloudwatch get-metric-data', 'aws cloudwatch get-metric-statistics',
        or similar CLI commands.

        IMPORTANT: Use the get_eks_metrics_guidance tool first to determine the correct dimensions for metric queries.
        Do not try to infer which dimensions are needed for EKS ContainerInsights metrics.

        IMPORTANT: When using pod metrics, note that `FullPodName` has the same prefix as `PodName` but includes a
        suffix with a random string (e.g., "my-pod-abc123"). Always use the version without the suffix for `PodName`
        dimension. The pod name returned by list_k8s_resources is the `FullPodName`.

        ## Requirements
        - The EKS cluster must have CloudWatch Container Insights enabled
        - The resource must exist in the specified cluster
        - The metric must be available in the specified namespace

        ## Response Information
        The response includes resource details (cluster), metric information (name, namespace),
        time range queried, and data points with timestamps and values.

        ## Usage Tips
        - Use appropriate statistics for different metrics (e.g., Average for CPU, Maximum for memory spikes)
        - Match the period to your analysis needs (smaller for detailed graphs, larger for trends)
        - For rate metrics like network traffic, Sum is often more useful than Average
        - Combine with get_cloudwatch_logs to correlate metrics with log events

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster
            metric_name: Metric name (e.g., cpu_usage_total, memory_rss)
            namespace: CloudWatch namespace
            dimensions: Dimensions to use for the CloudWatch metric query
            minutes: Number of minutes to look back
            start_time: Start time in ISO format (overrides minutes)
            end_time: End time in ISO format (defaults to now)
            limit: Maximum number of data points to return
            period: Period in seconds for the metric data points
            stat: Statistic to use for the metric

        Returns:
            CloudWatchMetricsResponse with metric data points and resource information
        
---

# Get Cloudwatch Metrics

Get metrics from CloudWatch for a specific resource.

        This tool retrieves metrics from CloudWatch for Kubernetes resources in an EKS cluster,
        allowing you to monitor performance, resource utilization, and system health. It supports
        various resource types and metrics with flexible time ranges and aggregation options for
        monitoring CPU/memory usage, analyzing network traffic, and identifying performance bottlenecks.

        IMPORTANT: Use this tool instead of 'aws cloudwatch get-metric-data', 'aws cloudwatch get-metric-statistics',
        or similar CLI commands.

        IMPORTANT: Use the get_eks_metrics_guidance tool first to determine the correct dimensions for metric queries.
        Do not try to infer which dimensions are needed for EKS ContainerInsights metrics.

        IMPORTANT: When using pod metrics, note that `FullPodName` has the same prefix as `PodName` but includes a
        suffix with a random string (e.g., "my-pod-abc123"). Always use the version without the suffix for `PodName`
        dimension. The pod name returned by list_k8s_resources is the `FullPodName`.

        ## Requirements
        - The EKS cluster must have CloudWatch Container Insights enabled
        - The resource must exist in the specified cluster
        - The metric must be available in the specified namespace

        ## Response Information
        The response includes resource details (cluster), metric information (name, namespace),
        time range queried, and data points with timestamps and values.

        ## Usage Tips
        - Use appropriate statistics for different metrics (e.g., Average for CPU, Maximum for memory spikes)
        - Match the period to your analysis needs (smaller for detailed graphs, larger for trends)
        - For rate metrics like network traffic, Sum is often more useful than Average
        - Combine with get_cloudwatch_logs to correlate metrics with log events

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster
            metric_name: Metric name (e.g., cpu_usage_total, memory_rss)
            namespace: CloudWatch namespace
            dimensions: Dimensions to use for the CloudWatch metric query
            minutes: Number of minutes to look back
            start_time: Start time in ISO format (overrides minutes)
            end_time: End time in ISO format (defaults to now)
            limit: Maximum number of data points to return
            period: Period in seconds for the metric data points
            stat: Statistic to use for the metric

        Returns:
            CloudWatchMetricsResponse with metric data points and resource information
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_name` | string | Yes | Name of the EKS cluster to get metrics for. |
| `metric_name` | string | Yes | Metric name to retrieve. Common examples:
            - cpu_usage_total: Total CPU usage
            - memory_rss: Resident Set Size memory usage
            - network_rx_bytes: Network bytes received
            - network_tx_bytes: Network bytes transmitted |
| `namespace` | string | Yes | CloudWatch namespace where the metric is stored. Common values:
            - "ContainerInsights": For container metrics
            - "AWS/EC2": For EC2 instance metrics
            - "AWS/EKS": For EKS control plane metrics |
| `dimensions` | object | Yes | Dimensions to use for the CloudWatch metric query. Must include appropriate dimensions for the resource type and metric (e.g., ClusterName, PodName, Namespace). |
| `minutes` | integer | No | Number of minutes to look back for metrics. Default: 15. Ignored if start_time is provided. IMPORTANT: Choose a time range appropriate for the metric resolution. |
| `start_time` | string | No | Start time in ISO format (e.g., "2023-01-01T00:00:00Z"). If provided, overrides the minutes parameter. IMPORTANT: Use this for precise historical analysis. |
| `end_time` | string | No | End time in ISO format (e.g., "2023-01-01T01:00:00Z"). If not provided, defaults to current time. IMPORTANT: Use with start_time for precise time ranges. |
| `limit` | integer | No | Maximum number of data points to return. Higher values (100-1000) provide more granular data but may impact performance. IMPORTANT: Balance between granularity and performance. |
| `period` | integer | No | Period in seconds for the metric data points. Default: 60 (1 minute). Lower values (1-60) provide higher resolution but may be less available. IMPORTANT: Match to your monitoring needs. |
| `stat` | string | No | Statistic to use for the metric aggregation:
            - Average: Mean value during the period
            - Sum: Total value during the period
            - Maximum: Highest value during the period
            - Minimum: Lowest value during the period
            - SampleCount: Number of samples during the period |

## AWS CLI

```bash
aws cloudwatch get-metric-data --metric-data-queries <dimensions> --start-time <start_time> --end-time <end_time> --max-datapoints <limit> --scan-by <period>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.get_metric_data(
    MetricDataQueries=dimensions,
    StartTime=start_time,
    EndTime=end_time,
    MaxDatapoints=limit,
    ScanBy=period,
)
```
