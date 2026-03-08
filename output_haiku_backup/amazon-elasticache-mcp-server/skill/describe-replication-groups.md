---
name: describe-replication-groups
description: Describe one or more ElastiCache replication groups.

    This tool returns information about provisioned replication groups. If a replication group ID
    is specified, information about only that replication group is returned. Otherwise, information
    about up to MaxRecords replication groups is returned.

    Parameters:
        replication_group_id (Optional[str]): The identifier for the replication group to describe.
            If not provided, information about all replication groups is returned.
        max_records (Optional[int]): The maximum number of records to include in the response.
            If more records exist than the specified MaxRecords value, a marker is included
            in the response so that the remaining results can be retrieved.
        marker (Optional[str]): An optional marker returned from a previous request. Use this marker
            for pagination of results from this operation. If this parameter is specified,
            the response includes only records beyond the marker, up to the value specified
            by MaxRecords.

    Returns:
        Dict containing information about the replication group(s), including:
        - ReplicationGroups: List of replication groups
        - Marker: Pagination marker for next set of results
    
---

# Describe-Replication-Groups

Describe one or more ElastiCache replication groups.

    This tool returns information about provisioned replication groups. If a replication group ID
    is specified, information about only that replication group is returned. Otherwise, information
    about up to MaxRecords replication groups is returned.

    Parameters:
        replication_group_id (Optional[str]): The identifier for the replication group to describe.
            If not provided, information about all replication groups is returned.
        max_records (Optional[int]): The maximum number of records to include in the response.
            If more records exist than the specified MaxRecords value, a marker is included
            in the response so that the remaining results can be retrieved.
        marker (Optional[str]): An optional marker returned from a previous request. Use this marker
            for pagination of results from this operation. If this parameter is specified,
            the response includes only records beyond the marker, up to the value specified
            by MaxRecords.

    Returns:
        Dict containing information about the replication group(s), including:
        - ReplicationGroups: List of replication groups
        - Marker: Pagination marker for next set of results
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `replication_group_id` | string | No |  |
| `max_records` | string | No |  |
| `marker` | string | No |  |

## AWS CLI

```bash
aws elasticache describe-replication-groups --replication-group-id <replication_group_id> --max-records <max_records> --marker <marker>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.describe_replication_groups(
    ReplicationGroupId=replication_group_id,
    MaxRecords=max_records,
    Marker=marker,
)
```
