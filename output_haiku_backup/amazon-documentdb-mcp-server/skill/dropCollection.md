---
name: dropCollection
description: Drop a collection from a DocumentDB database.

    This tool completely removes a collection and all its documents from the specified database.
    This operation cannot be undone, so use it with caution.

    Returns:
        Dict[str, Any]: Status of the drop operation
    
---

# Dropcollection

Drop a collection from a DocumentDB database.

    This tool completely removes a collection and all its documents from the specified database.
    This operation cannot be undone, so use it with caution.

    Returns:
        Dict[str, Any]: Status of the drop operation
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |
| `collection` | string | Yes | Name of the collection to drop |

## AWS CLI

```bash
aws docdb delete-collection --cluster-identifier <connection_id> --database-name <database> --collection-name <collection>
```

## boto3

```python
import boto3

client = boto3.client('docdb')
response = client.delete_collection(
    ClusterIdentifier=connection_id,
    DatabaseName=database,
    CollectionName=collection,
)
```
