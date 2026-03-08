---
name: describe-cache-engine-versions
description: Returns a list of the available cache engines and their versions.

    Parameters:
        engine (Optional[str]): The cache engine to return. Valid values: memcached | redis | valkey
        engine_version (Optional[str]): The cache engine version to return.
            Example: memcached 1.4.14, redis 6.x, valkey 8.0
        cache_parameter_group_family (Optional[str]): The name of a specific cache parameter group family.
            Valid values are: memcached1.4 | memcached1.5 | memcached1.6 | redis2.6 | redis2.8 |
            redis3.2 | redis4.0 | redis5.0 | redis6.x | redis7.x | valkey7.x | valkey8.x
        max_records (Optional[int]): The maximum number of records to include in the response.
            If more records exist than the specified MaxRecords value, a marker is included
            in the response so that the remaining results can be retrieved.
        marker (Optional[str]): An optional marker returned from a previous request. Use this marker
            for pagination of results from this operation. If this parameter is specified,
            the response includes only records beyond the marker, up to the value specified
            by MaxRecords.
        default_only (Optional[bool]): If true, specifies that only the default version of the specified engine
            or engine and major version combination is to be returned.

    Returns:
        Dict containing information about the cache engine versions, including:
        - CacheEngineVersions: List of cache engine versions
        - Marker: Pagination marker for next set of results
    
---

# Describe-Cache-Engine-Versions

Returns a list of the available cache engines and their versions.

    Parameters:
        engine (Optional[str]): The cache engine to return. Valid values: memcached | redis | valkey
        engine_version (Optional[str]): The cache engine version to return.
            Example: memcached 1.4.14, redis 6.x, valkey 8.0
        cache_parameter_group_family (Optional[str]): The name of a specific cache parameter group family.
            Valid values are: memcached1.4 | memcached1.5 | memcached1.6 | redis2.6 | redis2.8 |
            redis3.2 | redis4.0 | redis5.0 | redis6.x | redis7.x | valkey7.x | valkey8.x
        max_records (Optional[int]): The maximum number of records to include in the response.
            If more records exist than the specified MaxRecords value, a marker is included
            in the response so that the remaining results can be retrieved.
        marker (Optional[str]): An optional marker returned from a previous request. Use this marker
            for pagination of results from this operation. If this parameter is specified,
            the response includes only records beyond the marker, up to the value specified
            by MaxRecords.
        default_only (Optional[bool]): If true, specifies that only the default version of the specified engine
            or engine and major version combination is to be returned.

    Returns:
        Dict containing information about the cache engine versions, including:
        - CacheEngineVersions: List of cache engine versions
        - Marker: Pagination marker for next set of results
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `engine` | string | No |  |
| `engine_version` | string | No |  |
| `cache_parameter_group_family` | string | No |  |
| `max_records` | string | No |  |
| `marker` | string | No |  |
| `default_only` | string | No |  |

## AWS CLI

```bash
aws elasticache describe-cache-engine-versions --engine <engine> --engine-version <engine_version> --cache-parameter-group-family <cache_parameter_group_family> --max-records <max_records> --marker <marker> --default-only <default_only>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.describe_cache_engine_versions(
    Engine=engine,
    EngineVersion=engine_version,
    CacheParameterGroupFamily=cache_parameter_group_family,
    MaxRecords=max_records,
    Marker=marker,
    DefaultOnly=default_only,
)
```
