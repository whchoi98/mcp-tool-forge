---
name: ListAHOWorkflows
description: List available HealthOmics workflows.

    Args:
        ctx: MCP context for error reporting
        max_results: Maximum number of results to return (default: 10)
        next_token: Token for pagination

    Returns:
        Dictionary containing workflow information and next token if available
    
---

# Listahoworkflows

List available HealthOmics workflows.

    Args:
        ctx: MCP context for error reporting
        max_results: Maximum number of results to return (default: 10)
        next_token: Token for pagination

    Returns:
        Dictionary containing workflow information and next token if available
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Token for pagination from a previous response |

## AWS CLI

```bash
aws omics list-workflows --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_workflows(
    MaxResults=max_results,
    NextToken=next_token,
)
```
