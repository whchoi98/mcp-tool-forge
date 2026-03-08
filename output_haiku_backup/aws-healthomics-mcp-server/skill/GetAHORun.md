---
name: GetAHORun
description: Get details about a specific run.

    Args:
        ctx: MCP context for error reporting
        run_id: ID of the run to retrieve

    Returns:
        Dictionary containing run details or error dict including:
        - Basic run information (id, arn, name, status)
        - Workflow information (workflowId, workflowType, workflowVersionName)
        - Timing information (creationTime, startTime, stopTime)
        - Output locations (outputUri, runOutputUri)
        - IAM role (roleArn)
        - Run parameters and metadata
        - Status messages and failure reasons (if applicable)
    
---

# Getahorun

Get details about a specific run.

    Args:
        ctx: MCP context for error reporting
        run_id: ID of the run to retrieve

    Returns:
        Dictionary containing run details or error dict including:
        - Basic run information (id, arn, name, status)
        - Workflow information (workflowId, workflowType, workflowVersionName)
        - Timing information (creationTime, startTime, stopTime)
        - Output locations (outputUri, runOutputUri)
        - IAM role (roleArn)
        - Run parameters and metadata
        - Status messages and failure reasons (if applicable)
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run_id` | string | Yes | ID of the run to retrieve |

## AWS CLI

```bash
aws omics get-run --id <run_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_run(
    Id=run_id,
)
```
