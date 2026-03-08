---
name: get-patient-studies
description: Get all studies for a specific patient.
---

# Get Patient Studies

Get all studies for a specific patient.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `patient_id` | string | Yes | DICOM Patient ID |

## AWS CLI

```bash
aws medical-imaging search-image-sets --datastore-id <datastore_id> --search-criteria <patient_id>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.search_image_sets(
    DatastoreId=datastore_id,
    SearchCriteria={'PatientId': 'patient_id'},
)
```
