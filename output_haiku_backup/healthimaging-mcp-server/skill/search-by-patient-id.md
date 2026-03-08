---
name: search-by-patient-id
description: Search for image sets by patient ID.
---

# Search By Patient Id

Search for image sets by patient ID.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `patient_id` | string | Yes | DICOM Patient ID |
| `max_results` | integer | No | Maximum number of results to return |

## AWS CLI

```bash
aws medical-imaging search-image-sets --datastore-id <datastore_id> --search-criteria <patient_id> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.search_image_sets(
    DatastoreId=datastore_id,
    SearchCriteria=patient_id,
    MaxResults=max_results,
)
```
