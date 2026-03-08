---
name: create-bulk-import-schema
description: Construct and validate a bulk import schema.

    Args:
        asset_models: List of asset model definitions. Each must include:
            - assetModelName: string
            - assetModelExternalId: string (required for asset references)
            - assetModelProperties: list with name, externalId, dataType, type
            - assetModelHierarchies: list with name, externalId, childAssetModelExternalId
        assets: List of asset definitions. Each must include:
            - assetName: string
            - assetExternalId: string
            - assetModelExternalId: string (must match an asset model)
            - assetProperties: list with externalId (matching model property), alias
            - assetHierarchies: list with externalId (matching model hierarchy), childAssetExternalId

    Returns:
        dict: Validated JSON structure for AWS IoT SiteWise bulk import.
    
---

# Create Bulk Import Schema

Construct and validate a bulk import schema.

    Args:
        asset_models: List of asset model definitions. Each must include:
            - assetModelName: string
            - assetModelExternalId: string (required for asset references)
            - assetModelProperties: list with name, externalId, dataType, type
            - assetModelHierarchies: list with name, externalId, childAssetModelExternalId
        assets: List of asset definitions. Each must include:
            - assetName: string
            - assetExternalId: string
            - assetModelExternalId: string (must match an asset model)
            - assetProperties: list with externalId (matching model property), alias
            - assetHierarchies: list with externalId (matching model hierarchy), childAssetExternalId

    Returns:
        dict: Validated JSON structure for AWS IoT SiteWise bulk import.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `asset_models` | string | No |  |
| `assets` | string | No |  |

## AWS CLI

```bash
aws iotsitewise create-bulk-import-job --job-name <asset_models> --job-role-arn <assets>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.create_bulk_import_job(
    JobName=asset_models,
    JobRoleArn=assets,
)
```
