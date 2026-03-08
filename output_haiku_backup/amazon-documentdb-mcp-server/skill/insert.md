---
name: insert
description: Insert one or more documents into a DocumentDB collection.

    This tool inserts new documents into a specified collection.

    Returns:
        Dict[str, Any]: Insert operation results including document IDs
    
---

# Insert

Insert one or more documents into a DocumentDB collection.

    This tool inserts new documents into a specified collection.

    Returns:
        Dict[str, Any]: Insert operation results including document IDs
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |
| `collection` | string | Yes | Name of the collection |
| `documents` | string | Yes | Document or list of documents to insert |

## AWS CLI

```bash
aws docdb insert-documents --connection-id <connection_id> --database-name <database> --collection-name <collection> --documents <documents>
```

## boto3

```python
import boto3

client = boto3.client('docdb')
response = client.insert_documents(
    ConnectionId=connection_id,
    DatabaseName=database,
    CollectionName=collection,
    Documents=documents,
)
```
