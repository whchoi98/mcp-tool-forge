---
name: ListAHOReferenceStores
description: List HealthOmics reference stores.

    Args:
        ctx: MCP context for error reporting
        name_filter: Filter stores by name
        max_results: Maximum number of results to return
        next_token: Token for pagination

    Returns:
        Dictionary containing reference store list and optional next token
    
---

# Listahoreferencestores

List HealthOmics reference stores.

    Args:
        ctx: MCP context for error reporting
        name_filter: Filter stores by name
        max_results: Maximum number of results to return
        next_token: Token for pagination

    Returns:
        Dictionary containing reference store list and optional next token
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name_filter` | string | No | Filter stores by name |
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Token for pagination from a previous response |

## AWS CLI

```bash
aws omics list-reference-stores --max-results <max_results> --next-token <next_token> --filter <name_filter>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_reference_stores(
    MaxResults=max_results,
    NextToken=next_token,
    Filter=name_filter,
)
```
