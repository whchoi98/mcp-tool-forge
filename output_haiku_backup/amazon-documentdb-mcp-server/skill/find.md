---
name: find
description: Run a query against a DocumentDB collection.

    This tool queries documents from a specified collection based on a filter.

    Returns:
        List[Dict[str, Any]]: List of matching documents
    
---

# Find

Run a query against a DocumentDB collection.

    This tool queries documents from a specified collection based on a filter.

    Returns:
        List[Dict[str, Any]]: List of matching documents
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |
| `collection` | string | Yes | Name of the collection |
| `query` | object | Yes | Query filter (e.g., {"name": "example"}) |
| `projection` | string | No | Fields to include/exclude (e.g., {"_id": 0, "name": 1}) |
| `limit` | integer | No | Maximum number of documents to return (default: 10) |

## AWS CLI

```bash
aws docdb find-documents --connection-id <connection_id> --database-name <database> --collection-name <collection> --filter <query> --projection <projection> --max-results <limit>
```

## boto3

```python
import boto3

client = boto3.client('docdb')
response = client.find_documents(
    ConnectionId=connection_id,
    DatabaseName=database,
    CollectionName=collection,
    Filter=query,
    Projection=projection,
    MaxResults=limit,
)
```
