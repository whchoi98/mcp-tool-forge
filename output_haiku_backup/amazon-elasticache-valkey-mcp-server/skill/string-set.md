---
name: string-set
description: Set string value.

    Args:
        key: The name of the key
        value: The value to set
        ex: Expire time in seconds
        px: Expire time in milliseconds
        nx: Only set if key does not exist
        xx: Only set if key exists
        keepttl: Retain the time to live associated with the key

    Returns:
        Success message or error message
    
---

# String Set

Set string value.

    Args:
        key: The name of the key
        value: The value to set
        ex: Expire time in seconds
        px: Expire time in milliseconds
        nx: Only set if key does not exist
        xx: Only set if key exists
        keepttl: Retain the time to live associated with the key

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `value` | string | Yes |  |
| `ex` | string | No |  |
| `px` | string | No |  |
| `nx` | boolean | No |  |
| `xx` | boolean | No |  |
| `keepttl` | boolean | No |  |

