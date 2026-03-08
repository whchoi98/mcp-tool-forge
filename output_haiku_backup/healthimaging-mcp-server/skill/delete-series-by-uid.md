---
name: delete-series-by-uid
description: Delete a series by SeriesInstanceUID using metadata updates.
---

# Delete Series By Uid

Delete a series by SeriesInstanceUID using metadata updates.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `series_instance_uid` | string | Yes | DICOM Series Instance UID to delete |

## AWS CLI

```bash
aws medical-imaging delete-series --datastore-id <datastore_id> --series-instance-uid <series_instance_uid>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.delete_series(
    DatastoreId=datastore_id,
    SeriesInstanceUid=series_instance_uid,
)
```
