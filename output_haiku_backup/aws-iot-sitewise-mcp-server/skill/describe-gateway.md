---
name: describe-gateway
description: Retrieve information about a gateway.

    Args:
        gateway_id: The ID of the gateway device
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing gateway information
    
---

# Describe Gateway

Retrieve information about a gateway.

    Args:
        gateway_id: The ID of the gateway device
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing gateway information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `gateway_id` | string | Yes | The ID of the gateway device |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise describe-gateway --gateway-id <gateway_id>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_gateway(
    GatewayId=gateway_id,
)
```
