---
name: DeleteDbCluster
description: Deletes a Timestream for InfluxDB cluster by the db_cluster_id
---

# Deletedbcluster

Deletes a Timestream for InfluxDB cluster by the db_cluster_id

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `db_cluster_id` | string | Yes | Service-generated unique identifier of the DB cluster. |
| `tool_write_mode` | boolean | No | Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False) |

## AWS CLI

```bash
aws timestream-influxdb delete-db-cluster --db-cluster-id <db_cluster_id>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.delete_db_cluster(
    DbClusterId=db_cluster_id,
)
```
