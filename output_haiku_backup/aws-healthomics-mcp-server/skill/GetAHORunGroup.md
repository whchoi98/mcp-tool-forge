---
name: GetAHORunGroup
description: Get details of a specific HealthOmics run group.

    Args:
        ctx: MCP context for error reporting
        run_group_id: ID of the run group to retrieve

    Returns:
        Dictionary containing the run group details, or error dict
    
---

# Getahorungroup

Get details of a specific HealthOmics run group.

    Args:
        ctx: MCP context for error reporting
        run_group_id: ID of the run group to retrieve

    Returns:
        Dictionary containing the run group details, or error dict
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run_group_id` | string | Yes | ID of the run group to retrieve |

## AWS CLI

```bash
aws omics get-run-group --id <run_group_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_run_group(
    Id=run_group_id,
)
```
