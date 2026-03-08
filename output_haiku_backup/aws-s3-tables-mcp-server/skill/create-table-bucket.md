---
name: create-table-bucket
description: Creates an S3 table bucket.

    Permissions:
    You must have the s3tables:CreateTableBucket permission to use this operation.
    
---

# Create Table Bucket

Creates an S3 table bucket.

    Permissions:
    You must have the s3tables:CreateTableBucket permission to use this operation.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | string | Yes | Name of the table bucket to create. Must be 3-63 characters long and contain only lowercase letters, numbers, and hyphens. |
| `region_name` | string | No | The AWS region name where the operation should be performed. |

## AWS CLI

```bash
aws s3api create-bucket --bucket <name> --create-bucket-configuration <region_name>
```

## boto3

```python
import boto3

client = boto3.client('s3')
response = client.create_bucket(
    Bucket=name,
    CreateBucketConfiguration=region_name,
)
```
