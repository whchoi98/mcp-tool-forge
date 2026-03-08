---
name: list-bulk-import-jobs
description: List bulk import jobs in AWS IoT SiteWise.

    This function retrieves a paginated list of bulk import job summaries with optional filtering
    by job status. Each job summary includes basic information like job ID, name, status, and timestamps.

    Args:
        filter: Optional filter to apply to the list. Valid values:
            - ALL: List all jobs (default)
            - PENDING: Jobs waiting to start
            - RUNNING: Jobs currently executing
            - CANCELLED: Jobs that were cancelled
            - FAILED: Jobs that failed
            - COMPLETED_WITH_FAILURES: Jobs completed but with some failures
            - COMPLETED: Jobs that completed successfully
        next_token: Token for paginated results
        max_results: Maximum number of results to return (1-250, default: 25)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing:
        - success: Boolean indicating operation success
        - job_summaries: List of job summary objects
        - next_token: Token for next page (if applicable)

    Example:
        # List all bulk import jobs
        result = list_bulk_import_jobs()

        # List only running jobs
        result = list_bulk_import_jobs(filter="RUNNING")

        # List with pagination
        result = list_bulk_import_jobs(max_results=10, next_token="...")
    
---

# List Bulk Import Jobs

List bulk import jobs in AWS IoT SiteWise.

    This function retrieves a paginated list of bulk import job summaries with optional filtering
    by job status. Each job summary includes basic information like job ID, name, status, and timestamps.

    Args:
        filter: Optional filter to apply to the list. Valid values:
            - ALL: List all jobs (default)
            - PENDING: Jobs waiting to start
            - RUNNING: Jobs currently executing
            - CANCELLED: Jobs that were cancelled
            - FAILED: Jobs that failed
            - COMPLETED_WITH_FAILURES: Jobs completed but with some failures
            - COMPLETED: Jobs that completed successfully
        next_token: Token for paginated results
        max_results: Maximum number of results to return (1-250, default: 25)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing:
        - success: Boolean indicating operation success
        - job_summaries: List of job summary objects
        - next_token: Token for next page (if applicable)

    Example:
        # List all bulk import jobs
        result = list_bulk_import_jobs()

        # List only running jobs
        result = list_bulk_import_jobs(filter="RUNNING")

        # List with pagination
        result = list_bulk_import_jobs(max_results=10, next_token="...")
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `filter` | string | No | Filter to apply to the list of bulk import jobs. Valid values: ALL, PENDING, RUNNING, CANCELLED, FAILED, COMPLETED_WITH_FAILURES, COMPLETED |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-250) |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise list-bulk-import-jobs --filter <filter> --next-token <next_token> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.list_bulk_import_jobs(
    Filter=filter,
    NextToken=next_token,
    MaxResults=max_results,
)
```
