---
name: start-migration
description: Start migration to an Amazon ElastiCache replication group.

    This tool starts migration from a Redis instance to an ElastiCache replication group.
    It initiates the data migration process from the specified endpoint(s) to
    the target replication group.

    Args:
        request: The StartMigrationRequest object containing:
            - replication_group_id: The ID of the replication group to which data should be migrated
            - customer_node_endpoint_list: List of endpoints from which data should be migrated.
              For Valkey or Redis OSS (cluster mode disabled), the list should have only one element.

    Returns:
        Dict containing information about the migration start result.
    
---

# Start-Migration

Start migration to an Amazon ElastiCache replication group.

    This tool starts migration from a Redis instance to an ElastiCache replication group.
    It initiates the data migration process from the specified endpoint(s) to
    the target replication group.

    Args:
        request: The StartMigrationRequest object containing:
            - replication_group_id: The ID of the replication group to which data should be migrated
            - customer_node_endpoint_list: List of endpoints from which data should be migrated.
              For Valkey or Redis OSS (cluster mode disabled), the list should have only one element.

    Returns:
        Dict containing information about the migration start result.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | string | Yes |  |

## AWS CLI

```bash
aws elasticache modify-replication-group --replication-group-id <request> --replicas-migration <True>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.modify_replication_group(
    ReplicationGroupId=request,
    ReplicasMigration=True,
)
```
