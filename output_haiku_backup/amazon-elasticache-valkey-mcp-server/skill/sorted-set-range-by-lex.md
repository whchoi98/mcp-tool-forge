---
name: sorted-set-range-by-lex
description: Get range of members by lexicographical order.

    Args:
        key: The name of the key
        min_lex: Minimum value (inclusive)
        max_lex: Maximum value (inclusive)
        reverse: Return results in reverse order
        offset: Number of members to skip
        count: Maximum number of members to return

    Returns:
        List of members or error message
    
---

# Sorted Set Range By Lex

Get range of members by lexicographical order.

    Args:
        key: The name of the key
        min_lex: Minimum value (inclusive)
        max_lex: Maximum value (inclusive)
        reverse: Return results in reverse order
        offset: Number of members to skip
        count: Maximum number of members to return

    Returns:
        List of members or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `min_lex` | string | Yes |  |
| `max_lex` | string | Yes |  |
| `reverse` | boolean | No |  |
| `offset` | string | No |  |
| `count` | string | No |  |

