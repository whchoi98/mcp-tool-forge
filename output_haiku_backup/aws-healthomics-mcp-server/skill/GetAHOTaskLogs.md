---
name: GetAHOTaskLogs
description: Retrieve logs for a specific workflow task containing STDOUT and STDERR.

    These logs contain the output from a specific task process including:
    - Task container startup messages
    - Application-specific output and error messages
    - Task completion or failure information

    Args:
        ctx: MCP context for error reporting
        run_id: ID of the run
        task_id: ID of the specific task
        start_time: Optional start time for log retrieval (ISO format)
        end_time: Optional end time for log retrieval (ISO format)
        limit: Maximum number of log events to return (default: 100)
        next_token: Token for pagination from a previous response
        start_from_head: Whether to start from the beginning (True) or end (False) of the log stream

    Returns:
        Dictionary containing log events and next token if available
    
---

# Getahotasklogs

Retrieve logs for a specific workflow task containing STDOUT and STDERR.

    These logs contain the output from a specific task process including:
    - Task container startup messages
    - Application-specific output and error messages
    - Task completion or failure information

    Args:
        ctx: MCP context for error reporting
        run_id: ID of the run
        task_id: ID of the specific task
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
| `task_id` | string | Yes | ID of the specific task |
| `start_time` | string | No | Optional start time for log retrieval (ISO format) |
| `end_time` | string | No | Optional end time for log retrieval (ISO format) |
| `limit` | integer | No | Maximum number of log events to return |
| `next_token` | string | No | Token for pagination from a previous response |
| `start_from_head` | boolean | No | Whether to start from the beginning (True) or end (False) of the log stream |

## AWS CLI

```bash
aws omics get-run-task-logs --run-id <run_id> --task-id <task_id> --start-time <start_time> --end-time <end_time> --max-results <limit> --next-token <next_token> --start-from-head <start_from_head>
```

## boto3

```python
import boto3

client = boto3.client('healthomics')
response = client.get_run_task_logs(
    RunId=run_id,
    TaskId=task_id,
    StartTime=start_time,
    EndTime=end_time,
    MaxResults=limit,
    NextToken=next_token,
)
```
