---
name: describe-broker
description: Execute the AWS AmazonMQ `describe_broker` operation.
---

# Describe Broker

Execute the AWS AmazonMQ `describe_broker` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `BrokerId` | string | Yes |  |

## AWS CLI

```bash
aws mq describe-broker --broker-id <BrokerId> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.describe_broker(
    BrokerId=BrokerId,
    Region=region,
)
```
