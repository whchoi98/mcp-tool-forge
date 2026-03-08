---
name: start-message-move-task
description: Execute the AWS Amazon SQS `start_message_move_task` operation.
---

# Start Message Move Task

Execute the AWS Amazon SQS `start_message_move_task` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `SourceArn` | string | Yes |  |
| `DestinationArn` | string | No |  |
| `MaxNumberOfMessagesPerSecond` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs start-message-move-task --source-arn <SourceArn> --destination-arn <DestinationArn> --max-number-of-messages-per-second <MaxNumberOfMessagesPerSecond>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.start_message_move_task(
    SourceArn=SourceArn,
    DestinationArn=DestinationArn,
    MaxNumberOfMessagesPerSecond=MaxNumberOfMessagesPerSecond,
)
```
