---
name: GetAHOReadSetExportJob
description: Get details about a read set export job.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        export_job_id: The ID of the export job

    Returns:
        Dictionary containing the export job details
    
---

# Getahoreadsetexportjob

Get details about a read set export job.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        export_job_id: The ID of the export job

    Returns:
        Dictionary containing the export job details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sequence_store_id` | string | Yes | The ID of the sequence store |
| `export_job_id` | string | Yes | The ID of the export job |

## AWS CLI

```bash
aws omics get-read-set-export-job --sequence-store-id <sequence_store_id> --id <export_job_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_read_set_export_job(
    SequenceStoreId=sequence_store_id,
    Id=export_job_id,
)
```
