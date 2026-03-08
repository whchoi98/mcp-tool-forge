---
name: list-configuration-revisions
description: Execute the AWS AmazonMQ `list_configuration_revisions` operation.
---

# List Configuration Revisions

Execute the AWS AmazonMQ `list_configuration_revisions` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `ConfigurationId` | string | Yes |  |
| `MaxResults` | integer | No | <p>The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p> |
| `NextToken` | string | No | <p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p> |

## AWS CLI

```bash
aws mq list-configuration-revisions --configuration-id <ConfigurationId> --max-results <MaxResults> --next-token <NextToken>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.list_configuration_revisions(
    ConfigurationId=ConfigurationId,
    MaxResults=MaxResults,
    NextToken=NextToken,
)
```
