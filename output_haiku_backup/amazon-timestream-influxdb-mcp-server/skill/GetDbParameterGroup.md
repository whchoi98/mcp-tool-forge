---
name: GetDbParameterGroup
description: Get a Timestream for InfluxDB DB parameter group details for a db_parameter_group_id
---

# Getdbparametergroup

Get a Timestream for InfluxDB DB parameter group details for a db_parameter_group_id

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `identifier` | string | Yes | The id of the DB parameter group. |

## AWS CLI

```bash
aws timestream-influxdb get-db-parameter-group --db-parameter-group-identifier <identifier>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.get_db_parameter_group(
    DbParameterGroupIdentifier=identifier,
)
```
