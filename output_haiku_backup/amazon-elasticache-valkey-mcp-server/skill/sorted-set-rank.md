---
name: sorted-set-rank
description: Get rank of member in sorted set.

    Args:
        key: The name of the key
        member: The member to get rank for
        reverse: If True, get rank in reverse order (highest first)

    Returns:
        Rank or error message
    
---

# Sorted Set Rank

Get rank of member in sorted set.

    Args:
        key: The name of the key
        member: The member to get rank for
        reverse: If True, get rank in reverse order (highest first)

    Returns:
        Rank or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `member` | string | Yes |  |
| `reverse` | boolean | No |  |

