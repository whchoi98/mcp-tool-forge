---
name: get-ssh-tunnel-command-replication-group
description: Generates an SSH tunnel command to connect to an ElastiCache replication group through an EC2 jump host.

    Args:
        replication_group_id (str): ID of the ElastiCache replication group to connect to
        instance_id (str): ID of the EC2 instance to use as jump host

    Returns:
        Dict[str, Union[str, int]]: Dictionary containing the SSH tunnel command and related details

    Raises:
        ValueError: If required resources not found or information cannot be retrieved
    
---

# Get-Ssh-Tunnel-Command-Replication-Group

Generates an SSH tunnel command to connect to an ElastiCache replication group through an EC2 jump host.

    Args:
        replication_group_id (str): ID of the ElastiCache replication group to connect to
        instance_id (str): ID of the EC2 instance to use as jump host

    Returns:
        Dict[str, Union[str, int]]: Dictionary containing the SSH tunnel command and related details

    Raises:
        ValueError: If required resources not found or information cannot be retrieved
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `replication_group_id` | string | Yes |  |
| `instance_id` | string | Yes |  |

