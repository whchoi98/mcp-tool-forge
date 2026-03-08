---
name: list-associated-assets
description: Retrieve a paginated list of associated assets.

    Args:
        asset_id: The ID of the asset to query. Accepts UUID format (12345678-1234-1234-1234-123456789012)
                 or external ID format (externalId:my-external-id). Use list_assets to get the
                 correct ID if you only have the asset name.
        region: AWS region (default: us-east-1)
        hierarchy_id: The ID of the hierarchy by which child assets are             associated
        traversal_direction: The direction to list associated assets (
            PARENT,
            CHILD)         next_token: The token to be used for the next set of                                                 paginated results
        max_results: The maximum number of results to return (
            1-250,
            default: 50)

    Returns:
        Dictionary containing list of associated assets
    
---

# List Associated Assets

Retrieve a paginated list of associated assets.

    Args:
        asset_id: The ID of the asset to query. Accepts UUID format (12345678-1234-1234-1234-123456789012)
                 or external ID format (externalId:my-external-id). Use list_assets to get the
                 correct ID if you only have the asset name.
        region: AWS region (default: us-east-1)
        hierarchy_id: The ID of the hierarchy by which child assets are             associated
        traversal_direction: The direction to list associated assets (
            PARENT,
            CHILD)         next_token: The token to be used for the next set of                                                 paginated results
        max_results: The maximum number of results to return (
            1-250,
            default: 50)

    Returns:
        Dictionary containing list of associated assets
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `asset_id` | string | Yes | The ID of the asset to query (UUID format: 12345678-1234-1234-1234-123456789012 or external ID format: externalId:my-external-id) |
| `region` | string | No | AWS region |
| `hierarchy_id` | string | No | The ID of the hierarchy by which child assets are associated |
| `traversal_direction` | string | No | The direction to list associated assets (PARENT, CHILD) |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-250) |

## AWS CLI

```bash
aws iotsitewise list-associated-assets --asset-id <asset_id> --hierarchy-id <hierarchy_id> --traversal-direction <traversal_direction> --next-token <next_token> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.list_associated_assets(
    AssetId=asset_id,
    HierarchyId=hierarchy_id,
    TraversalDirection=traversal_direction,
    NextToken=next_token,
    MaxResults=max_results,
)
```
