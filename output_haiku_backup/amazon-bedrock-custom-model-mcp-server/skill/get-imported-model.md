---
name: get-imported-model
description: Get imported model details from Amazon Bedrock.

This tool retrieves detailed information about a custom model that was previously
imported into Amazon Bedrock. If the exact model name is not found, it will attempt
to find a close match using approximate matching.

## Usage Instructions
1. Provide the model name or ARN as the model_identifier parameter
2. The tool will attempt to find close matches if the exact name isn't found

## Information Returned
- Model ARN and creation time
- Model architecture details
- Whether the model supports chat or instructions
- Custom model units used for billing the model (if applicable)
- KMS key information (if encrypted)
- Import job details and data source

## How to Use This Information
- Verify model details before using in applications
- Check if the model supports instruction for chat applications using Bedrock Converse API
- Review the model details to trace model provenance
- Use the model ARN when configuring inference endpoints

Args:
    ctx: The MCP context
    model_identifier: The ID or name of the model to retrieve

Returns:
    str: Formatted markdown text containing the model details

Raises:
    ValueError: If model cannot be found even with approximate matching
    ClientError: If there is an error from the AWS service
---

# Get Imported Model

Get imported model details from Amazon Bedrock.

This tool retrieves detailed information about a custom model that was previously
imported into Amazon Bedrock. If the exact model name is not found, it will attempt
to find a close match using approximate matching.

## Usage Instructions
1. Provide the model name or ARN as the model_identifier parameter
2. The tool will attempt to find close matches if the exact name isn't found

## Information Returned
- Model ARN and creation time
- Model architecture details
- Whether the model supports chat or instructions
- Custom model units used for billing the model (if applicable)
- KMS key information (if encrypted)
- Import job details and data source

## How to Use This Information
- Verify model details before using in applications
- Check if the model supports instruction for chat applications using Bedrock Converse API
- Review the model details to trace model provenance
- Use the model ARN when configuring inference endpoints

Args:
    ctx: The MCP context
    model_identifier: The ID or name of the model to retrieve

Returns:
    str: Formatted markdown text containing the model details

Raises:
    ValueError: If model cannot be found even with approximate matching
    ClientError: If there is an error from the AWS service

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model_identifier` | string | Yes | Name or ARN of the model |

## AWS CLI

```bash
aws bedrock get-model-customization-job --model-customization-job-identifier <model_identifier>
```

## boto3

```python
import boto3

client = boto3.client('bedrock')
response = client.get_model_customization_job(
    ModelCustomizationJobIdentifier=model_identifier,
)
```
