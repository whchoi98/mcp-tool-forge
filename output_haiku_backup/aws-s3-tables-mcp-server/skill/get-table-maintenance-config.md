---
name: get-table-maintenance-config
description: Get details about the maintenance configuration of a table.

    Gets details about the maintenance configuration of a table. For more information, see S3 Tables maintenance in the Amazon Simple Storage Service User Guide.

    Permissions:
    You must have the s3tables:GetTableMaintenanceConfiguration permission to use this operation.
    
---

# Get Table Maintenance Config

Get details about the maintenance configuration of a table.

    Gets details about the maintenance configuration of a table. For more information, see S3 Tables maintenance in the Amazon Simple Storage Service User Guide.

    Permissions:
    You must have the s3tables:GetTableMaintenanceConfiguration permission to use this operation.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `table_bucket_arn` | string | Yes | Table bucket ARN |
| `namespace` | string | Yes | The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `name` | string | Yes | The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `region_name` | string | No | The AWS region name where the operation should be performed. |

## AWS CLI

```bash
aws s3api get-bucket-lifecycle-configuration --bucket <table_bucket_arn>
```

## boto3

```python
import boto3

client = boto3.client('s3')
response = client.get_bucket_lifecycle_configuration(
    Bucket=table_bucket_arn,
)
```
