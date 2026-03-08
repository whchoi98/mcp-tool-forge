---
name: GetAHOReadSetMetadata
description: Get metadata for a specific read set in a HealthOmics sequence store.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        read_set_id: The ID of the read set

    Returns:
        Dictionary containing read set metadata
    
---

# Getahoreadsetmetadata

Get metadata for a specific read set in a HealthOmics sequence store.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        read_set_id: The ID of the read set

    Returns:
        Dictionary containing read set metadata
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sequence_store_id` | string | Yes | The ID of the sequence store |
| `read_set_id` | string | Yes | The ID of the read set |

## AWS CLI

```bash
aws omics get-read-set --sequence-store-id <sequence_store_id> --id <read_set_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_read_set(
    SequenceStoreId=sequence_store_id,
    Id=read_set_id,
)
```
