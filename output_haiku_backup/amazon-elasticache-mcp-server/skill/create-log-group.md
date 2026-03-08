---
name: create-log-group
description: Create a new CloudWatch Logs log group.

    Args:
        log_group_name: The name of the log group to create
        kms_key_id: The Amazon Resource Name (ARN) of the KMS key to use for encryption
        tags: The key-value pairs to use for the tags
        log_group_class: Specify one of the following classes:
            STANDARD - Standard log events (default)
            INFREQUENT_ACCESS - Infrequent Access log events

    Returns:
        Dict containing success message or error details
    
---

# Create-Log-Group

Create a new CloudWatch Logs log group.

    Args:
        log_group_name: The name of the log group to create
        kms_key_id: The Amazon Resource Name (ARN) of the KMS key to use for encryption
        tags: The key-value pairs to use for the tags
        log_group_class: Specify one of the following classes:
            STANDARD - Standard log events (default)
            INFREQUENT_ACCESS - Infrequent Access log events

    Returns:
        Dict containing success message or error details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `log_group_name` | string | Yes |  |
| `kms_key_id` | string | No |  |
| `tags` | string | No |  |
| `log_group_class` | string | No |  |

## AWS CLI

```bash
aws logs create-log-group --log-group-name <log_group_name> --kms-key-id <kms_key_id> --tags <tags> --log-group-class <log_group_class>
```

## boto3

```python
import boto3

client = boto3.client('logs')
response = client.create_log_group(
    LogGroupName=log_group_name,
    KmsKeyId=kms_key_id,
    Tags=tags,
    LogGroupClass=log_group_class,
)
```
