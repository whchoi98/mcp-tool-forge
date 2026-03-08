---
name: delete-configuration
description: Execute the AWS AmazonMQ `delete_configuration` operation.
---

# Delete Configuration

Execute the AWS AmazonMQ `delete_configuration` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `ConfigurationId` | string | Yes |  |

## AWS CLI

```bash
aws mq delete-configuration --configuration-id <ConfigurationId> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.delete_configuration(
    ConfigurationId=ConfigurationId,
)
```
