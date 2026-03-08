---
name: StartAHORun
description: Start a workflow run.

    Args:
        ctx: MCP context for error reporting
        workflow_id: ID of the workflow to run
        role_arn: ARN of the IAM role to use for the run
        name: Name for the run
        output_uri: S3 URI for the run outputs
        parameters: Parameters for the workflow.
           Parameter names must match one of the keys in the workflow's parameter template.
           All non-optional parameters must be present, if they are not provided the workflow run will not start. No other parameter
           names are allowed.
           The descriptions of the parameters in the parameter template may provide clues to the type of the parameter. It may be
           necessary to inspect the workflow definition to determine the appropriate parameter type.
        workflow_version_name: Optional version name to run
        storage_type: Storage type (STATIC or DYNAMIC)
        storage_capacity: Storage capacity in GB (required for STATIC)
        cache_id: Optional ID of a run cache to use
        cache_behavior: Optional cache behavior (CACHE_ALWAYS or CACHE_ON_FAILURE)
        run_group_id: Optional ID of a run group to associate with this run

    Returns:
        Dictionary containing the run information or error dict
    
---

# Startahorun

Start a workflow run.

    Args:
        ctx: MCP context for error reporting
        workflow_id: ID of the workflow to run
        role_arn: ARN of the IAM role to use for the run
        name: Name for the run
        output_uri: S3 URI for the run outputs
        parameters: Parameters for the workflow.
           Parameter names must match one of the keys in the workflow's parameter template.
           All non-optional parameters must be present, if they are not provided the workflow run will not start. No other parameter
           names are allowed.
           The descriptions of the parameters in the parameter template may provide clues to the type of the parameter. It may be
           necessary to inspect the workflow definition to determine the appropriate parameter type.
        workflow_version_name: Optional version name to run
        storage_type: Storage type (STATIC or DYNAMIC)
        storage_capacity: Storage capacity in GB (required for STATIC)
        cache_id: Optional ID of a run cache to use
        cache_behavior: Optional cache behavior (CACHE_ALWAYS or CACHE_ON_FAILURE)
        run_group_id: Optional ID of a run group to associate with this run

    Returns:
        Dictionary containing the run information or error dict
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workflow_id` | string | Yes | ID of the workflow to run |
| `role_arn` | string | Yes | ARN of the IAM role to use for the run |
| `name` | string | Yes | Name for the run |
| `output_uri` | string | Yes | S3 URI for the run outputs |
| `parameters` | string | Yes | Parameters for the workflow. Parameter names must match one of the keys in the workflow's parameter template.
       All non-optional parameters must be present, if they are not provided the workflow run will not start. No other parameter names are allowed.
       The descriptions of the parameters in the parameter template may provide clues to the type of the parameter. It may be
       necessary to inspect the workflow definition to determine the appropriate parameter type.
        |
| `workflow_version_name` | string | No | Optional version name to run |
| `storage_type` | string | No | Storage type (STATIC or DYNAMIC). DYNAMIC is preferred except for runs with very large inputs (TiBs). |
| `storage_capacity` | string | No | Storage capacity in GB (required for STATIC). Storage is allocated in 1200 GiB chunks |
| `cache_id` | string | No | Optional ID of a run cache to use |
| `cache_behavior` | string | No | Optional cache behavior (CACHE_ALWAYS or CACHE_ON_FAILURE) |
| `run_group_id` | string | No | Optional ID of a run group to associate with this run |

## AWS CLI

```bash
aws omics start-run --workflow-id <workflow_id> --role-arn <role_arn> --name <name> --output-uri <output_uri> --parameters <parameters> --workflow-version-name <workflow_version_name> --storage-type <storage_type> --storage-capacity <storage_capacity> --run-group-id <run_group_id> --cache-id <cache_id> --cache-behavior <cache_behavior>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.start_run(
    WorkflowId=workflow_id,
    RoleArn=role_arn,
    Name=name,
    OutputUri=output_uri,
    Parameters=parameters,
    WorkflowVersionName=workflow_version_name,
    StorageType=storage_type,
    StorageCapacity=storage_capacity,
    RunGroupId=run_group_id,
    CacheId=cache_id,
    CacheBehavior=cache_behavior,
)
```
