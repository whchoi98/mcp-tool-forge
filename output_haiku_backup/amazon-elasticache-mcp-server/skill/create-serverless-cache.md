---
name: create-serverless-cache
description: Create a new Amazon ElastiCache serverless cache.

    This tool creates a new serverless cache with specified configuration including:
    - Serverless cache name and capacity
    - Optional VPC and security settings
    - Optional encryption settings
    - Optional snapshot restoration and backup settings
    - Optional usage limits and user groups
    - Optional tags

    Parameters:
        serverless_cache_name (str): Name of the serverless cache.
        engine (str): Cache engine type.
        description (Optional[str]): Description for the cache.
        kms_key_id (Optional[str]): KMS key ID for encryption.
        major_engine_version (Optional[str]): Major engine version.
        snapshot_arns_to_restore (Optional[List[str]]): List of snapshot ARNs to restore from.
        subnet_ids (Optional[List[str]]): List of subnet IDs for VPC configuration.
        tags (Optional[Union[str, List[Dict[str, Optional[str]]], Dict[str, Optional[str]]]]): Tags to apply to the cache.
            Tag requirements:
            - Key: (string) Required. The key for the tag. Must not be empty.
            - Value: (string) Optional. The tag's value. May be null.

            Supports three formats:
            1. Shorthand syntax: "Key=value,Key2=value2" or "Key=,Key2=" for null values
            2. Dictionary: {"key": "value", "key2": null}
            3. JSON array: [{"Key": "string", "Value": "string"}, {"Key": "string2", "Value": null}]

            Can be None if no tags are needed.
        security_group_ids (Optional[List[str]]): List of security group IDs.
        cache_usage_limits (Optional[CacheUsageLimits]): Usage limits for the cache. Structure:
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
        user_group_id (Optional[str]): ID of the user group to associate with the cache.
        snapshot_retention_limit (Optional[int]): Number of days for which ElastiCache retains automatic snapshots.
        daily_snapshot_time (Optional[str]): Time range (in UTC) when daily snapshots are taken (e.g., '04:00-05:00').

    Returns:
        Dict containing information about the created serverless cache.
    
---

# Create-Serverless-Cache

Create a new Amazon ElastiCache serverless cache.

    This tool creates a new serverless cache with specified configuration including:
    - Serverless cache name and capacity
    - Optional VPC and security settings
    - Optional encryption settings
    - Optional snapshot restoration and backup settings
    - Optional usage limits and user groups
    - Optional tags

    Parameters:
        serverless_cache_name (str): Name of the serverless cache.
        engine (str): Cache engine type.
        description (Optional[str]): Description for the cache.
        kms_key_id (Optional[str]): KMS key ID for encryption.
        major_engine_version (Optional[str]): Major engine version.
        snapshot_arns_to_restore (Optional[List[str]]): List of snapshot ARNs to restore from.
        subnet_ids (Optional[List[str]]): List of subnet IDs for VPC configuration.
        tags (Optional[Union[str, List[Dict[str, Optional[str]]], Dict[str, Optional[str]]]]): Tags to apply to the cache.
            Tag requirements:
            - Key: (string) Required. The key for the tag. Must not be empty.
            - Value: (string) Optional. The tag's value. May be null.

            Supports three formats:
            1. Shorthand syntax: "Key=value,Key2=value2" or "Key=,Key2=" for null values
            2. Dictionary: {"key": "value", "key2": null}
            3. JSON array: [{"Key": "string", "Value": "string"}, {"Key": "string2", "Value": null}]

            Can be None if no tags are needed.
        security_group_ids (Optional[List[str]]): List of security group IDs.
        cache_usage_limits (Optional[CacheUsageLimits]): Usage limits for the cache. Structure:
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
        user_group_id (Optional[str]): ID of the user group to associate with the cache.
        snapshot_retention_limit (Optional[int]): Number of days for which ElastiCache retains automatic snapshots.
        daily_snapshot_time (Optional[str]): Time range (in UTC) when daily snapshots are taken (e.g., '04:00-05:00').

    Returns:
        Dict containing information about the created serverless cache.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | string | Yes |  |

