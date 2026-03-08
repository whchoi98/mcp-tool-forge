---
name: list-computation-model-data-binding-usages
description: Find computation models that use a given resource in data binding.

    This API helps you find computation models which are bound to a given resource:
    - Asset model (fetch all computation models where any of this asset model's properties are bound)
    - Asset (fetch all computation models where any of this asset's properties are bound)
    - Asset model property (fetch all computation models where this property is bound)
    - Asset property (fetch all computation models where this property is bound)

    Args:
        data_binding_value_filter: Filter to specify which resource to search for (required)
        region: AWS region (default: us-east-1)
        max_results: Optional maximum number of results to return (1-250)
        next_token: Optional token for pagination to get the next set of results

    Returns:
        Dictionary containing the list of computation models that use the specified resource.

    Filter Examples:
        # Find computation models using any property from a specific asset
        data_binding_value_filter = {
            "asset": {
                "assetId": "12345678-1234-1234-1234-123456789012"
            }
        }

        # Find computation models using any property from a specific asset model
        data_binding_value_filter = {
            "assetModel": {
                "assetModelId": "12345678-1234-1234-1234-123456789012"
            }
        }

        # Find computation models using a specific asset property
        data_binding_value_filter = {
            "assetProperty": {
                "assetId": "12345678-1234-1234-1234-123456789012",
                "propertyId": "87654321-4321-4321-4321-210987654321"
            }
        }

        # Find computation models using a specific asset model property
        data_binding_value_filter = {
            "assetModelProperty": {
                "assetModelId": "12345678-1234-1234-1234-123456789012",
                "propertyId": "87654321-4321-4321-4321-210987654321"
            }
        }

    Usage Examples:
        # Find all computation models using properties from a specific asset
        result = list_computation_model_data_binding_usages(
            data_binding_value_filter={
                "asset": {"assetId": "12345678-1234-1234-1234-123456789012"}
            }
        )

        # Find computation models using a specific asset property with pagination
        result = list_computation_model_data_binding_usages(
            data_binding_value_filter={
                "assetProperty": {
                    "assetId": "12345678-1234-1234-1234-123456789012",
                    "propertyId": "87654321-4321-4321-4321-210987654321"
                }
            },
            max_results=50
        )

    Use Cases:
        - Check if an asset property is already bound to a computation model before binding it elsewhere
        - Find all computation models that depend on a specific asset or asset model
        - Audit which computation models are using properties from a particular asset
        - Identify dependencies before deleting or modifying assets/properties
    
---

# List Computation Model Data Binding Usages

Find computation models that use a given resource in data binding.

    This API helps you find computation models which are bound to a given resource:
    - Asset model (fetch all computation models where any of this asset model's properties are bound)
    - Asset (fetch all computation models where any of this asset's properties are bound)
    - Asset model property (fetch all computation models where this property is bound)
    - Asset property (fetch all computation models where this property is bound)

    Args:
        data_binding_value_filter: Filter to specify which resource to search for (required)
        region: AWS region (default: us-east-1)
        max_results: Optional maximum number of results to return (1-250)
        next_token: Optional token for pagination to get the next set of results

    Returns:
        Dictionary containing the list of computation models that use the specified resource.

    Filter Examples:
        # Find computation models using any property from a specific asset
        data_binding_value_filter = {
            "asset": {
                "assetId": "12345678-1234-1234-1234-123456789012"
            }
        }

        # Find computation models using any property from a specific asset model
        data_binding_value_filter = {
            "assetModel": {
                "assetModelId": "12345678-1234-1234-1234-123456789012"
            }
        }

        # Find computation models using a specific asset property
        data_binding_value_filter = {
            "assetProperty": {
                "assetId": "12345678-1234-1234-1234-123456789012",
                "propertyId": "87654321-4321-4321-4321-210987654321"
            }
        }

        # Find computation models using a specific asset model property
        data_binding_value_filter = {
            "assetModelProperty": {
                "assetModelId": "12345678-1234-1234-1234-123456789012",
                "propertyId": "87654321-4321-4321-4321-210987654321"
            }
        }

    Usage Examples:
        # Find all computation models using properties from a specific asset
        result = list_computation_model_data_binding_usages(
            data_binding_value_filter={
                "asset": {"assetId": "12345678-1234-1234-1234-123456789012"}
            }
        )

        # Find computation models using a specific asset property with pagination
        result = list_computation_model_data_binding_usages(
            data_binding_value_filter={
                "assetProperty": {
                    "assetId": "12345678-1234-1234-1234-123456789012",
                    "propertyId": "87654321-4321-4321-4321-210987654321"
                }
            },
            max_results=50
        )

    Use Cases:
        - Check if an asset property is already bound to a computation model before binding it elsewhere
        - Find all computation models that depend on a specific asset or asset model
        - Audit which computation models are using properties from a particular asset
        - Identify dependencies before deleting or modifying assets/properties
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `data_binding_value_filter` | object | Yes |  |
| `region` | string | No |  |
| `max_results` | string | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws iotsitewise list-computation-model-data-binding-usages --data-binding-value-filter <data_binding_value_filter> --region <region> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.list_computation_model_data_binding_usages(
    DataBindingValueFilter=data_binding_value_filter,
    Region=region,
    MaxResults=max_results,
    NextToken=next_token,
)
```
