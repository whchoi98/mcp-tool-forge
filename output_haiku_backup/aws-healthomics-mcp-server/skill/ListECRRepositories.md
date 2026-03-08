---
name: ListECRRepositories
description: List ECR repositories with HealthOmics accessibility status.

    Lists all ECR repositories in the current region and checks each repository's
    policy to determine if HealthOmics has the required permissions to pull images.

    Args:
        ctx: MCP context for error reporting
        max_results: Maximum number of results to return (default: 100, max: 1000)
        next_token: Pagination token from a previous response
        filter_healthomics_accessible: If True, only return repositories that are
            accessible by HealthOmics

    Returns:
        Dictionary containing:
        - repositories: List of ECR repositories with accessibility status
        - next_token: Pagination token if more results are available
        - total_count: Total number of repositories returned
    
---

# Listecrrepositories

List ECR repositories with HealthOmics accessibility status.

    Lists all ECR repositories in the current region and checks each repository's
    policy to determine if HealthOmics has the required permissions to pull images.

    Args:
        ctx: MCP context for error reporting
        max_results: Maximum number of results to return (default: 100, max: 1000)
        next_token: Pagination token from a previous response
        filter_healthomics_accessible: If True, only return repositories that are
            accessible by HealthOmics

    Returns:
        Dictionary containing:
        - repositories: List of ECR repositories with accessibility status
        - next_token: Pagination token if more results are available
        - total_count: Total number of repositories returned
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Pagination token from a previous response |
| `filter_healthomics_accessible` | boolean | No | Only return repositories accessible by HealthOmics |

