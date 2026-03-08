---
name: run-opencypher-query
description: Executes the provided openCypher against the graph.
---

# Run Opencypher Query

Executes the provided openCypher against the graph.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes |  |
| `parameters` | string | No |  |

## AWS CLI

```bash
aws neptune execute-open-cypher-query --query <query> --parameters <parameters>
```

## boto3

```python
import boto3

client = boto3.client('neptune')
response = client.execute_open_cypher_query(
    Query=query,
    Parameters=parameters,
)
```
