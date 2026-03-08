---
name: delete
description: Delete documents from a DocumentDB collection.

    This tool deletes documents that match a specified filter.

    Returns:
        Dict[str, Any]: Delete operation results
    
---

# Delete

Delete documents from a DocumentDB collection.

    This tool deletes documents that match a specified filter.

    Returns:
        Dict[str, Any]: Delete operation results
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |
| `collection` | string | Yes | Name of the collection |
| `filter` | object | Yes | Filter to select documents to delete |
| `many` | boolean | No | Whether to delete multiple documents (default: False) |

## AWS CLI

```bash
aws docdb delete-documents --connection-id <connection_id> --database-name <database> --collection-name <collection> --filter <filter> --many <many>
```

## boto3

```python
import boto3

client = boto3.client('docdb')
response = client.delete_documents(
    ConnectionId=connection_id,
    DatabaseName=database,
    CollectionName=collection,
    Filter=filter,
    Many=many,
)
```
