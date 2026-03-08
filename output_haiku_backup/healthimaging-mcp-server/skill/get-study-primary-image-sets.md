---
name: get-study-primary-image-sets
description: Get primary image sets for a specific study.
---

# Get Study Primary Image Sets

Get primary image sets for a specific study.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `study_instance_uid` | string | Yes | DICOM Study Instance UID |

## AWS CLI

```bash
aws medical-imaging search-image-sets --datastore-id <datastore_id> --search-criteria <study_instance_uid>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.search_image_sets(
    DatastoreId=datastore_id,
    SearchCriteria={'StudyInstanceUid': 'study_instance_uid'},
)
```
