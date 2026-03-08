---
name: list-policies
description: List IAM policies in the account.

    Args:
        scope: Scope of policies to list ("All", "AWS", or "Local")
        only_attached: Only return policies that are attached
        path_prefix: Optional path prefix to filter policies
        max_items: Maximum number of policies to return

    Returns:
        Dictionary containing list of policies and metadata
    
---

# List Policies

List IAM policies in the account.

    Args:
        scope: Scope of policies to list ("All", "AWS", or "Local")
        only_attached: Only return policies that are attached
        path_prefix: Optional path prefix to filter policies
        max_items: Maximum number of policies to return

    Returns:
        Dictionary containing list of policies and metadata
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `scope` | string | No | Scope of policies to list: "All", "AWS", or "Local" |
| `only_attached` | boolean | No | Only return policies that are attached to a user, group, or role |
| `path_prefix` | string | No | Path prefix to filter policies |
| `max_items` | integer | No | Maximum number of policies to return |

## AWS CLI

```bash
aws iam list-policies --scope <scope> --only-attached <only_attached> --path-prefix <path_prefix> --max-items <max_items>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.list_policies(
    Scope=scope,
    OnlyAttached=only_attached,
    PathPrefix=path_prefix,
    MaxItems=max_items,
)
```
