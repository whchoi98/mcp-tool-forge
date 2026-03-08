---
name: get-asset-property-value
description: Get the current value for the given asset property.

    Args:
        asset_id: The ID of the asset
        property_id: The ID of the asset property
        property_alias: The alias that identifies the property
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing current property value
    
---

# Get Asset Property Value

Get the current value for the given asset property.

    Args:
        asset_id: The ID of the asset
        property_id: The ID of the asset property
        property_alias: The alias that identifies the property
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing current property value
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `asset_id` | string | No | The ID of the asset |
| `property_id` | string | No | The ID of the asset property |
| `property_alias` | string | No | The alias that identifies the property |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise get-asset-property-value --asset-id <asset_id> --property-id <property_id> --property-alias <property_alias>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.get_asset_property_value(
    AssetId=asset_id,
    PropertyId=property_id,
    PropertyAlias=property_alias,
)
```
