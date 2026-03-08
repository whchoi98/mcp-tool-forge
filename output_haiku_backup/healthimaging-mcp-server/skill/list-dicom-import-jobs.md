---
name: list-dicom-import-jobs
description: List DICOM import jobs for a data store.
---

# List Dicom Import Jobs

List DICOM import jobs for a data store.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `job_status` | string | No | Filter by job status (SUBMITTED, IN_PROGRESS, COMPLETED, FAILED) |
| `next_token` | string | No | Token for pagination |
| `max_results` | string | No | Maximum number of results to return (1-50) |

## AWS CLI

```bash
aws medical-imaging list-dicom-import-jobs --datastore-id <datastore_id> --job-status <job_status> --next-token <next_token> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.list_dicom_import_jobs(
    DatastoreId=datastore_id,
    JobStatus=job_status,
    NextToken=next_token,
    MaxResults=max_results,
)
```
