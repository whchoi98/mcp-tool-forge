---
name: describe-default-encryption-config
description: Retrieve information about the default encryption configuration for your AWS account.

    Args:
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing default encryption configuration
    
---

# Describe Default Encryption Config

Retrieve information about the default encryption configuration for your AWS account.

    Args:
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing default encryption configuration
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise describe-default-encryption-configuration --region <region>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_default_encryption_configuration(
    Region=region,
)
```
