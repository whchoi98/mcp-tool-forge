---
name: GetAHOReferenceStore
description: Get details about a specific HealthOmics reference store.

    AWS HealthOmics allows only one reference store per account per region.
    If reference_store_id is not provided, it will be automatically resolved.

    Args:
        ctx: MCP context for error reporting
        reference_store_id: The ID of the reference store (auto-resolved if omitted)

    Returns:
        Dictionary containing reference store details
    
---

# Getahoreferencestore

Get details about a specific HealthOmics reference store.

    AWS HealthOmics allows only one reference store per account per region.
    If reference_store_id is not provided, it will be automatically resolved.

    Args:
        ctx: MCP context for error reporting
        reference_store_id: The ID of the reference store (auto-resolved if omitted)

    Returns:
        Dictionary containing reference store details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `reference_store_id` | string | No | The ID of the reference store. If not provided, auto-resolves the single store in the account/region. |

## AWS CLI

```bash
aws omics get-reference-store --reference-store-id <reference_store_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_reference_store(
    ReferenceStoreId=reference_store_id,
)
```
