---
name: fetch-agentcore-doc
description: Fetch full document content by URL.

    Retrieves complete AgentCore documentation content from URLs found via search_agentcore_docs
    or provided directly. Use this to get full documentation pages including:

    - Complete platform overview and service documentation
    - Detailed getting started guides with step-by-step instructions
    - Full API reference documentation
    - Comprehensive tutorial and example code
    - Complete deployment and configuration instructions
    - Integration guides for various frameworks (Strands, LangGraph, CrewAI, etc.)

    This provides the full content when search snippets aren't sufficient for
    understanding or implementing AgentCore features.

    Args:
        uri: Document URI (supports http/https URLs)

    Returns:
        Dictionary containing:
        - url: Canonical document URL
        - title: Document title
        - content: Full document text content
        - error: Error message (if fetch failed)

    
---

# Fetch Agentcore Doc

Fetch full document content by URL.

    Retrieves complete AgentCore documentation content from URLs found via search_agentcore_docs
    or provided directly. Use this to get full documentation pages including:

    - Complete platform overview and service documentation
    - Detailed getting started guides with step-by-step instructions
    - Full API reference documentation
    - Comprehensive tutorial and example code
    - Complete deployment and configuration instructions
    - Integration guides for various frameworks (Strands, LangGraph, CrewAI, etc.)

    This provides the full content when search snippets aren't sufficient for
    understanding or implementing AgentCore features.

    Args:
        uri: Document URI (supports http/https URLs)

    Returns:
        Dictionary containing:
        - url: Canonical document URL
        - title: Document title
        - content: Full document text content
        - error: Error message (if fetch failed)

    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `uri` | string | Yes |  |

