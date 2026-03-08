---
name: cache-add
description: Add a value to the cache only if the key doesn't exist.

    Args:
        key: The key to add
        value: The value to store
        expire: Optional expiration time in seconds

    Returns:
        Success message or error message
    
---

# Cache Add

Add a value to the cache only if the key doesn't exist.

    Args:
        key: The key to add
        value: The value to store
        expire: Optional expiration time in seconds

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `value` | string | Yes |  |
| `expire` | string | No |  |

