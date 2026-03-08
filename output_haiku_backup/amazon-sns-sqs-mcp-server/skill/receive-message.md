---
name: receive-message
description: Execute the AWS Amazon SQS `receive_message` operation.
---

# Receive Message

Execute the AWS Amazon SQS `receive_message` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `QueueUrl` | string | Yes |  |
| `AttributeNames` | string | No |  |
| `MessageSystemAttributeNames` | string | No |  |
| `MessageAttributeNames` | string | No |  |
| `MaxNumberOfMessages` | string | No |  |
| `VisibilityTimeout` | string | No |  |
| `WaitTimeSeconds` | string | No |  |
| `ReceiveRequestAttemptId` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs receive-message --queue-url <QueueUrl> --attribute-names <AttributeNames> --message-system-attribute-names <MessageSystemAttributeNames> --message-attribute-names <MessageAttributeNames> --max-number-of-messages <MaxNumberOfMessages> --visibility-timeout <VisibilityTimeout> --wait-time-seconds <WaitTimeSeconds> --receive-request-attempt-id <ReceiveRequestAttemptId>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.receive_message(
    QueueUrl=QueueUrl,
    AttributeNames=AttributeNames,
    MessageSystemAttributeNames=MessageSystemAttributeNames,
    MessageAttributeNames=MessageAttributeNames,
    MaxNumberOfMessages=MaxNumberOfMessages,
    VisibilityTimeout=VisibilityTimeout,
    WaitTimeSeconds=WaitTimeSeconds,
    ReceiveRequestAttemptId=ReceiveRequestAttemptId,
)
```
