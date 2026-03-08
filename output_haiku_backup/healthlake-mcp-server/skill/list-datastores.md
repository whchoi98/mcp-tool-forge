---
name: list-datastores
description: List all HealthLake datastores in the account
---

# List Datastores

List all HealthLake datastores in the account

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `filter` | string | No | Filter datastores by status (CREATING, ACTIVE, DELETING, DELETED) |

## AWS CLI

```bash
aws healthlake list-fhir-datastores --filter <filter>
```

## boto3

```python
import boto3

client = boto3.client('healthlake')
response = client.list_fhir_datastores(
    Filter=filter,
)
```
