---
name: ActivateAHOReadSets
description: Activate archived read sets in a HealthOmics sequence store.

    Starts an activation job to move read sets from archive storage back to active storage.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        read_set_ids: List of read set IDs to activate

    Returns:
        Dictionary containing the activation job information
    
---

# Activateahoreadsets

Activate archived read sets in a HealthOmics sequence store.

    Starts an activation job to move read sets from archive storage back to active storage.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        read_set_ids: List of read set IDs to activate

    Returns:
        Dictionary containing the activation job information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sequence_store_id` | string | Yes | The ID of the sequence store |
| `read_set_ids` | string | Yes | List of read set IDs to activate as a JSON list or array, e.g. ["id1", "id2"] |

## AWS CLI

```bash
aws omics start-read-set-activation-job --sequence-store-id <sequence_store_id> --read-set-ids <read_set_ids>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.start_read_set_activation_job(
    SequenceStoreId=sequence_store_id,
    ReadSetIds=read_set_ids,
)
```
