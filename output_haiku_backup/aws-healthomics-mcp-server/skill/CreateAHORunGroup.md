---
name: CreateAHORunGroup
description: Create a new HealthOmics run group.

    Args:
        ctx: MCP context for error reporting
        name: Name for the run group (1-128 characters)
        max_cpus: Maximum CPUs for the run group (1-100000)
        max_gpus: Maximum GPUs for the run group (1-100000)
        max_duration: Maximum duration in minutes (1-100000)
        max_runs: Maximum concurrent runs (1-100000)
        tags: Tags to apply to the run group

    Returns:
        Dictionary containing the created run group's id, arn, and tags, or error dict
    
---

# Createahorungroup

Create a new HealthOmics run group.

    Args:
        ctx: MCP context for error reporting
        name: Name for the run group (1-128 characters)
        max_cpus: Maximum CPUs for the run group (1-100000)
        max_gpus: Maximum GPUs for the run group (1-100000)
        max_duration: Maximum duration in minutes (1-100000)
        max_runs: Maximum concurrent runs (1-100000)
        tags: Tags to apply to the run group

    Returns:
        Dictionary containing the created run group's id, arn, and tags, or error dict
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | string | No | Name for the run group (1-128 characters) |
| `max_cpus` | string | No | Maximum CPUs for the run group (1-100000) |
| `max_gpus` | string | No | Maximum GPUs for the run group (1-100000) |
| `max_duration` | string | No | Maximum duration in minutes (1-100000) |
| `max_runs` | string | No | Maximum concurrent runs (1-100000) |
| `tags` | string | No | Tags to apply to the run group |

## AWS CLI

```bash
aws omics create-run-group --name <name> --max-cpus <max_cpus> --max-gpus <max_gpus> --max-duration <max_duration> --max-runs <max_runs> --tags <tags>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.create_run_group(
    Name=name,
    MaxCpus=max_cpus,
    MaxGpus=max_gpus,
    MaxDuration=max_duration,
    MaxRuns=max_runs,
    Tags=tags,
)
```
