---
name: set-queue-attributes
description: Execute the AWS Amazon SQS `set_queue_attributes` operation.
---

# Set Queue Attributes

Execute the AWS Amazon SQS `set_queue_attributes` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Attributes` | object | Yes |  |
| `QueueUrl` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs set-queue-attributes --queue-url <QueueUrl> --attributes <Attributes>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.set_queue_attributes(
    QueueUrl=QueueUrl,
    Attributes=Attributes,
)
```
