---
name: bitmap-set
description: Set the bit at offset to value.

    Args:
        key: The name of the bitmap key
        offset: The bit offset (0-based)
        value: The bit value (0 or 1)

    Returns:
        Success message or error message
    
---

# Bitmap Set

Set the bit at offset to value.

    Args:
        key: The name of the bitmap key
        offset: The bit offset (0-based)
        value: The bit value (0 or 1)

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `offset` | integer | Yes |  |
| `value` | integer | Yes |  |

