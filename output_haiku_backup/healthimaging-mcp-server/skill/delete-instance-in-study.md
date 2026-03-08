---
name: delete-instance-in-study
description: Delete a specific instance in a study.
---

# Delete Instance In Study

Delete a specific instance in a study.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `study_instance_uid` | string | Yes | DICOM Study Instance UID |
| `sop_instance_uid` | string | Yes | DICOM SOP Instance UID to delete |

## AWS CLI

```bash
aws medical-imaging delete-dicom-instance --datastore-id <datastore_id> --study-instance-uid <study_instance_uid> --sop-instance-uid <sop_instance_uid>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.delete_dicom_instance(
    DatastoreId=datastore_id,
    StudyInstanceUid=study_instance_uid,
    SeriesInstanceUid=,
    SopInstanceUid=sop_instance_uid,
)
```
