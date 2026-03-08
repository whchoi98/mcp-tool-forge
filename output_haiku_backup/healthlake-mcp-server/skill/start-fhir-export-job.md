---
name: start-fhir-export-job
description: Start a FHIR export job to export data from HealthLake
---

# Start Fhir Export Job

Start a FHIR export job to export data from HealthLake

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | HealthLake datastore ID |
| `output_data_config` | object | Yes | Output data configuration |
| `data_access_role_arn` | string | Yes | IAM role ARN for data access |
| `job_name` | string | No | Name for the export job |

## AWS CLI

```bash
aws healthlake start-fhir-export-job --datastore-id <datastore_id> --output-data-config <output_data_config> --data-access-role-arn <data_access_role_arn> --job-name <job_name>
```

## boto3

```python
import boto3

client = boto3.client('healthlake')
response = client.start_fhir_export_job(
    DatastoreId=datastore_id,
    OutputDataConfig=output_data_config,
    DataAccessRoleArn=data_access_role_arn,
    JobName=job_name,
)
```
