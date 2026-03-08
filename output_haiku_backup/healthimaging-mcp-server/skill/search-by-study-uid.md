---
name: search-by-study-uid
description: Search for image sets by study instance UID.
---

# Search By Study Uid

Search for image sets by study instance UID.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `study_instance_uid` | string | Yes | DICOM Study Instance UID |
| `max_results` | integer | No | Maximum number of results to return |

## AWS CLI

```bash
aws medical-imaging search-image-sets --datastore-id <datastore_id> --search-criteria <study_instance_uid> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.search_image_sets(
    DatastoreId=datastore_id,
    SearchCriteria=study_instance_uid,
    MaxResults=max_results,
)
```
