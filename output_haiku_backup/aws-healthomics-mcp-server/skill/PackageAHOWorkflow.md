---
name: PackageAHOWorkflow
description: Package workflow definition files into a base64-encoded ZIP.

    Args:
        ctx: MCP context for error reporting
        main_file_content: Content of the main workflow file
        main_file_name: Name of the main workflow file (default: main.wdl)
        additional_files: Dictionary of additional files (filename: content)

    Returns:
        Base64-encoded ZIP file containing the workflow definition, or error dict
    
---

# Packageahoworkflow

Package workflow definition files into a base64-encoded ZIP.

    Args:
        ctx: MCP context for error reporting
        main_file_content: Content of the main workflow file
        main_file_name: Name of the main workflow file (default: main.wdl)
        additional_files: Dictionary of additional files (filename: content)

    Returns:
        Base64-encoded ZIP file containing the workflow definition, or error dict
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `main_file_content` | string | Yes | Content of the main workflow file |
| `main_file_name` | string | No | Name of the main workflow file |
| `additional_files` | string | No | Dictionary of additional files (filename: content) |

