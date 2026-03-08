---
name: list-assets
description: Retrieve a paginated list of asset summaries.

    Args:
        region: AWS region (default: us-east-1)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-250, default: 50)
        asset_model_id: The ID of the asset model by which to filter the list of assets
        filter_type: The filter for the requested list of assets (ALL, TOP_LEVEL)

    Returns:
        Dictionary containing list of assets
    
---

# List Assets

Retrieve a paginated list of asset summaries.

    Args:
        region: AWS region (default: us-east-1)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-250, default: 50)
        asset_model_id: The ID of the asset model by which to filter the list of assets
        filter_type: The filter for the requested list of assets (ALL, TOP_LEVEL)

    Returns:
        Dictionary containing list of assets
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | No | AWS region |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-250) |
| `asset_model_id` | string | No | The ID of the asset model by which to filter the list of assets |
| `filter_type` | string | No | Filter assets by ALL or TOP_LEVEL |

## AWS CLI

```bash
aws iotsitewise list-assets --next-token <next_token> --max-results <max_results> --asset-model-id <asset_model_id> --filter <filter_type>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.list_assets(
    NextToken=next_token,
    MaxResults=max_results,
    AssetModelId=asset_model_id,
    Filter=filter_type,
)
```
