---
name: describe-broker-engine-types
description: Execute the AWS AmazonMQ `describe_broker_engine_types` operation.
---

# Describe Broker Engine Types

Execute the AWS AmazonMQ `describe_broker_engine_types` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `EngineType` | string | No | <p>Filter response by engine type.</p> |
| `MaxResults` | integer | No | <p>The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p> |
| `NextToken` | string | No | <p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p> |

## AWS CLI

```bash
aws mq describe-broker-engine-types --engine-type <EngineType> --max-results <MaxResults> --next-token <NextToken>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.describe_broker_engine_types(
    EngineType=EngineType,
    MaxResults=MaxResults,
    NextToken=NextToken,
)
```
