---
name: create-user
description: Create a new IAM user.

    This tool creates a new IAM user in your AWS account. The user will be created
    without any permissions by default - you'll need to attach policies separately.

    ## Security Best Practices:
    - Use descriptive user names that indicate the user's role or purpose
    - Set appropriate paths for organizational structure
    - Consider using permissions boundaries to limit maximum permissions
    - Follow the principle of least privilege when assigning permissions later

    Args:
        ctx: MCP context for error reporting
        user_name: The name of the new IAM user
        path: The path for the user (default: '/')
        permissions_boundary: Optional ARN of the permissions boundary policy

    Returns:
        CreateUserResponse containing the created user details
    
---

# Create User

Create a new IAM user.

    This tool creates a new IAM user in your AWS account. The user will be created
    without any permissions by default - you'll need to attach policies separately.

    ## Security Best Practices:
    - Use descriptive user names that indicate the user's role or purpose
    - Set appropriate paths for organizational structure
    - Consider using permissions boundaries to limit maximum permissions
    - Follow the principle of least privilege when assigning permissions later

    Args:
        ctx: MCP context for error reporting
        user_name: The name of the new IAM user
        path: The path for the user (default: '/')
        permissions_boundary: Optional ARN of the permissions boundary policy

    Returns:
        CreateUserResponse containing the created user details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ctx` | string | Yes |  |
| `user_name` | string | Yes | The name of the new IAM user |
| `path` | string | No | The path for the user |
| `permissions_boundary` | string | No | ARN of the permissions boundary policy |

## AWS CLI

```bash
aws iam create-user --user-name <user_name> --path <path> --permissions-boundary <permissions_boundary>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.create_user(
    UserName=user_name,
    Path=path,
    PermissionsBoundary=permissions_boundary,
)
```
