---
name: describe-action
description: Describe an action in AWS IoT SiteWise.

    Retrieves detailed information about a specific action, including
    its definition, payload, target resource, execution time, and resolution details.

    Args:
        action_id: The ID of the action to describe (required)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing the action details.

    Example:
        # Describe a specific action
        result = describe_action('12345678-1234-1234-1234-123456789012')

        # The response includes:
        # - actionId: The ID of the action
        # - actionDefinitionId: The ID of the action definition
        # - actionPayload: The JSON payload of the action
        # - targetResource: The resource the action was taken on
        # - resolveTo: The detailed resource this action resolves to (if applicable)
        # - executionTime: The time the action was executed
    
---

# Describe Action

Describe an action in AWS IoT SiteWise.

    Retrieves detailed information about a specific action, including
    its definition, payload, target resource, execution time, and resolution details.

    Args:
        action_id: The ID of the action to describe (required)
        region: AWS region (default: us-east-1)

    Returns:
        Dictionary containing the action details.

    Example:
        # Describe a specific action
        result = describe_action('12345678-1234-1234-1234-123456789012')

        # The response includes:
        # - actionId: The ID of the action
        # - actionDefinitionId: The ID of the action definition
        # - actionPayload: The JSON payload of the action
        # - targetResource: The resource the action was taken on
        # - resolveTo: The detailed resource this action resolves to (if applicable)
        # - executionTime: The time the action was executed
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `action_id` | string | Yes |  |
| `region` | string | No |  |

## AWS CLI

```bash
aws iotsitewise describe-action --action-id <action_id> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.describe_action(
    ActionId=action_id,
    Region=region,
)
```
