---
name: describe-configuration-revision
description: Execute the AWS AmazonMQ `describe_configuration_revision` operation.
---

# Describe Configuration Revision

Execute the AWS AmazonMQ `describe_configuration_revision` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `ConfigurationRevision` | string | Yes |  |
| `ConfigurationId` | string | Yes |  |

## AWS CLI

```bash
aws mq describe-configuration-revision --configuration-id <ConfigurationId> --configuration-revision <ConfigurationRevision>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.describe_configuration_revision(
    ConfigurationId=ConfigurationId,
    ConfigurationRevision=ConfigurationRevision,
)
```
