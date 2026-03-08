---
name: get-configuration-info
description: Gets information about MSK configurations.
---

# Get Configuration Info

Gets information about MSK configurations.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region |
| `action` | string | Yes | The operation to perform: 'describe', 'revisions', or 'revision_details' |
| `arn` | string | Yes | The Amazon Resource Name (ARN) of the configuration |
| `kwargs` | object | No | Additional arguments based on the action |

## AWS CLI

```bash
aws kafka describe-configuration --configuration-arn <arn> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('kafka')
response = client.describe_configuration(
    ConfigurationArn=arn,
    Region=region,
)
```
