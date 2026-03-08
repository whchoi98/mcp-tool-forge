---
name: set-topic-attributes
description: Execute the AWS Amazon SNS `set_topic_attributes` operation.
---

# Set Topic Attributes

Execute the AWS Amazon SNS `set_topic_attributes` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `AttributeName` | string | Yes |  |
| `TopicArn` | string | Yes |  |
| `AttributeValue` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns set-topic-attributes --topic-arn <TopicArn> --attribute-name <AttributeName> --attribute-value <AttributeValue>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.set_topic_attributes(
    TopicArn=TopicArn,
    AttributeName=AttributeName,
    AttributeValue=AttributeValue,
)
```
