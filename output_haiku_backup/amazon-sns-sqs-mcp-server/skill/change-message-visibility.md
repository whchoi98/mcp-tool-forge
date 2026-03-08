---
name: change-message-visibility
description: Execute the AWS Amazon SQS `change_message_visibility` operation.
---

# Change Message Visibility

Execute the AWS Amazon SQS `change_message_visibility` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `VisibilityTimeout` | integer | Yes |  |
| `ReceiptHandle` | string | Yes |  |
| `QueueUrl` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs change-message-visibility --visibility-timeout <VisibilityTimeout> --receipt-handle <ReceiptHandle> --queue-url <QueueUrl>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.change_message_visibility(
    VisibilityTimeout=VisibilityTimeout,
    ReceiptHandle=ReceiptHandle,
    QueueUrl=QueueUrl,
)
```
