---
name: get-resource-schema-information
description: Get schema information for an AWS resource.

    Parameters:
        resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")

    Returns:
        The resource schema information
    
---

# Get Resource Schema Information

Get schema information for an AWS resource.

    Parameters:
        resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")

    Returns:
        The resource schema information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_type` | string | Yes | The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance") |
| `region` | string | No | The AWS region that the operation should be performed in |

## AWS CLI

```bash
aws cloudcontrol get-resource-schema --type-name <resource_type> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('cloudcontrol')
response = client.get_resource_schema(
    TypeName=resource_type,
    Region=region,
)
```
