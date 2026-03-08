---
name: list-imported-models
description: List imported models in Amazon Bedrock.

This tool retrieves a list of models that have already been imported into Amazon Bedrock.
The results can be filtered and sorted using the optional request parameters.

## Usage Instructions
1. Call this tool without parameters to list all imported models
2. Optionally provide filtering parameters in the request:
   - creationTimeAfter: Filter models created after this time
   - creationTimeBefore: Filter models created before this time
   - nameContains: Filter models by name substring
   - sortBy: Sort results by field (e.g., CreationTime)
   - sortOrder: Sort order (Ascending, Descending)

## Information Returned
- Model name and ARN
- Creation time
- Model architecture
- Whether the model supports instruction tuning (✅ or ❌)

## How to Use This Information
- Note model names for use with other tools like get_imported_model
- Check instruction support to determine if models can be used for chat applications
- Review model architectures to understand model capabilities

## When to Use
- Before using get_imported_model to find the exact model name
- When you need to see all available models in your account
- To check if a specific model exists by filtering with nameContains
- To find the most recently imported models by sorting by creation time

Args:
    ctx: The MCP context
    request: Optional request parameters for filtering and sorting the results

Returns:
    str: Formatted markdown text containing the list of models

Raises:
    Exception: If there is an error listing the models
---

# List Imported Models

List imported models in Amazon Bedrock.

This tool retrieves a list of models that have already been imported into Amazon Bedrock.
The results can be filtered and sorted using the optional request parameters.

## Usage Instructions
1. Call this tool without parameters to list all imported models
2. Optionally provide filtering parameters in the request:
   - creationTimeAfter: Filter models created after this time
   - creationTimeBefore: Filter models created before this time
   - nameContains: Filter models by name substring
   - sortBy: Sort results by field (e.g., CreationTime)
   - sortOrder: Sort order (Ascending, Descending)

## Information Returned
- Model name and ARN
- Creation time
- Model architecture
- Whether the model supports instruction tuning (✅ or ❌)

## How to Use This Information
- Note model names for use with other tools like get_imported_model
- Check instruction support to determine if models can be used for chat applications
- Review model architectures to understand model capabilities

## When to Use
- Before using get_imported_model to find the exact model name
- When you need to see all available models in your account
- To check if a specific model exists by filtering with nameContains
- To find the most recently imported models by sorting by creation time

Args:
    ctx: The MCP context
    request: Optional request parameters for filtering and sorting the results

Returns:
    str: Formatted markdown text containing the list of models

Raises:
    Exception: If there is an error listing the models

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | string | No |  |

