---
name: get-table-metadata-location
description: Get the location of the S3 table metadata.

    Gets the S3 URI location of the table metadata, which contains the schema and other
    table configuration information.

    Permissions:
    You must have the s3tables:GetTableMetadataLocation permission to use this operation.
    
---

# Get Table Metadata Location

Get the location of the S3 table metadata.

    Gets the S3 URI location of the table metadata, which contains the schema and other
    table configuration information.

    Permissions:
    You must have the s3tables:GetTableMetadataLocation permission to use this operation.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `table_bucket_arn` | string | Yes | Table bucket ARN |
| `namespace` | string | Yes | The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `name` | string | Yes | The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `region_name` | string | No | The AWS region name where the operation should be performed. |

