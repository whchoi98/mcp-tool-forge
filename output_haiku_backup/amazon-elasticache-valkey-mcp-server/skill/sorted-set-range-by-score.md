---
name: sorted-set-range-by-score
description: Get range of members by score.

    Args:
        key: The name of the key
        min_score: Minimum score (inclusive)
        max_score: Maximum score (inclusive)
        withscores: Include scores in result
        reverse: Return results in reverse order
        offset: Number of members to skip
        count: Maximum number of members to return

    Returns:
        List of members (with scores if requested) or error message
    
---

# Sorted Set Range By Score

Get range of members by score.

    Args:
        key: The name of the key
        min_score: Minimum score (inclusive)
        max_score: Maximum score (inclusive)
        withscores: Include scores in result
        reverse: Return results in reverse order
        offset: Number of members to skip
        count: Maximum number of members to return

    Returns:
        List of members (with scores if requested) or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `min_score` | number | Yes |  |
| `max_score` | number | Yes |  |
| `withscores` | boolean | No |  |
| `reverse` | boolean | No |  |
| `offset` | string | No |  |
| `count` | string | No |  |

