---
name: list-role-policies
description: List all inline policies for an IAM role.

    This tool retrieves the names of all inline policies attached to the specified role.

    Args:
        role_name: The name of the IAM role

    Returns:
        InlinePolicyListResponse containing the list of policy names
    
---

# List Role Policies

List all inline policies for an IAM role.

    This tool retrieves the names of all inline policies attached to the specified role.

    Args:
        role_name: The name of the IAM role

    Returns:
        InlinePolicyListResponse containing the list of policy names
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `role_name` | string | Yes | The name of the IAM role |

## AWS CLI

```bash
aws iam list-role-policies --role-name <role_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.list_role_policies(
    RoleName=role_name,
)
```
