---
name: delete-access-key
description: Delete an access key for an IAM user.

    Args:
        user_name: The name of the IAM user
        access_key_id: The access key ID to delete

    Returns:
        Dictionary containing deletion status
    
---

# Delete Access Key

Delete an access key for an IAM user.

    Args:
        user_name: The name of the IAM user
        access_key_id: The access key ID to delete

    Returns:
        Dictionary containing deletion status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user_name` | string | Yes | The name of the IAM user |
| `access_key_id` | string | Yes | The access key ID to delete |

## AWS CLI

```bash
aws iam delete-access-key --user-name <user_name> --access-key-id <access_key_id>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.delete_access_key(
    UserName=user_name,
    AccessKeyId=access_key_id,
)
```
