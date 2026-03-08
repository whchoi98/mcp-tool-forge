---
name: get-resource-request-status
description: Get the status of a long running operation with the request token.
---

# Get Resource Request Status

Get the status of a long running operation with the request token.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request_token` | string | Yes | The request_token returned from the long running operation |
| `region` | string | No | The AWS region that the operation should be performed in |

## AWS CLI

```bash
aws cloudcontrol get-resource-request-status --request-token <request_token> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('cloudcontrol')
response = client.get_resource_request_status(
    RequestToken=request_token,
    Region=region,
)
```
