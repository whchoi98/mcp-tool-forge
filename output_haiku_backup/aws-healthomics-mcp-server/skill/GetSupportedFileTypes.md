---
name: GetSupportedFileTypes
description: Get information about supported genomics file types.

    Args:
        ctx: MCP context for error reporting

    Returns:
        Dictionary containing information about supported file types and their descriptions
    
---

# Getsupportedfiletypes

Get information about supported genomics file types.

    Args:
        ctx: MCP context for error reporting

    Returns:
        Dictionary containing information about supported file types and their descriptions
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|

## AWS CLI

```bash
aws omics list-file-types
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_file_types(
)
```
