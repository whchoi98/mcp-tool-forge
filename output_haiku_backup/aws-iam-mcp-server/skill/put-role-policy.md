---
name: put-role-policy
description: Create or update an inline policy for an IAM role.

    This tool creates a new inline policy or updates an existing one for the specified role.
    Inline policies are directly embedded in a single user, role, or group and have a one-to-one
    relationship with the identity.

    Args:
        role_name: The name of the IAM role
        policy_name: The name of the inline policy
        policy_document: The policy document in JSON format

    Returns:
        InlinePolicyResponse containing the policy details and operation status
    
---

# Put Role Policy

Create or update an inline policy for an IAM role.

    This tool creates a new inline policy or updates an existing one for the specified role.
    Inline policies are directly embedded in a single user, role, or group and have a one-to-one
    relationship with the identity.

    Args:
        role_name: The name of the IAM role
        policy_name: The name of the inline policy
        policy_document: The policy document in JSON format

    Returns:
        InlinePolicyResponse containing the policy details and operation status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `role_name` | string | Yes | The name of the IAM role |
| `policy_name` | string | Yes | The name of the inline policy |
| `policy_document` | string | Yes | The policy document in JSON format (string or dict) |

## AWS CLI

```bash
aws iam put-role-policy --role-name <role_name> --policy-name <policy_name> --policy-document <policy_document>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.put_role_policy(
    RoleName=role_name,
    PolicyName=policy_name,
    PolicyDocument=policy_document,
)
```
