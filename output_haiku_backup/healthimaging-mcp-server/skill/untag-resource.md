---
name: untag-resource
description: Remove tags from a resource.
---

# Untag Resource

Remove tags from a resource.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_arn` | string | Yes | The ARN of the resource to untag |
| `tag_keys` | array | Yes | The tag keys to remove from the resource |

## AWS CLI

```bash
aws healthimaging untag-resource --resource-arn <resource_arn> --tag-keys <tag_keys>
```

## boto3

```python
import boto3

client = boto3.client('healthimaging')
response = client.untag_resource(
    ResourceArn=resource_arn,
    TagKeys=tag_keys,
)
```
