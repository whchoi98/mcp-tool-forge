---
name: sorted-set-range
description: Get range of members from sorted set.

    Args:
        key: The name of the key
        start: Start index (inclusive)
        stop: Stop index (inclusive)
        withscores: Include scores in result
        reverse: Return results in reverse order

    Returns:
        List of members (with scores if requested) or error message
    
---

# Sorted Set Range

Get range of members from sorted set.

    Args:
        key: The name of the key
        start: Start index (inclusive)
        stop: Stop index (inclusive)
        withscores: Include scores in result
        reverse: Return results in reverse order

    Returns:
        List of members (with scores if requested) or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `start` | integer | No |  |
| `stop` | integer | No |  |
| `withscores` | boolean | No |  |
| `reverse` | boolean | No |  |

