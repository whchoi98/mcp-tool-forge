---
name: update-resource
description: Update an AWS resource.

    Parameters:
        resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")
        identifier: The primary identifier of the resource to update
        patch_document: A list of RFC 6902 JSON Patch operations to apply
        region: AWS region to use (e.g., "us-east-1", "us-west-2")

    Returns:
        Information about the updated resource with a consistent structure:
        {
            "status": Status of the operation ("SUCCESS", "PENDING", "FAILED", etc.)
            "resource_type": The AWS resource type
            "identifier": The resource identifier
            "is_complete": Boolean indicating whether the operation is complete
            "status_message": Human-readable message describing the result
            "request_token": A token that allows you to track long running operations via the get_resource_request_status tool
            "resource_info": Optional information about the resource properties
        }
    
---

# Update Resource

Update an AWS resource.

    Parameters:
        resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")
        identifier: The primary identifier of the resource to update
        patch_document: A list of RFC 6902 JSON Patch operations to apply
        region: AWS region to use (e.g., "us-east-1", "us-west-2")

    Returns:
        Information about the updated resource with a consistent structure:
        {
            "status": Status of the operation ("SUCCESS", "PENDING", "FAILED", etc.)
            "resource_type": The AWS resource type
            "identifier": The resource identifier
            "is_complete": Boolean indicating whether the operation is complete
            "status_message": Human-readable message describing the result
            "request_token": A token that allows you to track long running operations via the get_resource_request_status tool
            "resource_info": Optional information about the resource properties
        }
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_type` | string | Yes | The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance") |
| `identifier` | string | Yes | The primary identifier of the resource to get (e.g., bucket name for S3 buckets) |
| `patch_document` | array | No | A list of RFC 6902 JSON Patch operations to apply |
| `region` | string | No | The AWS region that the operation should be performed in |

## AWS CLI

```bash
aws cloudformation update-stack --stack-name <identifier> --template-body <patch_document> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('cloudformation')
response = client.update_stack(
    StackName=identifier,
    TemplateBody=patch_document,
    Region=region,
)
```
