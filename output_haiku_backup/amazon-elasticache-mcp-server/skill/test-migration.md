---
name: test-migration
description: Test migration to an Amazon ElastiCache replication group.

    This tool tests migration from a Redis instance to an ElastiCache replication group.
    It validates that data can be successfully migrated from the specified endpoint to
    the target replication group.

    Args:
        request: The TestMigrationRequest object containing:
            - replication_group_id: The ID of the replication group to which data is to be migrated
            - customer_node_endpoint_list: List of endpoints from which data should be migrated.
              List should have only one element with Address and Port fields.

    Returns:
        Dict containing information about the migration test result.
    
---

# Test-Migration

Test migration to an Amazon ElastiCache replication group.

    This tool tests migration from a Redis instance to an ElastiCache replication group.
    It validates that data can be successfully migrated from the specified endpoint to
    the target replication group.

    Args:
        request: The TestMigrationRequest object containing:
            - replication_group_id: The ID of the replication group to which data is to be migrated
            - customer_node_endpoint_list: List of endpoints from which data should be migrated.
              List should have only one element with Address and Port fields.

    Returns:
        Dict containing information about the migration test result.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | string | Yes |  |

