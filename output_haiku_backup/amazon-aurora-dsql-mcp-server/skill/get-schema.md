---
name: get-schema
description: Get the schema of the given table
---

# Get Schema

Get the schema of the given table

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `table_name` | string | Yes | name of the table |

## AWS CLI

```bash
aws rds describe-db-cluster-endpoints --db-cluster-endpoint-identifier <table_name>
```

## boto3

```python
import boto3

client = boto3.client('rds')
response = client.describe_db_cluster_endpoints(
    DBClusterEndpointIdentifier=table_name,
)
```
