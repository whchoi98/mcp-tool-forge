---
name: get-user-policy
description: Retrieve an inline policy for an IAM user.

    This tool retrieves the policy document for a specific inline policy attached to a user.

    Args:
        user_name: The name of the IAM user
        policy_name: The name of the inline policy

    Returns:
        InlinePolicyResponse containing the policy document and details
    
---

# Get User Policy

Retrieve an inline policy for an IAM user.

    This tool retrieves the policy document for a specific inline policy attached to a user.

    Args:
        user_name: The name of the IAM user
        policy_name: The name of the inline policy

    Returns:
        InlinePolicyResponse containing the policy document and details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user_name` | string | Yes | The name of the IAM user |
| `policy_name` | string | Yes | The name of the inline policy |

## AWS CLI

```bash
aws iam get-user-policy --user-name <user_name> --policy-name <policy_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.get_user_policy(
    UserName=user_name,
    PolicyName=policy_name,
)
```
