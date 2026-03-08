---
name: stream-group-create
description: Create consumer group.

    Args:
        key: The name of the key
        group_name: Name of consumer group
        id: ID to start reading from (default "$" for new entries only)
        mkstream: Create stream if it doesn't exist

    Returns:
        Success message or error message
    
---

# Stream Group Create

Create consumer group.

    Args:
        key: The name of the key
        group_name: Name of consumer group
        id: ID to start reading from (default "$" for new entries only)
        mkstream: Create stream if it doesn't exist

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `group_name` | string | Yes |  |
| `id` | string | No |  |
| `mkstream` | boolean | No |  |

