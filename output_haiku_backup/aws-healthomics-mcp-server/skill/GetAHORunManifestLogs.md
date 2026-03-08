---
name: GetAHORunManifestLogs
description: Retrieve run manifest logs produced when a workflow completes or fails.

    These logs contain a summary of the overall workflow including:
    - Runtime information
    - Inputs and input digests
    - Messages and status information
    - Task summaries with resource allocation and utilization metrics

    Args:
        ctx: MCP context for error reporting
        run_id: ID of the run
        run_uuid: Optional UUID of the run
        start_time: Optional start time for log retrieval (ISO format)
        end_time: Optional end time for log retrieval (ISO format)
        limit: Maximum number of log events to return (default: 100)
        next_token: Token for pagination from a previous response
        start_from_head: Whether to start from the beginning (True) or end (False) of the log stream

    Returns:
        Dictionary containing log events and next token if available
    
---

# Getahorunmanifestlogs

Retrieve run manifest logs produced when a workflow completes or fails.

    These logs contain a summary of the overall workflow including:
    - Runtime information
    - Inputs and input digests
    - Messages and status information
    - Task summaries with resource allocation and utilization metrics

    Args:
        ctx: MCP context for error reporting
        run_id: ID of the run
        run_uuid: Optional UUID of the run
        start_time: Optional start time for log retrieval (ISO format)
        end_time: Optional end time for log retrieval (ISO format)
        limit: Maximum number of log events to return (default: 100)
        next_token: Token for pagination from a previous response
        start_from_head: Whether to start from the beginning (True) or end (False) of the log stream

    Returns:
        Dictionary containing log events and next token if available
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run_id` | string | Yes | ID of the run |
| `run_uuid` | string | Yes | Optional UUID of the run |
| `start_time` | string | No | Optional start time for log retrieval (ISO format) |
| `end_time` | string | No | Optional end time for log retrieval (ISO format) |
| `limit` | integer | No | Maximum number of log events to return |
| `next_token` | string | No | Token for pagination from a previous response |
| `start_from_head` | boolean | No | Whether to start from the beginning (True) or end (False) of the log stream |

## AWS CLI

```bash
aws omics get-run-log --run-id <run_id> --start-time <start_time> --end-time <end_time> --max-results <limit> --next-token <next_token> --start-from-head <start_from_head>
```

## boto3

```python
import boto3

client = boto3.client('healthomics')
response = client.get_run_log(
    RunId=run_id,
    StartTime=start_time,
    EndTime=end_time,
    Limit=limit,
    NextToken=next_token,
    StartFromHead=start_from_head,
)
```
