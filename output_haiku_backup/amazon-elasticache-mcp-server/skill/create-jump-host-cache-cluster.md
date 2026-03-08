---
name: create-jump-host-cache-cluster
description: Creates an EC2 jump host instance to access an ElastiCache cluster via SSH tunnel.

    Args:
        cache_cluster_id (str): ID of the ElastiCache cluster to connect to
        key_name (str): Name of the EC2 key pair to use for SSH access
        subnet_id (str, optional): ID of the subnet to launch the EC2 instance in (must be public).
            If not provided and cache uses default VPC, will auto-select a default subnet.
        security_group_id (str, optional): ID of the security group to assign to the EC2 instance.
            If not provided and cache uses default VPC, will use the default security group.
        instance_type (str, optional): EC2 instance type. Defaults to "t3.small"

    Returns:
        Dict[str, Any]: Dictionary containing the created EC2 instance details

    Raises:
        ValueError: If subnet is not public or VPC compatibility check fails
    
---

# Create-Jump-Host-Cache-Cluster

Creates an EC2 jump host instance to access an ElastiCache cluster via SSH tunnel.

    Args:
        cache_cluster_id (str): ID of the ElastiCache cluster to connect to
        key_name (str): Name of the EC2 key pair to use for SSH access
        subnet_id (str, optional): ID of the subnet to launch the EC2 instance in (must be public).
            If not provided and cache uses default VPC, will auto-select a default subnet.
        security_group_id (str, optional): ID of the security group to assign to the EC2 instance.
            If not provided and cache uses default VPC, will use the default security group.
        instance_type (str, optional): EC2 instance type. Defaults to "t3.small"

    Returns:
        Dict[str, Any]: Dictionary containing the created EC2 instance details

    Raises:
        ValueError: If subnet is not public or VPC compatibility check fails
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cache_cluster_id` | string | Yes |  |
| `key_name` | string | Yes |  |
| `subnet_id` | string | No |  |
| `security_group_id` | string | No |  |
| `instance_type` | string | No |  |

