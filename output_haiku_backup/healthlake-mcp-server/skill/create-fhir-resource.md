---
name: create-fhir-resource
description: Create a new FHIR resource in HealthLake
---

# Create Fhir Resource

Create a new FHIR resource in HealthLake

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | HealthLake datastore ID |
| `resource_type` | string | Yes | FHIR resource type |
| `resource_data` | object | Yes | FHIR resource data as JSON object |

## AWS CLI

```bash
aws healthlake create-resource --datastore-id <datastore_id> --resource-type <resource_type> --resource-data <resource_data>
```

## boto3

```python
import boto3

client = boto3.client('healthlake')
response = client.create_resource(
    DatastoreId=datastore_id,
    ResourceType=resource_type,
    ResourceData=resource_data,
)
```
