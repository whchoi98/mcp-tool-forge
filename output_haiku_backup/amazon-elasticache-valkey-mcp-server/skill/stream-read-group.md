---
name: stream-read-group
description: Read entries from stream as part of consumer group.

    Args:
        key: The name of the key
        group_name: Name of consumer group
        consumer_name: Name of this consumer
        count: Maximum number of entries to return
        block: Milliseconds to block (optional)
        noack: Don't require acknowledgment

    Returns:
        List of entries or error message
    
---

# Stream Read Group

Read entries from stream as part of consumer group.

    Args:
        key: The name of the key
        group_name: Name of consumer group
        consumer_name: Name of this consumer
        count: Maximum number of entries to return
        block: Milliseconds to block (optional)
        noack: Don't require acknowledgment

    Returns:
        List of entries or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `group_name` | string | Yes |  |
| `consumer_name` | string | Yes |  |
| `count` | string | No |  |
| `block` | string | No |  |
| `noack` | boolean | No |  |

