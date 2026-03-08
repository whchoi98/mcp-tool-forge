---
name: subscribe
description: Execute AWS SNS Subscribe. Ensure that you set correct permission policies if required.
---

# Subscribe

Execute AWS SNS Subscribe. Ensure that you set correct permission policies if required.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Protocol` | string | Yes |  |
| `TopicArn` | string | Yes |  |
| `Endpoint` | string | No |  |
| `Attributes` | string | No |  |
| `ReturnSubscriptionArn` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns subscribe --protocol <Protocol> --topic-arn <TopicArn> --endpoint <Endpoint> --attributes <Attributes> --return-subscription-arn <ReturnSubscriptionArn> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.subscribe(
    Protocol=Protocol,
    TopicArn=TopicArn,
    Endpoint=Endpoint,
    Attributes=Attributes,
    ReturnSubscriptionArn=ReturnSubscriptionArn,
)
```
