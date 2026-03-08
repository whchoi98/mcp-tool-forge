---
name: list-computation-model-resolve-to-resources
description: List computation model resolve to resources in AWS IoT SiteWise.

    Retrieves a paginated list of resources that a computation model resolves to.
    This shows the specific assets or other resources that are associated with
    the computation model through resolve-to relationships.

    Args:
        computation_model_id: The ID of the computation model (required, must be in UUID format)
        region: AWS region (default: us-east-1)
        max_results: Optional maximum number of results to return (1-250)
        next_token: Optional token for pagination to get the next set of results

    Returns:
        Dictionary containing the list of resolve-to resources and pagination info.

    Example:
        # List all resolve-to resources for a computation model
        result = list_computation_model_resolve_to_resources(
            computation_model_id='12345678-1234-1234-1234-123456789012'
        )

        # List resolve-to resources with pagination
        result = list_computation_model_resolve_to_resources(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            max_results=50
        )

        # Get next page of results
        result = list_computation_model_resolve_to_resources(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            next_token=previous_result['nextToken']
        )

        # The response includes:
        # - success: Boolean indicating if the operation succeeded
        # - computationModelResolveToResourceSummaries: List of resources the computation model resolves to
        # - nextToken: Token for pagination (if more results available)
    
---

# List Computation Model Resolve To Resources

List computation model resolve to resources in AWS IoT SiteWise.

    Retrieves a paginated list of resources that a computation model resolves to.
    This shows the specific assets or other resources that are associated with
    the computation model through resolve-to relationships.

    Args:
        computation_model_id: The ID of the computation model (required, must be in UUID format)
        region: AWS region (default: us-east-1)
        max_results: Optional maximum number of results to return (1-250)
        next_token: Optional token for pagination to get the next set of results

    Returns:
        Dictionary containing the list of resolve-to resources and pagination info.

    Example:
        # List all resolve-to resources for a computation model
        result = list_computation_model_resolve_to_resources(
            computation_model_id='12345678-1234-1234-1234-123456789012'
        )

        # List resolve-to resources with pagination
        result = list_computation_model_resolve_to_resources(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            max_results=50
        )

        # Get next page of results
        result = list_computation_model_resolve_to_resources(
            computation_model_id='12345678-1234-1234-1234-123456789012',
            next_token=previous_result['nextToken']
        )

        # The response includes:
        # - success: Boolean indicating if the operation succeeded
        # - computationModelResolveToResourceSummaries: List of resources the computation model resolves to
        # - nextToken: Token for pagination (if more results available)
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `computation_model_id` | string | Yes |  |
| `region` | string | No |  |
| `max_results` | string | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws iotsitewise list-computation-model-resolve-to-resources --computation-model-id <computation_model_id> --region <region> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.list_computation_model_resolve_to_resources(
    ComputationModelId=computation_model_id,
    Region=region,
    MaxResults=max_results,
    NextToken=next_token,
)
```
