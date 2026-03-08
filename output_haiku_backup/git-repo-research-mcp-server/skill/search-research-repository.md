---
name: search-research-repository
description: Perform semantic search within an indexed repository.

    This tool searches an indexed repository using semantic search with Amazon Bedrock embeddings.
    It returns results ranked by relevance to the query.

    Args:
        ctx: MCP context object used for error reporting
        index_path: Name of the repository or path to the index to search
        query: The search query to use for semantic search
        limit: Maximum number of results to return
        threshold: Minimum similarity score threshold (0.0 to 1.0)

    Returns:
        Search results ranked by relevance to the query
    
---

# Search Research Repository

Perform semantic search within an indexed repository.

    This tool searches an indexed repository using semantic search with Amazon Bedrock embeddings.
    It returns results ranked by relevance to the query.

    Args:
        ctx: MCP context object used for error reporting
        index_path: Name of the repository or path to the index to search
        query: The search query to use for semantic search
        limit: Maximum number of results to return
        threshold: Minimum similarity score threshold (0.0 to 1.0)

    Returns:
        Search results ranked by relevance to the query
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `index_path` | string | Yes | Name of the repository or path to the index to search |
| `query` | string | Yes | The search query to use for semantic search |
| `limit` | integer | No | Maximum number of results to return |
| `threshold` | number | No | Minimum similarity score threshold (0.0 to 1.0) |

