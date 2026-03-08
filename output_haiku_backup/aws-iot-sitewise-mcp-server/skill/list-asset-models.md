---
name: list-asset-models
description: Retrieve a paginated list of summaries for all asset models.

    Args:
        region: AWS region (default: us-east-1)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-250, default: 50)
        asset_model_types: The type of asset model (ASSET_MODEL, COMPONENT_MODEL)

    Returns:
        Dictionary containing list of asset models
    
---

# List Asset Models

Retrieve a paginated list of summaries for all asset models.

    Args:
        region: AWS region (default: us-east-1)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-250, default: 50)
        asset_model_types: The type of asset model (ASSET_MODEL, COMPONENT_MODEL)

    Returns:
        Dictionary containing list of asset models
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | No | AWS region |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-250) |
| `asset_model_types` | string | No | The type of asset model (ASSET_MODEL, COMPONENT_MODEL) |

## AWS CLI

```bash
aws iotsitewise list-asset-models --next-token <next_token> --max-results <max_results> --asset-model-types <asset_model_types>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.list_asset_models(
    NextToken=next_token,
    MaxResults=max_results,
    AssetModelTypes=asset_model_types,
)
```
