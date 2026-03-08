---
name: update-fhir-resource
description: Update an existing FHIR resource in HealthLake
---

# Update Fhir Resource

Update an existing FHIR resource in HealthLake

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | HealthLake datastore ID |
| `resource_type` | string | Yes | FHIR resource type |
| `resource_id` | string | Yes | FHIR resource ID |
| `resource_data` | object | Yes | Updated FHIR resource data as JSON object |

## AWS CLI

```bash
aws healthlake update-resource --datastore-id <datastore_id> --resource-type <resource_type> --resource-id <resource_id> --resource-json <resource_data>
```

## boto3

```python
import boto3

client = boto3.client('healthlake')
response = client.update_resource(
    DatastoreId=datastore_id,
    ResourceType=resource_type,
    ResourceId=resource_id,
    ResourceJson=resource_data,
)
```
