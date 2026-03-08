---
name: list-groups
description: List IAM groups in the account.

    This tool retrieves a list of IAM groups from your AWS account with optional filtering.
    Use this to get an overview of all groups or find specific groups by path prefix.

    ## Usage Tips:
    - Use path_prefix to filter groups by organizational structure
    - Adjust max_items to control response size for large accounts
    - Results may be paginated for accounts with many groups

    Args:
        path_prefix: Optional path prefix to filter groups
        max_items: Maximum number of groups to return

    Returns:
        GroupsListResponse containing list of groups and metadata
    
---

# List Groups

List IAM groups in the account.

    This tool retrieves a list of IAM groups from your AWS account with optional filtering.
    Use this to get an overview of all groups or find specific groups by path prefix.

    ## Usage Tips:
    - Use path_prefix to filter groups by organizational structure
    - Adjust max_items to control response size for large accounts
    - Results may be paginated for accounts with many groups

    Args:
        path_prefix: Optional path prefix to filter groups
        max_items: Maximum number of groups to return

    Returns:
        GroupsListResponse containing list of groups and metadata
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path_prefix` | string | No | Path prefix to filter groups (e.g., "/division_abc/") |
| `max_items` | integer | No | Maximum number of groups to return |

## AWS CLI

```bash
aws iam list-groups --path-prefix <path_prefix> --max-items <max_items>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.list_groups(
    PathPrefix=path_prefix,
    MaxItems=max_items,
)
```
