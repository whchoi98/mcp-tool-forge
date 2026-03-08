---
name: list-message-move-tasks
description: Execute the AWS Amazon SQS `list_message_move_tasks` operation.
---

# List Message Move Tasks

Execute the AWS Amazon SQS `list_message_move_tasks` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `SourceArn` | string | Yes |  |
| `MaxResults` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs list-message-move-tasks --source-arn <SourceArn> --max-results <MaxResults> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.list_message_move_tasks(
    SourceArn=SourceArn,
    MaxResults=MaxResults,
)
```
