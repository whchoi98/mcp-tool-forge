---
name: list-image-set-versions
description: List versions of an image set.
---

# List Image Set Versions

List versions of an image set.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `image_set_id` | string | Yes | ID of the image set |
| `next_token` | string | No | Token for pagination |
| `max_results` | string | No | Maximum number of results to return (1-50) |

## AWS CLI

```bash
aws medical-imaging list-image-set-versions --datastore-id <datastore_id> --image-set-id <image_set_id> --next-token <next_token> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.list_image_set_versions(
    DatastoreId=datastore_id,
    ImageSetId=image_set_id,
    NextToken=next_token,
    MaxResults=max_results,
)
```
