---
name: list-queues
description: Execute the AWS Amazon SQS `list_queues` operation.
---

# List Queues

Execute the AWS Amazon SQS `list_queues` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `QueueNamePrefix` | string | No |  |
| `NextToken` | string | No |  |
| `MaxResults` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sqs list-queues --queue-name-prefix <QueueNamePrefix> --next-token <NextToken> --max-results <MaxResults>
```

## boto3

```python
import boto3

client = boto3.client('sqs')
response = client.list_queues(
    QueueNamePrefix=QueueNamePrefix,
    NextToken=NextToken,
    MaxResults=MaxResults,
)
```
