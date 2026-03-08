---
name: delete-cache-cluster
description: Delete an Amazon ElastiCache cache cluster.

    This tool deletes an existing cache cluster. Optionally, it can create a final
    snapshot of the cluster before deletion.

    Parameters:
        cache_cluster_id (str): The ID of the cache cluster to delete.
        final_snapshot_identifier (Optional[str]): The user-supplied name of a final
            cache cluster snapshot. This is the unique name that identifies the
            snapshot. ElastiCache creates the snapshot, and then deletes the cache
            cluster immediately afterward.

    Returns:
        Dict containing information about the deleted cache cluster.
    
---

# Delete-Cache-Cluster

Delete an Amazon ElastiCache cache cluster.

    This tool deletes an existing cache cluster. Optionally, it can create a final
    snapshot of the cluster before deletion.

    Parameters:
        cache_cluster_id (str): The ID of the cache cluster to delete.
        final_snapshot_identifier (Optional[str]): The user-supplied name of a final
            cache cluster snapshot. This is the unique name that identifies the
            snapshot. ElastiCache creates the snapshot, and then deletes the cache
            cluster immediately afterward.

    Returns:
        Dict containing information about the deleted cache cluster.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cache_cluster_id` | string | Yes |  |
| `final_snapshot_identifier` | string | No |  |

## AWS CLI

```bash
aws elasticache delete-cache-cluster --cache-cluster-id <cache_cluster_id> --final-snapshot-identifier <final_snapshot_identifier>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.delete_cache_cluster(
    CacheClusterId=cache_cluster_id,
    FinalSnapshotIdentifier=final_snapshot_identifier,
)
```
