---
name: CreateAHORunCache
description: Create a new HealthOmics run cache.

    Args:
        ctx: MCP context for error reporting
        cache_behavior: Cache behavior (CACHE_ALWAYS or CACHE_ON_FAILURE)
        cache_s3_location: S3 URI for cache storage (e.g., s3://bucket/prefix)
        name: Name for the run cache
        description: Description for the run cache
        tags: Tags to apply to the run cache
        cache_bucket_owner_id: AWS account ID of the S3 bucket owner

    Returns:
        Dictionary containing the created run cache's id, arn, and status, or error dict
    
---

# Createahoruncache

Create a new HealthOmics run cache.

    Args:
        ctx: MCP context for error reporting
        cache_behavior: Cache behavior (CACHE_ALWAYS or CACHE_ON_FAILURE)
        cache_s3_location: S3 URI for cache storage (e.g., s3://bucket/prefix)
        name: Name for the run cache
        description: Description for the run cache
        tags: Tags to apply to the run cache
        cache_bucket_owner_id: AWS account ID of the S3 bucket owner

    Returns:
        Dictionary containing the created run cache's id, arn, and status, or error dict
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cache_behavior` | string | Yes | Cache behavior (CACHE_ALWAYS or CACHE_ON_FAILURE) |
| `cache_s3_location` | string | Yes | S3 URI for cache storage (e.g., s3://bucket/prefix) |
| `name` | string | No | Name for the run cache |
| `description` | string | No | Description for the run cache |
| `tags` | string | No | Tags to apply to the run cache |
| `cache_bucket_owner_id` | string | No | AWS account ID of the S3 bucket owner for cross-account access |

## AWS CLI

```bash
aws omics create-run-cache --cache-behavior <cache_behavior> --s3-location <cache_s3_location> --name <name> --description <description> --tags <tags> --cache-bucket-owner-id <cache_bucket_owner_id>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.create_run_cache(
    CacheBehavior=cache_behavior,
    S3Location=cache_s3_location,
    Name=name,
    Description=description,
    Tags=tags,
    CacheBucketOwnerId=cache_bucket_owner_id,
)
```
