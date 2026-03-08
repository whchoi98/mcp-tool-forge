---
name: get-image-frame
description: Get a specific image frame.
---

# Get Image Frame

Get a specific image frame.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `image_set_id` | string | Yes | ID of the image set |
| `image_frame_information` | object | Yes | Image frame information |

## AWS CLI

```bash
aws medical-imaging get-image-frame --datastore-id <datastore_id> --image-set-id <image_set_id> --image-frame-information <image_frame_information>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.get_image_frame(
    DatastoreId=datastore_id,
    ImageSetId=image_set_id,
    ImageFrameInformation=image_frame_information,
)
```
