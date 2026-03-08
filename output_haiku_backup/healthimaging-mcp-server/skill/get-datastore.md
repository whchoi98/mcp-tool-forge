---
name: get-datastore
description: Get information about a specific data store.
---

# Get Datastore

Get information about a specific data store.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore to retrieve |

## AWS CLI

```bash
aws healthimaging get-datastore --datastore-id <datastore_id>
```

## boto3

```python
import boto3

client = boto3.client('healthimaging')
response = client.get_datastore(
    DatastoreId=datastore_id,
)
```
