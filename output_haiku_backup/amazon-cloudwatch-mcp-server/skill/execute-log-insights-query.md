---
name: execute-log-insights-query
description: Executes a CloudWatch Logs Insights query and waits for the results to be available.

        IMPORTANT: The operation must include exactly one of the following parameters: log_group_names, or log_group_identifiers.

        CRITICAL: The volume of returned logs can easily overwhelm the agent context window. Always include a limit in the query
        (| limit 50) or using the limit parameter.

        Usage: Use to query, filter, collect statistics, or find patterns in one or more log groups. For example, the following
        query lists exceptions per hour.

        ```
        filter @message like /Exception/
        | stats count(*) as exceptionCount by bin(1h)
        | sort exceptionCount desc
        ```

        Returns:
        --------
            A dictionary containing the final query results, including:
                - status: The current status of the query (e.g., Scheduled, Running, Complete, Failed, etc.)
                - results: A list of the actual query results if the status is Complete.
                - statistics: Query performance statistics
                - messages: Any informational messages about the query
        
---

# Execute Log Insights Query

Executes a CloudWatch Logs Insights query and waits for the results to be available.

        IMPORTANT: The operation must include exactly one of the following parameters: log_group_names, or log_group_identifiers.

        CRITICAL: The volume of returned logs can easily overwhelm the agent context window. Always include a limit in the query
        (| limit 50) or using the limit parameter.

        Usage: Use to query, filter, collect statistics, or find patterns in one or more log groups. For example, the following
        query lists exceptions per hour.

        ```
        filter @message like /Exception/
        | stats count(*) as exceptionCount by bin(1h)
        | sort exceptionCount desc
        ```

        Returns:
        --------
            A dictionary containing the final query results, including:
                - status: The current status of the query (e.g., Scheduled, Running, Complete, Failed, etc.)
                - results: A list of the actual query results if the status is Complete.
                - statistics: Query performance statistics
                - messages: Any informational messages about the query
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `log_group_names` | string | No | The list of up to 50 log group names to be queried. CRITICAL: Exactly one of [log_group_names, log_group_identifiers] should be non-null. |
| `log_group_identifiers` | string | No | The list of up to 50 logGroupIdentifiers to query. You can specify them by the log group name or ARN. If a log group that you're querying is in a source account and you're using a monitoring account, you must use the ARN. CRITICAL: Exactly one of [log_group_names, log_group_identifiers] should be non-null. |
| `start_time` | string | Yes | ISO 8601 formatted start time for the CloudWatch Logs Insights query window (e.g., "2025-04-19T20:00:00+00:00"). |
| `end_time` | string | Yes | ISO 8601 formatted end time for the CloudWatch Logs Insights query window (e.g., "2025-04-19T21:00:00+00:00"). |
| `query_string` | string | Yes | The query string in the Cloudwatch Log Insights Query Language. See https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html. |
| `limit` | string | No | The maximum number of log events to return. It is critical to use either this parameter or a `| limit <int>` operator in the query to avoid consuming too many tokens of the agent. |
| `max_timeout` | integer | No | Maximum time in second to poll for complete results before giving up |
| `region` | string | No | AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set. |
| `profile_name` | string | No | AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain. |

## AWS CLI

```bash
aws logs start-query --log-group-names <log_group_names> --log-group-identifiers <log_group_identifiers> --start-time <start_time> --end-time <end_time> --query-string <query_string> --limit <limit>
```

## boto3

```python
import boto3

client = boto3.client('logs')
response = client.start_query(
    LogGroupNames=log_group_names,
    LogGroupIdentifiers=log_group_identifiers,
    StartTime=start_time,
    EndTime=end_time,
    QueryString=query_string,
    Limit=limit,
)
```
