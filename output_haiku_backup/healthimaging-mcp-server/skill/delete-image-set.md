---
name: delete-image-set
description: Delete an image set.
---

# Delete Image Set

Delete an image set.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `image_set_id` | string | Yes | ID of the image set |
| `version_id` | string | No | Version ID of the image set |

## AWS CLI

```bash
aws medical-imaging delete-image-set --datastore-id <datastore_id> --image-set-id <image_set_id> --version <version_id>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.delete_image_set(
    DatastoreId=datastore_id,
    ImageSetId=image_set_id,
    Version=version_id,
)
```
