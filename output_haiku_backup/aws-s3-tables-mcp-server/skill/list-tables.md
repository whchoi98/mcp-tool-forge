---
name: list-tables
description: List all S3 tables across all table buckets and namespaces.

    Permissions:
    You must have the s3tables:ListTables permission to use this operation.
    
---

# List Tables

List all S3 tables across all table buckets and namespaces.

    Permissions:
    You must have the s3tables:ListTables permission to use this operation.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region_name` | string | No | The AWS region name where the operation should be performed. |

## AWS CLI

```bash
aws s3 ls --region <region_name>
```

## boto3

```python
import boto3

client = boto3.client('s3')
response = client.list_buckets(
)
```
