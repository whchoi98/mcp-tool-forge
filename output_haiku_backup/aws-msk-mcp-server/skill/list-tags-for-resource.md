---
name: list-tags-for-resource
description: Lists all tags for an MSK resource.
---

# List Tags For Resource

Lists all tags for an MSK resource.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region |
| `arn` | string | Yes | The Amazon Resource Name (ARN) of the resource |

## AWS CLI

```bash
aws kafka list-tags-for-resource --resource-arn <arn> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('kafka')
response = client.list_tags_for_resource(
    ResourceArn=arn,
    Region=region,
)
```
