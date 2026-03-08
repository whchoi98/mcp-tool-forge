---
name: stream-add
description: Add entry to stream.

    Args:
        key: The name of the key
        field_dict: Dictionary of field-value pairs
        id: Entry ID (default "*" for auto-generation)
        maxlen: Maximum length of stream (optional)
        approximate: Whether maxlen is approximate

    Returns:
        Success message or error message
    
---

# Stream Add

Add entry to stream.

    Args:
        key: The name of the key
        field_dict: Dictionary of field-value pairs
        id: Entry ID (default "*" for auto-generation)
        maxlen: Maximum length of stream (optional)
        approximate: Whether maxlen is approximate

    Returns:
        Success message or error message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | string | Yes |  |
| `field_dict` | object | Yes |  |
| `id` | string | No |  |
| `maxlen` | string | No |  |
| `approximate` | boolean | No |  |

