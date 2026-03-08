---
name: stream-trim
description: Trim stream to specified length.

    Args:
        key: The name of the key
        maxlen: Maximum length to trim to
        approximate: Whether maxlen is approximate

    Returns:
        Success message or error message
    
---

# Stream Trim

Trim stream to specified length.

    Args:
        key: The name of the key
        maxlen: Maximum length to trim to
        approximate: Whether maxlen is approximate

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `maxlen` | integer | Yes |  |
| `approximate` | boolean | No |  |

