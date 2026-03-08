---
name: describe-asset-model
description: Retrieve information about an asset model.

    Args:
        asset_model_id: The ID of the asset model. Accepts UUID format (12345678-1234-1234-1234-123456789012)
                       or external ID format (externalId:my-external-id). Use list_asset_models to get the
                       correct ID if you only have the asset model name.
        region: AWS region (default: us-east-1)
        exclude_properties: Whether to exclude asset model properties
        asset_model_version: The version of the asset model (LATEST, ACTIVE)

    Returns:
        Dictionary containing asset model information
    
---

# Describe Asset Model

Retrieve information about an asset model.

    Args:
        asset_model_id: The ID of the asset model. Accepts UUID format (12345678-1234-1234-1234-123456789012)
                       or external ID format (externalId:my-external-id). Use list_asset_models to get the
                       correct ID if you only have the asset model name.
        region: AWS region (default: us-east-1)
        exclude_properties: Whether to exclude asset model properties
        asset_model_version: The version of the asset model (LATEST, ACTIVE)

    Returns:
        Dictionary containing asset model information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `asset_model_id` | string | Yes | The ID of the asset model (UUID format: 12345678-1234-1234-1234-123456789012 or external ID format: externalId:my-external-id) |
| `region` | string | No | AWS region |
| `exclude_properties` | boolean | No | Whether to exclude asset model properties |
| `asset_model_version` | string | No | The version of the asset model (LATEST, ACTIVE) |

## AWS CLI

```bash
aws iotsitewise describe-asset-model --asset-model-id <asset_model_id> --exclude-properties <exclude_properties>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_asset_model(
    AssetModelId=asset_model_id,
    ExcludeProperties=exclude_properties,
)
```
