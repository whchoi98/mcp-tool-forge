---
name: ListAHORunGroups
description: List HealthOmics run groups.

    Args:
        ctx: MCP context for error reporting
        name: Filter by run group name
        max_results: Maximum number of results to return
        next_token: Token for pagination from a previous response

    Returns:
        Dictionary containing run group summaries and next token if available, or error dict
    
---

# Listahorungroups

List HealthOmics run groups.

    Args:
        ctx: MCP context for error reporting
        name: Filter by run group name
        max_results: Maximum number of results to return
        next_token: Token for pagination from a previous response

    Returns:
        Dictionary containing run group summaries and next token if available, or error dict
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | string | No | Filter by run group name |
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Token for pagination from a previous response |

## AWS CLI

```bash
aws omics list-run-groups --name <name> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_run_groups(
    Name=name,
    MaxResults=max_results,
    NextToken=next_token,
)
```
