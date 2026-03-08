---
name: countDocuments
description: Count documents in a DocumentDB collection.

    This tool counts the number of documents in a collection that match the provided filter.
    If no filter is provided, it counts all documents.

    Returns:
        Dict[str, Any]: Count result
    
---

# Countdocuments

Count documents in a DocumentDB collection.

    This tool counts the number of documents in a collection that match the provided filter.
    If no filter is provided, it counts all documents.

    Returns:
        Dict[str, Any]: Count result
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |
| `collection` | string | Yes | Name of the collection |
| `filter` | string | No | Query filter to count specific documents |

## AWS CLI

```bash
aws docdb count-documents --connection-id <connection_id> --database <database> --collection <collection> --filter <filter>
```

## boto3

```python
import boto3

client = boto3.client('docdb')
response = client.count_documents(
    ConnectionId=connection_id,
    DatabaseName=database,
    CollectionName=collection,
    Filter=filter,
)
```
