---
name: delete-message
description: Execute the AWS Amazon SQS `delete_message` operation.
---

# Delete Message

Execute the AWS Amazon SQS `delete_message` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ReceiptHandle` | string | Yes |  |
| `QueueUrl` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs delete-message --queue-url <QueueUrl> --receipt-handle <ReceiptHandle>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.delete_message(
    QueueUrl=QueueUrl,
    ReceiptHandle=ReceiptHandle,
)
```
