---
name: getDatabaseStats
description: Get statistics about a DocumentDB database.

    This tool retrieves statistics about the specified database,
    including storage information and collection data.

    Returns:
        Dict[str, Any]: Database statistics
    
---

# Getdatabasestats

Get statistics about a DocumentDB database.

    This tool retrieves statistics about the specified database,
    including storage information and collection data.

    Returns:
        Dict[str, Any]: Database statistics
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |

