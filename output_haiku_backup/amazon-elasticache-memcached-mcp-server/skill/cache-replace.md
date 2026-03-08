---
name: cache-replace
description: Replace a value in the cache only if the key exists.

    Args:
        key: The key to replace
        value: The new value
        expire: Optional expiration time in seconds

    Returns:
        Success message or error message
    
---

# Cache Replace

Replace a value in the cache only if the key exists.

    Args:
        key: The key to replace
        value: The new value
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
aws elasticache replace-cache-value --key <key> --value <value> --expiration <expire>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.replace_cache_value(
    Key=key,
    Value=value,
    Expiration=expire,
)
```
