---
name: GetAHOReferenceImportJob
description: Get details about a reference import job.

    AWS HealthOmics allows only one reference store per account per region.
    If reference_store_id is not provided, it will be automatically resolved.

    Args:
        ctx: MCP context for error reporting
        import_job_id: The ID of the import job
        reference_store_id: The ID of the reference store (auto-resolved if omitted)

    Returns:
        Dictionary containing the import job details
    
---

# Getahoreferenceimportjob

Get details about a reference import job.

    AWS HealthOmics allows only one reference store per account per region.
    If reference_store_id is not provided, it will be automatically resolved.

    Args:
        ctx: MCP context for error reporting
        import_job_id: The ID of the import job
        reference_store_id: The ID of the reference store (auto-resolved if omitted)

    Returns:
        Dictionary containing the import job details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `import_job_id` | string | Yes | The ID of the import job |
| `reference_store_id` | string | No | The ID of the reference store. If not provided, auto-resolves the single store in the account/region. |

## AWS CLI

```bash
aws omics get-reference-import-job --reference-import-job-id <import_job_id> --reference-store-id <reference_store_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_reference_import_job(
    ReferenceImportJobId=import_job_id,
    ReferenceStoreId=reference_store_id,
)
```
