---
name: cache-get-many
description: Get multiple values from the cache.

    Args:
        keys: List of keys to retrieve

    Returns:
        Dictionary of key-value pairs or error message
    
---

# Cache Get Many

Get multiple values from the cache.

    Args:
        keys: List of keys to retrieve

    Returns:
        Dictionary of key-value pairs or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keys` | array | Yes |  |

## AWS CLI

```bash
aws elasticache get-many --keys <keys>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.get_many(
    Keys=keys,
)
```
