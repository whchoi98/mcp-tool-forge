---
name: UpdateAHORunCache
description: Update an existing HealthOmics run cache.

    Args:
        ctx: MCP context for error reporting
        cache_id: ID of the run cache to update
        cache_behavior: New cache behavior
        name: New name for the run cache
        description: New description for the run cache

    Returns:
        Dictionary containing the run cache ID and update status, or error dict
    
---

# Updateahoruncache

Update an existing HealthOmics run cache.

    Args:
        ctx: MCP context for error reporting
        cache_id: ID of the run cache to update
        cache_behavior: New cache behavior
        name: New name for the run cache
        description: New description for the run cache

    Returns:
        Dictionary containing the run cache ID and update status, or error dict
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cache_id` | string | Yes | ID of the run cache to update |
| `cache_behavior` | string | No | New cache behavior |
| `name` | string | No | New name for the run cache |
| `description` | string | No | New description for the run cache |

## AWS CLI

```bash
aws omics update-run-cache --run-cache-id <cache_id> --cache-behavior <cache_behavior> --name <name> --description <description>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.update_run_cache(
    RunCacheId=cache_id,
    CacheBehavior=cache_behavior,
    Name=name,
    Description=description,
)
```
