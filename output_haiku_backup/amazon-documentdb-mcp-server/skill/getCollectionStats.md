---
name: getCollectionStats
description: Get statistics about a DocumentDB collection.

    This tool retrieves detailed statistics about the specified collection,
    including size, document count, and storage information.

    Returns:
        Dict[str, Any]: Collection statistics
    
---

# Getcollectionstats

Get statistics about a DocumentDB collection.

    This tool retrieves detailed statistics about the specified collection,
    including size, document count, and storage information.

    Returns:
        Dict[str, Any]: Collection statistics
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |
| `collection` | string | Yes | Name of the collection |

