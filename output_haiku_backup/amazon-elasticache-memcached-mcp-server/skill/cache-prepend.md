---
name: cache-prepend
description: Prepend a string to an existing value.

    Args:
        key: The key to prepend to
        value: String to prepend

    Returns:
        Success message or error message
    
---

# Cache Prepend

Prepend a string to an existing value.

    Args:
        key: The key to prepend to
        value: String to prepend

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `value` | string | Yes |  |

## AWS CLI

```bash
aws elasticache prepend-value --key <key> --value <value>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.prepend_value(
    Key=key,
    Value=value,
)
```
