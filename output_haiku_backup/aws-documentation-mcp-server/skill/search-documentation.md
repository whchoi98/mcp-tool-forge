---
name: search-documentation
description: Search AWS documentation using the official AWS Documentation Search API.

    ## Usage

    This tool searches across all AWS documentation for pages matching your search phrase.
    Use it to find relevant documentation when you don't have a specific URL.

    ## Search Tips

    - Use specific technical terms rather than general phrases
    - Include service names to narrow results (e.g., "S3 bucket versioning" instead of just "versioning")
    - Use quotes for exact phrase matching (e.g., "AWS Lambda function URLs")
    - Include abbreviations and alternative terms to improve results
    - Use guide_type and product_type filters found from a SearchResponse's "facets" property:
        - Filter only for broad search queries with patterns:
            - "What is [service]?" -> product_types: ["Amazon Simple Storage Service"]
            - "How to use <service 1> with <service 2>?" -> product_types: [<service 1>, <service 2>]
            - "[service] getting started" -> product_types: [<service>] + guide_types: ["User Guide, "Developer Guide"]
            - "API reference for [service]" -> product_types: [<service>] + guide_types: ["API Reference"]

    ## Result Interpretation

    Each SearchResponse includes:
    - search_results: List of documentation pages, each with:
        - rank_order: The relevance ranking (lower is more relevant)
        - url: The documentation page URL
        - title: The page title
        - context: A brief excerpt or summary (if available)
    - facets: Available filters (product_types, guide_types) for refining searches
    - query_id: Unique identifier for this search session


    Args:
        ctx: MCP context for logging and error handling
        search_phrase: Search phrase to use
        search_intent: The intent behind the search requested by the user
        limit: Maximum number of results to return
        product_types: Filter by AWS product/service
        guide_types: Filter by guide type

    Returns:
        List of search results with URLs, titles, query ID, context snippets, and facets for filtering
    
---

# Search Documentation

Search AWS documentation using the official AWS Documentation Search API.

    ## Usage

    This tool searches across all AWS documentation for pages matching your search phrase.
    Use it to find relevant documentation when you don't have a specific URL.

    ## Search Tips

    - Use specific technical terms rather than general phrases
    - Include service names to narrow results (e.g., "S3 bucket versioning" instead of just "versioning")
    - Use quotes for exact phrase matching (e.g., "AWS Lambda function URLs")
    - Include abbreviations and alternative terms to improve results
    - Use guide_type and product_type filters found from a SearchResponse's "facets" property:
        - Filter only for broad search queries with patterns:
            - "What is [service]?" -> product_types: ["Amazon Simple Storage Service"]
            - "How to use <service 1> with <service 2>?" -> product_types: [<service 1>, <service 2>]
            - "[service] getting started" -> product_types: [<service>] + guide_types: ["User Guide, "Developer Guide"]
            - "API reference for [service]" -> product_types: [<service>] + guide_types: ["API Reference"]

    ## Result Interpretation

    Each SearchResponse includes:
    - search_results: List of documentation pages, each with:
        - rank_order: The relevance ranking (lower is more relevant)
        - url: The documentation page URL
        - title: The page title
        - context: A brief excerpt or summary (if available)
    - facets: Available filters (product_types, guide_types) for refining searches
    - query_id: Unique identifier for this search session


    Args:
        ctx: MCP context for logging and error handling
        search_phrase: Search phrase to use
        search_intent: The intent behind the search requested by the user
        limit: Maximum number of results to return
        product_types: Filter by AWS product/service
        guide_types: Filter by guide type

    Returns:
        List of search results with URLs, titles, query ID, context snippets, and facets for filtering
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `search_phrase` | string | Yes | Search phrase to use |
| `search_intent` | string | No | For the search_phrase parameter, describe the search intent of the user. CRITICAL: Do not include any PII or customer data, describe only the AWS-related intent for search. |
| `limit` | integer | No | Maximum number of results to return |
| `product_types` | string | No | Filter results by AWS product/service (e.g., ["Amazon Simple Storage Service"]) |
| `guide_types` | string | No | Filter results by guide type (e.g., ["User Guide", "API Reference", "Developer Guide"]) |

