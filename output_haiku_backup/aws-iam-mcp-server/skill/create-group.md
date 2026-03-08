---
name: create-group
description: Create a new IAM group.

    This tool creates a new IAM group in your AWS account. The group will be created
    without any permissions by default - you'll need to attach policies separately.

    ## Security Best Practices:
    - Use descriptive group names that indicate the group's purpose
    - Set appropriate paths for organizational structure
    - Follow the principle of least privilege when assigning permissions later

    Args:
        group_name: The name of the new IAM group
        path: The path for the group (default: '/')

    Returns:
        CreateGroupResponse containing the created group details
    
---

# Create Group

Create a new IAM group.

    This tool creates a new IAM group in your AWS account. The group will be created
    without any permissions by default - you'll need to attach policies separately.

    ## Security Best Practices:
    - Use descriptive group names that indicate the group's purpose
    - Set appropriate paths for organizational structure
    - Follow the principle of least privilege when assigning permissions later

    Args:
        group_name: The name of the new IAM group
        path: The path for the group (default: '/')

    Returns:
        CreateGroupResponse containing the created group details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `group_name` | string | Yes | The name of the new IAM group |
| `path` | string | No | The path for the group |

## AWS CLI

```bash
aws iam create-group --group-name <group_name> --path <path>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.create_group(
    GroupName=group_name,
    Path=path,
)
```
