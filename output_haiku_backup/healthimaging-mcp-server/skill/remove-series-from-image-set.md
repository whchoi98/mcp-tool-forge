---
name: remove-series-from-image-set
description: Remove a specific series from an image set using DICOM hierarchy operations.
---

# Remove Series From Image Set

Remove a specific series from an image set using DICOM hierarchy operations.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `image_set_id` | string | Yes | ID of the image set |
| `series_instance_uid` | string | Yes | DICOM Series Instance UID to remove from the image set |

## AWS CLI

```bash
aws medical-imaging update-image-set-metadata --datastore-id <datastore_id> --image-set-id <image_set_id> --update-image-set-metadata-updates <{"RemoveSeries": ["series_instance_uid"]}>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.update_image_set_metadata(
    DatastoreId=datastore_id,
    ImageSetId=image_set_id,
    UpdateImageSetMetadataUpdates={'RemoveSeries': ['series_instance_uid']},
)
```
