---
name: get-log-events
description: Get log events from CloudWatch Logs.

    Args:
        log_group_name: The name of the log group
        log_group_identifier: The unique identifier of the log group
        log_stream_name: The name of the log stream
        start_time: The start of the time range, inclusive
        end_time: The end of the time range, inclusive
        next_token: The token for the next set of items to return
        limit: The maximum number of log events to return
        start_from_head: If true, read from oldest to newest
        unmask: If true, unmask sensitive log data

    Returns:
        Dict containing:
        - events: List of log events
        - nextForwardToken: Token for getting the next set of events
        - nextBackwardToken: Token for getting the previous set of events
    
---

# Get-Log-Events

Get log events from CloudWatch Logs.

    Args:
        log_group_name: The name of the log group
        log_group_identifier: The unique identifier of the log group
        log_stream_name: The name of the log stream
        start_time: The start of the time range, inclusive
        end_time: The end of the time range, inclusive
        next_token: The token for the next set of items to return
        limit: The maximum number of log events to return
        start_from_head: If true, read from oldest to newest
        unmask: If true, unmask sensitive log data

    Returns:
        Dict containing:
        - events: List of log events
        - nextForwardToken: Token for getting the next set of events
        - nextBackwardToken: Token for getting the previous set of events
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `log_stream_name` | string | Yes |  |
| `log_group_name` | string | No |  |
| `log_group_identifier` | string | No |  |
| `start_time` | string | No |  |
| `end_time` | string | No |  |
| `next_token` | string | No |  |
| `limit` | string | No |  |
| `start_from_head` | string | No |  |
| `unmask` | string | No |  |

## AWS CLI

```bash
aws logs get-log-events --log-stream-name <log_stream_name> --log-group-name <log_group_name> --start-time <start_time> --end-time <end_time> --next-token <next_token> --limit <limit> --start-from-head <start_from_head>
```

## boto3

```python
import boto3

client = boto3.client('logs')
response = client.get_log_events(
    LogStreamName=log_stream_name,
    LogGroupName=log_group_name,
    StartTime=start_time,
    EndTime=end_time,
    NextToken=next_token,
    Limit=limit,
    StartFromHead=start_from_head,
)
```
