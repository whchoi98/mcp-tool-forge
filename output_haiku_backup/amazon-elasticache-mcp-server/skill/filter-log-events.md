---
name: filter-log-events
description: Filter log events from CloudWatch Logs.

    Args:
        log_group_name: The name of the log group
        log_group_identifier: The unique identifier of the log group
        log_stream_names: Optional list of log stream names to search
        log_stream_name_prefix: Optional prefix to match log stream names
        start_time: The start of the time range, inclusive
        end_time: The end of the time range, inclusive
        filter_pattern: The filter pattern to use
        interleaved: If true, multiple log streams are interleaved
        unmask: If true, unmask sensitive log data
        starting_token: Token for getting the next set of events
        page_size: Number of events to return per page
        max_items: Maximum number of events to return in total

    Returns:
        Dict containing:
        - events: List of filtered log events
        - searchedLogStreams: List of log streams that were searched
        - nextToken: Token for getting the next set of events
    
---

# Filter-Log-Events

Filter log events from CloudWatch Logs.

    Args:
        log_group_name: The name of the log group
        log_group_identifier: The unique identifier of the log group
        log_stream_names: Optional list of log stream names to search
        log_stream_name_prefix: Optional prefix to match log stream names
        start_time: The start of the time range, inclusive
        end_time: The end of the time range, inclusive
        filter_pattern: The filter pattern to use
        interleaved: If true, multiple log streams are interleaved
        unmask: If true, unmask sensitive log data
        starting_token: Token for getting the next set of events
        page_size: Number of events to return per page
        max_items: Maximum number of events to return in total

    Returns:
        Dict containing:
        - events: List of filtered log events
        - searchedLogStreams: List of log streams that were searched
        - nextToken: Token for getting the next set of events
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `log_group_name` | string | No |  |
| `log_group_identifier` | string | No |  |
| `log_stream_names` | string | No |  |
| `log_stream_name_prefix` | string | No |  |
| `start_time` | string | No |  |
| `end_time` | string | No |  |
| `filter_pattern` | string | No |  |
| `interleaved` | string | No |  |
| `unmask` | string | No |  |
| `starting_token` | string | No |  |
| `page_size` | string | No |  |
| `max_items` | string | No |  |

## AWS CLI

```bash
aws logs filter-log-events --log-group-name <log_group_name> --log-group-identifier <log_group_identifier> --log-stream-names <log_stream_names> --log-stream-name-prefix <log_stream_name_prefix> --start-time <start_time> --end-time <end_time> --filter-pattern <filter_pattern> --interleaved <interleaved> --unmask <unmask> --next-token <starting_token> --limit <page_size>
```

## boto3

```python
import boto3

client = boto3.client('logs')
response = client.filter_log_events(
    LogGroupName=log_group_name,
    LogGroupIdentifier=log_group_identifier,
    LogStreamNames=log_stream_names,
    LogStreamNamePrefix=log_stream_name_prefix,
    StartTime=start_time,
    EndTime=end_time,
    FilterPattern=filter_pattern,
    Interleaved=interleaved,
    Unmask=unmask,
    NextToken=starting_token,
    Limit=page_size,
)
```
