---
name: get-bucket-metadata-config
description: Get the metadata table configuration for a regular general purpose S3 bucket.

    Retrieves the metadata table configuration for a regular general purpose bucket in s3. This configuration
    determines how metadata is stored and managed for the bucket.
    The response includes:
    - S3 Table Bucket ARN
    - S3 Table ARN
    - S3 Table Name
    - S3 Table Namespace

    Description:
    Amazon S3 Metadata accelerates data discovery by automatically capturing metadata for the objects in your general purpose buckets and storing it in read-only, fully managed Apache Iceberg tables that you can query. These read-only tables are called metadata tables. As objects are added to, updated, and removed from your general purpose buckets, S3 Metadata automatically refreshes the corresponding metadata tables to reflect the latest changes.
    By default, S3 Metadata provides three types of metadata:
    - System-defined metadata, such as an object's creation time and storage class
    - Custom metadata, such as tags and user-defined metadata that was included during object upload
    - Event metadata, such as when an object is updated or deleted, and the AWS account that made the request

    Metadata table schema:
    - bucket: String
    - key: String
    - sequence_number: String
    - record_type: String
    - record_timestamp: Timestamp (no time zone)
    - version_id: String
    - is_delete_marker: Boolean
    - size: Long
    - last_modified_date: Timestamp (no time zone)
    - e_tag: String
    - storage_class: String
    - is_multipart: Boolean
    - encryption_status: String
    - is_bucket_key_enabled: Boolean
    - kms_key_arn: String
    - checksum_algorithm: String
    - object_tags: Map<String, String>
    - user_metadata: Map<String, String>
    - requester: String
    - source_ip_address: String
    - request_id: String

    Permissions:
    You must have the s3:GetBucketMetadataConfiguration permission to use this operation.
    
---

# Get Bucket Metadata Config

Get the metadata table configuration for a regular general purpose S3 bucket.

    Retrieves the metadata table configuration for a regular general purpose bucket in s3. This configuration
    determines how metadata is stored and managed for the bucket.
    The response includes:
    - S3 Table Bucket ARN
    - S3 Table ARN
    - S3 Table Name
    - S3 Table Namespace

    Description:
    Amazon S3 Metadata accelerates data discovery by automatically capturing metadata for the objects in your general purpose buckets and storing it in read-only, fully managed Apache Iceberg tables that you can query. These read-only tables are called metadata tables. As objects are added to, updated, and removed from your general purpose buckets, S3 Metadata automatically refreshes the corresponding metadata tables to reflect the latest changes.
    By default, S3 Metadata provides three types of metadata:
    - System-defined metadata, such as an object's creation time and storage class
    - Custom metadata, such as tags and user-defined metadata that was included during object upload
    - Event metadata, such as when an object is updated or deleted, and the AWS account that made the request

    Metadata table schema:
    - bucket: String
    - key: String
    - sequence_number: String
    - record_type: String
    - record_timestamp: Timestamp (no time zone)
    - version_id: String
    - is_delete_marker: Boolean
    - size: Long
    - last_modified_date: Timestamp (no time zone)
    - e_tag: String
    - storage_class: String
    - is_multipart: Boolean
    - encryption_status: String
    - is_bucket_key_enabled: Boolean
    - kms_key_arn: String
    - checksum_algorithm: String
    - object_tags: Map<String, String>
    - user_metadata: Map<String, String>
    - requester: String
    - source_ip_address: String
    - request_id: String

    Permissions:
    You must have the s3:GetBucketMetadataConfiguration permission to use this operation.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `bucket` | string | Yes | The name of the S3 bucket to get metadata table configuration for. |
| `region_name` | string | No | The AWS region name where the operation should be performed. |

## AWS CLI

```bash
aws s3control get-bucket-metadata-configuration --bucket <bucket> --region <region_name>
```

## boto3

```python
import boto3

client = boto3.client('s3control')
response = client.get_bucket_metadata_configuration(
    Bucket=bucket,
    RegionName=region_name,
)
```
