---
name: TagResource
description: Tags are composed of a Key/Value pairs. Apply them to Timestream for InfluxDB resource.
---

# Tagresource

Tags are composed of a Key/Value pairs. Apply them to Timestream for InfluxDB resource.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_arn` | string | Yes | The Amazon Resource Name (ARN) of the tagged resource. |
| `tags` | object | Yes | A list of key-value pairs as tags. |
| `tool_write_mode` | boolean | No | Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False) |

## AWS CLI

```bash
aws timestream-influxdb tag-resource --resource-arn <resource_arn> --tags <tags>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.tag_resource(
    ResourceArn=resource_arn,
    Tags=tags,
)
```
