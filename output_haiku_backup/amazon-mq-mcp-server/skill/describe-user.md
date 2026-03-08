---
name: describe-user
description: Execute the AWS AmazonMQ `describe_user` operation.
---

# Describe User

Execute the AWS AmazonMQ `describe_user` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `Username` | string | Yes |  |
| `BrokerId` | string | Yes |  |

## AWS CLI

```bash
aws mq describe-user --broker-id <BrokerId> --username <Username> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.describe_user(
    BrokerId=BrokerId,
    Username=Username,
)
```
