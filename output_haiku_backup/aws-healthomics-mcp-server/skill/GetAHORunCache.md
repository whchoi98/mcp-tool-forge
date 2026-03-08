---
name: GetAHORunCache
description: Get details of a specific HealthOmics run cache.

    Args:
        ctx: MCP context for error reporting
        cache_id: ID of the run cache to retrieve

    Returns:
        Dictionary containing the run cache details, or error dict
    
---

# Getahoruncache

Get details of a specific HealthOmics run cache.

    Args:
        ctx: MCP context for error reporting
        cache_id: ID of the run cache to retrieve

    Returns:
        Dictionary containing the run cache details, or error dict
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cache_id` | string | Yes | ID of the run cache to retrieve |

## AWS CLI

```bash
aws omics get-run-cache --cache-id <cache_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_run_cache(
    CacheId=cache_id,
)
```
