---
name: search-transaction-spans
description: Executes a CloudWatch Logs Insights query for transaction search (100% sampled trace data).

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the search_transaction_spans tool in the cloudwatch-applicationsignals-mcp-server instead.

    IMPORTANT: If log_group_name is not provided use 'aws/spans' as default cloudwatch log group name.
    The volume of returned logs can easily overwhelm the agent context window. Always include a limit in the query
    (| limit 50) or using the limit parameter.

    Usage:
    "aws/spans" log group stores OpenTelemetry Spans data with many attributes for all monitored services.
    This provides 100% sampled data vs X-Ray's 5% sampling, giving more accurate results.
    User can write CloudWatch Logs Insights queries to group, list attribute with sum, avg.

    ```
    FILTER attributes.aws.local.service = "customers-service-java" and attributes.aws.local.environment = "eks:demo/default" and attributes.aws.remote.operation="InvokeModel"
    | STATS sum(`attributes.gen_ai.usage.output_tokens`) as `avg_output_tokens` by `attributes.gen_ai.request.model`, `attributes.aws.local.service`,bin(1h)
    | DISPLAY avg_output_tokens, `attributes.gen_ai.request.model`, `attributes.aws.local.service`
    ```

    Returns:
    --------
        A dictionary containing the final query results, including:
            - status: The current status of the query (e.g., Scheduled, Running, Complete, Failed, etc.)
            - results: A list of the actual query results if the status is Complete.
            - statistics: Query performance statistics
            - messages: Any informational messages about the query
            - transaction_search_status: Information about transaction search availability
    
---

# Search Transaction Spans

Executes a CloudWatch Logs Insights query for transaction search (100% sampled trace data).

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the search_transaction_spans tool in the cloudwatch-applicationsignals-mcp-server instead.

    IMPORTANT: If log_group_name is not provided use 'aws/spans' as default cloudwatch log group name.
    The volume of returned logs can easily overwhelm the agent context window. Always include a limit in the query
    (| limit 50) or using the limit parameter.

    Usage:
    "aws/spans" log group stores OpenTelemetry Spans data with many attributes for all monitored services.
    This provides 100% sampled data vs X-Ray's 5% sampling, giving more accurate results.
    User can write CloudWatch Logs Insights queries to group, list attribute with sum, avg.

    ```
    FILTER attributes.aws.local.service = "customers-service-java" and attributes.aws.local.environment = "eks:demo/default" and attributes.aws.remote.operation="InvokeModel"
    | STATS sum(`attributes.gen_ai.usage.output_tokens`) as `avg_output_tokens` by `attributes.gen_ai.request.model`, `attributes.aws.local.service`,bin(1h)
    | DISPLAY avg_output_tokens, `attributes.gen_ai.request.model`, `attributes.aws.local.service`
    ```

    Returns:
    --------
        A dictionary containing the final query results, including:
            - status: The current status of the query (e.g., Scheduled, Running, Complete, Failed, etc.)
            - results: A list of the actual query results if the status is Complete.
            - statistics: Query performance statistics
            - messages: Any informational messages about the query
            - transaction_search_status: Information about transaction search availability
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `log_group_name` | string | No | CloudWatch log group name (defaults to "aws/spans" if not provided) |
| `start_time` | string | No | Start time in ISO 8601 format (e.g., "2025-04-19T20:00:00+00:00") |
| `end_time` | string | No | End time in ISO 8601 format (e.g., "2025-04-19T21:00:00+00:00") |
| `query_string` | string | No | CloudWatch Logs Insights query string |
| `limit` | string | No | Maximum number of results to return |
| `max_timeout` | integer | No | Maximum time in seconds to wait for query completion |

## AWS CLI

```bash
aws logs start-query --log-group-name <log_group_name> --start-time <start_time> --end-time <end_time> --query-string <query_string> --limit <limit>
```

## boto3

```python
import boto3

client = boto3.client('logs')
response = client.start_query(
    LogGroupName=log_group_name,
    StartTime=start_time,
    EndTime=end_time,
    QueryString=query_string,
    Limit=limit,
)
```
