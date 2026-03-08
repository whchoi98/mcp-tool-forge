---
name: ListAHOWorkflowVersions
description: List versions of a workflow.

    Args:
        ctx: MCP context for error reporting
        workflow_id: ID of the workflow
        max_results: Maximum number of results to return (default: 10)
        next_token: Token for pagination

    Returns:
        Dictionary containing workflow version information and next token if available
    
---

# Listahoworkflowversions

List versions of a workflow.

    Args:
        ctx: MCP context for error reporting
        workflow_id: ID of the workflow
        max_results: Maximum number of results to return (default: 10)
        next_token: Token for pagination

    Returns:
        Dictionary containing workflow version information and next token if available
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workflow_id` | string | Yes | ID of the workflow |
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Token for pagination from a previous response |

## AWS CLI

```bash
aws omics list-workflow-versions --workflow-id <workflow_id> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_workflow_versions(
    WorkflowId=workflow_id,
    MaxResults=max_results,
    NextToken=next_token,
)
```
