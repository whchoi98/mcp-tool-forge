---
name: list-tags-for-resource
description: List tags for a resource.
---

# List Tags For Resource

List tags for a resource.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_arn` | string | Yes | The ARN of the resource to list tags for |

## AWS CLI

```bash
aws healthimaging list-tags-for-resource --resource-arn <resource_arn>
```

## boto3

```python
import boto3

client = boto3.client('healthimaging')
response = client.list_tags_for_resource(
    ResourceArn=resource_arn,
)
```
