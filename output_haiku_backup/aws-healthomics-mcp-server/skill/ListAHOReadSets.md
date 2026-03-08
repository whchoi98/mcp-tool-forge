---
name: ListAHOReadSets
description: List read sets in a HealthOmics sequence store with optional filtering.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        sample_id: Filter by sample ID
        subject_id: Filter by subject ID
        reference_arn: Filter by reference ARN
        status: Filter by read set status
        file_type: Filter by file type
        created_after: Filter for read sets created after this datetime
        created_before: Filter for read sets created before this datetime
        max_results: Maximum number of results to return
        next_token: Token for pagination

    Returns:
        Dictionary containing read set list and optional next token
    
---

# Listahoreadsets

List read sets in a HealthOmics sequence store with optional filtering.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        sample_id: Filter by sample ID
        subject_id: Filter by subject ID
        reference_arn: Filter by reference ARN
        status: Filter by read set status
        file_type: Filter by file type
        created_after: Filter for read sets created after this datetime
        created_before: Filter for read sets created before this datetime
        max_results: Maximum number of results to return
        next_token: Token for pagination

    Returns:
        Dictionary containing read set list and optional next token
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sequence_store_id` | string | Yes | The ID of the sequence store |
| `sample_id` | string | No | Filter by sample ID |
| `subject_id` | string | No | Filter by subject ID |
| `reference_arn` | string | No | Filter by reference ARN |
| `status` | string | No | Filter by read set status (e.g., ACTIVE, ARCHIVED) |
| `file_type` | string | No | Filter by file type (FASTQ, BAM, CRAM, or UBAM) |
| `created_after` | string | No | Filter for read sets created after this ISO 8601 datetime |
| `created_before` | string | No | Filter for read sets created before this ISO 8601 datetime |
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Token for pagination from a previous response |

## AWS CLI

```bash
aws omics list-read-sets --sequence-store-id <sequence_store_id> --sample-id <sample_id> --subject-id <subject_id> --reference-arn <reference_arn> --status <status> --file-type <file_type> --created-after <created_after> --created-before <created_before> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_read_sets(
    SequenceStoreId=sequence_store_id,
    SampleId=sample_id,
    SubjectId=subject_id,
    ReferenceArn=reference_arn,
    Status=status,
    FileType=file_type,
    CreatedAfter=created_after,
    CreatedBefore=created_before,
    MaxResults=max_results,
    NextToken=next_token,
)
```
