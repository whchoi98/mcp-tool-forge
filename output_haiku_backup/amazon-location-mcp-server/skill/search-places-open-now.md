---
name: search-places-open-now
description: Search for places that are open now using Amazon Location Service geo-places search_text API and filter by opening hours. If no open places, expand the search radius up to max_radius. Uses BiasPosition from geocode.
---

# Search Places Open Now

Search for places that are open now using Amazon Location Service geo-places search_text API and filter by opening hours. If no open places, expand the search radius up to max_radius. Uses BiasPosition from geocode.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes | Search query (address, place name, etc.) |
| `initial_radius` | integer | No | Initial search radius in meters for expansion |

## AWS CLI

```bash
aws location search-place-index-for-text --index-name <query> --text <query> --bias-position <bias_position> --max-results <max_results> --filter-bbox <filter_bbox>
```

## boto3

```python
import boto3

client = boto3.client('location')
response = client.search_place_index_for_text(
    IndexName=query,
    Text=query,
    BiasPosition=bias_position,
    MaxResults=max_results,
    FilterBBox=filter_bbox,
)
```
