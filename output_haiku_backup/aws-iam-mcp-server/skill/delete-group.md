---
name: delete-group
description: Delete an IAM group.

    Args:
        group_name: The name of the IAM group to delete
        force: If True, removes all members and attached policies first

    Returns:
        Dictionary containing deletion status
    
---

# Delete Group

Delete an IAM group.

    Args:
        group_name: The name of the IAM group to delete
        force: If True, removes all members and attached policies first

    Returns:
        Dictionary containing deletion status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `group_name` | string | Yes | The name of the IAM group to delete |
| `force` | boolean | No | Force delete by removing all members and policies first |

## AWS CLI

```bash
aws iam delete-group --group-name <group_name> --force <force>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.delete_group(
    GroupName=group_name,
    Force=force,
)
```
