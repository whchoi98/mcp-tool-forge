---
name: list-subscriptions
description: Execute the AWS Amazon SNS `list_subscriptions` operation.
---

# List Subscriptions

Execute the AWS Amazon SNS `list_subscriptions` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `NextToken` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns list-subscriptions --next-token <NextToken> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.list_subscriptions(
    NextToken=NextToken,
    Region=region,
)
```
