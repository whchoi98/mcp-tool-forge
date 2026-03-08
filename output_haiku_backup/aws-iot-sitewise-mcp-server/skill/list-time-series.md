---
name: list-time-series
description: Retrieve a paginated list of time series (data streams).

    Args:
        region: AWS region (default: us-east-1)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (
            1-250,
            default: 50)         asset_id: The ID of the asset in which the asset                                                                 property was created
        alias_prefix: The alias prefix of the time series
        time_series_type: The type of the time series (
            ASSOCIATED,
            DISASSOCIATED)

    Returns:
        Dictionary containing list of time series
    
---

# List Time Series

Retrieve a paginated list of time series (data streams).

    Args:
        region: AWS region (default: us-east-1)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (
            1-250,
            default: 50)         asset_id: The ID of the asset in which the asset                                                                 property was created
        alias_prefix: The alias prefix of the time series
        time_series_type: The type of the time series (
            ASSOCIATED,
            DISASSOCIATED)

    Returns:
        Dictionary containing list of time series
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | No | AWS region |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-250) |
| `asset_id` | string | No | The ID of the asset in which the asset property was created |
| `alias_prefix` | string | No | The alias prefix of the time series |
| `time_series_type` | string | No | The type of the time series (ASSOCIATED, DISASSOCIATED) |

## AWS CLI

```bash
aws iotsitewise list-time-series --next-token <next_token> --max-results <max_results> --asset-id <asset_id> --alias-prefix <alias_prefix> --time-series-type <time_series_type>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.list_time_series(
    NextToken=next_token,
    MaxResults=max_results,
    AssetId=asset_id,
    AliasPrefix=alias_prefix,
    TimeSeriesType=time_series_type,
)
```
