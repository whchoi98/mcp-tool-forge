---
name: add-user-to-group
description: Add a user to an IAM group.

    Args:
        group_name: The name of the IAM group
        user_name: The name of the IAM user

    Returns:
        GroupMembershipResponse containing operation status
    
---

# Add User To Group

Add a user to an IAM group.

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
aws iam add-user-to-group --group-name <group_name> --user-name <user_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.add_user_to_group(
    GroupName=group_name,
    UserName=user_name,
)
```
