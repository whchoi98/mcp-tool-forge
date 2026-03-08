---
name: get-interpl-asset-property-values
description: Get interpolated values for an asset property for a specified time interval.

    Args:
        asset_id: The ID of the asset
        property_id: The ID of the asset property
        property_alias: The alias that identifies the property
        start_time_in_seconds: The exclusive start of the range (Unix epoch             time in seconds)
        end_time_in_seconds: The inclusive end of the range (Unix epoch time             in seconds)
        quality: The quality of the asset property value (GOOD, BAD, UNCERTAIN)
        interval_in_seconds: The time interval in seconds over which to             interpolate data
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-4000, default: 100)
        interpolation_type: The interpolation type (LINEAR_INTERPOLATION,             LOCF_INTERPOLATION)
        interval_window_in_seconds: The query interval for the window
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing interpolated property values
    
---

# Get Interpl Asset Property Values

Get interpolated values for an asset property for a specified time interval.

    Args:
        asset_id: The ID of the asset
        property_id: The ID of the asset property
        property_alias: The alias that identifies the property
        start_time_in_seconds: The exclusive start of the range (Unix epoch             time in seconds)
        end_time_in_seconds: The inclusive end of the range (Unix epoch time             in seconds)
        quality: The quality of the asset property value (GOOD, BAD, UNCERTAIN)
        interval_in_seconds: The time interval in seconds over which to             interpolate data
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-4000, default: 100)
        interpolation_type: The interpolation type (LINEAR_INTERPOLATION,             LOCF_INTERPOLATION)
        interval_window_in_seconds: The query interval for the window
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing interpolated property values
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `asset_id` | string | No | The ID of the asset |
| `property_id` | string | No | The ID of the asset property |
| `property_alias` | string | No | The alias that identifies the property |
| `start_time_in_seconds` | string | No | The exclusive start of the range (Unix epoch time in seconds) |
| `end_time_in_seconds` | string | No | The inclusive end of the range (Unix epoch time in seconds) |
| `quality` | string | No | The quality of the asset property value (GOOD, BAD, UNCERTAIN) |
| `interval_in_seconds` | integer | No | The time interval in seconds over which to interpolate data |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-250) |
| `interpolation_type` | string | No | The interpolation type (LINEAR_INTERPOLATION, LOCF_INTERPOLATION) |
| `interval_window_in_seconds` | string | No | The query interval for interpolated values |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise get-interpolated-asset-property-values --asset-id <asset_id> --property-id <property_id> --property-alias <property_alias> --start-time-in-seconds <start_time_in_seconds> --end-time-in-seconds <end_time_in_seconds> --quality <quality> --interval-in-seconds <interval_in_seconds> --next-token <next_token> --max-results <max_results> --interpolation-type <interpolation_type> --interval-window-in-seconds <interval_window_in_seconds>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.get_interpolated_asset_property_values(
    AssetId=asset_id,
    PropertyId=property_id,
    PropertyAlias=property_alias,
    StartTimeInSeconds=start_time_in_seconds,
    EndTimeInSeconds=end_time_in_seconds,
    Quality=quality,
    IntervalInSeconds=interval_in_seconds,
    NextToken=next_token,
    MaxResults=max_results,
    InterpolationType=interpolation_type,
    IntervalWindowInSeconds=interval_window_in_seconds,
)
```
