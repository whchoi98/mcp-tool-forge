---
name: GetReactDocsByTopic
description: Get specific AWS web application UI setup documentation by topic.

    Parameters:
        topic: The topic of React documentation to retrieve.
          - "essential-knowledge": Essential knowledge for working with React applications.
          - "troubleshooting": Common issues and solutions when generating code.

    Returns:
        A markdown string containing the requested documentation
    
---

# Getreactdocsbytopic

Get specific AWS web application UI setup documentation by topic.

    Parameters:
        topic: The topic of React documentation to retrieve.
          - "essential-knowledge": Essential knowledge for working with React applications.
          - "troubleshooting": Common issues and solutions when generating code.

    Returns:
        A markdown string containing the requested documentation
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `topic` | string | Yes | The topic of React documentation to retrieve. Topics include: essential-knowledge, troubleshooting. |

