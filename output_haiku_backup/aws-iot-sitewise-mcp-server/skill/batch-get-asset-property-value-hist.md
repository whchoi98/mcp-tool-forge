---
name: batch-get-asset-property-value-hist
description: Get the historical values for multiple asset properties.

    Args:
        entries: The list of asset property historical value entries for the             batch get request
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-4000, default: 100)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing batch get history response
    
---

# Batch Get Asset Property Value Hist

Get the historical values for multiple asset properties.

    Args:
        entries: The list of asset property historical value entries for the             batch get request
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (1-4000, default: 100)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing batch get history response
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `entries` | array | Yes | The list of asset property historical value entries for the batch get request |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-4000) |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise batch-get-asset-property-value-history --entries <entries> --next-token <next_token> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.batch_get_asset_property_value_history(
    Entries=entries,
    NextToken=next_token,
    MaxResults=max_results,
)
```
