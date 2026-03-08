---
name: get-aws-account-info
description: Get information about the current AWS account being used.

    Common questions this tool answers:
    - "What AWS account am I using?"
    - "Which AWS region am I in?"
    - "What AWS profile is being used?"
    - "Show me my current AWS session information"

    Returns:
        A dictionary containing AWS account information:
        {
            "profile": The AWS profile name being used,
            "account_id": The AWS account ID,
            "region": The AWS region being used,
            "readonly_mode": True if the server is in read-only mode,
            "readonly_message": A message about read-only mode limitations if enabled,
            "using_env_vars": Boolean indicating if using environment variables for credentials
        }
    
---

# Get Aws Account Info

Get information about the current AWS account being used.

    Common questions this tool answers:
    - "What AWS account am I using?"
    - "Which AWS region am I in?"
    - "What AWS profile is being used?"
    - "Show me my current AWS session information"

    Returns:
        A dictionary containing AWS account information:
        {
            "profile": The AWS profile name being used,
            "account_id": The AWS account ID,
            "region": The AWS region being used,
            "readonly_mode": True if the server is in read-only mode,
            "readonly_message": A message about read-only mode limitations if enabled,
            "using_env_vars": Boolean indicating if using environment variables for credentials
        }
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|

## AWS CLI

```bash
aws sts get-caller-identity
```

## boto3

```python
import boto3

client = boto3.client('sts')
response = client.get_caller_identity(
)
```
