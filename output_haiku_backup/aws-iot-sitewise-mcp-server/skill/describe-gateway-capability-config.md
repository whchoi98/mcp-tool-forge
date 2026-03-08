---
name: describe-gateway-capability-config
description: Retrieve information about a gateway capability configuration.

    Args:
        gateway_id: The ID of the gateway that defines the capability             configuration
        capability_namespace: The namespace of the capability configuration
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing capability configuration information
    
---

# Describe Gateway Capability Config

Retrieve information about a gateway capability configuration.

    Args:
        gateway_id: The ID of the gateway that defines the capability             configuration
        capability_namespace: The namespace of the capability configuration
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing capability configuration information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `gateway_id` | string | Yes | The ID of the gateway that defines the capability configuration |
| `capability_namespace` | string | Yes | The namespace of the capability configuration |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws iotsitewise describe-gateway-capability-configuration --gateway-id <gateway_id> --capability-namespace <capability_namespace>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_gateway_capability_configuration(
    GatewayId=gateway_id,
    CapabilityNamespace=capability_namespace,
)
```
