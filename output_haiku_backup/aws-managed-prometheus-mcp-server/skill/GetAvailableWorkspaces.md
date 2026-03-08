---
name: GetAvailableWorkspaces
description: List all available Prometheus workspaces in the specified region.

    ## Usage
    - Use this tool to see all available Prometheus workspaces
    - Shows workspace ID, alias, status, and URL for active workspaces
    - IMPORTANT: When multiple workspaces are available, present them to the user and ask them to choose one
    - DO NOT automatically select a workspace; always ask the user to choose when multiple options exist
    - Uses DescribeWorkspace API to get the exact URL for each workspace
    - No manual URL construction is performed

    ## Example
    Input:
      region: "us-east-1"

    Output:
      {
        "workspaces": [
          {
            "workspace_id": "ws-12345678-abcd-1234-efgh-123456789012",
            "alias": "production",
            "status": "ACTIVE",
            "prometheus_url": "https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-12345678-abcd-1234-efgh-123456789012",
            "is_configured": true
          },
          {
            "workspace_id": "ws-87654321-dcba-4321-hgfe-210987654321",
            "alias": "development",
            "status": "ACTIVE",
            "prometheus_url": "https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-87654321-dcba-4321-hgfe-210987654321",
            "is_configured": false
          }
        ],
        "count": 2,
        "region": "us-east-1",
        "requires_user_selection": true,
        "configured_workspace_id": "ws-12345678-abcd-1234-efgh-123456789012"
      }
    
---

# Getavailableworkspaces

List all available Prometheus workspaces in the specified region.

    ## Usage
    - Use this tool to see all available Prometheus workspaces
    - Shows workspace ID, alias, status, and URL for active workspaces
    - IMPORTANT: When multiple workspaces are available, present them to the user and ask them to choose one
    - DO NOT automatically select a workspace; always ask the user to choose when multiple options exist
    - Uses DescribeWorkspace API to get the exact URL for each workspace
    - No manual URL construction is performed

    ## Example
    Input:
      region: "us-east-1"

    Output:
      {
        "workspaces": [
          {
            "workspace_id": "ws-12345678-abcd-1234-efgh-123456789012",
            "alias": "production",
            "status": "ACTIVE",
            "prometheus_url": "https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-12345678-abcd-1234-efgh-123456789012",
            "is_configured": true
          },
          {
            "workspace_id": "ws-87654321-dcba-4321-hgfe-210987654321",
            "alias": "development",
            "status": "ACTIVE",
            "prometheus_url": "https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-87654321-dcba-4321-hgfe-210987654321",
            "is_configured": false
          }
        ],
        "count": 2,
        "region": "us-east-1",
        "requires_user_selection": true,
        "configured_workspace_id": "ws-12345678-abcd-1234-efgh-123456789012"
      }
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | No | AWS region (defaults to current region) |
| `profile` | string | No | AWS profile to use (defaults to None) |

## AWS CLI

```bash
aws amp list-workspaces --region <region>
```

## boto3

```python
import boto3

client = boto3.client('amp')
response = client.list_workspaces(
    Region=region,
)
```
