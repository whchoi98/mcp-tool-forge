---
name: remove-instance-from-image-set
description: Remove a specific instance from an image set using DICOM hierarchy operations.
---

# Remove Instance From Image Set

Remove a specific instance from an image set using DICOM hierarchy operations.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `image_set_id` | string | Yes | ID of the image set |
| `series_instance_uid` | string | Yes | DICOM Series Instance UID containing the instance |
| `sop_instance_uid` | string | Yes | DICOM SOP Instance UID to remove from the image set |

## AWS CLI

```bash
aws healthimaging remove-image-set-instances --datastore-id <datastore_id> --image-set-id <image_set_id> --instances <[{"SeriesInstanceUid":"series_instance_uid","SopInstanceUid":"sop_instance_uid"}]>
```

## boto3

```python
import boto3

client = boto3.client('healthimaging')
response = client.remove_image_set_instances(
    DatastoreId=datastore_id,
    ImageSetId=image_set_id,
    Instances=[{'SeriesInstanceUid': 'series_instance_uid', 'SopInstanceUid': 'sop_instance_uid'}],
)
```
