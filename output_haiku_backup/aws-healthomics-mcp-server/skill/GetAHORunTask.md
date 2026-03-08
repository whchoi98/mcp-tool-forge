---
name: GetAHORunTask
description: Get details about a specific task.

    Args:
        ctx: MCP context for error reporting
        run_id: ID of the run
        task_id: ID of the task

    Returns:
        Dictionary containing task details including imageDetails when available
    
---

# Getahoruntask

Get details about a specific task.

    Args:
        ctx: MCP context for error reporting
        run_id: ID of the run
        task_id: ID of the task

    Returns:
        Dictionary containing task details including imageDetails when available
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run_id` | string | Yes | ID of the run |
| `task_id` | string | Yes | ID of the task |

## AWS CLI

```bash
aws omics get-run-task --run-id <run_id> --task-id <task_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_run_task(
    RunId=run_id,
    TaskId=task_id,
)
```
