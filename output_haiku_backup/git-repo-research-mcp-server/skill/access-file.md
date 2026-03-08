---
name: access-file
description: Access file or directory contents.

    This tool provides access to file or directory contents:
    - If the filepath references a text file, returns the content as a string
    - If the filepath references a directory, returns an array of files in the directory
    - If the filepath references a binary image (jpg, png), returns the image data

    For repository files, use the format: repository_name/repository/path/to/file
    Example: awslabs_mcp/repository/README.md

    For repositories with organization names, both formats are supported:
    - awslabs_mcp/repository/README.md (with underscore)
    - awslabs/mcp/repository/README.md (with slash)

    Args:
        ctx: MCP context object used for error reporting
        filepath: Path to the file or directory to access

    Returns:
        File content, directory listing, or image data
    
---

# Access File

Access file or directory contents.

    This tool provides access to file or directory contents:
    - If the filepath references a text file, returns the content as a string
    - If the filepath references a directory, returns an array of files in the directory
    - If the filepath references a binary image (jpg, png), returns the image data

    For repository files, use the format: repository_name/repository/path/to/file
    Example: awslabs_mcp/repository/README.md

    For repositories with organization names, both formats are supported:
    - awslabs_mcp/repository/README.md (with underscore)
    - awslabs/mcp/repository/README.md (with slash)

    Args:
        ctx: MCP context object used for error reporting
        filepath: Path to the file or directory to access

    Returns:
        File content, directory listing, or image data
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `filepath` | string | Yes | Path to the file or directory to access |

