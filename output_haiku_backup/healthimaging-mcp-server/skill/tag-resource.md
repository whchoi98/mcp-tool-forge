---
name: tag-resource
description: Add tags to a resource.
---

# Tag Resource

Add tags to a resource.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_arn` | string | Yes | The ARN of the resource to tag |
| `tags` | object | Yes | The tags to apply to the resource |

## AWS CLI

```bash
aws healthimaging tag-resource --resource-arn <resource_arn> --tags <tags>
```

## boto3

```python
import boto3

client = boto3.client('healthimaging')
response = client.tag_resource(
    ResourceArn=resource_arn,
    Tags=tags,
)
```
