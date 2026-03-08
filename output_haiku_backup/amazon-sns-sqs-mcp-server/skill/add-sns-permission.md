---
name: add-sns-permission
description: Execute the AWS Amazon SNS `add_permission` operation.
---

# Add Sns Permission

Execute the AWS Amazon SNS `add_permission` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ActionName` | array | Yes |  |
| `AWSAccountId` | array | Yes |  |
| `Label` | string | Yes |  |
| `TopicArn` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns add-permission --topic-arn <TopicArn> --label <Label> --aws-account-id <AWSAccountId> --action-name <ActionName>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.add_permission(
    TopicArn=TopicArn,
    Label=Label,
    AWSAccountId=AWSAccountId,
    ActionName=ActionName,
)
```
