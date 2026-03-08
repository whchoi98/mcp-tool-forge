---
name: cancel-message-move-task
description: Execute the AWS Amazon SQS `cancel_message_move_task` operation.
---

# Cancel Message Move Task

Execute the AWS Amazon SQS `cancel_message_move_task` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `TaskHandle` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs cancel-message-move-task --task-handle <TaskHandle> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.cancel_message_move_task(
    TaskHandle=TaskHandle,
    Region=region,
)
```
