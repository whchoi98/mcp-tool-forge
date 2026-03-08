---
name: DiagnoseAHORunFailure
description: Provides comprehensive diagnostic information for a failed workflow run.

    This function collects multiple sources of diagnostic information including:
    - Run details and failure reason
    - Engine logs from CloudWatch
    - Run manifest logs containing workflow summary and resource metrics (when detailed=True)
    - Task logs from all failed tasks
    - Actionable recommendations for troubleshooting

    Args:
        ctx: MCP context for error reporting
        run_id: ID of the failed run
        detailed: If False (default), excludes manifest logs and limits engine/task logs to last 50 lines
                 from 15 minutes before stop time to 5 minutes after. If True, includes all logs.

    Returns:
        Dictionary containing comprehensive diagnostic information including:
        - runId: The run identifier
        - status: Current run status
        - failureReason: AWS-provided failure reason
        - runUuid: Run UUID for log stream identification
        - engineLogs: Engine execution logs
        - manifestLogs: Run manifest logs with workflow summary (only when detailed=True)
        - failedTasks: List of failed tasks with their logs
        - recommendations: Troubleshooting recommendations
    
---

# Diagnoseahorunfailure

Provides comprehensive diagnostic information for a failed workflow run.

    This function collects multiple sources of diagnostic information including:
    - Run details and failure reason
    - Engine logs from CloudWatch
    - Run manifest logs containing workflow summary and resource metrics (when detailed=True)
    - Task logs from all failed tasks
    - Actionable recommendations for troubleshooting

    Args:
        ctx: MCP context for error reporting
        run_id: ID of the failed run
        detailed: If False (default), excludes manifest logs and limits engine/task logs to last 50 lines
                 from 15 minutes before stop time to 5 minutes after. If True, includes all logs.

    Returns:
        Dictionary containing comprehensive diagnostic information including:
        - runId: The run identifier
        - status: Current run status
        - failureReason: AWS-provided failure reason
        - runUuid: Run UUID for log stream identification
        - engineLogs: Engine execution logs
        - manifestLogs: Run manifest logs with workflow summary (only when detailed=True)
        - failedTasks: List of failed tasks with their logs
        - recommendations: Troubleshooting recommendations
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run_id` | string | Yes | ID of the failed run |
| `detailed` | boolean | No | If False, excludes manifest logs and limits engine/task logs to last 50 lines from 15 minutes before stop time to 5 minutes after. If True, includes all logs. False is suitable for most scenarios |

## AWS CLI

```bash
aws omics get-run --id <run_id> --export <detailed>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_run(
    Id=run_id,
    Export=detailed,
)
```
