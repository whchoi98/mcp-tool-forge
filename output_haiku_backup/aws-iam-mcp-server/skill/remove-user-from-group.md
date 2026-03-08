---
name: remove-user-from-group
description: Remove a user from an IAM group.

    Args:
        group_name: The name of the IAM group
        user_name: The name of the IAM user

    Returns:
        GroupMembershipResponse containing operation status
    
---

# Remove User From Group

Remove a user from an IAM group.

    Args:
        group_name: The name of the IAM group
        user_name: The name of the IAM user

    Returns:
        GroupMembershipResponse containing operation status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `group_name` | string | Yes | The name of the IAM group |
| `user_name` | string | Yes | The name of the IAM user |

## AWS CLI

```bash
aws iam remove-user-from-group --group-name <group_name> --user-name <user_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.remove_user_from_group(
    GroupName=group_name,
    UserName=user_name,
)
```
