---
name: ListMetrics
description: Get a list of all metric names.

    ## Usage
    - Use this tool to discover available metrics in the Prometheus server
    - Returns a sorted list of all metric names
    - Useful for exploration before crafting specific queries
    - If workspace_id is not known, use GetAvailableWorkspaces tool first to find available workspaces and ASK THE USER to choose one

    ## Example
    Input:
      workspace_id: "ws-12345678-abcd-1234-efgh-123456789012"
      region: "us-east-1"

    Output:
      {
        "metrics": [
          "go_gc_duration_seconds",
          "go_goroutines",
          "http_requests_total",
          ...
        ]
      }
    
---

# Listmetrics

Get a list of all metric names.

    ## Usage
    - Use this tool to discover available metrics in the Prometheus server
    - Returns a sorted list of all metric names
    - Useful for exploration before crafting specific queries
    - If workspace_id is not known, use GetAvailableWorkspaces tool first to find available workspaces and ASK THE USER to choose one

    ## Example
    Input:
      workspace_id: "ws-12345678-abcd-1234-efgh-123456789012"
      region: "us-east-1"

    Output:
      {
        "metrics": [
          "go_gc_duration_seconds",
          "go_goroutines",
          "http_requests_total",
          ...
        ]
      }
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workspace_id` | string | No | The Prometheus workspace ID to use (e.g., ws-12345678-abcd-1234-efgh-123456789012). Optional if a URL is configured via command line arguments. |
| `region` | string | No | AWS region (defaults to current region) |
| `profile` | string | No | AWS profile to use (defaults to None) |

## AWS CLI

```bash
aws amp list-metrics --workspace-id <workspace_id> --region <region> --profile <profile>
```

## boto3

```python
import boto3

client = boto3.client('amp')
response = client.list_metrics(
    WorkspaceId=workspace_id,
    Region=region,
)
```
