---
name: change-message-visibility-batch
description: Execute the AWS Amazon SQS `change_message_visibility_batch` operation.
---

# Change Message Visibility Batch

Execute the AWS Amazon SQS `change_message_visibility_batch` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Entries` | array | Yes |  |
| `QueueUrl` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs change-message-visibility-batch --queue-url <QueueUrl> --entries <Entries>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.change_message_visibility_batch(
    QueueUrl=QueueUrl,
    Entries=Entries,
)
```
