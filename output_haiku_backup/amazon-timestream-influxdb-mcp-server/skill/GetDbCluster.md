---
name: GetDbCluster
description: Returns a Timestream for InfluxDB DB cluster details by the db_cluster_id
---

# Getdbcluster

Returns a Timestream for InfluxDB DB cluster details by the db_cluster_id

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `db_cluster_id` | string | Yes | Service-generated unique identifier of the DB cluster. |

## AWS CLI

```bash
aws timestream-influxdb get-db-cluster --db-cluster-id <db_cluster_id>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.get_db_cluster(
    DbClusterId=db_cluster_id,
)
```
