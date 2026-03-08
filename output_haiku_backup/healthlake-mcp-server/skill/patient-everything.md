---
name: patient-everything
description: Retrieve all resources related to a specific patient using the FHIR $patient-everything operation
---

# Patient Everything

Retrieve all resources related to a specific patient using the FHIR $patient-everything operation

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | HealthLake datastore ID |
| `patient_id` | string | Yes | Patient resource ID |
| `start` | string | No | Start date for filtering resources (YYYY-MM-DD format) |
| `end` | string | No | End date for filtering resources (YYYY-MM-DD format) |
| `count` | integer | No | Maximum number of results to return (1-100, default: 100) |
| `next_token` | string | No | Pagination token for retrieving the next page of results. Use the complete URL from a previous response's pagination.next_token field. |

## AWS CLI

```bash
aws healthlake start-fhir-export-job --datastore-id <datastore_id> --output-data-config <s3_output_path> --start-time <start> --end-time <end> --max-results <count> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('healthlake')
response = client.start_fhir_export_job(
    DatastoreId=datastore_id,
    OutputDataConfig={'S3Configuration': {'S3Uri': 's3://bucket/path'}},
    StartTime=start,
    EndTime=end,
    MaxResults=count,
    NextToken=next_token,
)
```
