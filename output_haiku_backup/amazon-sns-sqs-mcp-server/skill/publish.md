---
name: publish
description: Execute the AWS Amazon SNS `publish` operation.
---

# Publish

Execute the AWS Amazon SNS `publish` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Message` | string | Yes |  |
| `TopicArn` | string | No |  |
| `TargetArn` | string | No |  |
| `PhoneNumber` | string | No |  |
| `Subject` | string | No |  |
| `MessageStructure` | string | No |  |
| `MessageAttributes` | string | No |  |
| `MessageDeduplicationId` | string | No |  |
| `MessageGroupId` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns publish --message <Message> --topic-arn <TopicArn> --target-arn <TargetArn> --phone-number <PhoneNumber> --subject <Subject> --message-structure <MessageStructure> --message-attributes <MessageAttributes> --message-deduplication-id <MessageDeduplicationId> --message-group-id <MessageGroupId>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.publish(
    Message=Message,
    TopicArn=TopicArn,
    TargetArn=TargetArn,
    PhoneNumber=PhoneNumber,
    Subject=Subject,
    MessageStructure=MessageStructure,
    MessageAttributes=MessageAttributes,
    MessageDeduplicationId=MessageDeduplicationId,
    MessageGroupId=MessageGroupId,
)
```
