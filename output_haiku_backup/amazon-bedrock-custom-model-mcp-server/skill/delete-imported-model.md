---
name: delete-imported-model
description: Delete an imported model from Amazon Bedrock.

This tool permanently deletes a custom model that was previously imported into Amazon Bedrock.
This operation cannot be undone and will permanently remove the model from your AWS account.

## Usage Instructions
1. Provide either the model name or ARN as the model_identifier parameter
2. You can get a list of available models using the list_imported_models tool
3. Verify you're deleting the correct model before proceeding

## Important Considerations
- This operation is IRREVERSIBLE - the model will be permanently deleted
- Any applications using this model will fail after deletion
- Consider backing up important model data before deletion
- Deletion may take some time to complete for large models

## When to Use
- When you no longer need a specific model
- To manage costs by removing unused models

Args:
    ctx: The MCP context
    model_identifier: The name or ARN of the model to delete

Returns:
    str: Formatted markdown text confirming the deletion

Raises:
    Exception: If there is an error deleting the model
---

# Delete Imported Model

Delete an imported model from Amazon Bedrock.

This tool permanently deletes a custom model that was previously imported into Amazon Bedrock.
This operation cannot be undone and will permanently remove the model from your AWS account.

## Usage Instructions
1. Provide either the model name or ARN as the model_identifier parameter
2. You can get a list of available models using the list_imported_models tool
3. Verify you're deleting the correct model before proceeding

## Important Considerations
- This operation is IRREVERSIBLE - the model will be permanently deleted
- Any applications using this model will fail after deletion
- Consider backing up important model data before deletion
- Deletion may take some time to complete for large models

## When to Use
- When you no longer need a specific model
- To manage costs by removing unused models

Args:
    ctx: The MCP context
    model_identifier: The name or ARN of the model to delete

Returns:
    str: Formatted markdown text confirming the deletion

Raises:
    Exception: If there is an error deleting the model

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model_identifier` | string | Yes |  |

## AWS CLI

```bash
aws bedrock delete-model --model-identifier <model_identifier>
```

## boto3

```python
import boto3

client = boto3.client('bedrock')
response = client.delete_model_invocation_logging_configuration(
    ModelIdentifier=model_identifier,
)
```
