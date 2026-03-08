---
name: search-agentcore-docs
description: Search curated AgentCore documentation and return ranked results with snippets.

    This tool provides access to the complete Amazon Bedrock AgentCore documentation including:

    **Platform Overview:**
    - What is Bedrock AgentCore, security overview, quotas and limits

    **Platform Services:**
    - AgentCore Runtime (serverless deployment and scaling)
    - AgentCore Memory (persistent knowledge with event and semantic memory)
    - AgentCore Code Interpreter (secure code execution in isolated sandboxes)
    - AgentCore Browser (fast, secure cloud-based browser for web interaction)
    - AgentCore Gateway (transform existing APIs into agent tools)
    - AgentCore Observability (real-time monitoring and tracing)
    - AgentCore Identity (secure authentication and access management)

    **Getting Started:**
    - Prerequisites & environment setup
    - Building your first agent or transforming existing code
    - Local development & testing
    - Deployment to AgentCore using CLI
    - Troubleshooting & enhancement

    **Examples & Tutorials:**
    - Basic agent creation, memory integration, tool usage
    - Streaming responses, error handling, authentication
    - Customer service agents, code review assistants, data analysis
    - Multi-agent workflows and integrations

    **API Reference:**
    - Data plane and control API documentation

    Use this to find relevant AgentCore documentation for any development question.

    Args:
        query: Search query string (e.g., "bedrock agentcore", "memory integration", "deployment guide")
        k: Maximum number of results to return (default: 5)

    Returns:
        List of dictionaries containing:
        - url: Document URL
        - title: Display title
        - score: Relevance score (0-1, higher is better)
        - snippet: Contextual content preview

    
---

# Search Agentcore Docs

Search curated AgentCore documentation and return ranked results with snippets.

    This tool provides access to the complete Amazon Bedrock AgentCore documentation including:

    **Platform Overview:**
    - What is Bedrock AgentCore, security overview, quotas and limits

    **Platform Services:**
    - AgentCore Runtime (serverless deployment and scaling)
    - AgentCore Memory (persistent knowledge with event and semantic memory)
    - AgentCore Code Interpreter (secure code execution in isolated sandboxes)
    - AgentCore Browser (fast, secure cloud-based browser for web interaction)
    - AgentCore Gateway (transform existing APIs into agent tools)
    - AgentCore Observability (real-time monitoring and tracing)
    - AgentCore Identity (secure authentication and access management)

    **Getting Started:**
    - Prerequisites & environment setup
    - Building your first agent or transforming existing code
    - Local development & testing
    - Deployment to AgentCore using CLI
    - Troubleshooting & enhancement

    **Examples & Tutorials:**
    - Basic agent creation, memory integration, tool usage
    - Streaming responses, error handling, authentication
    - Customer service agents, code review assistants, data analysis
    - Multi-agent workflows and integrations

    **API Reference:**
    - Data plane and control API documentation

    Use this to find relevant AgentCore documentation for any development question.

    Args:
        query: Search query string (e.g., "bedrock agentcore", "memory integration", "deployment guide")
        k: Maximum number of results to return (default: 5)

    Returns:
        List of dictionaries containing:
        - url: Document URL
        - title: Display title
        - score: Relevance score (0-1, higher is better)
        - snippet: Contextual content preview

    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes |  |
| `k` | integer | No |  |

## AWS CLI

```bash
aws bedrock-agent search-knowledge-base --knowledge-base-id <agentcore-docs> --search-query <query> --max-results <k>
```

## boto3

```python
import boto3

client = boto3.client('bedrock-agent')
response = client.search_knowledge_base(
    KnowledgeBaseId=agentcore-docs,
    SearchQuery=query,
    MaxResults=k,
)
```
