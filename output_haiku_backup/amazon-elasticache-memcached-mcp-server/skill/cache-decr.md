---
name: cache-decr
description: Decrement a counter in the cache.

    Args:
        key: The key to decrement
        value: Amount to decrement by (default 1)

    Returns:
        New value or error message
    
---

# Cache Decr

Decrement a counter in the cache.

    Args:
        key: The key to decrement
        value: Amount to decrement by (default 1)

    Returns:
        New value or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `value` | integer | No |  |

## AWS CLI

```bash
aws elasticache decrement-counter --key <key> --decrement-amount <value>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.decrement_counter(
    Key=key,
    DecrementAmount=value,
)
```
