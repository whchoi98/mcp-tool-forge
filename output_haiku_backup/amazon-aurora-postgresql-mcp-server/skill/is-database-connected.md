---
name: is-database-connected
description: Check if a connection has been established
---

# Is Database Connected

Check if a connection has been established

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_identifier` | string | Yes | cluster identifier |
| `db_endpoint` | string | No | database endpoint |
| `database` | string | No | database name |

## AWS CLI

```bash
aws rds describe-db-clusters --db-cluster-identifier <cluster_identifier>
```

## boto3

```python
import boto3

client = boto3.client('rds')
response = client.describe_db_clusters(
    DBClusterIdentifier=cluster_identifier,
)
```
