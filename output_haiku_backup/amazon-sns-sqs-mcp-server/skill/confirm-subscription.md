---
name: confirm-subscription
description: Execute the AWS Amazon SNS `confirm_subscription` operation.
---

# Confirm Subscription

Execute the AWS Amazon SNS `confirm_subscription` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Token` | string | Yes |  |
| `TopicArn` | string | Yes |  |
| `AuthenticateOnUnsubscribe` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns confirm-subscription --token <Token> --topic-arn <TopicArn> --authenticate-on-unsubscribe <AuthenticateOnUnsubscribe> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.confirm_subscription(
    Token=Token,
    TopicArn=TopicArn,
    AuthenticateOnUnsubscribe=AuthenticateOnUnsubscribe,
)
```
