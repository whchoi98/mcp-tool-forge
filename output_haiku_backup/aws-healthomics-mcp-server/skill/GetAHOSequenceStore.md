---
name: GetAHOSequenceStore
description: Get details about a specific HealthOmics sequence store.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store

    Returns:
        Dictionary containing sequence store details
    
---

# Getahosequencestore

Get details about a specific HealthOmics sequence store.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store

    Returns:
        Dictionary containing sequence store details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sequence_store_id` | string | Yes | The ID of the sequence store |

## AWS CLI

```bash
aws omics get-sequence-store --sequence-store-id <sequence_store_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_sequence_store(
    SequenceStoreId=sequence_store_id,
)
```
