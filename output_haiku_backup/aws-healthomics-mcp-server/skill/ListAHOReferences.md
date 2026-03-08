---
name: ListAHOReferences
description: List references in a HealthOmics reference store with optional filtering.

    AWS HealthOmics allows only one reference store per account per region.
    If reference_store_id is not provided, it will be automatically resolved.

    Args:
        ctx: MCP context for error reporting
        reference_store_id: The ID of the reference store (auto-resolved if omitted)
        name_filter: Filter references by name
        status_filter: Filter references by status
        max_results: Maximum number of results to return
        next_token: Token for pagination

    Returns:
        Dictionary containing reference list and optional next token
    
---

# Listahoreferences

List references in a HealthOmics reference store with optional filtering.

    AWS HealthOmics allows only one reference store per account per region.
    If reference_store_id is not provided, it will be automatically resolved.

    Args:
        ctx: MCP context for error reporting
        reference_store_id: The ID of the reference store (auto-resolved if omitted)
        name_filter: Filter references by name
        status_filter: Filter references by status
        max_results: Maximum number of results to return
        next_token: Token for pagination

    Returns:
        Dictionary containing reference list and optional next token
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `reference_store_id` | string | No | The ID of the reference store. If not provided, auto-resolves the single store in the account/region. |
| `name_filter` | string | No | Filter references by name |
| `status_filter` | string | No | Filter references by status (e.g., ACTIVE, DELETING) |
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Token for pagination from a previous response |

## AWS CLI

```bash
aws omics list-references --reference-store-id <reference_store_id> --name <name_filter> --status <status_filter> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_references(
    ReferenceStoreId=reference_store_id,
    Name=name_filter,
    Status=status_filter,
    MaxResults=max_results,
    NextToken=next_token,
)
```
