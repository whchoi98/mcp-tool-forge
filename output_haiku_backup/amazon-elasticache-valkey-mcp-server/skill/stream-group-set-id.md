---
name: stream-group-set-id
description: Set consumer group's last delivered ID.

    Args:
        key: The name of the key
        group_name: Name of consumer group
        id: ID to set as last delivered

    Returns:
        Success message or error message
    
---

# Stream Group Set Id

Set consumer group's last delivered ID.

    Args:
        key: The name of the key
        group_name: Name of consumer group
        id: ID to set as last delivered

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `group_name` | string | Yes |  |
| `id` | string | Yes |  |

