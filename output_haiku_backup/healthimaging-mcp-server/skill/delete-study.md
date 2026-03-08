---
name: delete-study
description: Delete all image sets for a specific study.
---

# Delete Study

Delete all image sets for a specific study.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `study_instance_uid` | string | Yes | DICOM Study Instance UID |

## AWS CLI

```bash
aws medical-imaging delete-study --datastore-id <datastore_id> --study-instance-uid <study_instance_uid>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.delete_study(
    DatastoreId=datastore_id,
    StudyInstanceUid=study_instance_uid,
)
```
