---
name: delete-user-policy
description: Delete an inline policy from an IAM user.

    This tool removes an inline policy from the specified user. The policy document
    will be permanently deleted and cannot be recovered.

    Args:
        user_name: The name of the IAM user
        policy_name: The name of the inline policy to delete

    Returns:
        Dictionary containing deletion status
    
---

# Delete User Policy

Delete an inline policy from an IAM user.

    This tool removes an inline policy from the specified user. The policy document
    will be permanently deleted and cannot be recovered.

    Args:
        user_name: The name of the IAM user
        policy_name: The name of the inline policy to delete

    Returns:
        Dictionary containing deletion status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user_name` | string | Yes | The name of the IAM user |
| `policy_name` | string | Yes | The name of the inline policy to delete |

## AWS CLI

```bash
aws iam delete-user-policy --user-name <user_name> --policy-name <policy_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.delete_user_policy(
    UserName=user_name,
    PolicyName=policy_name,
)
```
