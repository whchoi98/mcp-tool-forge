---
name: describe-broker-instance-options
description: Execute the AWS AmazonMQ `describe_broker_instance_options` operation.
---

# Describe Broker Instance Options

Execute the AWS AmazonMQ `describe_broker_instance_options` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `EngineType` | string | No | <p>Filter response by engine type.</p> |
| `HostInstanceType` | string | No | <p>Filter response by host instance type.</p> |
| `MaxResults` | integer | No | <p>The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p> |
| `NextToken` | string | No | <p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p> |
| `StorageType` | string | No | <p>Filter response by storage type.</p> |

## AWS CLI

```bash
aws mq describe-broker-instance-options --region <region> --engine-type <EngineType> --host-instance-type <HostInstanceType> --max-results <MaxResults> --next-token <NextToken> --storage-type <StorageType>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.describe_broker_instance_options(
    EngineType=EngineType,
    HostInstanceType=HostInstanceType,
    MaxResults=MaxResults,
    NextToken=NextToken,
    StorageType=StorageType,
)
```
