---
name: start-dicom-import-job
description: Start a DICOM import job.
---

# Start Dicom Import Job

Start a DICOM import job.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the target datastore |
| `data_access_role_arn` | string | Yes | IAM role ARN for data access |
| `input_s3_uri` | string | Yes | S3 URI of the input data |
| `job_name` | string | No | Name for the import job |
| `client_token` | string | No | Client token for idempotency |
| `output_s3_uri` | string | No | S3 URI for the output data |
| `input_owner_account_id` | string | No | Input owner account ID |

## AWS CLI

```bash
aws medical-imaging start-dicom-import-job --datastore-id <datastore_id> --data-access-role-arn <data_access_role_arn> --input-s3-uri <input_s3_uri> --job-name <job_name> --client-token <client_token> --output-s3-uri <output_s3_uri> --input-owner-account-id <input_owner_account_id>
```

## boto3

```python
import boto3

client = boto3.client('healthimaging')
response = client.start_dicom_import_job(
    DatastoreId=datastore_id,
    DataAccessRoleArn=data_access_role_arn,
    InputS3Uri=input_s3_uri,
    JobName=job_name,
    ClientToken=client_token,
    OutputS3Uri=output_s3_uri,
    InputOwnerAccountId=input_owner_account_id,
)
```
