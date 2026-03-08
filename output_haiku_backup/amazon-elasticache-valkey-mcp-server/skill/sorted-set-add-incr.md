---
name: sorted-set-add-incr
description: Add member to sorted set or increment its score.

    Args:
        key: The name of the key
        member: The member to add/update
        score: Score to add to existing score (or initial score)

    Returns:
        Success message or error message
    
---

# Sorted Set Add Incr

Add member to sorted set or increment its score.

    Args:
        key: The name of the key
        member: The member to add/update
        score: Score to add to existing score (or initial score)

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `member` | string | Yes |  |
| `score` | number | Yes |  |

