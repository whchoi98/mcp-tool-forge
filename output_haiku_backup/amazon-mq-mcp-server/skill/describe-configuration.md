---
name: describe-configuration
description: Execute the AWS AmazonMQ `describe_configuration` operation.
---

# Describe Configuration

Execute the AWS AmazonMQ `describe_configuration` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `ConfigurationId` | string | Yes |  |

## AWS CLI

```bash
aws mq describe-configuration --configuration-id <ConfigurationId> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.describe_configuration(
    ConfigurationId=ConfigurationId,
    Region=region,
)
```
