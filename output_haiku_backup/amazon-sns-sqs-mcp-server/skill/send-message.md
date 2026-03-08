---
name: send-message
description: Execute the AWS Amazon SQS `send_message` operation.
---

# Send Message

Execute the AWS Amazon SQS `send_message` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `MessageBody` | string | Yes |  |
| `QueueUrl` | string | Yes |  |
| `DelaySeconds` | string | No |  |
| `MessageAttributes` | string | No |  |
| `MessageSystemAttributes` | string | No |  |
| `MessageDeduplicationId` | string | No |  |
| `MessageGroupId` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs send-message --queue-url <QueueUrl> --message-body <MessageBody> --delay-seconds <DelaySeconds> --message-attributes <MessageAttributes> --message-system-attributes <MessageSystemAttributes> --message-deduplication-id <MessageDeduplicationId> --message-group-id <MessageGroupId>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.send_message(
    QueueUrl=QueueUrl,
    MessageBody=MessageBody,
    DelaySeconds=DelaySeconds,
    MessageAttributes=MessageAttributes,
    MessageSystemAttributes=MessageSystemAttributes,
    MessageDeduplicationId=MessageDeduplicationId,
    MessageGroupId=MessageGroupId,
)
```
