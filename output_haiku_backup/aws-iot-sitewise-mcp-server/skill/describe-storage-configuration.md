---
name: describe-storage-configuration
description: Retrieve information about the storage configuration for your AWS account.

    Args:
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing storage configuration
    
---

# Describe Storage Configuration

Retrieve information about the storage configuration for your AWS account.

    Args:
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing storage configuration
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise describe-storage-configuration --region <region>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_storage_configuration(
    Region=region,
)
```
