---
name: ListAHORunCaches
description: List HealthOmics run caches.

    Args:
        ctx: MCP context for error reporting
        name: Filter by run cache name
        status: Filter by run cache status
        cache_behavior: Filter by cache behavior
        max_results: Maximum number of results to return
        next_token: Token for pagination from a previous response

    Returns:
        Dictionary containing run cache summaries and next token if available, or error dict
    
---

# Listahoruncaches

List HealthOmics run caches.

    Args:
        ctx: MCP context for error reporting
        name: Filter by run cache name
        status: Filter by run cache status
        cache_behavior: Filter by cache behavior
        max_results: Maximum number of results to return
        next_token: Token for pagination from a previous response

    Returns:
        Dictionary containing run cache summaries and next token if available, or error dict
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | string | No | Filter by run cache name |
| `status` | string | No | Filter by run cache status |
| `cache_behavior` | string | No | Filter by cache behavior |
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Token for pagination from a previous response |

## AWS CLI

```bash
aws omics list-run-caches --name <name> --status <status> --cache-behavior <cache_behavior> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_run_caches(
    Name=name,
    Status=status,
    CacheBehavior=cache_behavior,
    MaxResults=max_results,
    NextToken=next_token,
)
```
