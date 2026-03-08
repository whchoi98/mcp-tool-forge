---
name: bitmap-pos
description: Find positions of bits set to a specific value.

    Args:
        key: The name of the bitmap key
        bit: Bit value to search for (0 or 1)
        start: Start offset (inclusive, optional)
        end: End offset (inclusive, optional)
        count: Maximum number of positions to return (optional)

    Returns:
        List of positions or error message
    
---

# Bitmap Pos

Find positions of bits set to a specific value.

    Args:
        key: The name of the bitmap key
        bit: Bit value to search for (0 or 1)
        start: Start offset (inclusive, optional)
        end: End offset (inclusive, optional)
        count: Maximum number of positions to return (optional)

    Returns:
        List of positions or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `bit` | integer | Yes |  |
| `start` | string | No |  |
| `end` | string | No |  |
| `count` | string | No |  |

