---
name: search-repos-on-github
description: Search for GitHub repositories based on keywords, scoped to specific organizations.

    This tool searches for GitHub repositories using the GitHub REST/GraphQL APIs, scoped to specific GitHub
    organizations (aws-samples, aws-solutions-library-samples, and awslabs).

    Results are filtered to only include repositories with specific licenses (Apache License 2.0,
    MIT, and MIT No Attribution) and are sorted by stars (descending) and then by updated date.

    For higher rate limits, you can set the GITHUB_TOKEN environment variable with a GitHub
    personal access token. Without a token, the API is limited to 60 requests per hour, and requests are
    made with the REST API. With a token, this increases to 5,000 requests per hour, and requests are made
    with the GraphQL API.

    Args:
        ctx: MCP context object used for error reporting
        keywords: List of keywords to search for
        num_results: Number of results to return

    Returns:
        List of GitHub repositories matching the search criteria
    
---

# Search Repos On Github

Search for GitHub repositories based on keywords, scoped to specific organizations.

    This tool searches for GitHub repositories using the GitHub REST/GraphQL APIs, scoped to specific GitHub
    organizations (aws-samples, aws-solutions-library-samples, and awslabs).

    Results are filtered to only include repositories with specific licenses (Apache License 2.0,
    MIT, and MIT No Attribution) and are sorted by stars (descending) and then by updated date.

    For higher rate limits, you can set the GITHUB_TOKEN environment variable with a GitHub
    personal access token. Without a token, the API is limited to 60 requests per hour, and requests are
    made with the REST API. With a token, this increases to 5,000 requests per hour, and requests are made
    with the GraphQL API.

    Args:
        ctx: MCP context object used for error reporting
        keywords: List of keywords to search for
        num_results: Number of results to return

    Returns:
        List of GitHub repositories matching the search criteria
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keywords` | array | Yes | List of keywords to search for GitHub repositories |
| `num_results` | integer | No | Number of results to return |

