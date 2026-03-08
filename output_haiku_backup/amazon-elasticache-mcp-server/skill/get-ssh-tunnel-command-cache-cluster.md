---
name: get-ssh-tunnel-command-cache-cluster
description: Generates an SSH tunnel command to connect to an ElastiCache cluster through an EC2 jump host.

    Args:
        cache_cluster_id (str): ID of the ElastiCache cluster to connect to
        instance_id (str): ID of the EC2 instance to use as jump host

    Returns:
        Dict[str, Union[str, int]]: Dictionary containing the SSH tunnel command and related details

    Raises:
        ValueError: If required resources not found or information cannot be retrieved
    
---

# Get-Ssh-Tunnel-Command-Cache-Cluster

Generates an SSH tunnel command to connect to an ElastiCache cluster through an EC2 jump host.

    Args:
        cache_cluster_id (str): ID of the ElastiCache cluster to connect to
        instance_id (str): ID of the EC2 instance to use as jump host

    Returns:
        Dict[str, Union[str, int]]: Dictionary containing the SSH tunnel command and related details

    Raises:
        ValueError: If required resources not found or information cannot be retrieved
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cache_cluster_id` | string | Yes |  |
| `instance_id` | string | Yes |  |

