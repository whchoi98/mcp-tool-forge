---
name: get-asset-property-aggregates
description: Get aggregated values for an asset property.

    Args:
        asset_id: The ID of the asset
        property_id: The ID of the asset property
        property_alias: The alias that identifies the property
        aggregate_types: The data aggregating function (AVERAGE, COUNT, MAXIMUM,             MINIMUM, SUM, STANDARD_DEVIATION)
        resolution: The time interval over which to aggregate data
        start_date: The exclusive start of the range (ISO 8601 format)
        end_date: The inclusive end of the range (ISO 8601 format)
        qualities: The quality by which to filter asset data (GOOD, BAD, UNCERTAIN)
        time_ordering: The chronological sorting order of the requested information             (ASCENDING, DESCENDING)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-4000, default: 100)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing property aggregates
    
---

# Get Asset Property Aggregates

Get aggregated values for an asset property.

    Args:
        asset_id: The ID of the asset
        property_id: The ID of the asset property
        property_alias: The alias that identifies the property
        aggregate_types: The data aggregating function (AVERAGE, COUNT, MAXIMUM,             MINIMUM, SUM, STANDARD_DEVIATION)
        resolution: The time interval over which to aggregate data
        start_date: The exclusive start of the range (ISO 8601 format)
        end_date: The inclusive end of the range (ISO 8601 format)
        qualities: The quality by which to filter asset data (GOOD, BAD, UNCERTAIN)
        time_ordering: The chronological sorting order of the requested information             (ASCENDING, DESCENDING)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-4000, default: 100)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing property aggregates
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `asset_id` | string | No | The ID of the asset |
| `property_id` | string | No | The ID of the asset property |
| `property_alias` | string | No | The alias that identifies the property |
| `aggregate_types` | string | No | The data aggregating function (AVERAGE, COUNT, MAXIMUM, MINIMUM, SUM, STANDARD_DEVIATION) |
| `resolution` | string | No | The time interval over which to aggregate data |
| `start_date` | string | No | The exclusive start of the range (ISO 8601 format) |
| `end_date` | string | No | The inclusive end of the range (ISO 8601 format) |
| `qualities` | string | No | The quality by which to filter asset data (GOOD, BAD, UNCERTAIN) |
| `time_ordering` | string | No | The chronological sorting order (ASCENDING, DESCENDING) |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-4000) |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise get-asset-property-aggregates --asset-id <asset_id> --property-id <property_id> --property-alias <property_alias> --aggregate-types <aggregate_types> --resolution <resolution> --start-time <start_date> --end-time <end_date> --qualities <qualities> --time-ordering <time_ordering> --next-token <next_token> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.get_asset_property_aggregates(
    AssetId=asset_id,
    PropertyId=property_id,
    PropertyAlias=property_alias,
    AggregateTypes=aggregate_types,
    Resolution=resolution,
    StartTime=start_date,
    EndTime=end_date,
    Qualities=qualities,
    TimeOrdering=time_ordering,
    NextToken=next_token,
    MaxResults=max_results,
)
```
