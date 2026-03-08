---
name: cache-set
description: Set a value in the cache.

    Args:
        key: The key to set
        value: The value to store
        expire: Optional expiration time in seconds

    Returns:
        Success message or error message
    
---

# Cache Set

Set a value in the cache.

    Args:
        key: The key to set
        value: The value to store
        expire: Optional expiration time in seconds

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `value` | string | Yes |  |
| `expire` | string | No |  |

## AWS CLI

```bash
aws elasticache set-cache-value --key <key> --value <value> --expiration <expire>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.set_cache_value(
    Key=key,
    Value=value,
    Expiration=expire,
)
```
