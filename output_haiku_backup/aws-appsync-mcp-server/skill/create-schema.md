---
name: create-schema
description: Creates a GraphQL schema for an AppSync API and polls until completion.

        This tool starts the schema creation process and automatically polls for the status
        until the operation completes (either SUCCESS or FAILED). The schema defines the
        structure of your GraphQL API, including types, queries, mutations, and subscriptions.
        
---

# Create Schema

Creates a GraphQL schema for an AppSync API and polls until completion.

        This tool starts the schema creation process and automatically polls for the status
        until the operation completes (either SUCCESS or FAILED). The schema defines the
        structure of your GraphQL API, including types, queries, mutations, and subscriptions.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `api_id` | string | Yes | The API ID for the GraphQL API |
| `definition` | string | Yes | The schema definition in GraphQL Schema Definition Language (SDL) |

## AWS CLI

```bash
aws appsync update-graphql-api --api-id <api_id> --definition <definition>
```

## boto3

```python
import boto3

client = boto3.client('appsync')
response = client.update_graphql_api(
    ApiId=api_id,
    Definition=definition,
)
```
