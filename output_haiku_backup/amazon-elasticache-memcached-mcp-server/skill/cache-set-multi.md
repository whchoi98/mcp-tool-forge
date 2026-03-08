---
name: cache-set-multi
description: Set multiple values in the cache (alias for set_many).

    Args:
        mapping: Dictionary of key-value pairs
        expire: Optional expiration time in seconds

    Returns:
        Success message or error message
    
---

# Cache Set Multi

Set multiple values in the cache (alias for set_many).

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
aws elasticache set-multi --mapping <mapping> --expire <expire>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.set_multi(
    Mapping=mapping,
    Expire=expire,
)
```
