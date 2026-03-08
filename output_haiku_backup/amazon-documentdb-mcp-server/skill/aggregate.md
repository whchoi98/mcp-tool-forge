---
name: aggregate
description: Run an aggregation pipeline against a DocumentDB collection.

    This tool executes a DocumentDB aggregation pipeline on a specified collection.

    Returns:
        List[Dict[str, Any]]: List of aggregation results
    
---

# Aggregate

Run an aggregation pipeline against a DocumentDB collection.

    This tool executes a DocumentDB aggregation pipeline on a specified collection.

    Returns:
        List[Dict[str, Any]]: List of aggregation results
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |
| `collection` | string | Yes | Name of the collection |
| `pipeline` | array | Yes | DocumentDB aggregation pipeline |
| `limit` | integer | No | Maximum number of documents to return (default: 10) |

## AWS CLI

```bash
aws docdb aggregate --connection-id <connection_id> --database <database> --collection <collection> --pipeline <pipeline> --limit <limit>
```

## boto3

```python
import boto3

client = boto3.client('docdb')
response = client.aggregate(
    ConnectionId=connection_id,
    DatabaseName=database,
    CollectionName=collection,
    Pipeline=pipeline,
    Limit=limit,
)
```
