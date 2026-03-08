---
name: describe-execution
description: Describe an execution in AWS IoT SiteWise.

    Retrieves detailed information about a specific execution, including execution details,
    status, timestamps, target resource information, and execution results. This provides
    comprehensive information about the execution process.

    Args:
        execution_id: The ID of the execution to describe (required)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing the execution details.

    Example:
        # Describe a specific execution
        result = describe_execution('87654321-4321-4321-4321-210987654321')

        # The response includes:
        # - executionId: The ID of the execution
        # - actionType: The type of action executed
        # - executionStatus: Current status with state information
        # - executionStartTime: When the execution started (Unix timestamp)
        # - executionEndTime: When the execution completed (Unix timestamp, if finished)
        # - executionDetails: Detailed information about the execution (key-value pairs)
        # - executionResult: The result of the execution (key-value pairs)
        # - targetResource: The resource the action was taken on
        # - resolveTo: The detailed resource this execution resolves to (if applicable)
        # - executionEntityVersion: Entity version used for the execution
        # - targetResourceVersion: Version of the target resource
    
---

# Describe Execution

Describe an execution in AWS IoT SiteWise.

    Retrieves detailed information about a specific execution, including execution details,
    status, timestamps, target resource information, and execution results. This provides
    comprehensive information about the execution process.

    Args:
        execution_id: The ID of the execution to describe (required)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing the execution details.

    Example:
        # Describe a specific execution
        result = describe_execution('87654321-4321-4321-4321-210987654321')

        # The response includes:
        # - executionId: The ID of the execution
        # - actionType: The type of action executed
        # - executionStatus: Current status with state information
        # - executionStartTime: When the execution started (Unix timestamp)
        # - executionEndTime: When the execution completed (Unix timestamp, if finished)
        # - executionDetails: Detailed information about the execution (key-value pairs)
        # - executionResult: The result of the execution (key-value pairs)
        # - targetResource: The resource the action was taken on
        # - resolveTo: The detailed resource this execution resolves to (if applicable)
        # - executionEntityVersion: Entity version used for the execution
        # - targetResourceVersion: Version of the target resource
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `execution_id` | string | Yes |  |
| `region` | string | No |  |

## AWS CLI

```bash
aws iotsitewise describe-execution --execution-id <execution_id> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_execution(
    ExecutionId=execution_id,
    Region=region,
)
```
