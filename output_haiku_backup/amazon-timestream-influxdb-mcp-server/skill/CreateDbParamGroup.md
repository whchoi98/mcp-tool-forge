---
name: CreateDbParamGroup
description: Creates a new Timestream for InfluxDB DB parameter group to associate with DB instances.
---

# Createdbparamgroup

Creates a new Timestream for InfluxDB DB parameter group to associate with DB instances.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | string | Yes | The name of the DB parameter group. The name must be unique per customer and per region. |
| `tool_write_mode` | boolean | No | Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False) |
| `description` | string | No | A description of the DB parameter group. |
| `parameters` | string | No | A list of the parameters that comprise the DB parameter group. |
| `tags` | string | No | A list of tags to assign to the DB. |

## AWS CLI

```bash
aws timestream-influxdb create-db-parameter-group --name <name> --description <description> --parameters <parameters> --tags <tags>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.create_db_parameter_group(
    Name=name,
    Description=description,
    Parameters=parameters,
    Tags=tags,
)
```
