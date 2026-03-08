---
name: get-datastore-details
description: Get detailed information about a specific HealthLake datastore
---

# Get Datastore Details

Get detailed information about a specific HealthLake datastore

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | HealthLake datastore ID |

## AWS CLI

```bash
aws healthlake describe-fhir-datastore --datastore-id <datastore_id>
```

## boto3

```python
import boto3

client = boto3.client('healthlake')
response = client.describe_fhir_datastore(
    DatastoreId=datastore_id,
)
```
