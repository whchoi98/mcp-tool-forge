---
name: delete-serverless-cache
description: Delete an Amazon ElastiCache serverless cache.

    This tool deletes a specified serverless cache from your AWS account.
    The cache must exist and be in a deletable state.

    Parameters:
        serverless_cache_name (str): Name of the serverless cache to delete.
        final_snapshot_name (Optional[str]): Name of the final snapshot to create before deletion.

    Returns:
        Dict containing the deletion response or error information.
    
---

# Delete-Serverless-Cache

Delete an Amazon ElastiCache serverless cache.

    This tool deletes a specified serverless cache from your AWS account.
    The cache must exist and be in a deletable state.

    Parameters:
        serverless_cache_name (str): Name of the serverless cache to delete.
        final_snapshot_name (Optional[str]): Name of the final snapshot to create before deletion.

    Returns:
        Dict containing the deletion response or error information.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serverless_cache_name` | string | Yes |  |
| `final_snapshot_name` | string | No |  |

## AWS CLI

```bash
aws elasticache delete-serverless-cache --serverless-cache-name <serverless_cache_name> --final-snapshot-name <final_snapshot_name>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.delete_serverless_cache(
    ServerlessCacheName=serverless_cache_name,
    FinalSnapshotName=final_snapshot_name,
)
```
