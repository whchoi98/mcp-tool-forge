---
name: publish-batch
description: Execute the AWS Amazon SNS `publish_batch` operation.
---

# Publish Batch

Execute the AWS Amazon SNS `publish_batch` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `PublishBatchRequestEntries` | array | Yes |  |
| `TopicArn` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns publish-batch --topic-arn <TopicArn> --publish-batch-request-entries <PublishBatchRequestEntries>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.publish_batch(
    PublishBatchRequestEntries=PublishBatchRequestEntries,
    TopicArn=TopicArn,
)
```
