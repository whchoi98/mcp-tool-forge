---
name: describe-time-series
description: Retrieve information about a time series (data stream).

    Args:
        alias: The alias that identifies the time series
        asset_id: The ID of the asset in which the asset property was created
        property_id: The ID of the asset property
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing time series information
    
---

# Describe Time Series

Retrieve information about a time series (data stream).

    Args:
        alias: The alias that identifies the time series
        asset_id: The ID of the asset in which the asset property was created
        property_id: The ID of the asset property
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing time series information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `alias` | string | No | The alias that identifies the time series |
| `asset_id` | string | No | The ID of the asset in which the asset property was created |
| `property_id` | string | No | The ID of the asset property |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise describe-time-series --alias <alias> --asset-id <asset_id> --property-id <property_id>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_time_series(
    Alias=alias,
    AssetId=asset_id,
    PropertyId=property_id,
)
```
