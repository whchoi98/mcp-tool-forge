---
name: ListTagsForResource
description: A list of tags applied to the resource.
---

# Listtagsforresource

A list of tags applied to the resource.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_arn` | string | Yes | The Amazon Resource Name (ARN) of the tagged resource. |

## AWS CLI

```bash
aws timestream-influxdb list-tags-for-resource --resource-arn <resource_arn>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.list_tags_for_resource(
    ResourceArn=resource_arn,
)
```
