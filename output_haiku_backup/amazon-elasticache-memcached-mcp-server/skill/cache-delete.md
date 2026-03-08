---
name: cache-delete
description: Delete a value from the cache.

    Args:
        key: The key to delete

    Returns:
        Success message or error message
    
---

# Cache Delete

Delete a value from the cache.

    Args:
        key: The key to delete

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |

## AWS CLI

```bash
aws elasticache delete-cache-cluster --cache-cluster-id <key>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.delete_cache_cluster(
    CacheClusterId=key,
)
```
