---
name: describe-computation-model
description: Describe a computation model in AWS IoT SiteWise.

    Retrieves detailed information about a specific computation model, including
    its configuration, data bindings, status, and metadata.

    Args:
        computation_model_id: The ID of the computation model to describe (required, must be in UUID format)
        region: AWS region (default: us-east-1)
        computation_model_version: Optional version of the computation model
                                 (LATEST, ACTIVE, or specific version number)

    Returns:
        Dictionary containing the computation model details.

    Example:
        # Describe the latest version of a computation model
        result = describe_computation_model('12345678-1234-1234-1234-123456789012')

        # Describe a specific version
        result = describe_computation_model(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            computation_model_version='1'
        )

        # Describe the active version
        result = describe_computation_model(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            computation_model_version='ACTIVE'
        )
    
---

# Describe Computation Model

Describe a computation model in AWS IoT SiteWise.

    Retrieves detailed information about a specific computation model, including
    its configuration, data bindings, status, and metadata.

    Args:
        computation_model_id: The ID of the computation model to describe (required, must be in UUID format)
        region: AWS region (default: us-east-1)
        computation_model_version: Optional version of the computation model
                                 (LATEST, ACTIVE, or specific version number)

    Returns:
        Dictionary containing the computation model details.

    Example:
        # Describe the latest version of a computation model
        result = describe_computation_model('12345678-1234-1234-1234-123456789012')

        # Describe a specific version
        result = describe_computation_model(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            computation_model_version='1'
        )

        # Describe the active version
        result = describe_computation_model(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            computation_model_version='ACTIVE'
        )
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `computation_model_id` | string | Yes |  |
| `region` | string | No |  |
| `computation_model_version` | string | No |  |

## AWS CLI

```bash
aws iotsitewise describe-computation-model --computation-model-id <computation_model_id> --computation-model-version <computation_model_version> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_computation_model(
    ComputationModelId=computation_model_id,
    ComputationModelVersion=computation_model_version,
)
```
