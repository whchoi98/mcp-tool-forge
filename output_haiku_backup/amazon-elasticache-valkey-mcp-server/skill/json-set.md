---
name: json-set
description: Set the JSON value at path.

    Args:
        key: The name of the key
        path: The path in the JSON document (e.g., "$.name" or "." for root)
        value: The value to set
        nx: Only set if path doesn't exist
        xx: Only set if path exists

    Returns:
        Success message or error message
    
---

# Json Set

Set the JSON value at path.

    Args:
        key: The name of the key
        path: The path in the JSON document (e.g., "$.name" or "." for root)
        value: The value to set
        nx: Only set if path doesn't exist
        xx: Only set if path exists

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `path` | string | Yes |  |
| `value` | string | Yes |  |
| `nx` | boolean | No |  |
| `xx` | boolean | No |  |

