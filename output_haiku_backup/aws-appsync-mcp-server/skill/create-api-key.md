---
name: create-api-key
description: Creates a unique key that you can distribute to clients who invoke your API.

        This operation creates an API key for the specified GraphQL API. API keys are used
        to authenticate requests when the API uses API_KEY authentication type.
        
---

# Create Api Key

Creates a unique key that you can distribute to clients who invoke your API.

        This operation creates an API key for the specified GraphQL API. API keys are used
        to authenticate requests when the API uses API_KEY authentication type.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `api_id` | string | Yes | The ID for the GraphQL API |
| `description` | string | No | A description of the purpose of the API key |
| `expires` | string | No | From the creation time, the time after which the API key expires (Unix timestamp) |

## AWS CLI

```bash
aws appsync create-api-key --api-id <api_id> --description <description> --expires <expires>
```

## boto3

```python
import boto3

client = boto3.client('appsync')
response = client.create_api_key(
    ApiId=api_id,
    Description=description,
    Expires=expires,
)
```
