---
name: get-queue-attributes
description: Execute the AWS Amazon SQS `get_queue_attributes` operation.
---

# Get Queue Attributes

Execute the AWS Amazon SQS `get_queue_attributes` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `QueueUrl` | string | Yes |  |
| `AttributeNames` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs get-queue-attributes --queue-url <QueueUrl> --attribute-names <AttributeNames> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.get_queue_attributes(
    QueueUrl=QueueUrl,
    AttributeNames=AttributeNames,
)
```
