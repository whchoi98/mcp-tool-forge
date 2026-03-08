---
name: QBusinessQueryTool
description: MCP tool to query Amazon Q Business and return a formatted response.

    This tool provides a Model Context Protocol interface for querying Amazon Q Business.
    It handles client initialization, query execution, and error handling automatically.

    Args:
        query (str): The question or query to send to Q Business

    Returns:
        str: Formatted response from Q Business or error message if the query fails

    Examples:
        >>> qbiz_local_query('What is our company policy on remote work?')
        "Qbiz response: According to company policy..."

        >>> qbiz_local_query('')
        "Error: Query cannot be empty"

    Note:
        Requires the following environment variables to be set:
        - AWS_REGION: AWS region where Q Business is deployed
        - QBUSINESS_APPLICATION_ID: ID of the Q Business application
        - AWS credentials must be configured (via AWS CLI, IAM roles, etc.)
    
---

# Qbusinessquerytool

MCP tool to query Amazon Q Business and return a formatted response.

    This tool provides a Model Context Protocol interface for querying Amazon Q Business.
    It handles client initialization, query execution, and error handling automatically.

    Args:
        query (str): The question or query to send to Q Business

    Returns:
        str: Formatted response from Q Business or error message if the query fails

    Examples:
        >>> qbiz_local_query('What is our company policy on remote work?')
        "Qbiz response: According to company policy..."

        >>> qbiz_local_query('')
        "Error: Query cannot be empty"

    Note:
        Requires the following environment variables to be set:
        - AWS_REGION: AWS region where Q Business is deployed
        - QBUSINESS_APPLICATION_ID: ID of the Q Business application
        - AWS credentials must be configured (via AWS CLI, IAM roles, etc.)
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes | User query, question or request to the Amazon Q Business application |

## AWS CLI

```bash
aws qbusiness chat --query <query>
```

## boto3

```python
import boto3

client = boto3.client('qbusiness')
response = client.chat(
    Query=query,
)
```
