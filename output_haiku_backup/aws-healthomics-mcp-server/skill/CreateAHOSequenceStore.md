---
name: CreateAHOSequenceStore
description: Create a new HealthOmics sequence store.

    Args:
        ctx: MCP context for error reporting
        name: Name for the new sequence store
        description: Optional description for the sequence store
        sse_kms_key_arn: KMS key ARN for server-side encryption
        fallback_location: S3 URI for the fallback location
        tags: Tags as a JSON string or dict

    Returns:
        Dictionary containing the created sequence store information
    
---

# Createahosequencestore

Create a new HealthOmics sequence store.

    Args:
        ctx: MCP context for error reporting
        name: Name for the new sequence store
        description: Optional description for the sequence store
        sse_kms_key_arn: KMS key ARN for server-side encryption
        fallback_location: S3 URI for the fallback location
        tags: Tags as a JSON string or dict

    Returns:
        Dictionary containing the created sequence store information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | string | Yes | Name for the new sequence store |
| `description` | string | No | Optional description for the sequence store |
| `sse_kms_key_arn` | string | No | KMS key ARN for server-side encryption of the sequence store |
| `fallback_location` | string | No | S3 URI for the fallback location of the sequence store |
| `tags` | string | No | Tags to apply to the sequence store as a JSON string or object, e.g. {"key": "value"} |

## AWS CLI

```bash
aws omics create-sequence-store --name <name> --description <description> --sse-config <sse_kms_key_arn> --fallback-location <fallback_location> --tags <tags>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.create_sequence_store(
    Name=name,
    Description=description,
    SseConfig={'KmsKeyArn': 'sse_kms_key_arn'},
    FallbackLocation=fallback_location,
    Tags=tags,
)
```
