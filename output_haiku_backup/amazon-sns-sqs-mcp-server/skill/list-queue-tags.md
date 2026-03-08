---
name: list-queue-tags
description: Execute the AWS Amazon SQS `list_queue_tags` operation.
---

# List Queue Tags

Execute the AWS Amazon SQS `list_queue_tags` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `QueueUrl` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs list-queue-tags --queue-url <QueueUrl> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.list_queue_tags(
    QueueUrl=QueueUrl,
    Region=region,
)
```
