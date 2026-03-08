---
name: ExecuteRangeQuery
description: Execute a range query and return the result.

    ## Usage
    - Use this tool to execute a PromQL query over a time range
    - The query will return a series of values for the specified time range
    - Useful for generating time series data for graphs or trend analysis
    - If workspace_id is not known, use GetAvailableWorkspaces tool first to find available workspaces and ASK THE USER to choose one
    - Uses DescribeWorkspace API to get the exact workspace URL
    - No manual URL construction is performed

    ## Example
    Input:
      workspace_id: "ws-12345678-abcd-1234-efgh-123456789012"
      query: "rate(node_cpu_seconds_total{mode=\"system\"}[5m])"
      start: "2023-04-01T00:00:00Z"
      end: "2023-04-01T01:00:00Z"
      step: "5m"

    Output:
      {
        "resultType": "matrix",
        "result": [
          {
            "metric": {"__name__": "rate", "mode": "system", "instance": "localhost:9100"},
            "values": [[1680307200, "0.01"], [1680307500, "0.012"], ...]
          }
        ]
      }
    
---

# Executerangequery

Execute a range query and return the result.

    ## Usage
    - Use this tool to execute a PromQL query over a time range
    - The query will return a series of values for the specified time range
    - Useful for generating time series data for graphs or trend analysis
    - If workspace_id is not known, use GetAvailableWorkspaces tool first to find available workspaces and ASK THE USER to choose one
    - Uses DescribeWorkspace API to get the exact workspace URL
    - No manual URL construction is performed

    ## Example
    Input:
      workspace_id: "ws-12345678-abcd-1234-efgh-123456789012"
      query: "rate(node_cpu_seconds_total{mode=\"system\"}[5m])"
      start: "2023-04-01T00:00:00Z"
      end: "2023-04-01T01:00:00Z"
      step: "5m"

    Output:
      {
        "resultType": "matrix",
        "result": [
          {
            "metric": {"__name__": "rate", "mode": "system", "instance": "localhost:9100"},
            "values": [[1680307200, "0.01"], [1680307500, "0.012"], ...]
          }
        ]
      }
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workspace_id` | string | No | The Prometheus workspace ID to use (e.g., ws-12345678-abcd-1234-efgh-123456789012). Optional if a URL is configured via command line arguments. |
| `query` | string | Yes | The PromQL query to execute |
| `start` | string | Yes | Start timestamp (RFC3339 or Unix timestamp) |
| `end` | string | Yes | End timestamp (RFC3339 or Unix timestamp) |
| `step` | string | Yes | Query resolution step width (duration format, e.g. '15s', '1m', '1h') |
| `region` | string | No | AWS region (defaults to current region) |
| `profile` | string | No | AWS profile to use (defaults to None) |

## AWS CLI

```bash
aws amp query-range --workspace-id <workspace_id> --query <query> --start-time <start> --end-time <end> --step <step> --region <region> --profile <profile>
```

## boto3

```python
import boto3

client = boto3.client('prometheus')
response = client.query_range(
    WorkspaceId=workspace_id,
    Query=query,
    StartTime=start,
    EndTime=end,
    Step=step,
)
```
