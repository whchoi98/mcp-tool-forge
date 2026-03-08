---
name: remove-sqs-permission
description: Execute the AWS Amazon SQS `remove_permission` operation.
---

# Remove Sqs Permission

Execute the AWS Amazon SQS `remove_permission` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Label` | string | Yes |  |
| `QueueUrl` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs remove-permission --queue-url <QueueUrl> --label <Label> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.remove_permission(
    QueueUrl=QueueUrl,
    Label=Label,
)
```
