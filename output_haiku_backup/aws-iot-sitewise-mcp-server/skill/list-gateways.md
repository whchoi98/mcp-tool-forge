---
name: list-gateways
description: Retrieve a paginated list of gateways.

    Args:
        region: AWS region (default: us-east-1)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (
            1-250,
            default: 50)

    Returns:
        Dictionary containing list of gateways
    
---

# List Gateways

Retrieve a paginated list of gateways.

    Args:
        region: AWS region (default: us-east-1)
        next_token: The token to be used for the next set of paginated results
        max_results: The maximum number of results to return (
            1-250,
            default: 50)

    Returns:
        Dictionary containing list of gateways
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | No | AWS region |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-250) |

## AWS CLI

```bash
aws iotsitewise list-gateways --next-token <next_token> --max-results <max_results> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.list_gateways(
    NextToken=next_token,
    MaxResults=max_results,
)
```
