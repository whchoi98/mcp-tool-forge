---
name: start-dicom-export-job
description: Start a DICOM export job.
---

# Start Dicom Export Job

Start a DICOM export job.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the source datastore |
| `data_access_role_arn` | string | Yes | IAM role ARN for data access |
| `output_s3_uri` | string | Yes | S3 URI for the output data |
| `job_name` | string | No | Name for the export job |
| `client_token` | string | No | Client token for idempotency |
| `study_instance_uid` | string | No | Study instance UID to export |
| `series_instance_uid` | string | No | Series instance UID to export |
| `sop_instance_uid` | string | No | SOP instance UID to export |
| `submitted_before` | string | No | Export images submitted before this date |
| `submitted_after` | string | No | Export images submitted after this date |

## AWS CLI

```bash
aws medical-imaging start-dicom-export-job --datastore-id <datastore_id> --data-access-role-arn <data_access_role_arn> --output-s3-uri <output_s3_uri> --job-name <job_name> --client-token <client_token> --study-instance-uid <study_instance_uid> --series-instance-uid <series_instance_uid> --sop-instance-uid <sop_instance_uid> --submitted-before <submitted_before> --submitted-after <submitted_after>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.start_dicom_export_job(
    DatastoreId=datastore_id,
    DataAccessRoleArn=data_access_role_arn,
    OutputS3Uri=output_s3_uri,
    JobName=job_name,
    ClientToken=client_token,
    StudyInstanceUid=study_instance_uid,
    SeriesInstanceUid=series_instance_uid,
    SopInstanceUid=sop_instance_uid,
    SubmittedBefore=submitted_before,
    SubmittedAfter=submitted_after,
)
```
