---
name: update-configuration
description: Execute the AWS AmazonMQ `update_configuration` operation.
---

# Update Configuration

Execute the AWS AmazonMQ `update_configuration` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `Data` | string | Yes |  |
| `ConfigurationId` | string | Yes |  |
| `Description` | string | No | <p>The description of the configuration.</p> |

## AWS CLI

```bash
aws mq update-configuration --configuration-id <ConfigurationId> --data <Data> --description <Description>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.update_configuration(
    ConfigurationId=ConfigurationId,
    Data=Data,
    Description=Description,
)
```
