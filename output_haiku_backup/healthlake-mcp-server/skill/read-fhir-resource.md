---
name: read-fhir-resource
description: Get a specific FHIR resource by ID
---

# Read Fhir Resource

Get a specific FHIR resource by ID

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | HealthLake datastore ID |
| `resource_type` | string | Yes | FHIR resource type |
| `resource_id` | string | Yes | FHIR resource ID |

## AWS CLI

```bash
aws healthlake read-resource --datastore-id <datastore_id> --resource-type <resource_type> --resource-id <resource_id>
```

## boto3

```python
import boto3

client = boto3.client('healthlake')
response = client.read_resource(
    DatastoreId=datastore_id,
    ResourceType=resource_type,
    ResourceId=resource_id,
)
```
