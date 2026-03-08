---
name: get-endpoint-attributes
description: Execute the AWS Amazon SNS `get_endpoint_attributes` operation.
---

# Get Endpoint Attributes

Execute the AWS Amazon SNS `get_endpoint_attributes` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `EndpointArn` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns get-endpoint-attributes --endpoint-arn <EndpointArn> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.get_endpoint_attributes(
    EndpointArn=EndpointArn,
)
```
