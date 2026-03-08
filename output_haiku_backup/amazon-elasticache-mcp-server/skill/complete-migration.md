---
name: complete-migration
description: Complete migration to an Amazon ElastiCache replication group.

    This tool completes the migration of data from a Redis instance to an ElastiCache replication group.
    It finalizes the data migration process and transitions the replication group to normal operation.

    Args:
        request: The CompleteMigrationRequest object containing:
            - replication_group_id: The ID of the replication group to which data is being migrated
            - force: (Optional) Forces the migration to stop without ensuring that data is in sync.
              It is recommended to use this option only to abort the migration and not recommended
              when application wants to continue migration to ElastiCache.

    Returns:
        Dict containing information about the migration completion result.
    
---

# Complete-Migration

Complete migration to an Amazon ElastiCache replication group.

    This tool completes the migration of data from a Redis instance to an ElastiCache replication group.
    It finalizes the data migration process and transitions the replication group to normal operation.

    Args:
        request: The CompleteMigrationRequest object containing:
            - replication_group_id: The ID of the replication group to which data is being migrated
            - force: (Optional) Forces the migration to stop without ensuring that data is in sync.
              It is recommended to use this option only to abort the migration and not recommended
              when application wants to continue migration to ElastiCache.

    Returns:
        Dict containing information about the migration completion result.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | string | Yes |  |

## AWS CLI

```bash
aws elasticache complete-migration --replication-group-id <request>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.complete_migration(
    ReplicationGroupId=request,
)
```
