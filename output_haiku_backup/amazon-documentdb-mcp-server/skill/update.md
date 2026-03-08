---
name: update
description: Update documents in a DocumentDB collection.

    This tool updates existing documents that match a specified filter.

    Returns:
        Dict[str, Any]: Update operation results
    
---

# Update

Update documents in a DocumentDB collection.

    This tool updates existing documents that match a specified filter.

    Returns:
        Dict[str, Any]: Update operation results
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |
| `collection` | string | Yes | Name of the collection |
| `filter` | object | Yes | Filter to select documents to update |
| `update` | object | Yes | Update operations to apply. It should either include DocumentDB operators like $set, or an entire document if the entire document needs to be replaced. |
| `upsert` | boolean | No | Whether to create a new document if no match is found (default: False) |
| `many` | boolean | No | Whether to update multiple documents (default: False) |

## AWS CLI

```bash
aws docdb update-documents --connection-id <connection_id> --database-name <database> --collection-name <collection> --filter <filter> --update <update> --upsert <upsert> --many <many>
```

## boto3

```python
import boto3

client = boto3.client('docdb')
response = client.update_documents(
    ConnectionId=connection_id,
    DatabaseName=database,
    CollectionName=collection,
    Filter=filter,
    Update=update,
    Upsert=upsert,
    Many=many,
)
```
