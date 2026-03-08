---
name: list-datastores
description: List all data stores in the account.
---

# List Datastores

List all data stores in the account.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_status` | string | No | Filter by datastore status (CREATING, ACTIVE, DELETING, DELETED) |
| `max_results` | string | No | Maximum number of results to return (1-100) |
| `next_token` | string | No | Token for pagination |

## AWS CLI

```bash
aws healthimaging list-datastores --datastore-status <datastore_status> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('healthimaging')
response = client.list_datastores(
    DatastoreStatus=datastore_status,
    MaxResults=max_results,
    NextToken=next_token,
)
```
