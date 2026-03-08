---
name: attach-user-policy
description: Attach a managed policy to an IAM user.

    Args:
        user_name: The name of the IAM user
        policy_arn: The ARN of the policy to attach

    Returns:
        Dictionary containing attachment status
    
---

# Attach User Policy

Attach a managed policy to an IAM user.

    Args:
        user_name: The name of the IAM user
        policy_arn: The ARN of the policy to attach

    Returns:
        Dictionary containing attachment status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user_name` | string | Yes | The name of the IAM user |
| `policy_arn` | string | Yes | The ARN of the policy to attach |

## AWS CLI

```bash
aws iam attach-user-policy --user-name <user_name> --policy-arn <policy_arn>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.attach_user_policy(
    UserName=user_name,
    PolicyArn=policy_arn,
)
```
