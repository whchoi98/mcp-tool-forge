---
name: list-move
description: Move element from one list to another.

    Args:
        source: Source list key
        destination: Destination list key
        wherefrom: Where to pop from ("LEFT" or "RIGHT")
        whereto: Where to push to ("LEFT" or "RIGHT")

    Returns:
        Moved value or error message
    
---

# List Move

Move element from one list to another.

    Args:
        source: Source list key
        destination: Destination list key
        wherefrom: Where to pop from ("LEFT" or "RIGHT")
        whereto: Where to push to ("LEFT" or "RIGHT")

    Returns:
        Moved value or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source` | string | Yes |  |
| `destination` | string | Yes |  |
| `wherefrom` | string | No |  |
| `whereto` | string | No |  |

