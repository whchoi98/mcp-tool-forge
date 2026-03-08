---
name: list-users
description: List IAM users in the account.

    This tool retrieves a list of IAM users from your AWS account with optional filtering.
    Use this to get an overview of all users or find specific users by path prefix.

    ## Usage Tips:
    - Use path_prefix to filter users by organizational structure
    - Adjust max_items to control response size for large accounts
    - Results may be paginated for accounts with many users

    Args:
        ctx: MCP context for error reporting
        path_prefix: Optional path prefix to filter users
        max_items: Maximum number of users to return

    Returns:
        UsersListResponse containing list of users and metadata
    
---

# List Users

List IAM users in the account.

    This tool retrieves a list of IAM users from your AWS account with optional filtering.
    Use this to get an overview of all users or find specific users by path prefix.

    ## Usage Tips:
    - Use path_prefix to filter users by organizational structure
    - Adjust max_items to control response size for large accounts
    - Results may be paginated for accounts with many users

    Args:
        ctx: MCP context for error reporting
        path_prefix: Optional path prefix to filter users
        max_items: Maximum number of users to return

    Returns:
        UsersListResponse containing list of users and metadata
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ctx` | string | Yes |  |
| `path_prefix` | string | No | Path prefix to filter users (e.g., "/division_abc/") |
| `max_items` | integer | No | Maximum number of users to return |

## AWS CLI

```bash
aws iam list-users --path-prefix <path_prefix> --max-items <max_items>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.list_users(
    PathPrefix=path_prefix,
    MaxItems=max_items,
)
```
