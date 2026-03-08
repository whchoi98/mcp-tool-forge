---
name: start-fhir-import-job
description: Start a FHIR import job to load data into HealthLake
---

# Start Fhir Import Job

Start a FHIR import job to load data into HealthLake

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | HealthLake datastore ID |
| `input_data_config` | object | Yes | Input data configuration |
| `job_output_data_config` | object | Yes | Output data configuration (required for import jobs) |
| `data_access_role_arn` | string | Yes | IAM role ARN for data access |
| `job_name` | string | No | Name for the import job |

## AWS CLI

```bash
aws healthlake start-fhir-import-job --datastore-id <datastore_id> --input-data-config <input_data_config> --job-output-data-config <job_output_data_config> --data-access-role-arn <data_access_role_arn> --job-name <job_name>
```

## boto3

```python
import boto3

client = boto3.client('healthlake')
response = client.start_fhir_import_job(
    DatastoreId=datastore_id,
    InputDataConfig=input_data_config,
    JobOutputDataConfig=job_output_data_config,
    DataAccessRoleArn=data_access_role_arn,
    JobName=job_name,
)
```
