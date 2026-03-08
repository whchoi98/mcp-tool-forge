---
name: create-namespace
description: Create a new namespace in an S3 table bucket.

    Creates a namespace. A namespace is a logical grouping of tables within your S3 table bucket,
    which you can use to organize S3 tables.

    Permissions:
    You must have the s3tables:CreateNamespace permission to use this operation.
    
---

# Create Namespace

Create a new namespace in an S3 table bucket.

    Creates a namespace. A namespace is a logical grouping of tables within your S3 table bucket,
    which you can use to organize S3 tables.

    Permissions:
    You must have the s3tables:CreateNamespace permission to use this operation.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `table_bucket_arn` | string | Yes | Table bucket ARN |
| `namespace` | string | Yes | The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `region_name` | string | No | The AWS region name where the operation should be performed. |

## AWS CLI

```bash
aws s3api put-bucket-tagging --bucket <table_bucket_arn> --tagging <Namespace={namespace}>
```

## boto3

```python
import boto3

client = boto3.client('s3')
response = client.put_bucket_tagging(
    Bucket=table_bucket_arn,
    Tagging={'TagSet': [{'Key': 'Namespace', 'Value': 'namespace'}]},
)
```
