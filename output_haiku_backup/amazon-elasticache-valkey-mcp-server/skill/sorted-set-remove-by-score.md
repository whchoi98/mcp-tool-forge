---
name: sorted-set-remove-by-score
description: Remove members by score range.

    Args:
        key: The name of the key
        min_score: Minimum score (inclusive)
        max_score: Maximum score (inclusive)

    Returns:
        Success message or error message
    
---

# Sorted Set Remove By Score

Remove members by score range.

    Args:
        key: The name of the key
        min_score: Minimum score (inclusive)
        max_score: Maximum score (inclusive)

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `min_score` | number | Yes |  |
| `max_score` | number | Yes |  |

