---
name: stream-read
description: Read entries from stream.

    Args:
        key: The name of the key
        count: Maximum number of entries to return
        block: Milliseconds to block (optional)
        last_id: Last ID received (default "$" for new entries only)

    Returns:
        List of entries or error message
    
---

# Stream Read

Read entries from stream.

    Args:
        key: The name of the key
        count: Maximum number of entries to return
        block: Milliseconds to block (optional)
        last_id: Last ID received (default "$" for new entries only)

    Returns:
        List of entries or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `count` | string | No |  |
| `block` | string | No |  |
| `last_id` | string | No |  |

