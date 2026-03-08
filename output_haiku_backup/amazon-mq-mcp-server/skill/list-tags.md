---
name: list-tags
description: Execute the AWS AmazonMQ `list_tags` operation.
---

# List Tags

Execute the AWS AmazonMQ `list_tags` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `ResourceArn` | string | Yes |  |

## AWS CLI

```bash
aws mq list-tags-for-resource --resource-arn <ResourceArn> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.list_tags(
    ResourceArn=ResourceArn,
    Region=region,
)
```
