---
name: get-recommended-metric-alarms
description: Gets recommended alarms for a CloudWatch metric.

        This tool retrieves alarm recommendations for a specific CloudWatch metric
        identified by its namespace, metric name, and dimensions. The recommendations
        are filtered to match the provided dimensions.

        Usage: Use this tool to get recommended alarm configurations for CloudWatch metrics,
        including thresholds, evaluation periods, and other alarm settings.

        Args:
            ctx: The MCP context object for error handling and logging.
            namespace: The metric namespace (e.g., "AWS/EC2", "AWS/Lambda")
            metric_name: The name of the metric (e.g., "CPUUtilization", "Duration")
            dimensions: List of dimensions with name and value pairs
            region: AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.
            profile_name: AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.
            statistic: The statistic to use for alarm recommendations. Must match the metric's data type:
                - Aggregate count metrics (RequestCount, Errors, Faults, Throttles, CacheHits, Connections, EventsProcessed): Use 'Sum'
                - Event occurrence metrics (Invocations, CacheMisses): Use 'SampleCount'
                - Utilization metrics (CPUUtilization, MemoryUtilization, DiskUtilization, NetworkUtilization): Use 'Average'
                - Latency/Time metrics (Duration, Latency, ResponseTime, ProcessingTime, Delay, ExecutionTime, WaitTime): Use 'Average'
                - Size metrics (PayloadSize, MessageSize, RequestSize, BodySize): Use 'Average'
                If uncertain about the correct statistic for a custom metric, ask the user
                to confirm the metric type before generating recommendations. Using the wrong statistic
                (e.g., 'Average' on Invocations) will produce ineffective alarm thresholds

        Returns:
            AlarmRecommendationResult: A result containing alarm recommendations and optional message.
                                     Empty recommendations list if no recommendations are found.

        Example:
            recommendations = await get_recommended_metric_alarms(
                ctx,
                namespace="AWS/EC2",
                metric_name="StatusCheckFailed_Instance",
                dimensions=[
                    Dimension(name="InstanceId", value="i-1234567890abcdef0")
                ]
            )
            for alarm in recommendations:
                print(f"Alarm: {alarm.alarmDescription}")
                print(f"Threshold: {alarm.threshold.staticValue}")
        
---

# Get Recommended Metric Alarms

Gets recommended alarms for a CloudWatch metric.

        This tool retrieves alarm recommendations for a specific CloudWatch metric
        identified by its namespace, metric name, and dimensions. The recommendations
        are filtered to match the provided dimensions.

        Usage: Use this tool to get recommended alarm configurations for CloudWatch metrics,
        including thresholds, evaluation periods, and other alarm settings.

        Args:
            ctx: The MCP context object for error handling and logging.
            namespace: The metric namespace (e.g., "AWS/EC2", "AWS/Lambda")
            metric_name: The name of the metric (e.g., "CPUUtilization", "Duration")
            dimensions: List of dimensions with name and value pairs
            region: AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.
            profile_name: AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.
            statistic: The statistic to use for alarm recommendations. Must match the metric's data type:
                - Aggregate count metrics (RequestCount, Errors, Faults, Throttles, CacheHits, Connections, EventsProcessed): Use 'Sum'
                - Event occurrence metrics (Invocations, CacheMisses): Use 'SampleCount'
                - Utilization metrics (CPUUtilization, MemoryUtilization, DiskUtilization, NetworkUtilization): Use 'Average'
                - Latency/Time metrics (Duration, Latency, ResponseTime, ProcessingTime, Delay, ExecutionTime, WaitTime): Use 'Average'
                - Size metrics (PayloadSize, MessageSize, RequestSize, BodySize): Use 'Average'
                If uncertain about the correct statistic for a custom metric, ask the user
                to confirm the metric type before generating recommendations. Using the wrong statistic
                (e.g., 'Average' on Invocations) will produce ineffective alarm thresholds

        Returns:
            AlarmRecommendationResult: A result containing alarm recommendations and optional message.
                                     Empty recommendations list if no recommendations are found.

        Example:
            recommendations = await get_recommended_metric_alarms(
                ctx,
                namespace="AWS/EC2",
                metric_name="StatusCheckFailed_Instance",
                dimensions=[
                    Dimension(name="InstanceId", value="i-1234567890abcdef0")
                ]
            )
            for alarm in recommendations:
                print(f"Alarm: {alarm.alarmDescription}")
                print(f"Threshold: {alarm.threshold.staticValue}")
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `namespace` | string | Yes | The namespace of the metric (e.g., 'AWS/EC2', 'AWS/Lambda') |
| `metric_name` | string | Yes | The name of the metric (e.g., 'CPUUtilization', 'Duration') |
| `dimensions` | array | No | List of dimensions that identify the metric, each with name and value |
| `region` | string | No | AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set. |
| `profile_name` | string | No | AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain. |
| `statistic` | string | No | The statistic to use for alarm recommendations |

## AWS CLI

```bash
aws cloudwatch describe-alarms-for-metric --namespace <namespace> --metric-name <metric_name> --dimensions <dimensions> --statistic <statistic>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.describe_alarm_for_metric(
    Namespace=namespace,
    MetricName=metric_name,
    Dimensions=dimensions,
    Statistic=statistic,
)
```
