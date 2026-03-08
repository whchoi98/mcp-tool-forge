---
name: create-cluster
description: Create an Aurora Postgres cluster
---

# Create Cluster

Create an Aurora Postgres cluster

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | region |
| `cluster_identifier` | string | Yes | cluster identifier |
| `database` | string | No | default database name |
| `engine_version` | string | No | engine version |

## AWS CLI

```bash
aws rds create-db-cluster --cluster-identifier <cluster_identifier> --engine <aurora-postgresql> --engine-version <engine_version> --database-name <database> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('rds')
response = client.create_db_cluster(
    ClusterIdentifier=cluster_identifier,
    Engine=aurora-postgresql,
    EngineVersion=engine_version,
    DatabaseName=database,
    Region=region,
)
```
