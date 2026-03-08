---
name: delete-user
description: Delete an IAM user.

    Args:
        user_name: The name of the IAM user to delete
        force: If True, removes all attached policies, groups, and access keys first

    Returns:
        Dictionary containing deletion status
    
---

# Delete User

Delete an IAM user.

    Args:
        user_name: The name of the IAM user to delete
        force: If True, removes all attached policies, groups, and access keys first

    Returns:
        Dictionary containing deletion status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user_name` | string | Yes | The name of the IAM user to delete |
| `force` | boolean | No | Force delete user by removing all attached policies, groups, and access keys first |

## AWS CLI

```bash
aws iam delete-user --user-name <user_name> --force <force>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.delete_user(
    UserName=user_name,
    Force=force,
)
```
