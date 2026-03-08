---
name: reverse-geocode
description: Reverse geocode coordinates to an address using Amazon Location Service geo-places reverse_geocode API.
---

# Reverse Geocode

Reverse geocode coordinates to an address using Amazon Location Service geo-places reverse_geocode API.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `longitude` | number | Yes | Longitude of the location |
| `latitude` | number | Yes | Latitude of the location |

## AWS CLI

```bash
aws location search-place-index-for-position --index-name <default> --position <longitude,latitude>
```

## boto3

```python
import boto3

client = boto3.client('location')
response = client.search_place_index_for_position(
    IndexName=default,
    Position=longitude,latitude,
)
```
