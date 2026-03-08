---
name: put-user-policy
description: Create or update an inline policy for an IAM user.

    This tool creates a new inline policy or updates an existing one for the specified user.
    Inline policies are directly embedded in a single user, role, or group and have a one-to-one
    relationship with the identity.

    ## Security Best Practices:
    - Follow the principle of least privilege when creating policies
    - Use managed policies for common permissions that can be reused
    - Regularly review and audit inline policies
    - Test policies using simulate_principal_policy before applying

    Args:
        user_name: The name of the IAM user
        policy_name: The name of the inline policy
        policy_document: The policy document in JSON format

    Returns:
        InlinePolicyResponse containing the policy details and operation status
    
---

# Put User Policy

Create or update an inline policy for an IAM user.

    This tool creates a new inline policy or updates an existing one for the specified user.
    Inline policies are directly embedded in a single user, role, or group and have a one-to-one
    relationship with the identity.

    ## Security Best Practices:
    - Follow the principle of least privilege when creating policies
    - Use managed policies for common permissions that can be reused
    - Regularly review and audit inline policies
    - Test policies using simulate_principal_policy before applying

    Args:
        user_name: The name of the IAM user
        policy_name: The name of the inline policy
        policy_document: The policy document in JSON format

    Returns:
        InlinePolicyResponse containing the policy details and operation status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user_name` | string | Yes | The name of the IAM user |
| `policy_name` | string | Yes | The name of the inline policy |
| `policy_document` | string | Yes | The policy document in JSON format (string or dict) |

## AWS CLI

```bash
aws iam put-user-policy --user-name <user_name> --policy-name <policy_name> --policy-document <policy_document>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.put_user_policy(
    UserName=user_name,
    PolicyName=policy_name,
    PolicyDocument=policy_document,
)
```
