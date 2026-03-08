---
name: GetAHOWorkflow
description: Get details about a specific workflow.

    Args:
        ctx: MCP context for error reporting
        workflow_id: ID of the workflow to retrieve
        export_definition: Whether to include a presigned URL for downloading the workflow definition ZIP file

    Returns:
        Dictionary containing workflow details. When export_definition=True, includes a 'definition'
        field with a presigned URL for downloading the workflow definition ZIP file.
    
---

# Getahoworkflow

Get details about a specific workflow.

    Args:
        ctx: MCP context for error reporting
        workflow_id: ID of the workflow to retrieve
        export_definition: Whether to include a presigned URL for downloading the workflow definition ZIP file

    Returns:
        Dictionary containing workflow details. When export_definition=True, includes a 'definition'
        field with a presigned URL for downloading the workflow definition ZIP file.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workflow_id` | string | Yes | ID of the workflow to retrieve |
| `export_definition` | boolean | No | Whether to include a presigned URL for downloading the workflow definition ZIP file |

## AWS CLI

```bash
aws omics get-workflow --id <workflow_id> --export <export_definition>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.get_workflow(
    Id=workflow_id,
    Export=export_definition,
)
```
