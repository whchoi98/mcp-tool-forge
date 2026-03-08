---
name: get-ssh-tunnel-command-serverless-cache
description: Generates an SSH tunnel command to connect to an ElastiCache serverless cache through an EC2 jump host.

    Args:
        serverless_cache_name (str): Name of the ElastiCache serverless cache to connect to
        instance_id (str): ID of the EC2 instance to use as jump host

    Returns:
        Dict[str, Union[str, int]]: Dictionary containing the SSH tunnel command and related details

    Raises:
        ValueError: If required resources not found or information cannot be retrieved
    
---

# Get-Ssh-Tunnel-Command-Serverless-Cache

Generates an SSH tunnel command to connect to an ElastiCache serverless cache through an EC2 jump host.

    Args:
        serverless_cache_name (str): Name of the ElastiCache serverless cache to connect to
        instance_id (str): ID of the EC2 instance to use as jump host

    Returns:
        Dict[str, Union[str, int]]: Dictionary containing the SSH tunnel command and related details

    Raises:
        ValueError: If required resources not found or information cannot be retrieved
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serverless_cache_name` | string | Yes |  |
| `instance_id` | string | Yes |  |

