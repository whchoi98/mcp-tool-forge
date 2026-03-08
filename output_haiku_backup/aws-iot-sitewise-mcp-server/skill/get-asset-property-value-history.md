---
name: get-asset-property-value-history
description: Get the history of an asset property's values.

    Args:
        asset_id: The ID of the asset
        property_id: The ID of the asset property
        property_alias: The alias that identifies the property
        start_date: The exclusive start of the range (ISO 8601 format)
        end_date: The inclusive end of the range (ISO 8601 format)
        qualities: The quality by which to filter asset data (GOOD, BAD, UNCERTAIN)
        time_ordering: The chronological sorting order of the requested information             (ASCENDING, DESCENDING)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-4000, default: 100)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing property value history
    
---

# Get Asset Property Value History

Get the history of an asset property's values.

    Args:
        asset_id: The ID of the asset
        property_id: The ID of the asset property
        property_alias: The alias that identifies the property
        start_date: The exclusive start of the range (ISO 8601 format)
        end_date: The inclusive end of the range (ISO 8601 format)
        qualities: The quality by which to filter asset data (GOOD, BAD, UNCERTAIN)
        time_ordering: The chronological sorting order of the requested information             (ASCENDING, DESCENDING)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-4000, default: 100)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing property value history
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `asset_id` | string | No | The ID of the asset |
| `property_id` | string | No | The ID of the asset property |
| `property_alias` | string | No | The alias that identifies the property |
| `start_date` | string | No | The exclusive start of the range (ISO 8601 format) |
| `end_date` | string | No | The inclusive end of the range (ISO 8601 format) |
| `qualities` | string | No | The quality by which to filter asset data (GOOD, BAD, UNCERTAIN) |
| `time_ordering` | string | No | The chronological sorting order (ASCENDING, DESCENDING) |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-4000) |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise get-asset-property-value-history --asset-id <asset_id> --property-id <property_id> --property-alias <property_alias> --start-date <start_date> --end-date <end_date> --qualities <qualities> --time-ordering <time_ordering> --next-token <next_token> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.get_asset_property_value_history(
    AssetId=asset_id,
    PropertyId=property_id,
    PropertyAlias=property_alias,
    StartDate=start_date,
    EndDate=end_date,
    Qualities=qualities,
    TimeOrdering=time_ordering,
    NextToken=next_token,
    MaxResults=max_results,
)
```
