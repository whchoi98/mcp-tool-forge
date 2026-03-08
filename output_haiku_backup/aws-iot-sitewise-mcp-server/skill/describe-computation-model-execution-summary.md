---
name: describe-computation-model-execution-summary
description: Describe a computation model execution summary in AWS IoT SiteWise.

    This tool intelligently determines whether to use resolve parameters based on the
    computation model configuration:
    - For Asset Model Level Configuration: Uses resolve parameters if provided to get execution summary for specific assets
    - For Asset Level Configuration: Ignores resolve parameters as they're not needed (already tied to specific assets)

    **Smart Optimization**: If you know the configuration type, provide it via the `configuration_type`
    parameter to avoid an additional API call to describe_computation_model for type detection.

    Args:
        computation_model_id: The ID of the computation model (required, must be in UUID format)
        region: AWS region (default: us-east-1)
        resolve_to_resource_id: Optional ID of the resolved resource (only used for asset model level configurations)
        resolve_to_resource_type: Optional type of the resolved resource (ASSET, only used for asset model level configurations)
        configuration_type: Optional configuration type hint to avoid auto-detection API call.
                          Use 'asset_model_level' or 'asset model level configuration' for Asset Model Level,
                          or 'asset_level' or 'asset level configuration' for Asset Level.
                          If not provided, the function will auto-detect by calling describe_computation_model.

    Returns:
        Dictionary containing the computation model execution summary and configuration type information.

    Example:
        # Auto-detect configuration type (makes additional API call)
        result = describe_computation_model_execution_summary(
            '12345678-1234-1234-1234-123456789012'
        )

        # Optimized: Provide known configuration type to skip auto-detection
        result = describe_computation_model_execution_summary(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            configuration_type='asset_model_level'
        )

        # Asset model level configuration resolved to a specific asset
        result = describe_computation_model_execution_summary(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            resolve_to_resource_id='87654321-4321-4321-4321-210987654321',
            resolve_to_resource_type='ASSET',
            configuration_type='asset_model_level'  # Skip auto-detection for better performance
        )

        # Asset level configuration (resolve parameters will be ignored)
        result = describe_computation_model_execution_summary(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            configuration_type='asset_level'  # Skip auto-detection for better performance
        )

    Performance Tips:
        - Use configuration_type parameter when you know the computation model type to avoid extra API calls
        - For Asset Model Level configurations, consider providing resolve parameters for specific asset context
        - For Asset Level configurations, resolve parameters are automatically ignored (already tied to specific assets)
    
---

# Describe Computation Model Execution Summary

Describe a computation model execution summary in AWS IoT SiteWise.

    This tool intelligently determines whether to use resolve parameters based on the
    computation model configuration:
    - For Asset Model Level Configuration: Uses resolve parameters if provided to get execution summary for specific assets
    - For Asset Level Configuration: Ignores resolve parameters as they're not needed (already tied to specific assets)

    **Smart Optimization**: If you know the configuration type, provide it via the `configuration_type`
    parameter to avoid an additional API call to describe_computation_model for type detection.

    Args:
        computation_model_id: The ID of the computation model (required, must be in UUID format)
        region: AWS region (default: us-east-1)
        resolve_to_resource_id: Optional ID of the resolved resource (only used for asset model level configurations)
        resolve_to_resource_type: Optional type of the resolved resource (ASSET, only used for asset model level configurations)
        configuration_type: Optional configuration type hint to avoid auto-detection API call.
                          Use 'asset_model_level' or 'asset model level configuration' for Asset Model Level,
                          or 'asset_level' or 'asset level configuration' for Asset Level.
                          If not provided, the function will auto-detect by calling describe_computation_model.

    Returns:
        Dictionary containing the computation model execution summary and configuration type information.

    Example:
        # Auto-detect configuration type (makes additional API call)
        result = describe_computation_model_execution_summary(
            '12345678-1234-1234-1234-123456789012'
        )

        # Optimized: Provide known configuration type to skip auto-detection
        result = describe_computation_model_execution_summary(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            configuration_type='asset_model_level'
        )

        # Asset model level configuration resolved to a specific asset
        result = describe_computation_model_execution_summary(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            resolve_to_resource_id='87654321-4321-4321-4321-210987654321',
            resolve_to_resource_type='ASSET',
            configuration_type='asset_model_level'  # Skip auto-detection for better performance
        )

        # Asset level configuration (resolve parameters will be ignored)
        result = describe_computation_model_execution_summary(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            configuration_type='asset_level'  # Skip auto-detection for better performance
        )

    Performance Tips:
        - Use configuration_type parameter when you know the computation model type to avoid extra API calls
        - For Asset Model Level configurations, consider providing resolve parameters for specific asset context
        - For Asset Level configurations, resolve parameters are automatically ignored (already tied to specific assets)
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `computation_model_id` | string | Yes |  |
| `region` | string | No |  |
| `resolve_to_resource_id` | string | No |  |
| `resolve_to_resource_type` | string | No |  |
| `configuration_type` | string | No |  |

## AWS CLI

```bash
aws iotsitewise describe-computation-model-execution-summary --computation-model-id <computation_model_id> --region <region> --resolve-to-resource-id <resolve_to_resource_id> --resolve-to-resource-type <resolve_to_resource_type> --configuration-type <configuration_type>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_computation_model_execution_summary(
    ComputationModelId=computation_model_id,
    Region=region,
    ResolveToResourceId=resolve_to_resource_id,
    ResolveToResourceType=resolve_to_resource_type,
    ConfigurationType=configuration_type,
)
```
