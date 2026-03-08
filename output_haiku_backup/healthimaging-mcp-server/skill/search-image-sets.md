---
name: search-image-sets
description: Search for image sets in a data store.
---

# Search Image Sets

Search for image sets in a data store.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `search_criteria` | string | No | Search criteria |
| `next_token` | string | No | Token for pagination |
| `max_results` | string | No | Maximum number of results to return (1-50) |

## AWS CLI

```bash
aws medical-imaging search-image-sets --datastore-id <datastore_id> --search-criteria <search_criteria> --next-token <next_token> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.search_image_sets(
    DatastoreId=datastore_id,
    SearchCriteria=search_criteria,
    NextToken=next_token,
    MaxResults=max_results,
)
```
