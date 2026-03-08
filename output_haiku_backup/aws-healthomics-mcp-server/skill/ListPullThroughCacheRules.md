---
name: ListPullThroughCacheRules
description: List pull-through cache rules with HealthOmics usability status.

    Lists all ECR pull-through cache rules in the current region and evaluates
    each rule's usability by HealthOmics. A pull-through cache is usable by
    HealthOmics if:
    1. The registry permissions policy grants HealthOmics the required permissions
    2. A repository creation template exists for the prefix
    3. The template grants HealthOmics the required image pull permissions

    Args:
        ctx: MCP context for error reporting
        max_results: Maximum number of results to return (default: 100, max: 1000)
        next_token: Pagination token from a previous response

    Returns:
        Dictionary containing:
        - rules: List of pull-through cache rules with usability status
        - next_token: Pagination token if more results are available
    
---

# Listpullthroughcacherules

List pull-through cache rules with HealthOmics usability status.

    Lists all ECR pull-through cache rules in the current region and evaluates
    each rule's usability by HealthOmics. A pull-through cache is usable by
    HealthOmics if:
    1. The registry permissions policy grants HealthOmics the required permissions
    2. A repository creation template exists for the prefix
    3. The template grants HealthOmics the required image pull permissions

    Args:
        ctx: MCP context for error reporting
        max_results: Maximum number of results to return (default: 100, max: 1000)
        next_token: Pagination token from a previous response

    Returns:
        Dictionary containing:
        - rules: List of pull-through cache rules with usability status
        - next_token: Pagination token if more results are available
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Pagination token from a previous response |

## AWS CLI

```bash
aws ecr describe-pull-through-cache-rules --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('ecr')
response = client.describe_pull_through_cache_rules(
    MaxResults=max_results,
    NextToken=next_token,
)
```
