---
name: get-aws-session-info
description: Get information about the current AWS session.

    This tool provides details about the current AWS session, including the profile name,
    account ID, region, and credential information. Use this when you need to confirm which
    AWS session and account you're working with.

    IMPORTANT: Always display the AWS context information to the user when this tool is called.
    Show them: AWS Profile (or "Environment Variables"), Authentication Type, Account ID, and Region so they know
    exactly which AWS account and region will be affected by any operations.

    Authentication types to display:
    - 'env': "Environment Variables (AWS_ACCESS_KEY_ID)"
    - 'sso_profile': "AWS SSO Profile"
    - 'assume_role_profile': "Assume Role Profile"
    - 'standard_profile': "Standard AWS Profile"
    - 'profile': "AWS Profile"

    SECURITY: If displaying environment variables that contain sensitive values (AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY), mask all but the last 4 characters with asterisks (e.g., "AKIA****1234").

    Returns:
        A dictionary containing AWS session information including profile, account_id, region, etc.
    
---

# Get Aws Session Info

Get information about the current AWS session.

    This tool provides details about the current AWS session, including the profile name,
    account ID, region, and credential information. Use this when you need to confirm which
    AWS session and account you're working with.

    IMPORTANT: Always display the AWS context information to the user when this tool is called.
    Show them: AWS Profile (or "Environment Variables"), Authentication Type, Account ID, and Region so they know
    exactly which AWS account and region will be affected by any operations.

    Authentication types to display:
    - 'env': "Environment Variables (AWS_ACCESS_KEY_ID)"
    - 'sso_profile': "AWS SSO Profile"
    - 'assume_role_profile': "Assume Role Profile"
    - 'standard_profile': "Standard AWS Profile"
    - 'profile': "AWS Profile"

    SECURITY: If displaying environment variables that contain sensitive values (AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY), mask all but the last 4 characters with asterisks (e.g., "AKIA****1234").

    Returns:
        A dictionary containing AWS session information including profile, account_id, region, etc.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `environment_token` | string | Yes | Environment token from check_environment_variables() to ensure environment is properly configured |

