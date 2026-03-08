---
name: create-replication-group
description: Create an Amazon ElastiCache replication group.

    This tool creates a new replication group with specified configuration including:
    - Basic replication group settings
    - Cache node configuration
    - Network and security settings
    - Encryption settings
    - Backup and maintenance settings
    - Monitoring and logging settings

    Args:
        request: The CreateReplicationGroupRequest object containing all parameters

    Returns:
        Dict containing information about the created replication group.
    
---

# Create-Replication-Group

Create an Amazon ElastiCache replication group.

    This tool creates a new replication group with specified configuration including:
    - Basic replication group settings
    - Cache node configuration
    - Network and security settings
    - Encryption settings
    - Backup and maintenance settings
    - Monitoring and logging settings

    Args:
        request: The CreateReplicationGroupRequest object containing all parameters

    Returns:
        Dict containing information about the created replication group.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | string | Yes |  |

## AWS CLI

```bash
aws elasticache create-replication-group --replication-group-id <request> --replication-group-description <request>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.create_replication_group(
    ReplicationGroupId=request,
    ReplicationGroupDescription=request,
)
```
