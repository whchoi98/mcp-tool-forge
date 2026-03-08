---
name: listDatabases
description: List all available databases in the DocumentDB cluster.

    This tool returns the names of all accessible databases in the connected cluster.

    Returns:
        Dict[str, Any]: List of database names
    
---

# Listdatabases

List all available databases in the DocumentDB cluster.

    This tool returns the names of all accessible databases in the connected cluster.

    Returns:
        Dict[str, Any]: List of database names
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |

