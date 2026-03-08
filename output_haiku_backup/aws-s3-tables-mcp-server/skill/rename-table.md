---
name: rename-table
description: Rename an S3 table or move it to a different S3 namespace.

    Renames an S3 table or moves it to a different S3 namespace within the same S3 table bucket.
    This operation maintains the table's data and configuration while updating its location.

    Permissions:
    You must have the s3tables:RenameTable permission to use this operation.
    
---

# Rename Table

Rename an S3 table or move it to a different S3 namespace.

    Renames an S3 table or moves it to a different S3 namespace within the same S3 table bucket.
    This operation maintains the table's data and configuration while updating its location.

    Permissions:
    You must have the s3tables:RenameTable permission to use this operation.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `table_bucket_arn` | string | Yes | Table bucket ARN |
| `namespace` | string | Yes | The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `name` | string | Yes | The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `new_name` | string | No | The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `new_namespace_name` | string | No | The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `version_token` | string | No | The version token of the S3 table. Must be 1-2048 characters long. |
| `region_name` | string | No | The AWS region name where the operation should be performed. |

