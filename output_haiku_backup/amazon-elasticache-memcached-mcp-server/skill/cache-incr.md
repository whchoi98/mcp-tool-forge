---
name: cache-incr
description: Increment a counter in the cache.

    Args:
        key: The key to increment
        value: Amount to increment by (default 1)

    Returns:
        New value or error message
    
---

# Cache Incr

Increment a counter in the cache.

    Args:
        key: The key to increment
        value: Amount to increment by (default 1)

    Returns:
        New value or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `value` | integer | No |  |

## AWS CLI

```bash
aws elasticache increment-counter --key <key> --value <value>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.increment_counter(
    Key=key,
    Value=value,
)
```
