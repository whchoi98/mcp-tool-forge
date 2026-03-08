---
name: list-roles
description: List IAM roles in the account.

    Args:
        path_prefix: Optional path prefix to filter roles
        max_items: Maximum number of roles to return

    Returns:
        Dictionary containing list of roles and metadata
    
---

# List Roles

List IAM roles in the account.

    Args:
        path_prefix: Optional path prefix to filter roles
        max_items: Maximum number of roles to return

    Returns:
        Dictionary containing list of roles and metadata
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path_prefix` | string | No | Path prefix to filter roles (e.g., "/service-role/") |
| `max_items` | integer | No | Maximum number of roles to return |

## AWS CLI

```bash
aws iam list-roles --path-prefix <path_prefix> --max-items <max_items>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.list_roles(
    PathPrefix=path_prefix,
    MaxItems=max_items,
)
```
