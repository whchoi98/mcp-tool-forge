---
name: cache-gets
description: Get a value and its CAS token from the cache.

    Args:
        key: The key to retrieve

    Returns:
        Value and CAS token or error message
    
---

# Cache Gets

Get a value and its CAS token from the cache.

    Args:
        key: The key to retrieve

    Returns:
        Value and CAS token or error message
    

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
