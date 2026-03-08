---
name: copy-image-set
description: Copy an image set.
---

# Copy Image Set

Copy an image set.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the destination datastore |
| `source_image_set_id` | string | Yes | ID of the source image set |
| `copy_image_set_information` | object | Yes | Copy information |
| `source_datastore_id` | string | No | ID of the source datastore |

## AWS CLI

```bash
aws medical-imaging copy-image-set --destination-datastore-id <datastore_id> --source-image-set-id <source_image_set_id> --copy-image-set-information <copy_image_set_information> --source-datastore-id <source_datastore_id>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.copy_image_set(
    DestinationDatastoreId=datastore_id,
    SourceImageSetId=source_image_set_id,
    CopyImageSetInformation=copy_image_set_information,
    SourceDatastoreId=source_datastore_id,
)
```
