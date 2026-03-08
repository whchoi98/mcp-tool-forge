---
name: list-dead-letter-source-queues
description: Execute the AWS Amazon SQS `list_dead_letter_source_queues` operation.
---

# List Dead Letter Source Queues

Execute the AWS Amazon SQS `list_dead_letter_source_queues` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `QueueUrl` | string | Yes |  |
| `NextToken` | string | No |  |
| `MaxResults` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs list-dead-letter-source-queues --queue-url <QueueUrl> --next-token <NextToken> --max-results <MaxResults>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.list_dead_letter_source_queues(
    QueueUrl=QueueUrl,
    NextToken=NextToken,
    MaxResults=MaxResults,
)
```
