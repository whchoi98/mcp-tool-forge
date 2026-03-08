---
name: get-metadata-transfer-job
description: Get details of a metadata transfer job.

    Args:
        metadata_transfer_job_id: The ID of the metadata transfer job to retrieve
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing job details
    
---

# Get Metadata Transfer Job

Get details of a metadata transfer job.

    Args:
        metadata_transfer_job_id: The ID of the metadata transfer job to retrieve
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing job details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `metadata_transfer_job_id` | string | Yes | The metadata transfer job ID to retrieve |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise describe-metadata-transfer-job --job-id <metadata_transfer_job_id> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_metadata_transfer_job(
    JobId=metadata_transfer_job_id,
    Region=region,
)
```
