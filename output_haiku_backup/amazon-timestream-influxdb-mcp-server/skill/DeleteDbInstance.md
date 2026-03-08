---
name: DeleteDbInstance
description: Deletes a Timestream for InfluxDB DB instance by the instance-identifier
---

# Deletedbinstance

Deletes a Timestream for InfluxDB DB instance by the instance-identifier

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `identifier` | string | Yes | The id of the DB instance. |
| `tool_write_mode` | boolean | No | Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False) |

## AWS CLI

```bash
aws timestream-influxdb delete-db-instance --db-instance-id <identifier>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.delete_db_instance(
    DbInstanceId=identifier,
)
```
