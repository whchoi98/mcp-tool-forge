---
name: GetServerInfo
description: Get information about the Prometheus server configuration.

    ## Usage
    - Use this tool to retrieve the current server configuration
    - Returns details about the Prometheus URL, AWS region, profile, and service name
    - Useful for debugging connection issues
    - If workspace_id is not known, use GetAvailableWorkspaces tool first to find available workspaces and ASK THE USER to choose one
    - Uses DescribeWorkspace API to get the exact workspace URL
    - No manual URL construction is performed

    ## Example
    Input:
      workspace_id: "ws-12345678-abcd-1234-efgh-123456789012"
      region: "us-east-1"

    Output:
      {
        "prometheus_url": "https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-12345678-abcd-1234-efgh-123456789012",
        "aws_region": "us-east-1",
        "aws_profile": "default",
        "service_name": "aps"
      }
    
---

# Getserverinfo

Get information about the Prometheus server configuration.

    ## Usage
    - Use this tool to retrieve the current server configuration
    - Returns details about the Prometheus URL, AWS region, profile, and service name
    - Useful for debugging connection issues
    - If workspace_id is not known, use GetAvailableWorkspaces tool first to find available workspaces and ASK THE USER to choose one
    - Uses DescribeWorkspace API to get the exact workspace URL
    - No manual URL construction is performed

    ## Example
    Input:
      workspace_id: "ws-12345678-abcd-1234-efgh-123456789012"
      region: "us-east-1"

    Output:
      {
        "prometheus_url": "https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-12345678-abcd-1234-efgh-123456789012",
        "aws_region": "us-east-1",
        "aws_profile": "default",
        "service_name": "aps"
      }
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workspace_id` | string | No | The Prometheus workspace ID to use (e.g., ws-12345678-abcd-1234-efgh-123456789012). Optional if a URL is configured via command line arguments. |
| `region` | string | No | AWS region (defaults to current region) |
| `profile` | string | No | AWS profile to use (defaults to None) |

## AWS CLI

```bash
aws amp describe-workspace --workspace-id <workspace_id> --region <region> --profile <profile>
```

## boto3

```python
import boto3

client = boto3.client('amp')
response = client.describe_workspace(
    WorkspaceId=workspace_id,
)
```
