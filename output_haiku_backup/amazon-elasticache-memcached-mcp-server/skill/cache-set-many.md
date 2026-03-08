---
name: cache-set-many
description: Set multiple values in the cache.

    Args:
        mapping: Dictionary of key-value pairs
        expire: Optional expiration time in seconds

    Returns:
        Success message or error message
    
---

# Cache Set Many

Set multiple values in the cache.

    Args:
        mapping: Dictionary of key-value pairs
        expire: Optional expiration time in seconds

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `mapping` | object | Yes |  |
| `expire` | string | No |  |

## AWS CLI

```bash
aws elasticache set-many --mapping <mapping> --expire <expire>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.set_many(
    Mapping=mapping,
    Expiration=expire,
)
```
