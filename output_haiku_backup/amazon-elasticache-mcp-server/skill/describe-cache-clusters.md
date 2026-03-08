---
name: describe-cache-clusters
description: Describe one or more ElastiCache cache clusters.

    This tool returns information about provisioned cache clusters. If a cache cluster ID
    is specified, information about only that cache cluster is returned. Otherwise, information
    about up to MaxRecords cache clusters is returned.

    Parameters:
        cache_cluster_id (Optional[str]): The identifier for the cache cluster to describe.
            If not provided, information about all cache clusters is returned.
        max_records (Optional[int]): The maximum number of records to include in the response.
            If more records exist than the specified MaxRecords value, a marker is included
            in the response so that the remaining results can be retrieved.
        marker (Optional[str]): An optional marker returned from a previous request. Use this marker
            for pagination of results from this operation. If this parameter is specified,
            the response includes only records beyond the marker, up to the value specified
            by MaxRecords.
        show_cache_node_info (Optional[bool]): Whether to include detailed information about
            cache nodes in the response.
        show_cache_clusters_not_in_replication_groups (Optional[bool]): Whether to show only
            cache clusters that are not members of a replication group.

    Returns:
        Dict containing information about the cache cluster(s), including:
        - CacheClusters: List of cache clusters
        - Marker: Pagination marker for next set of results
    
---

# Describe-Cache-Clusters

Describe one or more ElastiCache cache clusters.

    This tool returns information about provisioned cache clusters. If a cache cluster ID
    is specified, information about only that cache cluster is returned. Otherwise, information
    about up to MaxRecords cache clusters is returned.

    Parameters:
        cache_cluster_id (Optional[str]): The identifier for the cache cluster to describe.
            If not provided, information about all cache clusters is returned.
        max_records (Optional[int]): The maximum number of records to include in the response.
            If more records exist than the specified MaxRecords value, a marker is included
            in the response so that the remaining results can be retrieved.
        marker (Optional[str]): An optional marker returned from a previous request. Use this marker
            for pagination of results from this operation. If this parameter is specified,
            the response includes only records beyond the marker, up to the value specified
            by MaxRecords.
        show_cache_node_info (Optional[bool]): Whether to include detailed information about
            cache nodes in the response.
        show_cache_clusters_not_in_replication_groups (Optional[bool]): Whether to show only
            cache clusters that are not members of a replication group.

    Returns:
        Dict containing information about the cache cluster(s), including:
        - CacheClusters: List of cache clusters
        - Marker: Pagination marker for next set of results
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cache_cluster_id` | string | No |  |
| `max_records` | string | No |  |
| `marker` | string | No |  |
| `show_cache_node_info` | string | No |  |
| `show_cache_clusters_not_in_replication_groups` | string | No |  |

## AWS CLI

```bash
aws elasticache describe-cache-clusters --cache-cluster-id <cache_cluster_id> --max-records <max_records> --marker <marker> --show-cache-node-info <show_cache_node_info> --show-cache-clusters-not-in-replication-groups <show_cache_clusters_not_in_replication_groups>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.describe_cache_clusters(
    CacheClusterId=cache_cluster_id,
    MaxRecords=max_records,
    Marker=marker,
    ShowCacheNodeInfo=show_cache_node_info,
    ShowCacheClustersNotInReplicationGroups=show_cache_clusters_not_in_replication_groups,
)
```
