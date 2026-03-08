---
name: batch-apply-update-action
description: Apply service update to multiple ElastiCache resources.

    Parameters:
        service_update_name (str): The unique ID of the service update to apply.
        replication_group_ids (Optional[List[str]]): List of replication group IDs to update.
            Either this or cache_cluster_ids must be provided.
        cache_cluster_ids (Optional[List[str]]): List of cache cluster IDs to update.
            Either this or replication_group_ids must be provided.

    Returns:
        Dict containing information about the batch update operation.
    
---

# Batch-Apply-Update-Action

Apply service update to multiple ElastiCache resources.

    Parameters:
        service_update_name (str): The unique ID of the service update to apply.
        replication_group_ids (Optional[List[str]]): List of replication group IDs to update.
            Either this or cache_cluster_ids must be provided.
        cache_cluster_ids (Optional[List[str]]): List of cache cluster IDs to update.
            Either this or replication_group_ids must be provided.

    Returns:
        Dict containing information about the batch update operation.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `service_update_name` | string | Yes |  |
| `replication_group_ids` | string | No |  |
| `cache_cluster_ids` | string | No |  |

## AWS CLI

```bash
aws elasticache batch-apply-update-action --service-update-name <service_update_name> --replication-group-ids <replication_group_ids> --cache-cluster-ids <cache_cluster_ids>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.batch_apply_update_action(
    ServiceUpdateName=service_update_name,
    ReplicationGroupIds=replication_group_ids,
    CacheClusterIds=cache_cluster_ids,
)
```
