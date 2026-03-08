---
name: list-executions
description: List executions for a specific target resource in AWS IoT SiteWise.

    Retrieves a paginated list of executions that occurred after performing execute actions
    on the specified target resource. This shows the progress status, error information,
    and execution details for training actions, inference schedules, and other action types.

    Args:
        target_resource_id: The ID of the target resource to list executions for (required, must be in UUID format)
        target_resource_type: The type of resource - ASSET or COMPUTATION_MODEL (required)
        region: AWS region (default: us-east-1)
        action_type: Optional type of action executed to filter results
        max_results: Optional maximum number of results to return (1-250)
        next_token: Optional token for pagination to get the next set of results
        resolve_to_resource_id: Optional ID of the resolved resource
        resolve_to_resource_type: Optional type of the resolved resource (ASSET)

    Returns:
        Dictionary containing the list of executions and pagination info.

    Example:
        # List all executions for a computation model
        result = list_executions(
            target_resource_id='12345678-1234-1234-1234-123456789012',
            target_resource_type='COMPUTATION_MODEL'
        )

        # List executions for an asset with pagination
        result = list_executions(
            target_resource_id='87654321-4321-4321-4321-210987654321',
            target_resource_type='ASSET',
            max_results=50
        )

        # List executions filtered by action type
        result = list_executions(
            target_resource_id='12345678-1234-1234-1234-123456789012',
            target_resource_type='COMPUTATION_MODEL',
            action_type='AWS/ANOMALY_DETECTION_TRAINING'
        )

        # List executions resolved to a specific asset
        result = list_executions(
            target_resource_id='12345678-1234-1234-1234-123456789012',
            target_resource_type='COMPUTATION_MODEL',
            resolve_to_resource_id='11111111-1111-1111-1111-111111111111',
            resolve_to_resource_type='ASSET'
        )

        # Get next page of results
        result = list_executions(
            target_resource_id='12345678-1234-1234-1234-123456789012',
            target_resource_type='COMPUTATION_MODEL',
            next_token=previous_result['nextToken']
        )
    
---

# List Executions

List executions for a specific target resource in AWS IoT SiteWise.

    Retrieves a paginated list of executions that occurred after performing execute actions
    on the specified target resource. This shows the progress status, error information,
    and execution details for training actions, inference schedules, and other action types.

    Args:
        target_resource_id: The ID of the target resource to list executions for (required, must be in UUID format)
        target_resource_type: The type of resource - ASSET or COMPUTATION_MODEL (required)
        region: AWS region (default: us-east-1)
        action_type: Optional type of action executed to filter results
        max_results: Optional maximum number of results to return (1-250)
        next_token: Optional token for pagination to get the next set of results
        resolve_to_resource_id: Optional ID of the resolved resource
        resolve_to_resource_type: Optional type of the resolved resource (ASSET)

    Returns:
        Dictionary containing the list of executions and pagination info.

    Example:
        # List all executions for a computation model
        result = list_executions(
            target_resource_id='12345678-1234-1234-1234-123456789012',
            target_resource_type='COMPUTATION_MODEL'
        )

        # List executions for an asset with pagination
        result = list_executions(
            target_resource_id='87654321-4321-4321-4321-210987654321',
            target_resource_type='ASSET',
            max_results=50
        )

        # List executions filtered by action type
        result = list_executions(
            target_resource_id='12345678-1234-1234-1234-123456789012',
            target_resource_type='COMPUTATION_MODEL',
            action_type='AWS/ANOMALY_DETECTION_TRAINING'
        )

        # List executions resolved to a specific asset
        result = list_executions(
            target_resource_id='12345678-1234-1234-1234-123456789012',
            target_resource_type='COMPUTATION_MODEL',
            resolve_to_resource_id='11111111-1111-1111-1111-111111111111',
            resolve_to_resource_type='ASSET'
        )

        # Get next page of results
        result = list_executions(
            target_resource_id='12345678-1234-1234-1234-123456789012',
            target_resource_type='COMPUTATION_MODEL',
            next_token=previous_result['nextToken']
        )
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `target_resource_id` | string | Yes |  |
| `target_resource_type` | string | Yes |  |
| `region` | string | No |  |
| `action_type` | string | No |  |
| `max_results` | string | No |  |
| `next_token` | string | No |  |
| `resolve_to_resource_id` | string | No |  |
| `resolve_to_resource_type` | string | No |  |

## AWS CLI

```bash
aws iotsitewise list-executions --target-resource-id <target_resource_id> --target-resource-type <target_resource_type> --region <region> --action-type <action_type> --max-results <max_results> --next-token <next_token> --resolve-to-resource-id <resolve_to_resource_id> --resolve-to-resource-type <resolve_to_resource_type>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.list_executions(
    TargetResourceId=target_resource_id,
    TargetResourceType=target_resource_type,
    Region=region,
    ActionType=action_type,
    MaxResults=max_results,
    NextToken=next_token,
    ResolveToResourceId=resolve_to_resource_id,
    ResolveToResourceType=resolve_to_resource_type,
)
```
