---
name: connect-jump-host-serverless-cache
description: Configures an existing EC2 instance as a jump host to access an ElastiCache serverless cache.

    Args:
        serverless_cache_name (str): Name of the ElastiCache serverless cache to connect to
        instance_id (str): ID of the EC2 instance to use as jump host

    Returns:
        Dict[str, Any]: Dictionary containing connection details and configuration status

    Raises:
        ValueError: If VPC compatibility check fails or required resources not found
    
---

# Connect-Jump-Host-Serverless-Cache

Configures an existing EC2 instance as a jump host to access an ElastiCache serverless cache.

    Args:
        serverless_cache_name (str): Name of the ElastiCache serverless cache to connect to
        instance_id (str): ID of the EC2 instance to use as jump host

    Returns:
        Dict[str, Any]: Dictionary containing connection details and configuration status

    Raises:
        ValueError: If VPC compatibility check fails or required resources not found
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serverless_cache_name` | string | Yes |  |
| `instance_id` | string | Yes |  |

