---
name: ListAHOReadSetExportJobs
description: List read set export jobs for a sequence store.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        max_results: Maximum number of results to return
        next_token: Token for pagination

    Returns:
        Dictionary containing export job list and optional next token
    
---

# Listahoreadsetexportjobs

List read set export jobs for a sequence store.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        max_results: Maximum number of results to return
        next_token: Token for pagination

    Returns:
        Dictionary containing export job list and optional next token
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sequence_store_id` | string | Yes | The ID of the sequence store |
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Token for pagination from a previous response |

## AWS CLI

```bash
aws omics list-read-set-export-jobs --sequence-store-id <sequence_store_id> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_read_set_export_jobs(
    SequenceStoreId=sequence_store_id,
    MaxResults=max_results,
    NextToken=next_token,
)
```
