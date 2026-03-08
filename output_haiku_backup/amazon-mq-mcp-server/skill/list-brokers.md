---
name: list-brokers
description: Execute the AWS AmazonMQ `list_brokers` operation.
---

# List Brokers

Execute the AWS AmazonMQ `list_brokers` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `MaxResults` | integer | No | <p>The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p> |
| `NextToken` | string | No | <p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p> |

## AWS CLI

```bash
aws mq list-brokers --region <region> --max-results <MaxResults> --next-token <NextToken>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.list_brokers(
    Region=region,
    MaxResults=MaxResults,
    NextToken=NextToken,
)
```
