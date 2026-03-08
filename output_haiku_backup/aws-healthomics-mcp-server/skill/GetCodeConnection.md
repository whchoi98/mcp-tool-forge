---
name: GetCodeConnection
description: Get details about a specific CodeConnection.

    This function retrieves detailed information about a specific AWS
    CodeConnection, including its current status and guidance on next steps.
    Use this to check if a connection is ready for use with HealthOmics
    workflows or if OAuth authorization is still required.

    Args:
        ctx: MCP context for error reporting
        connection_arn: ARN of the connection to retrieve

    Returns:
        Dictionary containing:
        - connection_arn: ARN of the connection
        - connection_name: Name of the connection
        - connection_status: Status (PENDING, AVAILABLE, ERROR)
        - provider_type: Git provider type
        - owner_account_id: AWS account that owns the connection
        - host_arn: ARN of the host (for self-managed providers, if present)
        - guidance: Status-based guidance message for the user

    Raises:
        ValueError: If connection_arn format is invalid
        botocore.exceptions.ClientError: If connection is not found or AWS API call fails
        botocore.exceptions.BotoCoreError: If AWS API call fails
    
---

# Getcodeconnection

Get details about a specific CodeConnection.

    This function retrieves detailed information about a specific AWS
    CodeConnection, including its current status and guidance on next steps.
    Use this to check if a connection is ready for use with HealthOmics
    workflows or if OAuth authorization is still required.

    Args:
        ctx: MCP context for error reporting
        connection_arn: ARN of the connection to retrieve

    Returns:
        Dictionary containing:
        - connection_arn: ARN of the connection
        - connection_name: Name of the connection
        - connection_status: Status (PENDING, AVAILABLE, ERROR)
        - provider_type: Git provider type
        - owner_account_id: AWS account that owns the connection
        - host_arn: ARN of the host (for self-managed providers, if present)
        - guidance: Status-based guidance message for the user

    Raises:
        ValueError: If connection_arn format is invalid
        botocore.exceptions.ClientError: If connection is not found or AWS API call fails
        botocore.exceptions.BotoCoreError: If AWS API call fails
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_arn` | string | Yes | ARN of the connection to retrieve |

## AWS CLI

```bash
aws healthomics get-connection --connection-arn <connection_arn>
```

## boto3

```python
import boto3

client = boto3.client('healthomics')
response = client.get_connection(
    ConnectionArn=connection_arn,
)
```
