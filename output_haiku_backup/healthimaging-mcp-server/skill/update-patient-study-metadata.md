---
name: update-patient-study-metadata
description: Update Patient/Study metadata for an entire study.
---

# Update Patient Study Metadata

Update Patient/Study metadata for an entire study.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `study_instance_uid` | string | Yes | DICOM Study Instance UID |
| `patient_updates` | object | Yes | Patient-level DICOM metadata updates |
| `study_updates` | object | Yes | Study-level DICOM metadata updates |

## AWS CLI

```bash
aws medical-imaging update-image-set-metadata --datastore-id <datastore_id> --study-instance-uid <study_instance_uid> --patient-metadata <patient_updates> --study-metadata <study_updates>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.update_image_set_metadata(
    DatastoreId=datastore_id,
    StudyInstanceUid=study_instance_uid,
    PatientMetadata=patient_updates,
    StudyMetadata=study_updates,
)
```
