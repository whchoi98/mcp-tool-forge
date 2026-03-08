---
name: list-asset-model-properties
description: Retrieve a paginated list of properties associated with an asset model.

    Args:
        asset_model_id: The ID of the asset model. Accepts UUID format (12345678-1234-1234-1234-123456789012)
                       or external ID format (externalId:my-external-id). Use list_asset_models to get the
                       correct ID if you only have the asset model name.
        region: AWS region (default: us-east-1)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (
            1-250,
            default: 50)         asset_model_version: The version of the asset model (
                LATEST,
                ACTIVE)
        filter_type: Filters the requested list of asset model properties (
            ALL,
            BASE)

    Returns:
        Dictionary containing list of asset model properties
    
---

# List Asset Model Properties

Retrieve a paginated list of properties associated with an asset model.

    Args:
        asset_model_id: The ID of the asset model. Accepts UUID format (12345678-1234-1234-1234-123456789012)
                       or external ID format (externalId:my-external-id). Use list_asset_models to get the
                       correct ID if you only have the asset model name.
        region: AWS region (default: us-east-1)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (
            1-250,
            default: 50)         asset_model_version: The version of the asset model (
                LATEST,
                ACTIVE)
        filter_type: Filters the requested list of asset model properties (
            ALL,
            BASE)

    Returns:
        Dictionary containing list of asset model properties
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `asset_model_id` | string | Yes | The ID of the asset model (UUID format: 12345678-1234-1234-1234-123456789012 or external ID format: externalId:my-external-id) |
| `region` | string | No | AWS region |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-250) |
| `asset_model_version` | string | No | The version of the asset model (LATEST, ACTIVE) |
| `filter_type` | string | No | Filter properties by type (ALL, BASE) |

## AWS CLI

```bash
aws iotsitewise list-asset-model-properties --asset-model-id <asset_model_id> --next-token <next_token> --max-results <max_results> --asset-model-version <asset_model_version> --filter-type <filter_type>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.list_asset_model_properties(
    AssetModelId=asset_model_id,
    NextToken=next_token,
    MaxResults=max_results,
    AssetModelVersion=asset_model_version,
    FilterType=filter_type,
)
```
