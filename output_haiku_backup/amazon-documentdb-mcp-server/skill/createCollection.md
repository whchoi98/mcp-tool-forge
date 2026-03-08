---
name: createCollection
description: Create a new collection in a DocumentDB database.

    This tool creates a new collection in the specified database.

    Returns:
        Dict[str, Any]: Status of collection creation
    
---

# Createcollection

Create a new collection in a DocumentDB database.

    This tool creates a new collection in the specified database.

    Returns:
        Dict[str, Any]: Status of collection creation
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |
| `collection` | string | Yes | Name of the collection to create |

## AWS CLI

```bash
aws docdb create-collection --cluster-identifier <connection_id> --database-name <database> --collection-name <collection>
```

## boto3

```python
import boto3

client = boto3.client('docdb')
response = client.create_collection(
    ClusterIdentifier=connection_id,
    DatabaseName=database,
    CollectionName=collection,
)
```
