---
name: get-image-set-metadata
description: Get metadata for a specific image set.
---

# Get Image Set Metadata

Get metadata for a specific image set.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `image_set_id` | string | Yes | ID of the image set |
| `version_id` | string | No | Version ID of the image set |

## AWS CLI

```bash
aws medical-imaging get-image-set-metadata --datastore-id <datastore_id> --image-set-id <image_set_id> --version-id <version_id>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.get_image_set_metadata(
    DatastoreId=datastore_id,
    ImageSetId=image_set_id,
    VersionId=version_id,
)
```
