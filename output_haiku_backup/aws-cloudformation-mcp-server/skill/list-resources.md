---
name: list-resources
description: List AWS resources of a specified type.

    Parameters:
        resource_type: The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
        region: AWS region to use (e.g., "us-east-1", "us-west-2")

    Returns:
        A list of resource identifiers
    
---

# List Resources

List AWS resources of a specified type.

    Parameters:
        resource_type: The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
        region: AWS region to use (e.g., "us-east-1", "us-west-2")

    Returns:
        A list of resource identifiers
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_type` | string | Yes | The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance") |
| `region` | string | No | The AWS region that the operation should be performed in |

## AWS CLI

```bash
aws cloudformation list-stack-resources --stack-name <resource_type> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('cloudformation')
response = client.list_stack_resources(
    StackName=resource_type,
)
```
