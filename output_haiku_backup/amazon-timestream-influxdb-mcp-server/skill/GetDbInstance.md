---
name: GetDbInstance
description: Returns a Timestream for InfluxDB DB instance details by the instance-identifier
---

# Getdbinstance

Returns a Timestream for InfluxDB DB instance details by the instance-identifier

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `identifier` | string | Yes | The id of the DB instance. |

## AWS CLI

```bash
aws timestream-influxdb get-db-instance --db-instance-id <identifier>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.get_db_instance(
    DbInstanceId=identifier,
)
```
