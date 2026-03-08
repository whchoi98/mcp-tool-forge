---
name: get-topic-attributes
description: Execute the AWS Amazon SNS `get_topic_attributes` operation.
---

# Get Topic Attributes

Execute the AWS Amazon SNS `get_topic_attributes` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `TopicArn` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns get-topic-attributes --topic-arn <TopicArn>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.get_topic_attributes(
    TopicArn=TopicArn,
)
```
