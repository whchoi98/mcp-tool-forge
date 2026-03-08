---
name: batch-get-asset-property-aggregates
description: Get aggregated values for multiple asset properties.

    Args:
        entries: The list of asset property aggregate entries for the batch get request
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-4000, default: 100)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing batch get aggregates response
    
---

# Batch Get Asset Property Aggregates

Get aggregated values for multiple asset properties.

    Args:
        entries: The list of asset property aggregate entries for the batch get request
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-4000, default: 100)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing batch get aggregates response
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `entries` | array | Yes | The list of asset property aggregate entries for the batch get request |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-4000) |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise batch-get-asset-property-aggregates --entries <entries> --next-token <next_token> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.batch_get_asset_property_aggregates(
    Entries=entries,
    NextToken=next_token,
    MaxResults=max_results,
)
```
