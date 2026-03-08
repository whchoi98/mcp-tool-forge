---
name: delete-fhir-resource
description: Delete a FHIR resource from HealthLake
---

# Delete Fhir Resource

Delete a FHIR resource from HealthLake

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | HealthLake datastore ID |
| `resource_type` | string | Yes | FHIR resource type |
| `resource_id` | string | Yes | FHIR resource ID |

## AWS CLI

```bash
aws healthlake delete-resource --datastore-id <datastore_id> --resource-type <resource_type> --resource-id <resource_id>
```

## boto3

```python
import boto3

client = boto3.client('healthlake')
response = client.delete_resource(
    DatastoreId=datastore_id,
    ResourceType=resource_type,
    ResourceId=resource_id,
)
```
