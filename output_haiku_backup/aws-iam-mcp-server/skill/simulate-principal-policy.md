---
name: simulate-principal-policy
description: Simulate IAM policy evaluation for a principal.

    Args:
        policy_source_arn: ARN of the user or role to simulate
        action_names: List of actions to simulate
        resource_arns: Optional list of resource ARNs to test against
        context_entries: Optional context entries for the simulation

    Returns:
        Dictionary containing simulation results
    
---

# Simulate Principal Policy

Simulate IAM policy evaluation for a principal.

    Args:
        policy_source_arn: ARN of the user or role to simulate
        action_names: List of actions to simulate
        resource_arns: Optional list of resource ARNs to test against
        context_entries: Optional context entries for the simulation

    Returns:
        Dictionary containing simulation results
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `policy_source_arn` | string | Yes | ARN of the user or role to simulate |
| `action_names` | array | Yes | List of actions to simulate |
| `resource_arns` | string | No | List of resource ARNs to test against |
| `context_entries` | string | No | Context entries for the simulation |

## AWS CLI

```bash
aws iam simulate-principal-policy --policy-source-arn <policy_source_arn> --action-names <action_names> --resource-arns <resource_arns> --context-entries <context_entries>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.simulate_principal_policy(
    PolicySourceArn=policy_source_arn,
    ActionNames=action_names,
    ResourceArns=resource_arns,
    ContextEntries=context_entries,
)
```
