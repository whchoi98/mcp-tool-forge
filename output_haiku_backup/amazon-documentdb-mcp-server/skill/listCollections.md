---
name: listCollections
description: List collections in a DocumentDB database.

    This tool returns the names of all collections in a specified database.

    Returns:
        List[str]: List of collection names
    
---

# Listcollections

List collections in a DocumentDB database.

    This tool returns the names of all collections in a specified database.

    Returns:
        List[str]: List of collection names
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |

