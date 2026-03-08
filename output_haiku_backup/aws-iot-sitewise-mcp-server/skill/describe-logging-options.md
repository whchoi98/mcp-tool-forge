---
name: describe-logging-options
description: Retrieve the current AWS IoT SiteWise logging options.

    Args:
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing logging options
    
---

# Describe Logging Options

Retrieve the current AWS IoT SiteWise logging options.

    Args:
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing logging options
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise describe-logging-options --region <region>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_logging_options(
    Region=region,
)
```
