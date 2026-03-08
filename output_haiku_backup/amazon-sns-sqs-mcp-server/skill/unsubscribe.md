---
name: unsubscribe
description: Execute the AWS Amazon SNS `unsubscribe` operation.
---

# Unsubscribe

Execute the AWS Amazon SNS `unsubscribe` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `SubscriptionArn` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns unsubscribe --subscription-arn <SubscriptionArn>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.unsubscribe(
    SubscriptionArn=SubscriptionArn,
)
```
