---
name: ListAHORuns
description: List workflow runs.

    Args:
        ctx: MCP context for error reporting
        max_results: Maximum number of results to return (default: 10)
        next_token: Token for pagination
        status: Filter by run status
        created_after: Filter for runs created after this timestamp (ISO format)
        created_before: Filter for runs created before this timestamp (ISO format)
        run_group_id: Optional run group ID to filter runs

    Returns:
        Dictionary containing run information and next token if available, or error dict
    
---

# Listahoruns

List workflow runs.

    Args:
        ctx: MCP context for error reporting
        max_results: Maximum number of results to return (default: 10)
        next_token: Token for pagination
        status: Filter by run status
        created_after: Filter for runs created after this timestamp (ISO format)
        created_before: Filter for runs created before this timestamp (ISO format)
        run_group_id: Optional run group ID to filter runs

    Returns:
        Dictionary containing run information and next token if available, or error dict
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Token for pagination from a previous response |
| `status` | string | No | Filter by run status |
| `created_after` | string | No | Filter for runs created after this timestamp (ISO format) |
| `created_before` | string | No | Filter for runs created before this timestamp (ISO format) |
| `run_group_id` | string | No | Optional run group ID to filter runs |

## AWS CLI

```bash
aws omics list-runs --max-results <max_results> --next-token <next_token> --status <status> --created-after <created_after> --created-before <created_before> --run-group-id <run_group_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_runs(
    MaxResults=max_results,
    NextToken=next_token,
    Status=status,
    CreatedAfter=created_after,
    CreatedBefore=created_before,
    RunGroupId=run_group_id,
)
```
