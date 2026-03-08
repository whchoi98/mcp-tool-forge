---
name: analyze-log-group
description: Analyzes a CloudWatch log group for anomalies, message patterns, and error patterns within a specified time window.

        This tool performs an analysis of the specified log group by:
        1. Discovering and checking log anomaly detectors associated with the log group
        2. Retrieving anomalies from those detectors that fall within the specified time range
        3. Identifying the top 5 most common message patterns
        4. Finding the top 5 patterns containing error-related terms

        Usage: Use this tool to detect anomalies and understand common patterns in your log data, particularly
        focusing on error patterns that might indicate issues. This can help identify potential problems and
        understand the typical behavior of your application.

        Returns:
        --------
        A LogsAnalysisResult object containing:
            - log_anomaly_results: Information about anomaly detectors and their findings
                * anomaly_detectors: List of anomaly detectors for the log group
                * anomalies: List of anomalies that fall within the specified time range
            - top_patterns: Results of the query for most common message patterns
            - top_patterns_containing_errors: Results of the query for patterns containing error-related terms
                (error, exception, fail, timeout, fatal)
        
---

# Analyze Log Group

Analyzes a CloudWatch log group for anomalies, message patterns, and error patterns within a specified time window.

        This tool performs an analysis of the specified log group by:
        1. Discovering and checking log anomaly detectors associated with the log group
        2. Retrieving anomalies from those detectors that fall within the specified time range
        3. Identifying the top 5 most common message patterns
        4. Finding the top 5 patterns containing error-related terms

        Usage: Use this tool to detect anomalies and understand common patterns in your log data, particularly
        focusing on error patterns that might indicate issues. This can help identify potential problems and
        understand the typical behavior of your application.

        Returns:
        --------
        A LogsAnalysisResult object containing:
            - log_anomaly_results: Information about anomaly detectors and their findings
                * anomaly_detectors: List of anomaly detectors for the log group
                * anomalies: List of anomalies that fall within the specified time range
            - top_patterns: Results of the query for most common message patterns
            - top_patterns_containing_errors: Results of the query for patterns containing error-related terms
                (error, exception, fail, timeout, fatal)
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `log_group_arn` | string | Yes | The log group arn to look for anomalies in, as returned by the describe_log_groups tools |
| `start_time` | string | Yes | ISO 8601 formatted start time for the CloudWatch Logs Insights query window (e.g., "2025-04-19T20:00:00+00:00"). |
| `end_time` | string | Yes | ISO 8601 formatted end time for the CloudWatch Logs Insights query window (e.g., "2025-04-19T21:00:00+00:00"). |
| `region` | string | No | AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set. |
| `profile_name` | string | No | AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain. |

## AWS CLI

```bash
aws logs start-query --log-group-name <log_group_arn> --start-time <start_time> --end-time <end_time> --query-string <SELECT * FROM CloudWatchLogs> --region <region> --profile <profile_name>
```

## boto3

```python
import boto3

client = boto3.client('logs')
response = client.start_query(
    LogGroupName=log_group_arn,
    StartTime=start_time,
    EndTime=end_time,
    QueryString=SELECT * FROM CloudWatchLogs,
)
```
