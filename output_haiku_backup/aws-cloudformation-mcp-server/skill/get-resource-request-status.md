---
name: get-resource-request-status
description: Get the status of a long running operation with the request token.

    Args:
        request_token: The request_token returned from the long running operation
        region: AWS region to use (e.g., "us-east-1", "us-west-2")

    Returns:
        Detailed information about the request status structured as
        {
            "status": Status of the operation ("SUCCESS", "PENDING", "FAILED", "NOT_FOUND", etc.)
            "resource_type": The AWS resource type
            "identifier": The resource identifier
            "is_complete": Boolean indicating whether the operation is complete
            "status_message": Human-readable message describing the result
            "request_token": A token that allows you to track long running operations via the get_resource_request_status tool
            "error_code": A code associated with any errors if the request failed
            "retry_after": A duration to wait before retrying the request
        }
    
---

# Get Resource Request Status

Get the status of a long running operation with the request token.

    Args:
        request_token: The request_token returned from the long running operation
        region: AWS region to use (e.g., "us-east-1", "us-west-2")

    Returns:
        Detailed information about the request status structured as
        {
            "status": Status of the operation ("SUCCESS", "PENDING", "FAILED", "NOT_FOUND", etc.)
            "resource_type": The AWS resource type
            "identifier": The resource identifier
            "is_complete": Boolean indicating whether the operation is complete
            "status_message": Human-readable message describing the result
            "request_token": A token that allows you to track long running operations via the get_resource_request_status tool
            "error_code": A code associated with any errors if the request failed
            "retry_after": A duration to wait before retrying the request
        }
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request_token` | string | Yes | The request_token returned from the long running operation |
| `region` | string | No | The AWS region that the operation should be performed in |

## AWS CLI

```bash
aws cloudformation describe-stack-set-operation --operation-id <request_token> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('cloudformation')
response = client.describe_stack_set_operation(
    OperationId=request_token,
    StackSetName=,
    Region=region,
)
```
