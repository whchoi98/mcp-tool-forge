---
name: delete-role-policy
description: Delete an inline policy from an IAM role.

    This tool removes an inline policy from the specified role. The policy document
    will be permanently deleted and cannot be recovered.

    Args:
        role_name: The name of the IAM role
        policy_name: The name of the inline policy to delete

    Returns:
        Dictionary containing deletion status
    
---

# Delete Role Policy

Delete an inline policy from an IAM role.

    This tool removes an inline policy from the specified role. The policy document
    will be permanently deleted and cannot be recovered.

    Args:
        role_name: The name of the IAM role
        policy_name: The name of the inline policy to delete

    Returns:
        Dictionary containing deletion status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `role_name` | string | Yes | The name of the IAM role |
| `policy_name` | string | Yes | The name of the inline policy to delete |

## AWS CLI

```bash
aws iam delete-role-policy --role-name <role_name> --policy-name <policy_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.delete_role_policy(
    RoleName=role_name,
    PolicyName=policy_name,
)
```
