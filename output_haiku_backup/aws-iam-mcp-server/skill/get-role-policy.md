---
name: get-role-policy
description: Retrieve an inline policy for an IAM role.

    This tool retrieves the policy document for a specific inline policy attached to a role.

    Args:
        role_name: The name of the IAM role
        policy_name: The name of the inline policy

    Returns:
        InlinePolicyResponse containing the policy document and details
    
---

# Get Role Policy

Retrieve an inline policy for an IAM role.

    This tool retrieves the policy document for a specific inline policy attached to a role.

    Args:
        role_name: The name of the IAM role
        policy_name: The name of the inline policy

    Returns:
        InlinePolicyResponse containing the policy document and details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `role_name` | string | Yes | The name of the IAM role |
| `policy_name` | string | Yes | The name of the inline policy |

## AWS CLI

```bash
aws iam get-role-policy --role-name <role_name> --policy-name <policy_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.get_role_policy(
    RoleName=role_name,
    PolicyName=policy_name,
)
```
