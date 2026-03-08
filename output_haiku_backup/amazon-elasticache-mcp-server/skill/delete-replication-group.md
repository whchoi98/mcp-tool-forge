---
name: delete-replication-group
description: Delete an Amazon ElastiCache replication group.

    This tool deletes an existing replication group. You can optionally retain the primary cluster
    as a standalone cache cluster or create a final snapshot before deletion.

    Parameters:
        replication_group_id (str): The identifier of the replication group to delete.
        retain_primary_cluster (Optional[bool]): If True, retains the primary cluster as a standalone
            cache cluster. If False, deletes all clusters in the replication group.
        final_snapshot_name (Optional[str]): The name of a final cache cluster snapshot to create
            before deleting the replication group.

    Returns:
        Dict containing information about the deleted replication group.
    
---

# Delete-Replication-Group

Delete an Amazon ElastiCache replication group.

    This tool deletes an existing replication group. You can optionally retain the primary cluster
    as a standalone cache cluster or create a final snapshot before deletion.

    Parameters:
        replication_group_id (str): The identifier of the replication group to delete.
        retain_primary_cluster (Optional[bool]): If True, retains the primary cluster as a standalone
            cache cluster. If False, deletes all clusters in the replication group.
        final_snapshot_name (Optional[str]): The name of a final cache cluster snapshot to create
            before deleting the replication group.

    Returns:
        Dict containing information about the deleted replication group.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `replication_group_id` | string | Yes |  |
| `retain_primary_cluster` | string | No |  |
| `final_snapshot_name` | string | No |  |

## AWS CLI

```bash
aws elasticache delete-replication-group --replication-group-id <replication_group_id> --retain-primary-cluster <retain_primary_cluster> --final-snapshot-identifier <final_snapshot_name>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.delete_replication_group(
    ReplicationGroupId=replication_group_id,
    RetainPrimaryCluster=retain_primary_cluster,
    FinalSnapshotIdentifier=final_snapshot_name,
)
```
