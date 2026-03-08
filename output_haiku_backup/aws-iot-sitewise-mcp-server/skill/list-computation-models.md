---
name: list-computation-models
description: List computation models in AWS IoT SiteWise.

    Retrieves a paginated list of computation models in your AWS account.
    You can filter by computation model type and control pagination.

    Args:
        region: AWS region (default: us-east-1)
        computation_model_type: Optional filter by computation model type (e.g., 'ANOMALY_DETECTION')
        max_results: Optional maximum number of results to return (1-250, default: AWS default)
        next_token: Optional token for pagination to get the next set of results

    Returns:
        Dictionary containing the list of computation models and pagination info.

    Example:
        # List all computation models
        result = list_computation_models()

        # List only anomaly detection models with pagination
        result = list_computation_models(
            computation_model_type='ANOMALY_DETECTION',
            max_results=50
        )

        # Get next page of results
        result = list_computation_models(next_token=previous_result['nextToken'])
    
---

# List Computation Models

List computation models in AWS IoT SiteWise.

    Retrieves a paginated list of computation models in your AWS account.
    You can filter by computation model type and control pagination.

    Args:
        region: AWS region (default: us-east-1)
        computation_model_type: Optional filter by computation model type (e.g., 'ANOMALY_DETECTION')
        max_results: Optional maximum number of results to return (1-250, default: AWS default)
        next_token: Optional token for pagination to get the next set of results

    Returns:
        Dictionary containing the list of computation models and pagination info.

    Example:
        # List all computation models
        result = list_computation_models()

        # List only anomaly detection models with pagination
        result = list_computation_models(
            computation_model_type='ANOMALY_DETECTION',
            max_results=50
        )

        # Get next page of results
        result = list_computation_models(next_token=previous_result['nextToken'])
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | No |  |
| `computation_model_type` | string | No |  |
| `max_results` | string | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws iotsitewise list-computation-models --region <region> --computation-model-type <computation_model_type> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.list_computation_models(
    Region=region,
    ComputationModelType=computation_model_type,
    MaxResults=max_results,
    NextToken=next_token,
)
```
