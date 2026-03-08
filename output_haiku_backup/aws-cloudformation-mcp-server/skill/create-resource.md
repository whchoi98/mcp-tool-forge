---
name: create-resource
description: Create an AWS resource.

    Parameters:
        resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")
        properties: A dictionary of properties for the resource
        region: AWS region to use (e.g., "us-east-1", "us-west-2")

    Returns:
        Information about the created resource with a consistent structure:
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

# Create Resource

Create an AWS resource.

    Parameters:
        resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")
        properties: A dictionary of properties for the resource
        region: AWS region to use (e.g., "us-east-1", "us-west-2")

    Returns:
        Information about the created resource with a consistent structure:
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
| `properties` | object | Yes | A dictionary of properties for the resource |
| `region` | string | No | The AWS region that the operation should be performed in |

## AWS CLI

```bash
aws cloudformation create-stack --stack-name <resource_type> --template-body <properties> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('cloudformation')
response = client.create_stack(
    StackName=resource_type,
    TemplateBody=properties,
    Region=region,
)
```
