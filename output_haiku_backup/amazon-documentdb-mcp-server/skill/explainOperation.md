---
name: explainOperation
description: Get an explanation of how an operation will be executed.

    This tool returns the execution plan for a query or aggregation operation,
    helping you understand how DocumentDB will process your operations.

    Returns:
        Dict[str, Any]: Operation explanation
    
---

# Explainoperation

Get an explanation of how an operation will be executed.

    This tool returns the execution plan for a query or aggregation operation,
    helping you understand how DocumentDB will process your operations.

    Returns:
        Dict[str, Any]: Operation explanation
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |
| `collection` | string | Yes | Name of the collection |
| `operation_type` | string | Yes | Type of operation to explain (find, aggregate) |
| `query` | string | No | Query for find operations |
| `pipeline` | string | No | Pipeline for DocumentDB aggregation operations |
| `verbosity` | string | No | Explanation verbosity level (queryPlanner, executionStats) |

## AWS CLI

```bash
aws docdb explain-operation --connection-id <connection_id> --database-name <database> --collection-name <collection> --operation-type <operation_type> --query <query> --pipeline <pipeline> --verbosity <verbosity>
```

## boto3

```python
import boto3

client = boto3.client('docdb')
response = client.explain_operation(
    ConnectionId=connection_id,
    DatabaseName=database,
    CollectionName=collection,
    OperationType=operation_type,
    Query=query,
    Pipeline=pipeline,
    Verbosity=verbosity,
)
```
