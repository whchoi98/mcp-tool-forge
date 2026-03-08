---
name: expire
description: Set an expiration time for a Redis key.

    Args:
        name: The Redis key.
        expire_seconds: Time in seconds after which the key should expire.

    Returns:
        A success message or an error message.
    
---

# Expire

Set an expiration time for a Redis key.

    Args:
        name: The Redis key.
        expire_seconds: Time in seconds after which the key should expire.

    Returns:
        A success message or an error message.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | string | Yes |  |
| `expire_seconds` | integer | Yes |  |

