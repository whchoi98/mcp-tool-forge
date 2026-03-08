---
name: describe-asset
description: Retrieve information about an asset.

    Args:
        asset_id: The ID of the asset. Accepts UUID format (12345678-1234-1234-1234-123456789012)
                 or external ID format (externalId:my-external-id). Use list_assets to get the
                 correct ID if you only have the asset name.
        region: AWS region (default: us-east-1)
        exclude_properties: Whether to exclude asset properties from the             response

    Returns:
        Dictionary containing asset information
    
---

# Describe Asset

Retrieve information about an asset.

    Args:
        asset_id: The ID of the asset. Accepts UUID format (12345678-1234-1234-1234-123456789012)
                 or external ID format (externalId:my-external-id). Use list_assets to get the
                 correct ID if you only have the asset name.
        region: AWS region (default: us-east-1)
        exclude_properties: Whether to exclude asset properties from the             response

    Returns:
        Dictionary containing asset information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `asset_id` | string | Yes | The ID of the asset (UUID format: 12345678-1234-1234-1234-123456789012 or external ID format: externalId:my-external-id) |
| `region` | string | No | AWS region |
| `exclude_properties` | boolean | No | Whether to exclude asset properties from the response |

## AWS CLI

```bash
aws iotsitewise describe-asset --asset-id <asset_id> --exclude-properties <exclude_properties>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_asset(
    AssetId=asset_id,
    ExcludeProperties=exclude_properties,
)
```
