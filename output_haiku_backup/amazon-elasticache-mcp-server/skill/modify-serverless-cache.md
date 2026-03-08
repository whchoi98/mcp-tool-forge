---
name: modify-serverless-cache
description: Modify an Amazon ElastiCache serverless cache.

    This tool modifies the configuration of an existing serverless cache including:
    - Cache description
    - Engine version
    - Snapshot settings
    - Usage limits
    - Security groups
    - User groups

    Parameters:
        serverless_cache_name (str): Name of the serverless cache to modify.
        apply_immediately (Optional[bool]): Whether to apply changes immediately or during maintenance window.
        description (Optional[str]): New description for the cache.
        major_engine_version (Optional[str]): New major engine version.
        snapshot_retention_limit (Optional[int]): Number of days for which ElastiCache retains automatic snapshots.
        daily_snapshot_time (Optional[str]): Time range (in UTC) when daily snapshots are taken (e.g., '04:00-05:00').
        cache_usage_limits (Optional[CacheUsageLimits]): New usage limits for the cache. Structure:
            {
                "DataStorage": {
                    "Maximum": int,  # Maximum storage in GB
                    "Minimum": int,  # Minimum storage in GB
                    "Unit": "GB"     # Storage unit (currently only GB is supported)
                },
                "ECPUPerSecond": {
                    "Maximum": int,  # Maximum ECPU per second
                    "Minimum": int   # Minimum ECPU per second
                }
            }
        security_group_ids (Optional[List[str]]): List of security group IDs.
        user_group_id (Optional[str]): ID of the user group to associate with the cache.

    Returns:
        Dict containing information about the modified serverless cache.
    
---

# Modify-Serverless-Cache

Modify an Amazon ElastiCache serverless cache.

    This tool modifies the configuration of an existing serverless cache including:
    - Cache description
    - Engine version
    - Snapshot settings
    - Usage limits
    - Security groups
    - User groups

    Parameters:
        serverless_cache_name (str): Name of the serverless cache to modify.
        apply_immediately (Optional[bool]): Whether to apply changes immediately or during maintenance window.
        description (Optional[str]): New description for the cache.
        major_engine_version (Optional[str]): New major engine version.
        snapshot_retention_limit (Optional[int]): Number of days for which ElastiCache retains automatic snapshots.
        daily_snapshot_time (Optional[str]): Time range (in UTC) when daily snapshots are taken (e.g., '04:00-05:00').
        cache_usage_limits (Optional[CacheUsageLimits]): New usage limits for the cache. Structure:
            {
                "DataStorage": {
                    "Maximum": int,  # Maximum storage in GB
                    "Minimum": int,  # Minimum storage in GB
                    "Unit": "GB"     # Storage unit (currently only GB is supported)
                },
                "ECPUPerSecond": {
                    "Maximum": int,  # Maximum ECPU per second
                    "Minimum": int   # Minimum ECPU per second
                }
            }
        security_group_ids (Optional[List[str]]): List of security group IDs.
        user_group_id (Optional[str]): ID of the user group to associate with the cache.

    Returns:
        Dict containing information about the modified serverless cache.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | string | Yes |  |

## AWS CLI

```bash
aws elasticache modify-serverless-cache --serverless-cache-name <request>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.modify_serverless_cache(
    ServerlessCacheName=request,
)
```
