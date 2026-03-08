---
name: get-queue-url
description: Execute the AWS Amazon SQS `get_queue_url` operation.
---

# Get Queue Url

Execute the AWS Amazon SQS `get_queue_url` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `QueueName` | string | Yes |  |
| `QueueOwnerAWSAccountId` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs get-queue-url --queue-name <QueueName> --queue-owner-aws-account-id <QueueOwnerAWSAccountId>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.get_queue_url(
    QueueName=QueueName,
    QueueOwnerAWSAccountId=QueueOwnerAWSAccountId,
)
```
