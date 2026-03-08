---
name: ListCodeConnections
description: List available CodeConnections.

    This function retrieves existing CodeConnections that can be used with
    HealthOmics workflows. Connections can be filtered by provider type and
    results are paginated.

    Args:
        ctx: MCP context for error reporting
        provider_type_filter: Optional filter by Git provider type
        max_results: Maximum number of results to return (default: 100)
        next_token: Token for pagination from a previous response

    Returns:
        Dictionary containing:
        - connections: List of connection objects with connection_arn, connection_name,
          connection_status, provider_type, and ready_for_workflows flag
        - nextToken: Token for retrieving the next page (if more results exist)

    Raises:
        ValueError: If provider_type_filter is invalid
        botocore.exceptions.BotoCoreError: If AWS API call fails
    
---

# Listcodeconnections

List available CodeConnections.

    This function retrieves existing CodeConnections that can be used with
    HealthOmics workflows. Connections can be filtered by provider type and
    results are paginated.

    Args:
        ctx: MCP context for error reporting
        provider_type_filter: Optional filter by Git provider type
        max_results: Maximum number of results to return (default: 100)
        next_token: Token for pagination from a previous response

    Returns:
        Dictionary containing:
        - connections: List of connection objects with connection_arn, connection_name,
          connection_status, provider_type, and ready_for_workflows flag
        - nextToken: Token for retrieving the next page (if more results exist)

    Raises:
        ValueError: If provider_type_filter is invalid
        botocore.exceptions.BotoCoreError: If AWS API call fails
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `provider_type_filter` | string | No | Filter by provider type: Bitbucket, GitHub, GitHubEnterpriseServer, GitLab, GitLabSelfManaged |
| `max_results` | integer | No | Maximum number of results to return |
| `next_token` | string | No | Token for pagination from a previous response |

## AWS CLI

```bash
aws codeconnections list-connections --provider-type-filter <provider_type_filter> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('codeconnections')
response = client.list_connections(
    ProviderTypeFilter=provider_type_filter,
    MaxResults=max_results,
    NextToken=next_token,
)
```
