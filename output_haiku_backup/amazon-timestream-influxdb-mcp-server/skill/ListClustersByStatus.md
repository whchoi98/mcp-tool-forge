---
name: ListClustersByStatus
description: Returns a list of Timestream for InfluxDB DB clusters filtered by status (case-insensitive).
---

# Listclustersbystatus

Returns a list of Timestream for InfluxDB DB clusters filtered by status (case-insensitive).

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `status` | string | Yes | The status to filter DB clusters by (case-insensitive). |

## AWS CLI

```bash
aws timestream-influxdb list-clusters --cluster-status <status>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.list_clusters(
    ClusterStatus=status,
)
```
