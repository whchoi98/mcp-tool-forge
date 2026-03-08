---
name: UpdateAHOSequenceStore
description: Update a HealthOmics sequence store.

    Internally fetches the current ETag before performing the update to handle
    optimistic concurrency control.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store to update
        name: New name for the sequence store
        description: New description for the sequence store
        fallback_location: New S3 URI for the fallback location

    Returns:
        Dictionary containing the updated sequence store details
    
---

# Updateahosequencestore

Update a HealthOmics sequence store.

    Internally fetches the current ETag before performing the update to handle
    optimistic concurrency control.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store to update
        name: New name for the sequence store
        description: New description for the sequence store
        fallback_location: New S3 URI for the fallback location

    Returns:
        Dictionary containing the updated sequence store details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sequence_store_id` | string | Yes | The ID of the sequence store to update |
| `name` | string | No | New name for the sequence store |
| `description` | string | No | New description for the sequence store |
| `fallback_location` | string | No | New S3 URI for the fallback location |

## AWS CLI

```bash
aws omics update-sequence-store --sequence-store-id <sequence_store_id> --name <name> --description <description> --fallback-location <fallback_location>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.update_sequence_store(
    SequenceStoreId=sequence_store_id,
    Name=name,
    Description=description,
    FallbackLocation=fallback_location,
)
```
