---
name: list-subscriptions-by-topic
description: Execute the AWS Amazon SNS `list_subscriptions_by_topic` operation.
---

# List Subscriptions By Topic

Execute the AWS Amazon SNS `list_subscriptions_by_topic` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `TopicArn` | string | Yes |  |
| `NextToken` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns list-subscriptions-by-topic --topic-arn <TopicArn> --next-token <NextToken> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.list_subscriptions_by_topic(
    TopicArn=TopicArn,
    NextToken=NextToken,
)
```
