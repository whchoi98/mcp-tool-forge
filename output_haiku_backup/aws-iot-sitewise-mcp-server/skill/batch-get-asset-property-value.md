---
name: batch-get-asset-property-value
description: Get the current values for multiple asset properties.

    Args:
        entries: The list of asset property identifiers for the batch get request
        next_token: The token to be used for the next set of paginated results
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing batch get response
    
---

# Batch Get Asset Property Value

Get the current values for multiple asset properties.

    Args:
        entries: The list of asset property identifiers for the batch get request
        next_token: The token to be used for the next set of paginated results
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing batch get response
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `entries` | array | Yes | The list of asset property identifiers for the batch get request |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise batch-get-asset-property-value --entries <entries> --next-token <next_token> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.batch_get_asset_property_value(
    Entries=entries,
    NextToken=next_token,
)
```
