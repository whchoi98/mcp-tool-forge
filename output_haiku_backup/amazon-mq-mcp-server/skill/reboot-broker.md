---
name: reboot-broker
description: Execute the AWS AmazonMQ `reboot_broker` operation.
---

# Reboot Broker

Execute the AWS AmazonMQ `reboot_broker` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `BrokerId` | string | Yes |  |

## AWS CLI

```bash
aws mq reboot-broker --broker-id <BrokerId> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.reboot_broker(
    BrokerId=BrokerId,
    Region=region,
)
```
