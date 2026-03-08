---
name: ListAHOReferenceImportJobs
description: List reference import jobs for a reference store.

    AWS HealthOmics allows only one reference store per account per region.
    If reference_store_id is not provided, it will be automatically resolved.

    Args:
        ctx: MCP context for error reporting
        reference_store_id: The ID of the reference store (auto-resolved if omitted)
        max_results: Maximum number of results to return
        next_token: Token for pagination

    Returns:
        Dictionary containing import job list and optional next token
    
---

# Listahoreferenceimportjobs

List reference import jobs for a reference store.

    AWS HealthOmics allows only one reference store per account per region.
    If reference_store_id is not provided, it will be automatically resolved.

    Args:
        ctx: MCP context for error reporting
        reference_store_id: The ID of the reference store (auto-resolved if omitted)
        max_results: Maximum number of results to return
        next_token: Token for pagination

    Returns:
        Dictionary containing import job list and optional next token
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `reference_store_id` | string | No | The ID of the reference store. If not provided, auto-resolves the single store in the account/region. |
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Token for pagination from a previous response |

## AWS CLI

```bash
aws omics list-reference-import-jobs --reference-store-id <reference_store_id> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_reference_import_jobs(
    ReferenceStoreId=reference_store_id,
    MaxResults=max_results,
    NextToken=next_token,
)
```
