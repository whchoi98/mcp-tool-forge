---
name: cache-cas
description: Set a value using CAS (Check And Set).

    Args:
        key: The key to set
        value: The value to store
        cas: CAS token from gets()
        expire: Optional expiration time in seconds

    Returns:
        Success message or error message
    
---

# Cache Cas

Set a value using CAS (Check And Set).

    Args:
        key: The key to set
        value: The value to store
        cas: CAS token from gets()
        expire: Optional expiration time in seconds

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `value` | string | Yes |  |
| `cas` | integer | Yes |  |
| `expire` | string | No |  |

## AWS CLI

```bash
aws elasticache set-cache-parameter --key <key> --value <value> --cas <cas> --ttl <expire>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.set_cache_parameter(
    Key=key,
    Value=value,
    Cas=cas,
    Ttl=expire,
)
```
