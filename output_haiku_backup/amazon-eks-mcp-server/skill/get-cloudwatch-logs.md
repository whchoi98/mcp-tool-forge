---
name: get-cloudwatch-logs
description: Get logs from CloudWatch for a specific resource.

        This tool retrieves logs from CloudWatch for Kubernetes resources in an EKS cluster,
        allowing you to analyze application behavior, troubleshoot issues, and monitor system
        health. It supports filtering by resource type, time range, and content for troubleshooting
        application errors, investigating security incidents, and analyzing startup configuration issues.

        IMPORTANT: Use this tool instead of 'aws logs get-log-events', 'aws logs filter-log-events',
        or 'aws logs start-query' commands.

        ## Requirements
        - The server must be run with the `--allow-sensitive-data-access` flag
        - The EKS cluster must have CloudWatch logging enabled
        - The resource must exist in the specified cluster

        ## Response Information
        The response includes resource details (type, name, cluster), log group information,
        time range queried, and formatted log entries with timestamps and messages.

        ## Usage Tips
        - Start with a small time range (15-30 minutes) and expand if needed
        - Use filter_pattern to narrow down results (e.g., "ERROR", "exception")
        - For JSON logs, the tool automatically parses nested structures
        - Combine with get_k8s_events for comprehensive troubleshooting
        - Use resource_type="cluster" when querying cluster-level logs to avoid filtering by cluster name twice

        Args:
            ctx: MCP context
            resource_type: Resource type (pod, node, container, cluster). When "cluster" is specified, logs are not filtered by resource_name.
            cluster_name: Name of the EKS cluster
            log_type: Log type (application, host, performance, control-plane, or custom)
            resource_name: Resource name to search for in log messages. Optional when resource_type is "cluster".
            minutes: Number of minutes to look back
            start_time: Start time in ISO format (overrides minutes)
            end_time: End time in ISO format (defaults to now)
            limit: Maximum number of log entries to return
            filter_pattern: Additional CloudWatch Logs filter pattern
            fields: Custom fields to include in the query results

        Returns:
            CloudWatchLogsResponse with log entries and resource information
        
---

# Get Cloudwatch Logs

Get logs from CloudWatch for a specific resource.

        This tool retrieves logs from CloudWatch for Kubernetes resources in an EKS cluster,
        allowing you to analyze application behavior, troubleshoot issues, and monitor system
        health. It supports filtering by resource type, time range, and content for troubleshooting
        application errors, investigating security incidents, and analyzing startup configuration issues.

        IMPORTANT: Use this tool instead of 'aws logs get-log-events', 'aws logs filter-log-events',
        or 'aws logs start-query' commands.

        ## Requirements
        - The server must be run with the `--allow-sensitive-data-access` flag
        - The EKS cluster must have CloudWatch logging enabled
        - The resource must exist in the specified cluster

        ## Response Information
        The response includes resource details (type, name, cluster), log group information,
        time range queried, and formatted log entries with timestamps and messages.

        ## Usage Tips
        - Start with a small time range (15-30 minutes) and expand if needed
        - Use filter_pattern to narrow down results (e.g., "ERROR", "exception")
        - For JSON logs, the tool automatically parses nested structures
        - Combine with get_k8s_events for comprehensive troubleshooting
        - Use resource_type="cluster" when querying cluster-level logs to avoid filtering by cluster name twice

        Args:
            ctx: MCP context
            resource_type: Resource type (pod, node, container, cluster). When "cluster" is specified, logs are not filtered by resource_name.
            cluster_name: Name of the EKS cluster
            log_type: Log type (application, host, performance, control-plane, or custom)
            resource_name: Resource name to search for in log messages. Optional when resource_type is "cluster".
            minutes: Number of minutes to look back
            start_time: Start time in ISO format (overrides minutes)
            end_time: End time in ISO format (defaults to now)
            limit: Maximum number of log entries to return
            filter_pattern: Additional CloudWatch Logs filter pattern
            fields: Custom fields to include in the query results

        Returns:
            CloudWatchLogsResponse with log entries and resource information
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_type` | string | Yes | Resource type to search logs for. Valid values: "pod", "node", "container". This determines how logs are filtered. |
| `cluster_name` | string | Yes | Name of the EKS cluster where the resource is located. Used to construct the CloudWatch log group name. |
| `log_type` | string | Yes | Log type to query. Options:
            - "application": Container/application logs
            - "host": Node-level system logs
            - "performance": Performance metrics logs
            - "control-plane": EKS control plane logs
            - Or provide a custom CloudWatch log group name directly |
| `resource_name` | string | No | Resource name to search for in log messages (e.g., pod name, node name, container name). Used to filter logs for the specific resource. |
| `minutes` | integer | No | Number of minutes to look back for logs. Default: 15. Ignored if start_time is provided. Use smaller values for recent issues, larger values for historical analysis. |
| `start_time` | string | No | Start time in ISO format (e.g., "2023-01-01T00:00:00Z"). If provided, overrides the minutes parameter. IMPORTANT: Use this for precise time ranges. |
| `end_time` | string | No | End time in ISO format (e.g., "2023-01-01T01:00:00Z"). If not provided, defaults to current time. IMPORTANT: Use with start_time for precise time ranges. |
| `limit` | integer | No | Maximum number of log entries to return. Use lower values (10-50) for faster queries, higher values (100-1000) for more comprehensive results. IMPORTANT: Higher values may impact performance. |
| `filter_pattern` | string | No | Additional CloudWatch Logs filter pattern to apply. Uses CloudWatch Logs Insights syntax (e.g., "ERROR", "field=value"). IMPORTANT: Use this to narrow down results for specific issues. |
| `fields` | string | No | Custom fields to include in the query results (defaults to "@timestamp, @message"). Use CloudWatch Logs Insights field syntax. IMPORTANT: Only specify if you need fields beyond the default timestamp and message. |

## AWS CLI

```bash
aws logs filter-log-events --log-group-name <cluster_name> --start-time <start_time> --end-time <end_time> --filter-pattern <filter_pattern> --limit <limit>
```

## boto3

```python
import boto3

client = boto3.client('logs')
response = client.filter_log_events(
    LogGroupName=cluster_name,
    StartTime=start_time,
    EndTime=end_time,
    FilterPattern=filter_pattern,
    Limit=limit,
)
```
