---
name: get-patient-dicomweb-studies
description: Retrieve DICOMweb SearchStudies level information for a given patient ID.
---

# Get Patient Dicomweb Studies

Retrieve DICOMweb SearchStudies level information for a given patient ID.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `patient_id` | string | Yes | DICOM Patient ID |

## AWS CLI

```bash
aws medical-imaging search-dicom-studies --datastore-id <datastore_id> --search-criteria <{"PatientId": "patient_id"}>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.search_dicom_studies(
    DatastoreId=datastore_id,
    SearchCriteria={'PatientId': 'patient_id'},
)
```
