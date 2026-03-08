---
name: create-api-cache
description: Creates a cache for the GraphQL API.

        This operation creates an API cache for the specified GraphQL API. Caching improves
        performance by storing frequently requested data and reducing the number of requests
        to data sources.
        
---

# Create Api Cache

Creates a cache for the GraphQL API.

        This operation creates an API cache for the specified GraphQL API. Caching improves
        performance by storing frequently requested data and reducing the number of requests
        to data sources.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `api_id` | string | Yes | The GraphQL API ID |
| `ttl` | integer | Yes | TTL in seconds for entries in the API cache. Valid values are 1-3600 seconds |
| `api_caching_behavior` | string | Yes | Caching behavior. Valid values: FULL_REQUEST_CACHING, PER_RESOLVER_CACHING |
| `type` | string | Yes | The cache instance type. Valid values: SMALL, MEDIUM, LARGE, XLARGE, LARGE_2X, LARGE_4X, LARGE_8X, LARGE_12X |
| `transit_encryption_enabled` | string | No | Transit encryption flag when connecting to cache |
| `at_rest_encryption_enabled` | string | No | At-rest encryption flag for cache |
| `health_metrics_config` | string | No | The health metrics configuration. Valid values: ENABLED, DISABLED |

## AWS CLI

```bash
aws appsync update-api-cache --api-id <api_id> --ttl <ttl> --api-caching-behavior <api_caching_behavior> --type <type> --transit-encryption-enabled <transit_encryption_enabled> --at-rest-encryption-enabled <at_rest_encryption_enabled> --health-metrics-config <health_metrics_config>
```

## boto3

```python
import boto3

client = boto3.client('appsync')
response = client.update_api_cache(
    ApiId=api_id,
    Ttl=ttl,
    ApiCachingBehavior=api_caching_behavior,
    Type=type,
    TransitEncryptionEnabled=transit_encryption_enabled,
    AtRestEncryptionEnabled=at_rest_encryption_enabled,
    HealthMetricsConfig=health_metrics_config,
)
```
