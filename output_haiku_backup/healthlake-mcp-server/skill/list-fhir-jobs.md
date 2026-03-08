---
name: list-fhir-jobs
description: List FHIR import/export jobs
---

# List Fhir Jobs

List FHIR import/export jobs

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | HealthLake datastore ID |
| `job_status` | string | No | Filter jobs by status |
| `job_type` | string | No | Type of job to list |

## AWS CLI

```bash
aws healthlake list-fhir-jobs --datastore-id <datastore_id> --job-status <job_status> --job-type <job_type>
```

## boto3

```python
import boto3

client = boto3.client('healthlake')
response = client.list_fhir_jobs(
    DatastoreId=datastore_id,
    JobStatus=job_status,
    JobType=job_type,
)
```
