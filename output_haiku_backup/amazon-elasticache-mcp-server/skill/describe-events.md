---
name: describe-events
description: Returns events related to clusters, cache security groups, and parameter groups.

    Parameters:
        source_type (Optional[str]): The event source to retrieve events for. If not specified, all
            events are returned. Valid values: cache-cluster | cache-parameter-group |
            cache-security-group | cache-subnet-group | replication-group | user | user-group
        source_identifier (Optional[str]): The identifier of the event source for which events are
            returned. For example, if source_type is cache-cluster, you can specify a cluster
            identifier to see all events for only that cluster.
        start_time (Optional[datetime]): The beginning of the time interval to retrieve events for,
            specified in ISO 8601 format.
        end_time (Optional[datetime]): The end of the time interval to retrieve events for,
            specified in ISO 8601 format.
        duration (Optional[int]): The number of minutes worth of events to retrieve.
        max_records (Optional[int]): The maximum number of records to include in the response.
            If more records exist than the specified MaxRecords value, a marker is included
            in the response so that the remaining results can be retrieved.
        marker (Optional[str]): An optional marker returned from a previous request. Use this marker
            for pagination of results from this operation. If this parameter is specified,
            the response includes only records beyond the marker, up to the value specified
            by MaxRecords.

    Returns:
        Dict containing information about the events, including:
        - Events: List of events
        - Marker: Pagination marker for next set of results
    
---

# Describe-Events

Returns events related to clusters, cache security groups, and parameter groups.

    Parameters:
        source_type (Optional[str]): The event source to retrieve events for. If not specified, all
            events are returned. Valid values: cache-cluster | cache-parameter-group |
            cache-security-group | cache-subnet-group | replication-group | user | user-group
        source_identifier (Optional[str]): The identifier of the event source for which events are
            returned. For example, if source_type is cache-cluster, you can specify a cluster
            identifier to see all events for only that cluster.
        start_time (Optional[datetime]): The beginning of the time interval to retrieve events for,
            specified in ISO 8601 format.
        end_time (Optional[datetime]): The end of the time interval to retrieve events for,
            specified in ISO 8601 format.
        duration (Optional[int]): The number of minutes worth of events to retrieve.
        max_records (Optional[int]): The maximum number of records to include in the response.
            If more records exist than the specified MaxRecords value, a marker is included
            in the response so that the remaining results can be retrieved.
        marker (Optional[str]): An optional marker returned from a previous request. Use this marker
            for pagination of results from this operation. If this parameter is specified,
            the response includes only records beyond the marker, up to the value specified
            by MaxRecords.

    Returns:
        Dict containing information about the events, including:
        - Events: List of events
        - Marker: Pagination marker for next set of results
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source_type` | string | No |  |
| `source_identifier` | string | No |  |
| `start_time` | string | No |  |
| `end_time` | string | No |  |
| `duration` | string | No |  |
| `max_records` | string | No |  |
| `marker` | string | No |  |

## AWS CLI

```bash
aws elasticache describe-events --source-type <source_type> --source-identifier <source_identifier> --start-time <start_time> --end-time <end_time> --duration <duration> --max-records <max_records> --marker <marker>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.describe_events(
    SourceType=source_type,
    SourceIdentifier=source_identifier,
    StartTime=start_time,
    EndTime=end_time,
    Duration=duration,
    MaxRecords=max_records,
    Marker=marker,
)
```
