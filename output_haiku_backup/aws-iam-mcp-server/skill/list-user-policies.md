---
name: list-user-policies
description: List all inline policies for an IAM user.

    This tool retrieves the names of all inline policies attached to the specified user.

    Args:
        user_name: The name of the IAM user

    Returns:
        InlinePolicyListResponse containing the list of policy names
    
---

# List User Policies

List all inline policies for an IAM user.

    This tool retrieves the names of all inline policies attached to the specified user.

    Args:
        user_name: The name of the IAM user

    Returns:
        InlinePolicyListResponse containing the list of policy names
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user_name` | string | Yes | The name of the IAM user |

## AWS CLI

```bash
aws iam list-user-policies --user-name <user_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.list_user_policies(
    UserName=user_name,
)
```
