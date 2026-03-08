---
name: create-jump-host-replication-group
description: Creates an EC2 jump host instance to access an ElastiCache replication group via SSH tunnel.

    Args:
        replication_group_id (str): ID of the ElastiCache replication group to connect to
        key_name (str): Name of the EC2 key pair to use for SSH access
        subnet_id (str, optional): ID of the subnet to launch the EC2 instance in (must be public).
            If not provided and replication group uses default VPC, will auto-select a default subnet.
        security_group_id (str, optional): ID of the security group to assign to the EC2 instance.
            If not provided and replication group uses default VPC, will use the default security group.
        instance_type (str, optional): EC2 instance type. Defaults to "t3.small"

    Returns:
        Dict[str, Any]: Dictionary containing the created EC2 instance details

    Raises:
        ValueError: If subnet is not public or VPC compatibility check fails
    
---

# Create-Jump-Host-Replication-Group

Creates an EC2 jump host instance to access an ElastiCache replication group via SSH tunnel.

    Args:
        replication_group_id (str): ID of the ElastiCache replication group to connect to
        key_name (str): Name of the EC2 key pair to use for SSH access
        subnet_id (str, optional): ID of the subnet to launch the EC2 instance in (must be public).
            If not provided and replication group uses default VPC, will auto-select a default subnet.
        security_group_id (str, optional): ID of the security group to assign to the EC2 instance.
            If not provided and replication group uses default VPC, will use the default security group.
        instance_type (str, optional): EC2 instance type. Defaults to "t3.small"

    Returns:
        Dict[str, Any]: Dictionary containing the created EC2 instance details

    Raises:
        ValueError: If subnet is not public or VPC compatibility check fails
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `replication_group_id` | string | Yes |  |
| `key_name` | string | Yes |  |
| `subnet_id` | string | No |  |
| `security_group_id` | string | No |  |
| `instance_type` | string | No |  |

## AWS CLI

```bash
aws ec2 run-instances --key-name <key_name> --subnet-id <subnet_id> --security-group-ids <security_group_id> --instance-type <instance_type>
```

## boto3

```python
import boto3

client = boto3.client('ec2')
response = client.run_instances(
    KeyName=key_name,
    SubnetId=subnet_id,
    SecurityGroupIds=security_group_id,
    InstanceType=instance_type,
)
```
