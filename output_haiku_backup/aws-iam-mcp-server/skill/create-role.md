---
name: create-role
description: Create a new IAM role.

    Args:
        role_name: The name of the new IAM role
        assume_role_policy_document: The trust policy document in JSON format
        path: The path for the role (default: '/')
        description: Optional description of the role
        max_session_duration: Maximum session duration in seconds
        permissions_boundary: Optional ARN of the permissions boundary policy

    Returns:
        Dictionary containing the created role details
    
---

# Create Role

Create a new IAM role.

    Args:
        role_name: The name of the new IAM role
        assume_role_policy_document: The trust policy document in JSON format
        path: The path for the role (default: '/')
        description: Optional description of the role
        max_session_duration: Maximum session duration in seconds
        permissions_boundary: Optional ARN of the permissions boundary policy

    Returns:
        Dictionary containing the created role details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `role_name` | string | Yes | The name of the new IAM role |
| `assume_role_policy_document` | string | Yes | The trust policy document in JSON format (string or dict) |
| `path` | string | No | The path for the role |
| `description` | string | No | Description of the role |
| `max_session_duration` | integer | No | Maximum session duration in seconds (3600-43200) |
| `permissions_boundary` | string | No | ARN of the permissions boundary policy |

## AWS CLI

```bash
aws iam create-role --role-name <role_name> --assume-role-policy-document <assume_role_policy_document> --path <path> --description <description> --max-session-duration <max_session_duration> --permissions-boundary <permissions_boundary>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=assume_role_policy_document,
    Path=path,
    Description=description,
    MaxSessionDuration=max_session_duration,
    PermissionsBoundary=permissions_boundary,
)
```
