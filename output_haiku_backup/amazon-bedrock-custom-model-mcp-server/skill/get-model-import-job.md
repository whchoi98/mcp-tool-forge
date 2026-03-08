---
name: get-model-import-job
description: Get model import job details from Amazon Bedrock.

This tool retrieves detailed information about a model import job in Amazon Bedrock.
If the exact job name is not found, it will attempt to find a close match.

## Usage Instructions
1. Provide the job name or ARN as the job_identifier parameter
2. The tool will attempt to find close matches if the exact name isn't found

## Information Returned
- Job status (In Progress, Completed, or Failed)
- Creation, modification, and completion timestamps
- Job ARN and failure message (if applicable)
- Model details including name and ARN
- Configuration details including role ARN, data source, VPC config, and KMS key

## When to Use
- To check the status of an ongoing model import
- To troubleshoot failed imports by examining error messages
- To verify the configuration of a completed import
- To get the ARN of an imported model after job completion

## Status Indicators
- 🔄 In Progress: The import job is currently running
- ✅ Completed: The import job has successfully completed
- ❌ Failed: The import job encountered an error

Args:
    ctx: The MCP context
    job_identifier: The name or ARN of the model import job to retrieve

Returns:
    str: Formatted markdown text containing the job details

Raises:
    ValueError: If job cannot be found even with approximate matching
    ClientError: If there is an error from the AWS service
---

# Get Model Import Job

Get model import job details from Amazon Bedrock.

This tool retrieves detailed information about a model import job in Amazon Bedrock.
If the exact job name is not found, it will attempt to find a close match.

## Usage Instructions
1. Provide the job name or ARN as the job_identifier parameter
2. The tool will attempt to find close matches if the exact name isn't found

## Information Returned
- Job status (In Progress, Completed, or Failed)
- Creation, modification, and completion timestamps
- Job ARN and failure message (if applicable)
- Model details including name and ARN
- Configuration details including role ARN, data source, VPC config, and KMS key

## When to Use
- To check the status of an ongoing model import
- To troubleshoot failed imports by examining error messages
- To verify the configuration of a completed import
- To get the ARN of an imported model after job completion

## Status Indicators
- 🔄 In Progress: The import job is currently running
- ✅ Completed: The import job has successfully completed
- ❌ Failed: The import job encountered an error

Args:
    ctx: The MCP context
    job_identifier: The name or ARN of the model import job to retrieve

Returns:
    str: Formatted markdown text containing the job details

Raises:
    ValueError: If job cannot be found even with approximate matching
    ClientError: If there is an error from the AWS service

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `job_identifier` | string | Yes | Name or ARN of the job |

## AWS CLI

```bash
aws bedrock get-model-import-job --job-identifier <job_identifier>
```

## boto3

```python
import boto3

client = boto3.client('bedrock')
response = client.get_model_import_job(
    JobIdentifier=job_identifier,
)
```
