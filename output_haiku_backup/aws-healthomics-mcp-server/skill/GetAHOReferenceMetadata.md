---
name: GetAHOReferenceMetadata
description: Get metadata for a specific reference in a HealthOmics reference store.

    AWS HealthOmics allows only one reference store per account per region.
    If reference_store_id is not provided, it will be automatically resolved.

    Args:
        ctx: MCP context for error reporting
        reference_id: The ID of the reference
        reference_store_id: The ID of the reference store (auto-resolved if omitted)

    Returns:
        Dictionary containing reference metadata
    
---

# Getahoreferencemetadata

Get metadata for a specific reference in a HealthOmics reference store.

    AWS HealthOmics allows only one reference store per account per region.
    If reference_store_id is not provided, it will be automatically resolved.

    Args:
        ctx: MCP context for error reporting
        reference_id: The ID of the reference
        reference_store_id: The ID of the reference store (auto-resolved if omitted)

    Returns:
        Dictionary containing reference metadata
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `reference_id` | string | Yes | The ID of the reference |
| `reference_store_id` | string | No | The ID of the reference store. If not provided, auto-resolves the single store in the account/region. |

## AWS CLI

```bash
aws omics get-reference --reference-id <reference_id> --reference-store-id <reference_store_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_reference(
    ReferenceId=reference_id,
    ReferenceStoreId=reference_store_id,
)
```
