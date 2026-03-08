---
name: list-model-import-jobs
description: List model import jobs in Amazon Bedrock.

This tool retrieves a list of model import jobs in Amazon Bedrock.
The results can be filtered and sorted using the optional request parameters.

## Usage Instructions
1. Call this tool without parameters to list all model import jobs
2. Optionally provide filtering parameters in the request:
   - creationTimeAfter: Filter jobs created after this time
   - creationTimeBefore: Filter jobs created before this time
   - statusEquals: Filter jobs by status (InProgress, Completed, Failed)
   - nameContains: Filter jobs by name substring
   - sortBy: Sort results by field (e.g., CreationTime)
   - sortOrder: Sort order (Ascending, Descending)

## Information Returned
- Job name and ARN
- Status with visual indicator (🔄 In Progress, ✅ Completed, ❌ Failed)
- Creation and last modified times
- Associated model name and ARN

## How to Use This Information
- Monitor ongoing imports with status indicators
- Find recently created or modified jobs
- Identify completed jobs to access their imported models
- Troubleshoot failed imports

## When to Use
- To check the status of recent model imports
- Before using get_model_import_job to find the exact job name
- To monitor multiple ongoing imports
- To verify if a specific import job exists
- To find the job associated with a specific model

Args:
    ctx: The MCP context
    request: Optional request parameters for filtering and sorting the results

Returns:
    str: Formatted markdown text containing the list of jobs

Raises:
    Exception: If there is an error listing the jobs
---

# List Model Import Jobs

List model import jobs in Amazon Bedrock.

This tool retrieves a list of model import jobs in Amazon Bedrock.
The results can be filtered and sorted using the optional request parameters.

## Usage Instructions
1. Call this tool without parameters to list all model import jobs
2. Optionally provide filtering parameters in the request:
   - creationTimeAfter: Filter jobs created after this time
   - creationTimeBefore: Filter jobs created before this time
   - statusEquals: Filter jobs by status (InProgress, Completed, Failed)
   - nameContains: Filter jobs by name substring
   - sortBy: Sort results by field (e.g., CreationTime)
   - sortOrder: Sort order (Ascending, Descending)

## Information Returned
- Job name and ARN
- Status with visual indicator (🔄 In Progress, ✅ Completed, ❌ Failed)
- Creation and last modified times
- Associated model name and ARN

## How to Use This Information
- Monitor ongoing imports with status indicators
- Find recently created or modified jobs
- Identify completed jobs to access their imported models
- Troubleshoot failed imports

## When to Use
- To check the status of recent model imports
- Before using get_model_import_job to find the exact job name
- To monitor multiple ongoing imports
- To verify if a specific import job exists
- To find the job associated with a specific model

Args:
    ctx: The MCP context
    request: Optional request parameters for filtering and sorting the results

Returns:
    str: Formatted markdown text containing the list of jobs

Raises:
    Exception: If there is an error listing the jobs

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | string | No |  |

