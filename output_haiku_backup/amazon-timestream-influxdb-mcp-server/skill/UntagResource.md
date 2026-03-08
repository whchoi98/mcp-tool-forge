---
name: UntagResource
description: Removes the tags, identified by the keys, from the specified resource.
---

# Untagresource

Removes the tags, identified by the keys, from the specified resource.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_arn` | string | Yes | The Amazon Resource Name (ARN) of the tagged resource. |
| `tag_keys` | array | Yes | The keys used to identify the tags to remove. |
| `tool_write_mode` | boolean | No | Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False) |

## AWS CLI

```bash
aws timestream-influxdb untag-resource --resource-arn <resource_arn> --tag-keys <tag_keys>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.untag_resource(
    ResourceArn=resource_arn,
    TagKeys=tag_keys,
)
```
