---
name: geocode
description: Get coordinates for a location name or address using Amazon Location Service geo-places geocode API.
---

# Geocode

Get coordinates for a location name or address using Amazon Location Service geo-places geocode API.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `location` | string | Yes | Location name or address to geocode |

## AWS CLI

```bash
aws location search-place-index-for-text --index-name <location> --text <location>
```

## boto3

```python
import boto3

client = boto3.client('location')
response = client.search_place_index_for_text(
    IndexName=location,
    Text=location,
)
```
