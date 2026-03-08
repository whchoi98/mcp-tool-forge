---
name: delete-research-repository
description: Delete an indexed repository.

    This tool deletes an indexed repository and its associated files.
    It can be identified by repository name or the full path to the index.

    Args:
        ctx: MCP context object used for error reporting
        repository_name_or_path: Name of the repository or path to the index to delete
        index_directory: Directory to look for indices (optional, uses default if not provided)

    Returns:
        Status of the delete operation
    
---

# Delete Research Repository

Delete an indexed repository.

    This tool deletes an indexed repository and its associated files.
    It can be identified by repository name or the full path to the index.

    Args:
        ctx: MCP context object used for error reporting
        repository_name_or_path: Name of the repository or path to the index to delete
        index_directory: Directory to look for indices (optional, uses default if not provided)

    Returns:
        Status of the delete operation
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `repository_name_or_path` | string | Yes | Name of the repository or path to the index to delete |
| `index_directory` | string | No | Directory to look for indices (optional, uses default if not provided) |

