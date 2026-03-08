---
name: StartAHOReadSetExportJob
description: Start a read set export job to export read sets from a sequence store to S3.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        destination_s3_uri: S3 URI for the export destination
        role_arn: IAM role ARN for the export job
        read_set_ids: List of read set IDs to export

    Returns:
        Dictionary containing the export job information
    
---

# Startahoreadsetexportjob

Start a read set export job to export read sets from a sequence store to S3.

    Args:
        ctx: MCP context for error reporting
        sequence_store_id: The ID of the sequence store
        destination_s3_uri: S3 URI for the export destination
        role_arn: IAM role ARN for the export job
        read_set_ids: List of read set IDs to export

    Returns:
        Dictionary containing the export job information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sequence_store_id` | string | Yes | The ID of the sequence store |
| `destination_s3_uri` | string | Yes | S3 URI for the export destination |
| `role_arn` | string | Yes | IAM role ARN for the export job |
| `read_set_ids` | string | Yes | List of read set IDs to export as a JSON list or array, e.g. ["id1", "id2"] |

## AWS CLI

```bash
aws omics start-read-set-export-job --sequence-store-id <sequence_store_id> --destination-s3-uri <destination_s3_uri> --role-arn <role_arn> --read-set-ids <read_set_ids>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.start_read_set_export_job(
    SequenceStoreId=sequence_store_id,
    DestinationS3Uri=destination_s3_uri,
    RoleArn=role_arn,
    ReadSetIds=read_set_ids,
)
```
