---
name: UpdateAHORunGroup
description: Update an existing HealthOmics run group.

    Args:
        ctx: MCP context for error reporting
        run_group_id: ID of the run group to update
        name: New name for the run group
        max_cpus: New maximum CPUs
        max_gpus: New maximum GPUs
        max_duration: New maximum duration in minutes
        max_runs: New maximum concurrent runs

    Returns:
        Dictionary containing the run group ID and update status, or error dict
    
---

# Updateahorungroup

Update an existing HealthOmics run group.

    Args:
        ctx: MCP context for error reporting
        run_group_id: ID of the run group to update
        name: New name for the run group
        max_cpus: New maximum CPUs
        max_gpus: New maximum GPUs
        max_duration: New maximum duration in minutes
        max_runs: New maximum concurrent runs

    Returns:
        Dictionary containing the run group ID and update status, or error dict
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run_group_id` | string | Yes | ID of the run group to update |
| `name` | string | No | New name for the run group |
| `max_cpus` | string | No | New maximum CPUs |
| `max_gpus` | string | No | New maximum GPUs |
| `max_duration` | string | No | New maximum duration in minutes |
| `max_runs` | string | No | New maximum concurrent runs |

## AWS CLI

```bash
aws omics update-run-group --id <run_group_id> --name <name> --max-cpus <max_cpus> --max-gpus <max_gpus> --max-duration <max_duration> --max-runs <max_runs>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.update_run_group(
    Id=run_group_id,
    Name=name,
    MaxCpus=max_cpus,
    MaxGpus=max_gpus,
    MaxDuration=max_duration,
    MaxRuns=max_runs,
)
```
