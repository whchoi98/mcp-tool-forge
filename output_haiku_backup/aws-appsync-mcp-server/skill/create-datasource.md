---
name: create-datasource
description: Creates a DataSource object for a GraphQL API.

        This operation creates a data source for the specified GraphQL API. Data sources
        connect your GraphQL API to various backend services like DynamoDB, Lambda,
        HTTP endpoints, and more.
        
---

# Create Datasource

Creates a DataSource object for a GraphQL API.

        This operation creates a data source for the specified GraphQL API. Data sources
        connect your GraphQL API to various backend services like DynamoDB, Lambda,
        HTTP endpoints, and more.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `api_id` | string | Yes | The API ID for the GraphQL API for the DataSource |
| `name` | string | Yes | A user-supplied name for the DataSource |
| `type` | string | Yes | The type of the DataSource. Valid values: AWS_LAMBDA, AMAZON_DYNAMODB, AMAZON_ELASTICSEARCH, HTTP, NONE, RELATIONAL_DATABASE, AMAZON_EVENTBRIDGE, AMAZON_OPENSEARCH_SERVICE |
| `description` | string | No | A description of the DataSource |
| `service_role_arn` | string | No | The AWS IAM service role ARN for the data source. Format: arn:aws:iam::ACCOUNT-ID:role/ROLE-NAME |
| `dynamodb_config` | string | No | Amazon DynamoDB settings |
| `lambda_config` | string | No | AWS Lambda settings |
| `elasticsearch_config` | string | No | Amazon OpenSearch Service settings |
| `open_search_service_config` | string | No | Amazon OpenSearch Service settings |
| `http_config` | string | No | HTTP endpoint settings |
| `relational_database_config` | string | No | Relational database settings |
| `event_bridge_config` | string | No | Amazon EventBridge settings |
| `metrics_config` | string | No | Enables or disables enhanced DataSource metrics. Valid values: ENABLED, DISABLED |

## AWS CLI

```bash
aws appsync create-data-source --api-id <api_id> --name <name> --type <type> --description <description> --service-role-arn <service_role_arn> --dynamodb-config <dynamodb_config> --lambda-config <lambda_config> --elasticsearch-config <elasticsearch_config> --open-search-service-config <open_search_service_config> --http-config <http_config> --relational-database-config <relational_database_config> --event-bridge-config <event_bridge_config> --metrics-config <metrics_config>
```

## boto3

```python
import boto3

client = boto3.client('appsync')
response = client.create_data_source(
    ApiId=api_id,
    Name=name,
    Type=type,
    Description=description,
    ServiceRoleArn=service_role_arn,
    DynamodbConfig=dynamodb_config,
    LambdaConfig=lambda_config,
    ElasticsearchConfig=elasticsearch_config,
    OpenSearchServiceConfig=open_search_service_config,
    HttpConfig=http_config,
    RelationalDatabaseConfig=relational_database_config,
    EventBridgeConfig=event_bridge_config,
    MetricsConfig=metrics_config,
)
```
