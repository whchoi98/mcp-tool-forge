---
name: get-graph-schema
description: Get the schema for the graph including the vertex and edge labels as well as the
    (vertex)-[edge]->(vertex) combinations.
    
---

# Get Graph Schema

Get the schema for the graph including the vertex and edge labels as well as the
    (vertex)-[edge]->(vertex) combinations.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|

## AWS CLI

```bash
aws neptune get-graph-schema
```

## boto3

```python
import boto3

client = boto3.client('neptune')
response = client.get_graph_schema(
)
```
