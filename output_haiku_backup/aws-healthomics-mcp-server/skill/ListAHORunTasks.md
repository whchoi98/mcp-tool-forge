---
name: ListAHORunTasks
description: List tasks for a specific run.

    Args:
        ctx: MCP context for error reporting
        run_id: ID of the run
        max_results: Maximum number of results to return (default: 10)
        next_token: Token for pagination
        status: Filter by task status

    Returns:
        Dictionary containing task information and next token if available
    
---

# Listahoruntasks

List tasks for a specific run.

    Args:
        ctx: MCP context for error reporting
        run_id: ID of the run
        max_results: Maximum number of results to return (default: 10)
        next_token: Token for pagination
        status: Filter by task status

    Returns:
        Dictionary containing task information and next token if available
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run_id` | string | Yes | ID of the run |
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Token for pagination from a previous response |
| `status` | string | No | Filter by task status |

## AWS CLI

```bash
aws omics list-run-tasks --run-id <run_id> --max-results <max_results> --next-token <next_token> --status <status>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_run_tasks(
    RunId=run_id,
    MaxResults=max_results,
    NextToken=next_token,
    Status=status,
)
```
