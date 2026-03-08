---
name: set-subscription-attributes
description: Execute the AWS Amazon SNS `set_subscription_attributes` operation.
---

# Set Subscription Attributes

Execute the AWS Amazon SNS `set_subscription_attributes` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `AttributeName` | string | Yes |  |
| `SubscriptionArn` | string | Yes |  |
| `AttributeValue` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns set-subscription-attributes --subscription-arn <SubscriptionArn> --attribute-name <AttributeName> --attribute-value <AttributeValue>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.set_subscription_attributes(
    SubscriptionArn=SubscriptionArn,
    AttributeName=AttributeName,
    AttributeValue=AttributeValue,
)
```
