---
name: GetAHOReadSetImportJob
description: Get details about a read set import job.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        import_job_id: The ID of the import job

    Returns:
        Dictionary containing the import job details
    
---

# Getahoreadsetimportjob

Get details about a read set import job.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        import_job_id: The ID of the import job

    Returns:
        Dictionary containing the import job details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sequence_store_id` | string | Yes | The ID of the sequence store |
| `import_job_id` | string | Yes | The ID of the import job |

## AWS CLI

```bash
aws omics get-read-set-import-job --sequence-store-id <sequence_store_id> --id <import_job_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_read_set_import_job(
    SequenceStoreId=sequence_store_id,
    Id=import_job_id,
)
```
