---
name: update-table-metadata-location
description: Update the metadata location for an S3 table.

    Updates the metadata location for an S3 table. The metadata location of an S3 table must be an S3 URI that begins with the S3 table's warehouse location.
    The metadata location for an Apache Iceberg S3 table must end with .metadata.json, or if the metadata file is Gzip-compressed, .metadata.json.gz.

    Permissions:
    You must have the s3tables:UpdateTableMetadataLocation permission to use this operation.
    
---

# Update Table Metadata Location

Update the metadata location for an S3 table.

    Updates the metadata location for an S3 table. The metadata location of an S3 table must be an S3 URI that begins with the S3 table's warehouse location.
    The metadata location for an Apache Iceberg S3 table must end with .metadata.json, or if the metadata file is Gzip-compressed, .metadata.json.gz.

    Permissions:
    You must have the s3tables:UpdateTableMetadataLocation permission to use this operation.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `table_bucket_arn` | string | Yes | Table bucket ARN |
| `namespace` | string | Yes | The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `name` | string | Yes | The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `metadata_location` | string | Yes | The new metadata location for the S3 table. Must be 1-2048 characters long. |
| `version_token` | string | Yes | The version token of the S3 table. Must be 1-2048 characters long. |
| `region_name` | string | No | The AWS region name where the operation should be performed. |

## AWS CLI

```bash
aws glue update-table --database-name <namespace> --table-input <metadata_location> --version-id <version_token>
```

## boto3

```python
import boto3

client = boto3.client('glue')
response = client.update_table(
    DatabaseName=namespace,
    TableInput={'Name': 'name', 'StorageDescriptor': {'Location': 'metadata_location'}},
    VersionId=version_token,
)
```
