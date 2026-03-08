---
name: create-model-import-job
description: Create a model import job to import a model into Amazon Bedrock.

This tool creates a model import job in Amazon Bedrock to import a custom model.
The job name and model name are mandatory parameters. The S3 URI for the model data source
is optional and will be automatically inferred from the model name if not provided.

## Usage Instructions
1. Create descriptive job and model names based on the model you want to import
   - The tool itself will automatically add a timestamp suffix to distinguish names from multiple imports
   - Example: For a LLAMA-2 model, use "llama-2-import-job" and "llama-2" for job name and model name respectively
2. The S3 URI is NOT required - it will be automatically inferred from the model name
3. For advanced configurations, you can optionally specify:
   - Role ARN for permissions
   - VPC configuration for secure imports
   - KMS key for encryption
   - Tags for resource organization

## Best Practices
- Use clear, descriptive names for both jobName and importedModelName
- Name the model based on its architecture and purpose (e.g., "llama-2-7b-chat")
- When importing multiple versions of the same model, use consistent naming with version indicators

Args:
    ctx: The MCP context
    request: The model import job request containing job name, model name, and optional parameters

Returns:
    str: Formatted markdown text containing the model import job details

Raises:
    Exception: If there is an error creating the model import job
---

# Create Model Import Job

Create a model import job to import a model into Amazon Bedrock.

This tool creates a model import job in Amazon Bedrock to import a custom model.
The job name and model name are mandatory parameters. The S3 URI for the model data source
is optional and will be automatically inferred from the model name if not provided.

## Usage Instructions
1. Create descriptive job and model names based on the model you want to import
   - The tool itself will automatically add a timestamp suffix to distinguish names from multiple imports
   - Example: For a LLAMA-2 model, use "llama-2-import-job" and "llama-2" for job name and model name respectively
2. The S3 URI is NOT required - it will be automatically inferred from the model name
3. For advanced configurations, you can optionally specify:
   - Role ARN for permissions
   - VPC configuration for secure imports
   - KMS key for encryption
   - Tags for resource organization

## Best Practices
- Use clear, descriptive names for both jobName and importedModelName
- Name the model based on its architecture and purpose (e.g., "llama-2-7b-chat")
- When importing multiple versions of the same model, use consistent naming with version indicators

Args:
    ctx: The MCP context
    request: The model import job request containing job name, model name, and optional parameters

Returns:
    str: Formatted markdown text containing the model import job details

Raises:
    Exception: If there is an error creating the model import job

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | object | Yes | Request model for creating a model import job. |

## AWS CLI

```bash
aws bedrock create-model-import-job --model-import-job-name <request.modelImportJobName> --custom-model-arn <request.customModelArn> --model-artifact <request.modelArtifact> --model-type <request.modelType> --input-specification <request.inputSpecification> --client-request-token <request.clientRequestToken>
```

## boto3

```python
import boto3

client = boto3.client('bedrock')
response = client.create_model_import_job(
    ModelImportJobName=request.modelImportJobName,
    CustomModelArn=request.customModelArn,
    ModelArtifact=request.modelArtifact,
    ModelType=request.modelType,
    InputSpecification=request.inputSpecification,
    ClientRequestToken=request.clientRequestToken,
)
```
