---
name: get-subscription-attributes
description: Execute the AWS Amazon SNS `get_subscription_attributes` operation.
---

# Get Subscription Attributes

Execute the AWS Amazon SNS `get_subscription_attributes` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `SubscriptionArn` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns get-subscription-attributes --subscription-arn <SubscriptionArn> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.get_subscription_attributes(
    SubscriptionArn=SubscriptionArn,
)
```
