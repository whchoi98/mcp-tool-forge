---
name: CreateCodeConnection
description: Create a new CodeConnection.

    This function creates a new AWS CodeConnection for connecting to a
    third-party Git provider. The connection will be created in PENDING
    status and requires OAuth authorization in the AWS Console to become
    AVAILABLE.

    Args:
        ctx: MCP context for error reporting
        connection_name: Name for the new connection
        provider_type: Git provider type (Bitbucket, GitHub, GitHubEnterpriseServer,
            GitLab, GitLabSelfManaged)
        tags: Optional tags to apply to the connection

    Returns:
        Dictionary containing:
        - connection_arn: ARN of the created connection
        - console_url: AWS Console URL for completing OAuth authorization
        - guidance: Instructions for completing the connection setup

    Raises:
        ValueError: If provider_type is invalid
        botocore.exceptions.BotoCoreError: If AWS API call fails
    
---

# Createcodeconnection

Create a new CodeConnection.

    This function creates a new AWS CodeConnection for connecting to a
    third-party Git provider. The connection will be created in PENDING
    status and requires OAuth authorization in the AWS Console to become
    AVAILABLE.

    Args:
        ctx: MCP context for error reporting
        connection_name: Name for the new connection
        provider_type: Git provider type (Bitbucket, GitHub, GitHubEnterpriseServer,
            GitLab, GitLabSelfManaged)
        tags: Optional tags to apply to the connection

    Returns:
        Dictionary containing:
        - connection_arn: ARN of the created connection
        - console_url: AWS Console URL for completing OAuth authorization
        - guidance: Instructions for completing the connection setup

    Raises:
        ValueError: If provider_type is invalid
        botocore.exceptions.BotoCoreError: If AWS API call fails
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_name` | string | Yes | Name for the new connection |
| `provider_type` | string | Yes | Git provider type: Bitbucket, GitHub, GitHubEnterpriseServer, GitLab, GitLabSelfManaged |
| `tags` | string | No | Optional tags to apply to the connection |

## AWS CLI

```bash
aws codestar-connections create-connection --connection-name <connection_name> --provider-type <provider_type> --tags <tags>
```

## boto3

```python
import boto3

client = boto3.client('codestar-connections')
response = client.create_connection(
    ConnectionName=connection_name,
    ProviderType=provider_type,
    Tags=tags,
)
```
