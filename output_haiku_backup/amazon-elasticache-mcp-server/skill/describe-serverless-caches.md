---
name: describe-serverless-caches
description: Describe Amazon ElastiCache serverless caches in your AWS account.

    This tool retrieves detailed information about serverless caches including:
    - Cache configuration
    - Cache endpoints
    - Cache status
    - Cache size
    - Cache connections

    Parameters:
        serverless_cache_name (Optional[str]): Name of the serverless cache to describe. If not provided, describes all caches.
        max_items (Optional[int]): Maximum number of results to return.
        starting_token (Optional[str]): Token to start the list from a specific page.
        page_size (Optional[int]): Number of records to include in each page.

    Returns:
        Dict containing information about the serverless cache(s).
    
---

# Describe-Serverless-Caches

Describe Amazon ElastiCache serverless caches in your AWS account.

    This tool retrieves detailed information about serverless caches including:
    - Cache configuration
    - Cache endpoints
    - Cache status
    - Cache size
    - Cache connections

    Parameters:
        serverless_cache_name (Optional[str]): Name of the serverless cache to describe. If not provided, describes all caches.
        max_items (Optional[int]): Maximum number of results to return.
        starting_token (Optional[str]): Token to start the list from a specific page.
        page_size (Optional[int]): Number of records to include in each page.

    Returns:
        Dict containing information about the serverless cache(s).
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serverless_cache_name` | string | No |  |
| `max_items` | string | No |  |
| `starting_token` | string | No |  |
| `page_size` | string | No |  |

## AWS CLI

```bash
aws elasticache describe-serverless-caches --serverless-cache-name <serverless_cache_name> --max-results <max_items> --next-token <starting_token> --max-records <page_size>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.describe_serverless_caches(
    ServerlessCacheName=serverless_cache_name,
    MaxResults=max_items,
    NextToken=starting_token,
    MaxRecords=page_size,
)
```
