---
name: create-access-key
description: Create a new access key for an IAM user.

    Args:
        user_name: The name of the IAM user

    Returns:
        Dictionary containing the new access key details
    
---

# Create Access Key

Create a new access key for an IAM user.

    Args:
        user_name: The name of the IAM user

    Returns:
        Dictionary containing the new access key details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user_name` | string | Yes | The name of the IAM user |

## AWS CLI

```bash
aws iam create-access-key --user-name <user_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.create_access_key(
    UserName=user_name,
)
```
