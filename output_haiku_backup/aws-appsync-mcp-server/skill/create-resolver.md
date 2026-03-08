---
name: create-resolver
description: Creates a resolver for a GraphQL field in an AppSync API.

        A resolver is the bridge between your GraphQL schema and your data sources.
        It defines how to fetch or modify data for a specific field in your schema.
        Resolvers can be unit resolvers (attached to a single data source) or
        pipeline resolvers (composed of multiple functions).
        
---

# Create Resolver

Creates a resolver for a GraphQL field in an AppSync API.

        A resolver is the bridge between your GraphQL schema and your data sources.
        It defines how to fetch or modify data for a specific field in your schema.
        Resolvers can be unit resolvers (attached to a single data source) or
        pipeline resolvers (composed of multiple functions).
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `api_id` | string | Yes | The API ID for the GraphQL API |
| `type_name` | string | Yes | The name of the type (e.g., Query, Mutation, Subscription) |
| `field_name` | string | Yes | The name of the field to attach the resolver to |
| `data_source_name` | string | No | The name of the data source (required for unit resolvers) |
| `request_mapping_template` | string | No | The request mapping template in VTL (Velocity Template Language) |
| `response_mapping_template` | string | No | The response mapping template in VTL (Velocity Template Language) |
| `kind` | string | No | The resolver kind: UNIT or PIPELINE |
| `pipeline_config` | string | No | Pipeline configuration for PIPELINE resolvers with functions list |
| `sync_config` | string | No | Sync configuration for conflict resolution |
| `caching_config` | string | No | Caching configuration for the resolver |
| `max_batch_size` | string | No | Maximum batch size for batch operations |
| `runtime` | string | No | Runtime configuration (name and runtimeVersion) |
| `code` | string | No | The resolver code for JavaScript/TypeScript resolvers |
| `metrics_config` | string | No | Metrics configuration: ENABLED or DISABLED |

## AWS CLI

```bash
aws appsync create-resolver --api-id <api_id> --type-name <type_name> --field-name <field_name> --data-source-name <data_source_name> --request-mapping-template <request_mapping_template> --response-mapping-template <response_mapping_template> --kind <kind> --pipeline-config <pipeline_config> --sync-config <sync_config> --caching-config <caching_config> --max-batch-size <max_batch_size> --runtime <runtime> --code <code> --metrics-config <metrics_config>
```

## boto3

```python
import boto3

client = boto3.client('appsync')
response = client.create_resolver(
    ApiId=api_id,
    TypeName=type_name,
    FieldName=field_name,
    DataSourceName=data_source_name,
    RequestMappingTemplate=request_mapping_template,
    ResponseMappingTemplate=response_mapping_template,
    Kind=kind,
    PipelineConfig=pipeline_config,
    SyncConfig=sync_config,
    CachingConfig=caching_config,
    MaxBatchSize=max_batch_size,
    Runtime=runtime,
    Code=code,
    MetricsConfig=metrics_config,
)
```
