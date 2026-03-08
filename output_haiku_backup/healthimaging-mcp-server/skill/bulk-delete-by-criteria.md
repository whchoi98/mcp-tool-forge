---
name: bulk-delete-by-criteria
description: Delete multiple image sets matching specified criteria.
---

# Bulk Delete By Criteria

Delete multiple image sets matching specified criteria.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `criteria` | object | Yes | Search criteria for image sets to delete (e.g., {'DICOMPatientId': 'patient123'}) |
| `max_deletions` | integer | No | Maximum number of image sets to delete (safety limit) |

## AWS CLI

```bash
aws medical-imaging search-image-sets --datastore-id <datastore_id> --search-criteria <criteria> --max-results <max_deletions>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.search_image_sets(
    DatastoreId=datastore_id,
    SearchCriteria=criteria,
    MaxResults=max_deletions,
)
```
