---
name: get-series-primary-image-set
description: Get the primary image set for a given series.
---

# Get Series Primary Image Set

Get the primary image set for a given series.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `series_instance_uid` | string | Yes | DICOM Series Instance UID |

## AWS CLI

```bash
aws healthimaging get-dicom-series-image-set --datastore-id <datastore_id> --series-instance-uid <series_instance_uid>
```

## boto3

```python
import boto3

client = boto3.client('healthimaging')
response = client.get_dicom_series_image_set(
    DatastoreId=datastore_id,
    SeriesInstanceUid=series_instance_uid,
)
```
