---
name: detach-group-policy
description: Detach a managed policy from an IAM group.

    Args:
        group_name: The name of the IAM group
        policy_arn: The ARN of the policy to detach

    Returns:
        GroupPolicyAttachmentResponse containing operation status
    
---

# Detach Group Policy

Detach a managed policy from an IAM group.

    Args:
        group_name: The name of the IAM group
        policy_arn: The ARN of the policy to detach

    Returns:
        GroupPolicyAttachmentResponse containing operation status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `group_name` | string | Yes | The name of the IAM group |
| `policy_arn` | string | Yes | The ARN of the policy to detach |

## AWS CLI

```bash
aws iam detach-group-policy --group-name <group_name> --policy-arn <policy_arn>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.detach_group_policy(
    GroupName=group_name,
    PolicyArn=policy_arn,
)
```
