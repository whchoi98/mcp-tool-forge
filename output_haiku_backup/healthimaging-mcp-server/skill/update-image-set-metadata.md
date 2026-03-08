---
name: update-image-set-metadata
description: Update metadata for an image set.
---

# Update Image Set Metadata

Update metadata for an image set.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `image_set_id` | string | Yes | ID of the image set |
| `latest_version_id` | string | Yes | Latest version ID of the image set |
| `update_image_set_metadata_updates` | object | Yes | Metadata updates |

## AWS CLI

```bash
aws medical-imaging update-image-set-metadata --datastore-id <datastore_id> --image-set-id <image_set_id> --latest-version <latest_version_id> --update-image-set-metadata-updates <update_image_set_metadata_updates>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.update_image_set_metadata(
    DatastoreId=datastore_id,
    ImageSetId=image_set_id,
    LatestVersion=latest_version_id,
    UpdateImageSetMetadataUpdates=update_image_set_metadata_updates,
)
```
