---
name: LsInstancesByStatus
description: Returns a list of Timestream for InfluxDB DB instances filtered by status (case-insensitive).
---

# Lsinstancesbystatus

Returns a list of Timestream for InfluxDB DB instances filtered by status (case-insensitive).

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `status` | string | Yes | The status to filter DB instances by (case-insensitive). |

## AWS CLI

```bash
aws timestream-influxdb list-db-instances --status <status>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.list_db_instances(
    Status=status,
)
```
