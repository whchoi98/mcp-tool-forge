---
name: json-arrtrim
description: Trim array at path to include only elements within range.

    Args:
        key: The name of the key
        path: The path in the JSON document
        start: Start index (inclusive)
        stop: Stop index (inclusive)

    Returns:
        New array length or error message
    
---

# Json Arrtrim

Trim array at path to include only elements within range.

    Args:
        key: The name of the key
        path: The path in the JSON document
        start: Start index (inclusive)
        stop: Stop index (inclusive)

    Returns:
        New array length or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `path` | string | Yes |  |
| `start` | integer | Yes |  |
| `stop` | integer | Yes |  |

