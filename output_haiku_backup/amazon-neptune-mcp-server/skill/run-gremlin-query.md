---
name: run-gremlin-query
description: Executes the provided Tinkerpop Gremlin against the graph.
---

# Run Gremlin Query

Executes the provided Tinkerpop Gremlin against the graph.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes |  |

## AWS CLI

```bash
aws neptune execute-gremlin-query --query <query>
```

## boto3

```python
import boto3

client = boto3.client('neptune')
response = client.execute_gremlin_query(
    Query=query,
)
```
