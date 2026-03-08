---
name: promote
description: Execute the AWS AmazonMQ `promote` operation.
---

# Promote

Execute the AWS AmazonMQ `promote` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `Mode` | string | Yes |  |
| `BrokerId` | string | Yes |  |

## AWS CLI

```bash
aws mq promote-broker --broker-id <BrokerId> --mode <Mode>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.promote_broker(
    BrokerId=BrokerId,
    Mode=Mode,
)
```
