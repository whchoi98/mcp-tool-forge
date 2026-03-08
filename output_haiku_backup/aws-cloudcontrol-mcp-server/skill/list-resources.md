---
name: list-resources
description: List AWS resources of a specified type.

    Parameters:
        resource_type: The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
        region: AWS region to use (e.g., "us-east-1", "us-west-2")


    Returns:
        A dictionary containing:
        {
            "resources": List of resource identifiers
        }
    
---

# List Resources

List AWS resources of a specified type.

    Parameters:
        resource_type: The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance")
        region: AWS region to use (e.g., "us-east-1", "us-west-2")


    Returns:
        A dictionary containing:
        {
            "resources": List of resource identifiers
        }
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_type` | string | Yes | The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance") |
| `region` | string | No | The AWS region that the operation should be performed in |
| `analyze_security` | boolean | No | Whether to perform security analysis on the resources (limited to first 5 resources) |
| `max_resources_to_analyze` | integer | No | Maximum number of resources to analyze when analyze_security=True |

