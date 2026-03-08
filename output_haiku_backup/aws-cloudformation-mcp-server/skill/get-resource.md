---
name: get-resource
description: Get details of a specific AWS resource.

    Parameters:
        resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")
        identifier: The primary identifier of the resource to get (e.g., bucket name for S3 buckets)
        region: AWS region to use (e.g., "us-east-1", "us-west-2")

    Returns:
        Detailed information about the specified resource with a consistent structure:
        {
            "identifier": The resource identifier,
            "properties": The detailed information about the resource
        }
    
---

# Get Resource

Get details of a specific AWS resource.

    Parameters:
        resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")
        identifier: The primary identifier of the resource to get (e.g., bucket name for S3 buckets)
        region: AWS region to use (e.g., "us-east-1", "us-west-2")

    Returns:
        Detailed information about the specified resource with a consistent structure:
        {
            "identifier": The resource identifier,
            "properties": The detailed information about the resource
        }
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_type` | string | Yes | The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance") |
| `identifier` | string | Yes | The primary identifier of the resource to get (e.g., bucket name for S3 buckets) |
| `region` | string | No | The AWS region that the operation should be performed in |

## AWS CLI

```bash
aws cloudformation describe-stack-resources --stack-name <identifier> --logical-resource-id <resource_type> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('cloudformation')
response = client.describe_stack_resource(
    StackName=identifier,
    LogicalResourceId=resource_type,
    StackResourceName=identifier,
)
```
