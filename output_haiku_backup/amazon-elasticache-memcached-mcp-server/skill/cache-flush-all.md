---
name: cache-flush-all
description: Flush all cache entries.

    Args:
        delay: Optional delay in seconds before flushing

    Returns:
        Success message or error message
    
---

# Cache Flush All

Flush all cache entries.

    Args:
        delay: Optional delay in seconds before flushing

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `delay` | integer | No |  |

## AWS CLI

```bash
aws elasticache flush-cache-cluster --cache-cluster-id <server>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.flush_cache_cluster(
    CacheClusterId=server,
)
```
