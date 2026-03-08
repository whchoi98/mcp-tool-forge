---
name: describe-bulk-import-job
description: Get detailed information about a specific bulk import job in AWS IoT SiteWise.

    This function retrieves comprehensive details about a bulk import job including its configuration,
    status, progress, error information, and execution statistics.

    Args:
        job_id: The unique identifier of the bulk import job (UUID format)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing:
        - success: Boolean indicating operation success
        - job_id: The job identifier
        - job_name: The job name
        - job_status: Current status of the job
        - job_role_arn: IAM role ARN used by the job
        - files: List of input files
        - error_report_location: S3 location for error reports
        - job_configuration: Job configuration details
        - job_creation_date: When the job was created
        - job_last_update_date: When the job was last updated
        - adaptive_ingestion: Whether adaptive ingestion is enabled
        - delete_files_after_import: Whether files are deleted after import
        - Additional fields based on job status and execution

    Example:
        # Get details for a specific job
        result = describe_bulk_import_job(
            job_id="12345678-1234-1234-1234-123456789012"
        )

        if result['success']:
            print(f"Job Status: {result['job_status']}")
            print(f"Job Name: {result['job_name']}")
    
---

# Describe Bulk Import Job

Get detailed information about a specific bulk import job in AWS IoT SiteWise.

    This function retrieves comprehensive details about a bulk import job including its configuration,
    status, progress, error information, and execution statistics.

    Args:
        job_id: The unique identifier of the bulk import job (UUID format)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing:
        - success: Boolean indicating operation success
        - job_id: The job identifier
        - job_name: The job name
        - job_status: Current status of the job
        - job_role_arn: IAM role ARN used by the job
        - files: List of input files
        - error_report_location: S3 location for error reports
        - job_configuration: Job configuration details
        - job_creation_date: When the job was created
        - job_last_update_date: When the job was last updated
        - adaptive_ingestion: Whether adaptive ingestion is enabled
        - delete_files_after_import: Whether files are deleted after import
        - Additional fields based on job status and execution

    Example:
        # Get details for a specific job
        result = describe_bulk_import_job(
            job_id="12345678-1234-1234-1234-123456789012"
        )

        if result['success']:
            print(f"Job Status: {result['job_status']}")
            print(f"Job Name: {result['job_name']}")
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `job_id` | string | Yes | The ID of the bulk import job to describe (UUID format) |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise describe-bulk-import-job --job-id <job_id> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_bulk_import_job(
    JobId=job_id,
    Region=region,
)
```
