---
name: get-user
description: Get detailed information about a specific IAM user.

    This tool retrieves comprehensive information about an IAM user including
    attached policies, group memberships, and access keys. Use this to get
    a complete picture of a user's permissions and configuration.

    ## Usage Tips:
    - Use this after list_users to get detailed information about specific users
    - Review attached policies to understand user permissions
    - Check access keys to identify potential security issues

    Args:
        ctx: MCP context for error reporting
        user_name: The name of the IAM user

    Returns:
        UserDetailsResponse containing comprehensive user information
    
---

# Get User

Get detailed information about a specific IAM user.

    This tool retrieves comprehensive information about an IAM user including
    attached policies, group memberships, and access keys. Use this to get
    a complete picture of a user's permissions and configuration.

    ## Usage Tips:
    - Use this after list_users to get detailed information about specific users
    - Review attached policies to understand user permissions
    - Check access keys to identify potential security issues

    Args:
        ctx: MCP context for error reporting
        user_name: The name of the IAM user

    Returns:
        UserDetailsResponse containing comprehensive user information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ctx` | string | Yes |  |
| `user_name` | string | Yes | The name of the IAM user to retrieve |

## AWS CLI

```bash
aws iam get-user --user-name <user_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.get_user(
    UserName=user_name,
)
```
