---
name: delete-datastore
description: Delete a data store from AWS HealthImaging.
---

# Delete Datastore

Delete a data store from AWS HealthImaging.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore to delete |

## AWS CLI

```bash
aws medical-imaging delete-datastore --datastore-id <datastore_id>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.delete_datastore(
    DatastoreId=datastore_id,
)
```
