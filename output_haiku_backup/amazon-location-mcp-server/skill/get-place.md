---
name: get-place
description: Get details for a place using Amazon Location Service geo-places get_place API. Output is standardized and includes all fields, even if empty or not available.
---

# Get Place

Get details for a place using Amazon Location Service geo-places get_place API. Output is standardized and includes all fields, even if empty or not available.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `place_id` | string | Yes | The unique PlaceId for the place |
| `mode` | string | No | Output mode: 'summary' (default) or 'raw' for all AWS fields |

## AWS CLI

```bash
aws location get-place --place-id <place_id> --index-name <mode>
```

## boto3

```python
import boto3

client = boto3.client('location')
response = client.get_place(
    PlaceId=place_id,
    IndexName=mode,
)
```
