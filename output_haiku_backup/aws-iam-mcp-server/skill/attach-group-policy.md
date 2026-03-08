---
name: attach-group-policy
description: Attach a managed policy to an IAM group.

    Args:
        group_name: The name of the IAM group
        policy_arn: The ARN of the policy to attach

    Returns:
        GroupPolicyAttachmentResponse containing operation status
    
---

# Attach Group Policy

Attach a managed policy to an IAM group.

    Args:
        group_name: The name of the IAM group
        policy_arn: The ARN of the policy to attach

    Returns:
        GroupPolicyAttachmentResponse containing operation status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `group_name` | string | Yes | The name of the IAM group |
| `policy_arn` | string | Yes | The ARN of the policy to attach |

## AWS CLI

```bash
aws iam attach-group-policy --group-name <group_name> --policy-arn <policy_arn>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.attach_group_policy(
    GroupName=group_name,
    PolicyArn=policy_arn,
)
```
