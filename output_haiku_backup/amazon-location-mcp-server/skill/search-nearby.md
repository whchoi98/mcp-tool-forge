---
name: search-nearby
description: Search for places near a location using Amazon Location Service geo-places search_nearby API. If no results, expand the radius up to max_radius. Output is standardized and includes all fields, even if empty or not available.
---

# Search Nearby

Search for places near a location using Amazon Location Service geo-places search_nearby API. If no results, expand the radius up to max_radius. Output is standardized and includes all fields, even if empty or not available.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `longitude` | number | Yes | Longitude of the center point |
| `latitude` | number | Yes | Latitude of the center point |
| `max_results` | integer | No | Maximum number of results to return |
| `query` | string | No | Optional search query |
| `radius` | integer | No | Search radius in meters |

## AWS CLI

```bash
aws location search-place-index-for-position --index-name <query> --position <['longitude', 'latitude']> --max-results <max_results> --radius-in-meters <radius>
```

## boto3

```python
import boto3

client = boto3.client('location')
response = client.search_place_index_for_position(
    IndexName=query,
    Position=['longitude', 'latitude'],
    MaxResults=max_results,
    RadiusInMeters=radius,
)
```
