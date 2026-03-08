---
name: list-topics
description: Execute the AWS Amazon SNS `list_topics` operation.
---

# List Topics

Execute the AWS Amazon SNS `list_topics` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `NextToken` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns list-topics --next-token <NextToken> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.list_topics(
    NextToken=NextToken,
)
```
