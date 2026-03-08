---
name: list-tags-for-resource
description: Execute the AWS Amazon SNS `list_tags_for_resource` operation.
---

# List Tags For Resource

Execute the AWS Amazon SNS `list_tags_for_resource` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ResourceArn` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns list-tags-for-resource --resource-arn <ResourceArn> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.list_tags_for_resource(
    ResourceArn=ResourceArn,
)
```
