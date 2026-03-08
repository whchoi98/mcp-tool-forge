---
name: get-metric-data
description: Retrieves CloudWatch metric data for a specific metric.

        This tool retrieves metric data from CloudWatch for a specific metric identified by its
        namespace, metric name, and dimensions, within a specified time range. It can use either
        standard GetMetricData API or CloudWatch Metrics Insights for more advanced querying.

        The function automatically determines whether to use standard GetMetricData or Metrics Insights
        based on the parameters provided. If any Metrics Insights specific parameters are provided
        (group_by_dimension, schema_dimension_keys, limit, sort_order, or order_by_statistic), it will use Metrics Insights.

        When using group_by_dimension, you must include that dimension in schema_dimension_keys.

        Usage: Use this tool to get actual metric data from CloudWatch for analysis or visualization.

        Returns:
            GetMetricDataResponse: An object containing the metric data results

        Example 1 (Standard GetMetricData):
            result = await get_metric_data(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                start_time="2023-01-01T00:00:00Z",
                dimensions=[
                    Dimension(name="InstanceId", value="i-1234567890abcdef0")
                ],
                statistic="Average"
                # Period will be auto-calculated based on time window and target_datapoints
            )

        Example 2 (Metrics Insights with group by):
            result = await get_metric_data(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                start_time="2023-01-01T00:00:00Z",
                end_time="2023-01-02T00:00:00Z",
                statistic="AVG",
                schema_dimension_keys=["InstanceType"],
                group_by_dimension="InstanceType"
                # This will generate a query like: SELECT AVG("CPUUtilization") FROM SCHEMA("AWS/EC2", "InstanceType") GROUP BY "InstanceType"
            )

        Example 3 (Metrics Insights with schema dimension keys):
            result = await get_metric_data(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                start_time="2023-01-01T00:00:00Z",
                end_time="2023-01-02T00:00:00Z",
                statistic="AVG",
                schema_dimension_keys=["InstanceId", "InstanceType"],
                group_by_dimension="InstanceId"
                # This will generate a query like: SELECT AVG("CPUUtilization") FROM SCHEMA("AWS/EC2", "InstanceId", "InstanceType") GROUP BY "InstanceId"
            )

        Example 4 (Metrics Insights with ORDER BY and LIMIT to find the top 5 EC2 instances with the highest CPU utilization):
            result = await get_metric_data(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                start_time="2023-01-01T00:00:00Z",
                end_time="2023-01-02T00:00:00Z",
                statistic="AVG",
                schema_dimension_keys=["InstanceId"],
                group_by_dimension="InstanceId",
                sort_order="DESC",
                limit=5,
                order_by_statistic="MAX"
                # This will generate a query like: SELECT AVG("CPUUtilization") FROM SCHEMA("AWS/EC2", "InstanceId") GROUP BY "InstanceId" ORDER BY MAX() DESC LIMIT 5
            )

        Example 5 (Metrics Insights with ORDER BY without sort direction to find the EC2 instances with the highest CPU utilization ordered by default ASC):
            result = await get_metric_data(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                start_time="2023-01-01T00:00:00Z",
                end_time="2023-01-02T00:00:00Z",
                statistic="AVG",
                schema_dimension_keys=["InstanceId"],
                group_by_dimension="InstanceId",
                order_by_statistic="MAX"
                # This will generate a query like: SELECT AVG("CPUUtilization") FROM SCHEMA("AWS/EC2", "InstanceId") GROUP BY "InstanceId" ORDER BY MAX()
            )

        Example 6 (Metrics Insights without ORDER BY clause to find the EC2 instances with the highest CPU utilization in no specific order):
            result = await get_metric_data(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                start_time="2023-01-01T00:00:00Z",
                end_time="2023-01-02T00:00:00Z",
                statistic="AVG",
                schema_dimension_keys=["InstanceId"],
                group_by_dimension="InstanceId"
                # This will generate a query like: SELECT AVG("CPUUtilization") FROM SCHEMA("AWS/EC2", "InstanceId") GROUP BY "InstanceId"
                # No ORDER BY clause is added since neither order_by_statistic nor sort_order is specified
            )

        For each result:
            for metric_result in result.metricDataResults:
                print(f"Metric: {metric_result.label}")
                for datapoint in metric_result.datapoints:
                    print(f"  {datapoint.timestamp}: {datapoint.value}")
        
---

# Get Metric Data

Retrieves CloudWatch metric data for a specific metric.

        This tool retrieves metric data from CloudWatch for a specific metric identified by its
        namespace, metric name, and dimensions, within a specified time range. It can use either
        standard GetMetricData API or CloudWatch Metrics Insights for more advanced querying.

        The function automatically determines whether to use standard GetMetricData or Metrics Insights
        based on the parameters provided. If any Metrics Insights specific parameters are provided
        (group_by_dimension, schema_dimension_keys, limit, sort_order, or order_by_statistic), it will use Metrics Insights.

        When using group_by_dimension, you must include that dimension in schema_dimension_keys.

        Usage: Use this tool to get actual metric data from CloudWatch for analysis or visualization.

        Returns:
            GetMetricDataResponse: An object containing the metric data results

        Example 1 (Standard GetMetricData):
            result = await get_metric_data(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                start_time="2023-01-01T00:00:00Z",
                dimensions=[
                    Dimension(name="InstanceId", value="i-1234567890abcdef0")
                ],
                statistic="Average"
                # Period will be auto-calculated based on time window and target_datapoints
            )

        Example 2 (Metrics Insights with group by):
            result = await get_metric_data(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                start_time="2023-01-01T00:00:00Z",
                end_time="2023-01-02T00:00:00Z",
                statistic="AVG",
                schema_dimension_keys=["InstanceType"],
                group_by_dimension="InstanceType"
                # This will generate a query like: SELECT AVG("CPUUtilization") FROM SCHEMA("AWS/EC2", "InstanceType") GROUP BY "InstanceType"
            )

        Example 3 (Metrics Insights with schema dimension keys):
            result = await get_metric_data(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                start_time="2023-01-01T00:00:00Z",
                end_time="2023-01-02T00:00:00Z",
                statistic="AVG",
                schema_dimension_keys=["InstanceId", "InstanceType"],
                group_by_dimension="InstanceId"
                # This will generate a query like: SELECT AVG("CPUUtilization") FROM SCHEMA("AWS/EC2", "InstanceId", "InstanceType") GROUP BY "InstanceId"
            )

        Example 4 (Metrics Insights with ORDER BY and LIMIT to find the top 5 EC2 instances with the highest CPU utilization):
            result = await get_metric_data(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                start_time="2023-01-01T00:00:00Z",
                end_time="2023-01-02T00:00:00Z",
                statistic="AVG",
                schema_dimension_keys=["InstanceId"],
                group_by_dimension="InstanceId",
                sort_order="DESC",
                limit=5,
                order_by_statistic="MAX"
                # This will generate a query like: SELECT AVG("CPUUtilization") FROM SCHEMA("AWS/EC2", "InstanceId") GROUP BY "InstanceId" ORDER BY MAX() DESC LIMIT 5
            )

        Example 5 (Metrics Insights with ORDER BY without sort direction to find the EC2 instances with the highest CPU utilization ordered by default ASC):
            result = await get_metric_data(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                start_time="2023-01-01T00:00:00Z",
                end_time="2023-01-02T00:00:00Z",
                statistic="AVG",
                schema_dimension_keys=["InstanceId"],
                group_by_dimension="InstanceId",
                order_by_statistic="MAX"
                # This will generate a query like: SELECT AVG("CPUUtilization") FROM SCHEMA("AWS/EC2", "InstanceId") GROUP BY "InstanceId" ORDER BY MAX()
            )

        Example 6 (Metrics Insights without ORDER BY clause to find the EC2 instances with the highest CPU utilization in no specific order):
            result = await get_metric_data(
                ctx,
                namespace="AWS/EC2",
                metric_name="CPUUtilization",
                start_time="2023-01-01T00:00:00Z",
                end_time="2023-01-02T00:00:00Z",
                statistic="AVG",
                schema_dimension_keys=["InstanceId"],
                group_by_dimension="InstanceId"
                # This will generate a query like: SELECT AVG("CPUUtilization") FROM SCHEMA("AWS/EC2", "InstanceId") GROUP BY "InstanceId"
                # No ORDER BY clause is added since neither order_by_statistic nor sort_order is specified
            )

        For each result:
            for metric_result in result.metricDataResults:
                print(f"Metric: {metric_result.label}")
                for datapoint in metric_result.datapoints:
                    print(f"  {datapoint.timestamp}: {datapoint.value}")
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `namespace` | string | Yes |  |
| `metric_name` | string | Yes |  |
| `start_time` | string | Yes | The start time for the metric data query (ISO format or datetime) |
| `dimensions` | array | No |  |
| `end_time` | string | No | The end time for the metric data query (ISO format or datetime), defaults to current time |
| `statistic` | string | No | The statistic to use for the metric |
| `target_datapoints` | integer | No | Target number of data points to return (default: 60). Controls the granularity of the returned data. |
| `group_by_dimension` | string | No | Dimension name to group by in Metrics Insights mode. Must be included in schema_dimension_keys. |
| `schema_dimension_keys` | array | No | List of dimension keys to include in the SCHEMA definition for Metrics Insights query. |
| `limit` | string | No | Maximum number of results to return in Metrics Insights mode (used with LIMIT clause). |
| `sort_order` | string | No | Sort order for results when using ORDER BY in Metrics Insights. Can be 'ASC', 'DESC', or None. |
| `order_by_statistic` | string | No | Statistic to use in the ORDER BY clause. Required if sort_order is specified. |
| `region` | string | No | AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set. |
| `profile_name` | string | No | AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain. |

## AWS CLI

```bash
aws cloudwatch get-metric-data --metric-data-queries <metric_data_queries> --start-time <start_time> --end-time <end_time> --max-datapoints <target_datapoints> --region <region> --profile <profile_name>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.get_metric_data(
    MetricDataQueries=metric_data_queries,
    StartTime=start_time,
    EndTime=end_time,
    MaxDatapoints=target_datapoints,
)
```
