---
name: create-research-repository
description: Build a FAISS index for a Git repository.

    This tool indexes a Git repository (local or remote) using FAISS and Amazon Bedrock embeddings.
    The index can then be used for semantic search within the repository.

    Args:
        ctx: MCP context object used for progress tracking and error reporting
        repository_path: Path to local repository or URL to remote repository
        output_path: Where to store the index (optional, uses default if not provided)
        embedding_model: Which AWS embedding model to use
        include_patterns: Glob patterns for files to include (optional)
        exclude_patterns: Glob patterns for files to exclude (optional)
        chunk_size: Maximum size of each chunk in characters
        chunk_overlap: Overlap between chunks in characters

    Returns:
        Information about the created index
    
---

# Create Research Repository

Build a FAISS index for a Git repository.

    This tool indexes a Git repository (local or remote) using FAISS and Amazon Bedrock embeddings.
    The index can then be used for semantic search within the repository.

    Args:
        ctx: MCP context object used for progress tracking and error reporting
        repository_path: Path to local repository or URL to remote repository
        output_path: Where to store the index (optional, uses default if not provided)
        embedding_model: Which AWS embedding model to use
        include_patterns: Glob patterns for files to include (optional)
        exclude_patterns: Glob patterns for files to exclude (optional)
        chunk_size: Maximum size of each chunk in characters
        chunk_overlap: Overlap between chunks in characters

    Returns:
        Information about the created index
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `repository_path` | string | Yes | Path to local repository or URL to remote repository |
| `output_path` | string | No | Where to store the index (optional, uses default if not provided) |
| `embedding_model` | string | No | Which AWS embedding model to use |
| `include_patterns` | string | No | Glob patterns for files to include (optional). Defaults to common source code and documentation files. |
| `exclude_patterns` | string | No | Glob patterns for files to exclude (optional). Defaults to common binary files, build artifacts, and VCS directories. |
| `chunk_size` | integer | No | Maximum size of each chunk in characters |
| `chunk_overlap` | integer | No | Overlap between chunks in characters |

