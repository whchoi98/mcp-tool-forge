---
name: StartAHOReferenceImportJob
description: Start a reference import job to import reference files from S3 into a reference store.

    AWS HealthOmics allows only one reference store per account per region.
    If reference_store_id is not provided, it will be automatically resolved.

    Each source in the sources list is validated against the ReferenceImportSource model
    and must include:
      - sourceFile: S3 URI pointing to a FASTA reference file (e.g. "s3://bucket/GRCh38.fasta")
      - name: A name for the reference (e.g. "GRCh38")
      - description (optional): A description of the reference
      - tags (optional): Key-value tags as {"key": "value"}

    Example sources JSON:
        [{"sourceFile": "s3://bucket/GRCh38.fasta", "name": "GRCh38",
          "description": "Human reference genome build 38",
          "tags": {"build": "38", "species": "human"}}]

    Args:
        ctx: MCP context for error reporting
        role_arn: IAM role ARN for the import job
        sources: JSON list of import sources (validated against ReferenceImportSource)
        reference_store_id: The ID of the reference store (auto-resolved if omitted)

    Returns:
        Dictionary containing the import job information
    
---

# Startahoreferenceimportjob

Start a reference import job to import reference files from S3 into a reference store.

    AWS HealthOmics allows only one reference store per account per region.
    If reference_store_id is not provided, it will be automatically resolved.

    Each source in the sources list is validated against the ReferenceImportSource model
    and must include:
      - sourceFile: S3 URI pointing to a FASTA reference file (e.g. "s3://bucket/GRCh38.fasta")
      - name: A name for the reference (e.g. "GRCh38")
      - description (optional): A description of the reference
      - tags (optional): Key-value tags as {"key": "value"}

    Example sources JSON:
        [{"sourceFile": "s3://bucket/GRCh38.fasta", "name": "GRCh38",
          "description": "Human reference genome build 38",
          "tags": {"build": "38", "species": "human"}}]

    Args:
        ctx: MCP context for error reporting
        role_arn: IAM role ARN for the import job
        sources: JSON list of import sources (validated against ReferenceImportSource)
        reference_store_id: The ID of the reference store (auto-resolved if omitted)

    Returns:
        Dictionary containing the import job information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `role_arn` | string | Yes | IAM role ARN for the import job |
| `sources` | string | Yes | JSON list of import sources. Each source requires: sourceFile (S3 URI to a FASTA reference file), name. Optional fields: description, tags. Example: [{"sourceFile": "s3://bucket/GRCh38.fasta", "name": "GRCh38", "description": "Human reference genome build 38", "tags": {"build": "38", "species": "human"}}] |
| `reference_store_id` | string | No | The ID of the reference store. If not provided, auto-resolves the single store in the account/region. |

## AWS CLI

```bash
aws omics start-reference-import-job --reference-store-id <reference_store_id> --role-arn <role_arn> --sources <sources>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.start_reference_import_job(
    ReferenceStoreId=reference_store_id,
    RoleArn=role_arn,
    Sources=sources,
)
```
