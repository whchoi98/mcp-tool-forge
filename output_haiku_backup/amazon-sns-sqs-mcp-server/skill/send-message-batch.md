---
name: send-message-batch
description: Execute the AWS Amazon SQS `send_message_batch` operation.
---

# Send Message Batch

Execute the AWS Amazon SQS `send_message_batch` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Entries` | array | Yes |  |
| `QueueUrl` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs send-message-batch --queue-url <QueueUrl> --entries <Entries>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.send_message_batch(
    QueueUrl=QueueUrl,
    Entries=Entries,
)
```
