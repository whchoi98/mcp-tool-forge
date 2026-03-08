---
name: add-sqs-permission
description: Execute the AWS Amazon SQS `add_permission` operation.
---

# Add Sqs Permission

Execute the AWS Amazon SQS `add_permission` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Actions` | array | Yes |  |
| `AWSAccountIds` | array | Yes |  |
| `Label` | string | Yes |  |
| `QueueUrl` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs add-permission --actions <Actions> --aws-account-ids <AWSAccountIds> --label <Label> --queue-url <QueueUrl>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.add_permission(
    Actions=Actions,
    AWSAccountIds=AWSAccountIds,
    Label=Label,
    QueueUrl=QueueUrl,
)
```
