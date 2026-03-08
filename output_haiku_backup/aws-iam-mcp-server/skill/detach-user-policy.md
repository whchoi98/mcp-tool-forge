---
name: detach-user-policy
description: Detach a managed policy from an IAM user.

    Args:
        user_name: The name of the IAM user
        policy_arn: The ARN of the policy to detach

    Returns:
        Dictionary containing detachment status
    
---

# Detach User Policy

Detach a managed policy from an IAM user.

    Args:
        user_name: The name of the IAM user
        policy_arn: The ARN of the policy to detach

    Returns:
        Dictionary containing detachment status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user_name` | string | Yes | The name of the IAM user |
| `policy_arn` | string | Yes | The ARN of the policy to detach |

## AWS CLI

```bash
aws iam detach-user-policy --user-name <user_name> --policy-arn <policy_arn>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.detach_user_policy(
    UserName=user_name,
    PolicyArn=policy_arn,
)
```
