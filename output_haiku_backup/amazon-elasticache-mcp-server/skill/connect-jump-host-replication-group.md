---
name: connect-jump-host-replication-group
description: Configures an existing EC2 instance as a jump host to access an ElastiCache replication group.

    Args:
        replication_group_id (str): ID of the ElastiCache replication group to connect to
        instance_id (str): ID of the EC2 instance to use as jump host

    Returns:
        Dict[str, Any]: Dictionary containing connection details and configuration status

    Raises:
        ValueError: If VPC compatibility check fails or required resources not found
    
---

# Connect-Jump-Host-Replication-Group

Configures an existing EC2 instance as a jump host to access an ElastiCache replication group.

    Args:
        replication_group_id (str): ID of the ElastiCache replication group to connect to
        instance_id (str): ID of the EC2 instance to use as jump host

    Returns:
        Dict[str, Any]: Dictionary containing connection details and configuration status

    Raises:
        ValueError: If VPC compatibility check fails or required resources not found
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `replication_group_id` | string | Yes |  |
| `instance_id` | string | Yes |  |

