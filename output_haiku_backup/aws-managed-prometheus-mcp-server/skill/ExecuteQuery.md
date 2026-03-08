---
name: ExecuteQuery
description: Execute a PromQL query against Amazon Managed Prometheus.

    ## Usage
    - Use this tool to execute a PromQL query at a specific instant in time
    - The query will return the current value of the specified metrics
    - For time series data over a range, use execute_range_query instead
    - If workspace_id is not known, use GetAvailableWorkspaces tool first to find available workspaces and ASK THE USER to choose one
    - Uses DescribeWorkspace API to get the exact workspace URL
    - No manual URL construction is performed

    ## Example
    Input:
      workspace_id: "ws-12345678-abcd-1234-efgh-123456789012"
      query: "up"
      region: "us-east-1"

    Output:
      {
        "resultType": "vector",
        "result": [
          {
            "metric": {"__name__": "up", "instance": "localhost:9090", "job": "prometheus"},
            "value": [1680307200, "1"]
          },
          {
            "metric": {"__name__": "up", "instance": "localhost:9100", "job": "node"},
            "value": [1680307200, "1"]
          }
        ]
      }

    Example queries:
    - `up` - Shows which targets are up
    - `rate(node_cpu_seconds_total{mode="system"}[1m])` - CPU usage rate
    - `sum by(instance) (rate(node_network_receive_bytes_total[5m]))` - Network receive rate by instance
    
---

# Executequery

Execute a PromQL query against Amazon Managed Prometheus.

    ## Usage
    - Use this tool to execute a PromQL query at a specific instant in time
    - The query will return the current value of the specified metrics
    - For time series data over a range, use execute_range_query instead
    - If workspace_id is not known, use GetAvailableWorkspaces tool first to find available workspaces and ASK THE USER to choose one
    - Uses DescribeWorkspace API to get the exact workspace URL
    - No manual URL construction is performed

    ## Example
    Input:
      workspace_id: "ws-12345678-abcd-1234-efgh-123456789012"
      query: "up"
      region: "us-east-1"

    Output:
      {
        "resultType": "vector",
        "result": [
          {
            "metric": {"__name__": "up", "instance": "localhost:9090", "job": "prometheus"},
            "value": [1680307200, "1"]
          },
          {
            "metric": {"__name__": "up", "instance": "localhost:9100", "job": "node"},
            "value": [1680307200, "1"]
          }
        ]
      }

    Example queries:
    - `up` - Shows which targets are up
    - `rate(node_cpu_seconds_total{mode="system"}[1m])` - CPU usage rate
    - `sum by(instance) (rate(node_network_receive_bytes_total[5m]))` - Network receive rate by instance
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workspace_id` | string | No | The Prometheus workspace ID to use (e.g., ws-12345678-abcd-1234-efgh-123456789012). Optional if a URL is configured via command line arguments. |
| `query` | string | Yes | The PromQL query to execute |
| `time` | string | No | Optional timestamp for query evaluation (RFC3339 or Unix timestamp) |
| `region` | string | No | AWS region (defaults to current region) |
| `profile` | string | No | AWS profile to use (defaults to None) |

## AWS CLI

```bash
aws amp query --workspace-id <workspace_id> --query <query> --time <time> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('prometheusservice')
response = client.query_metric_data(
    WorkspaceId=workspace_id,
    Query=query,
    Time=time,
    Region=region,
)
```
