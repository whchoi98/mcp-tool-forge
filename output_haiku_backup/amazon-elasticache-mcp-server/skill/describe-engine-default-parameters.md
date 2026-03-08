---
name: describe-engine-default-parameters
description: Returns the default engine and system parameter information for the specified cache engine family.

    Parameters:
        cache_parameter_group_family (str): The name of the cache parameter group family.
            Valid values are: memcached1.4 | memcached1.5 | memcached1.6 | redis2.6 | redis2.8 |
            redis3.2 | redis4.0 | redis5.0 | redis6.x | redis7.x | valkey7.x | valkey8.x
        max_records (Optional[int]): The maximum number of records to include in the response.
            If more records exist than the specified MaxRecords value, a marker is included
            in the response so that the remaining results can be retrieved.
        marker (Optional[str]): An optional marker returned from a previous request. Use this marker
            for pagination of results from this operation. If this parameter is specified,
            the response includes only records beyond the marker, up to the value specified
            by MaxRecords.

    Returns:
        Dict containing information about the engine default parameters, including:
        - Parameters: List of parameters with their details
        - CacheParameterGroupFamily: The name of the cache parameter group family
        - Marker: Pagination marker for next set of results
    
---

# Describe-Engine-Default-Parameters

Returns the default engine and system parameter information for the specified cache engine family.

    Parameters:
        cache_parameter_group_family (str): The name of the cache parameter group family.
            Valid values are: memcached1.4 | memcached1.5 | memcached1.6 | redis2.6 | redis2.8 |
            redis3.2 | redis4.0 | redis5.0 | redis6.x | redis7.x | valkey7.x | valkey8.x
        max_records (Optional[int]): The maximum number of records to include in the response.
            If more records exist than the specified MaxRecords value, a marker is included
            in the response so that the remaining results can be retrieved.
        marker (Optional[str]): An optional marker returned from a previous request. Use this marker
            for pagination of results from this operation. If this parameter is specified,
            the response includes only records beyond the marker, up to the value specified
            by MaxRecords.

    Returns:
        Dict containing information about the engine default parameters, including:
        - Parameters: List of parameters with their details
        - CacheParameterGroupFamily: The name of the cache parameter group family
        - Marker: Pagination marker for next set of results
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cache_parameter_group_family` | string | Yes |  |
| `max_records` | string | No |  |
| `marker` | string | No |  |

## AWS CLI

```bash
aws elasticache describe-engine-default-parameters --cache-parameter-group-family <cache_parameter_group_family> --max-records <max_records> --marker <marker>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.describe_engine_default_parameters(
    CacheParameterGroupFamily=cache_parameter_group_family,
    MaxRecords=max_records,
    Marker=marker,
)
```
