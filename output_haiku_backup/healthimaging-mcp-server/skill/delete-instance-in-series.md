---
name: delete-instance-in-series
description: Delete a specific instance in a series.
---

# Delete Instance In Series

Delete a specific instance in a series.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `series_instance_uid` | string | Yes | DICOM Series Instance UID |
| `sop_instance_uid` | string | Yes | DICOM SOP Instance UID to delete |

## AWS CLI

```bash
aws medical-imaging delete-dicom-instance --datastore-id <datastore_id> --series-instance-uid <series_instance_uid> --sop-instance-uid <sop_instance_uid>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.delete_dicom_instance(
    DatastoreId=datastore_id,
    SeriesInstanceUid=series_instance_uid,
    SopInstanceUid=sop_instance_uid,
)
```
