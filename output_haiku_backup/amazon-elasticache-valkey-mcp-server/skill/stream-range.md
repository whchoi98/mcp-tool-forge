---
name: stream-range
description: Get range of entries from stream.

    Args:
        key: The name of the key
        start: Start ID (default "-" for beginning)
        end: End ID (default "+" for end)
        count: Maximum number of entries to return
        reverse: Return entries in reverse order

    Returns:
        List of entries or error message
    
---

# Stream Range

Get range of entries from stream.

    Args:
        key: The name of the key
        start: Start ID (default "-" for beginning)
        end: End ID (default "+" for end)
        count: Maximum number of entries to return
        reverse: Return entries in reverse order

    Returns:
        List of entries or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `start` | string | No |  |
| `end` | string | No |  |
| `count` | string | No |  |
| `reverse` | boolean | No |  |

