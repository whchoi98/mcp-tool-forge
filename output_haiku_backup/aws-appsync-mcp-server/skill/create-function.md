---
name: create-function
description: Creates a Function object for a GraphQL API.

        This operation creates a function for the specified GraphQL API. Functions
        are reusable pieces of resolver logic that can be attached to multiple fields
        in your GraphQL schema.
        
---

# Create Function

Creates a Function object for a GraphQL API.

        This operation creates a function for the specified GraphQL API. Functions
        are reusable pieces of resolver logic that can be attached to multiple fields
        in your GraphQL schema.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `api_id` | string | Yes | The GraphQL API ID |
| `name` | string | Yes | The Function name |
| `data_source_name` | string | Yes | The Function DataSource name |
| `description` | string | No | The Function description |
| `request_mapping_template` | string | No | The Function request mapping template |
| `response_mapping_template` | string | No | The Function response mapping template |
| `function_version` | string | No | The version of the request mapping template. Currently, the supported value is 2018-05-29 |
| `sync_config` | string | No | Describes a Sync configuration for a resolver |
| `max_batch_size` | string | No | The maximum batching size for a resolver |
| `runtime` | string | No | Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function |
| `code` | string | No | The function code that contains the request and response functions |

## AWS CLI

```bash
aws appsync create-function --api-id <api_id> --name <name> --data-source-name <data_source_name> --description <description> --request-mapping-template <request_mapping_template> --response-mapping-template <response_mapping_template> --function-version <function_version> --sync-config <sync_config> --max-batch-size <max_batch_size> --runtime <runtime> --code <code>
```

## boto3

```python
import boto3

client = boto3.client('appsync')
response = client.create_function(
    ApiId=api_id,
    Name=name,
    DataSourceName=data_source_name,
    Description=description,
    RequestMappingTemplate=request_mapping_template,
    ResponseMappingTemplate=response_mapping_template,
    FunctionVersion=function_version,
    SyncConfig=sync_config,
    MaxBatchSize=max_batch_size,
    Runtime=runtime,
    Code=code,
)
```
