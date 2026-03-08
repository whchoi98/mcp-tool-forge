---
name: search-places
description: Search for places using Amazon Location Service geo-places search_text API. Geocode the query using the geocode API to get BiasPosition. If no results, try a bounding box filter. Includes contact info and opening hours if present. Output is standardized and includes all fields, even if empty or not available.
---

# Search Places

Search for places using Amazon Location Service geo-places search_text API. Geocode the query using the geocode API to get BiasPosition. If no results, try a bounding box filter. Includes contact info and opening hours if present. Output is standardized and includes all fields, even if empty or not available.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes | Search query (address, place name, etc.) |
| `max_results` | integer | No | Maximum number of results to return |
| `mode` | string | No | Output mode: 'summary' (default) or 'raw' for all AWS fields |

## AWS CLI

```bash
aws location search-place-index-for-text --index-name <query> --text <query> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('location')
response = client.search_place_index_for_text(
    IndexName=query,
    Text=query,
    MaxResults=max_results,
)
```
