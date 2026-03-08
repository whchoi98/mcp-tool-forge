---
name: create-graphql-api
description: Creates a GraphQL API.

        This operation creates a new GraphQL API with the specified configuration.
        The API will be created with the authentication type and other settings provided.
        Supports various authentication types including API_KEY, AWS_IAM, AMAZON_COGNITO_USER_POOLS,
        OPENID_CONNECT, and AWS_LAMBDA.

        When authentication_type is API_KEY, an API key is automatically created with a 7-day expiry.
        
---

# Create Graphql Api

Creates a GraphQL API.

        This operation creates a new GraphQL API with the specified configuration.
        The API will be created with the authentication type and other settings provided.
        Supports various authentication types including API_KEY, AWS_IAM, AMAZON_COGNITO_USER_POOLS,
        OPENID_CONNECT, and AWS_LAMBDA.

        When authentication_type is API_KEY, an API key is automatically created with a 7-day expiry.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | string | Yes | A user-supplied name for the GraphQL API |
| `authentication_type` | string | Yes | The authentication type: API_KEY, AWS_IAM, AMAZON_COGNITO_USER_POOLS, OPENID_CONNECT, AWS_LAMBDA |
| `log_config` | string | No | The Amazon CloudWatch Logs configuration |
| `user_pool_config` | string | No | The Amazon Cognito user pool configuration |
| `open_id_connect_config` | string | No | The OpenID Connect configuration |
| `tags` | string | No | A TagMap object |
| `additional_authentication_providers` | string | No | A list of additional authentication providers |
| `xray_enabled` | string | No | A flag indicating whether to enable X-Ray tracing |
| `lambda_authorizer_config` | string | No | Configuration for AWS Lambda function authorization |
| `visibility` | string | No | Sets the value of the GraphQL API to public (GLOBAL) or private (PRIVATE) |
| `api_type` | string | No | The value that indicates whether the GraphQL API is a standard API (GRAPHQL) or merged API (MERGED) |
| `merged_api_execution_role_arn` | string | No | The Identity and Access Management service role ARN for a merged API |
| `owner_contact` | string | No | The owner contact information for an API resource |
| `introspection_config` | string | No | Sets the value of the GraphQL API to enable (ENABLED) or disable (DISABLED) introspection |
| `query_depth_limit` | string | No | The maximum depth a query can have in a single request |
| `resolver_count_limit` | string | No | The maximum number of resolvers that can be invoked in a single request |
| `enhanced_metrics_config` | string | No | The enhancedMetricsConfig object |

