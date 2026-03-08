---
name: get-dicom-export-job
description: Get information about a DICOM export job.
---

# Get Dicom Export Job

Get information about a DICOM export job.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `job_id` | string | Yes | ID of the export job |

## AWS CLI

```bash
aws medical-imaging get-dicom-export-job --datastore-id <datastore_id> --job-id <job_id>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.get_dicom_export_job(
    DatastoreId=datastore_id,
    JobId=job_id,
)
```
