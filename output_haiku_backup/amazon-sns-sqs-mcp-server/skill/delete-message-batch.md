---
name: delete-message-batch
description: Execute the AWS Amazon SQS `delete_message_batch` operation.
---

# Delete Message Batch

Execute the AWS Amazon SQS `delete_message_batch` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Entries` | array | Yes |  |
| `QueueUrl` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs delete-message-batch --queue-url <QueueUrl> --entries <Entries>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.delete_message_batch(
    QueueUrl=QueueUrl,
    Entries=Entries,
)
```
