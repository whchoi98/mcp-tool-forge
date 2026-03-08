---
name: get-patient-series
description: Get all series for a specific patient.
---

# Get Patient Series

Get all series for a specific patient.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `patient_id` | string | Yes | DICOM Patient ID |

## AWS CLI

```bash
aws healthimaging list-dicom-series --datastore-id <datastore_id> --patient-id <patient_id>
```

## boto3

```python
import boto3

client = boto3.client('healthimaging')
response = client.list_dicom_series(
    DatastoreId=datastore_id,
    PatientId=patient_id,
)
```
