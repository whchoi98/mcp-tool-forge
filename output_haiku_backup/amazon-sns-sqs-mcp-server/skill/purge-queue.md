---
name: purge-queue
description: Execute the AWS Amazon SQS `purge_queue` operation.
---

# Purge Queue

Execute the AWS Amazon SQS `purge_queue` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `QueueUrl` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs purge-queue --queue-url <QueueUrl> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.purge_queue(
    QueueUrl=QueueUrl,
    Region=region,
)
```
