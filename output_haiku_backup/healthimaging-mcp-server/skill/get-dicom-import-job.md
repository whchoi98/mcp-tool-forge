---
name: get-dicom-import-job
description: Get information about a DICOM import job.
---

# Get Dicom Import Job

Get information about a DICOM import job.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `job_id` | string | Yes | ID of the import job |

## AWS CLI

```bash
aws medical-imaging get-dicom-import-job --datastore-id <datastore_id> --job-id <job_id>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.get_dicom_import_job(
    DatastoreId=datastore_id,
    JobId=job_id,
)
```
