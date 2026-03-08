---
name: StartAHOReadSetImportJob
description: Start a read set import job to import genomic files from S3 into a sequence store.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        role_arn: IAM role ARN for the import job
        sources: JSON list of import sources
        tags: Tags as a JSON string or dict

    Returns:
        Dictionary containing the import job information
    
---

# Startahoreadsetimportjob

Start a read set import job to import genomic files from S3 into a sequence store.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        role_arn: IAM role ARN for the import job
        sources: JSON list of import sources
        tags: Tags as a JSON string or dict

    Returns:
        Dictionary containing the import job information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sequence_store_id` | string | Yes | The ID of the sequence store |
| `role_arn` | string | Yes | IAM role ARN for the import job |
| `sources` | string | Yes | JSON list of import sources. Each source requires: sourceFileType (FASTQ|BAM|CRAM|UBAM), sourceFiles (object with source1 required, source2 optional for paired-end FASTQ), subjectId, sampleId. Optional fields: referenceArn, name, description, generatedFrom, tags. Example: [{"sourceFileType": "FASTQ", "sourceFiles": {"source1": "s3://bucket/sample_R1.fastq.gz", "source2": "s3://bucket/sample_R2.fastq.gz"}, "subjectId": "subject-1", "sampleId": "sample-1", "referenceArn": "arn:aws:omics:us-east-1:123456789012:referenceStore/123/reference/456", "name": "my-reads"}] |
| `tags` | string | No | Tags to apply to the import job as a JSON string or object, e.g. {"key": "value"} |

## AWS CLI

```bash
aws omics start-read-set-import-job --sequence-store-id <sequence_store_id> --role-arn <role_arn> --sources <sources> --tags <tags>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.start_read_set_import_job(
    SequenceStoreId=sequence_store_id,
    RoleArn=role_arn,
    Sources=sources,
    Tags=tags,
)
```
