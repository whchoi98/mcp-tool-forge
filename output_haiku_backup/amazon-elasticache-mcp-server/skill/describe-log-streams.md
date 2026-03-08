---
name: describe-log-streams
description: Describe CloudWatch Logs log streams.

    Args:
        log_group_name: The name of the log group containing the log streams to describe.
        log_group_identifier: The unique identifier of the log group.
        log_stream_name_prefix: The prefix to match when describing log streams.
        order_by: The parameter to sort by (LogStreamName or LastEventTime).
        descending: If true, results are returned in descending order.
        starting_token: Token for starting the list from a specific page.
        page_size: Number of records to include in each page.
        max_items: Maximum number of records to return in total.

    Returns:
        Dict containing information about the log streams or error details.
    
---

# Describe-Log-Streams

Describe CloudWatch Logs log streams.

    Args:
        log_group_name: The name of the log group containing the log streams to describe.
        log_group_identifier: The unique identifier of the log group.
        log_stream_name_prefix: The prefix to match when describing log streams.
        order_by: The parameter to sort by (LogStreamName or LastEventTime).
        descending: If true, results are returned in descending order.
        starting_token: Token for starting the list from a specific page.
        page_size: Number of records to include in each page.
        max_items: Maximum number of records to return in total.

    Returns:
        Dict containing information about the log streams or error details.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `log_group_name` | string | No |  |
| `log_group_identifier` | string | No |  |
| `log_stream_name_prefix` | string | No |  |
| `order_by` | string | No |  |
| `descending` | string | No |  |
| `starting_token` | string | No |  |
| `page_size` | string | No |  |
| `max_items` | string | No |  |

## AWS CLI

```bash
aws logs describe-log-streams --log-group-name <log_group_name> --log-group-identifier <log_group_identifier> --log-stream-name-prefix <log_stream_name_prefix> --order-by <order_by> --descending <descending> --starting-token <starting_token> --max-items <page_size>
```

## boto3

```python
import boto3

client = boto3.client('logs')
response = client.describe_log_streams(
    LogGroupName=log_group_name,
    LogGroupIdentifier=log_group_identifier,
    LogStreamNamePrefix=log_stream_name_prefix,
    OrderBy=order_by,
    Descending=descending,
    NextToken=starting_token,
    Limit=page_size,
)
```
