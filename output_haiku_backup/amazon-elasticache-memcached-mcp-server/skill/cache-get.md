---
name: cache-get
description: Get a value from the cache.

    Args:
        key: The key to retrieve

    Returns:
        Value or error message
    
---

# Cache Get

Get a value from the cache.

    Args:
        key: The key to retrieve

    Returns:
        Value or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |

## AWS CLI

```bash
aws elasticache get-item --key <key>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.get_item(
    Key=key,
)
```
