---
name: storage-lens
description: Query S3 Storage Lens metrics data using Athena SQL.

IMPORTANT USAGE GUIDELINES:
- Before using this tool, provide a 1-3 sentence explanation starting with "EXPLANATION:"
- Use standard SQL syntax for Athena queries
- Use {table} as a placeholder for the Storage Lens metrics table name
- Perform aggregations (GROUP BY) when analyzing data across multiple dimensions

This tool allows you to analyze S3 Storage Lens metrics data using SQL queries.
Storage Lens provides metrics about your S3 storage, including:

- Storage metrics: Total bytes, object counts by storage class
- Cost optimization metrics: Transition opportunities, incomplete multipart uploads
- Data protection metrics: Replication, versioning, encryption status
- Activity metrics: Upload, download, and request metrics

STORAGE LENS EXPORT SCHEMA:
The Storage Lens export data has the following standard columns:
- version_number: The version of the S3 Storage Lens metrics being used
- configuration_id: The configuration_id of your S3 Storage Lens configuration
- report_date: The date that the metrics were tracked
- aws_account_number: Your AWS account number
- aws_region: The AWS Region for which the metrics are being tracked
- storage_class: The storage class (STANDARD, STANDARD_IA, GLACIER, etc.)
- record_type: The type of artifact being reported (ACCOUNT, BUCKET, PREFIX, STORAGE_LENS_GROUP_BUCKET, STORAGE_LENS_GROUP_ACCOUNT)
- record_value: The value of the record_type artifact (account ID, bucket name, prefix, or Storage Lens group ARN)
- bucket_name: The name of the bucket (when record_type is BUCKET or PREFIX)
- metric_name: The name of the metric (e.g., 'StorageBytes', 'ObjectCount', 'EncryptedStorageBytes')
- metric_value: The numeric value of the metric

IMPORTANT: Metrics are stored in rows, not columns. Each row represents one metric value for a specific combination of dimensions.

Environment variables:
- STORAGE_LENS_MANIFEST_LOCATION: S3 URI to manifest file or folder (required)
- STORAGE_LENS_OUTPUT_LOCATION: S3 location for Athena query results (optional)

Example queries:
1. Top 10 buckets by storage size:
   SELECT
       bucket_name,
       SUM(CAST(metric_value AS BIGINT)) as total_size
   FROM {table}
   WHERE metric_name = 'StorageBytes'
   GROUP BY bucket_name
   ORDER BY total_size DESC
   LIMIT 10

2. Storage distribution by storage class:
   SELECT
       storage_class,
       SUM(CAST(metric_value AS BIGINT)) as total_size
   FROM {table}
   WHERE metric_name = 'StorageBytes'
   GROUP BY storage_class
   ORDER BY total_size DESC

3. Buckets with incomplete multipart uploads:
   SELECT
       bucket_name,
       SUM(CAST(metric_value AS BIGINT)) as incomplete_bytes
   FROM {table}
   WHERE metric_name = 'IncompleteMultipartUploadStorageBytes'
     AND CAST(metric_value AS BIGINT) > 0
   GROUP BY bucket_name
   ORDER BY incomplete_bytes DESC

4. Storage Distribution by Region and Storage Class:
   SELECT
       aws_region,
       storage_class,
       SUM(CAST(metric_value AS BIGINT)) as total_bytes
   FROM {table}
   WHERE metric_name = 'StorageBytes'
   GROUP BY aws_region, storage_class
   ORDER BY total_bytes DESC

5. Object Lifecycle Management Opportunities:
   SELECT
       aws_region,
       storage_class,
       SUM(CASE WHEN metric_name = 'NonCurrentVersionStorageBytes' THEN CAST(metric_value AS BIGINT) ELSE 0 END) as noncurrent_bytes,
       SUM(CASE WHEN metric_name = 'StorageBytes' THEN CAST(metric_value AS BIGINT) ELSE 0 END) as total_bytes
   FROM {table}
   WHERE metric_name IN ('NonCurrentVersionStorageBytes', 'StorageBytes')
   GROUP BY aws_region, storage_class
   HAVING SUM(CASE WHEN metric_name = 'NonCurrentVersionStorageBytes' THEN CAST(metric_value AS BIGINT) ELSE 0 END) > 0
   ORDER BY noncurrent_bytes DESC

6. Lifecycle Rule Analysis:
   SELECT
       bucket_name,
       SUM(CASE WHEN metric_name = 'TotalLifecycleRuleCount' THEN CAST(metric_value AS INTEGER) ELSE 0 END) as lifecycle_rule_count,
       SUM(CASE WHEN metric_name = 'StorageBytes' THEN CAST(metric_value AS BIGINT) ELSE 0 END) as total_bytes
   FROM {table}
   WHERE metric_name IN ('TotalLifecycleRuleCount', 'StorageBytes')
   GROUP BY bucket_name
   ORDER BY lifecycle_rule_count ASC, total_bytes DESC
---

# Storage-Lens

Query S3 Storage Lens metrics data using Athena SQL.

IMPORTANT USAGE GUIDELINES:
- Before using this tool, provide a 1-3 sentence explanation starting with "EXPLANATION:"
- Use standard SQL syntax for Athena queries
- Use {table} as a placeholder for the Storage Lens metrics table name
- Perform aggregations (GROUP BY) when analyzing data across multiple dimensions

This tool allows you to analyze S3 Storage Lens metrics data using SQL queries.
Storage Lens provides metrics about your S3 storage, including:

- Storage metrics: Total bytes, object counts by storage class
- Cost optimization metrics: Transition opportunities, incomplete multipart uploads
- Data protection metrics: Replication, versioning, encryption status
- Activity metrics: Upload, download, and request metrics

STORAGE LENS EXPORT SCHEMA:
The Storage Lens export data has the following standard columns:
- version_number: The version of the S3 Storage Lens metrics being used
- configuration_id: The configuration_id of your S3 Storage Lens configuration
- report_date: The date that the metrics were tracked
- aws_account_number: Your AWS account number
- aws_region: The AWS Region for which the metrics are being tracked
- storage_class: The storage class (STANDARD, STANDARD_IA, GLACIER, etc.)
- record_type: The type of artifact being reported (ACCOUNT, BUCKET, PREFIX, STORAGE_LENS_GROUP_BUCKET, STORAGE_LENS_GROUP_ACCOUNT)
- record_value: The value of the record_type artifact (account ID, bucket name, prefix, or Storage Lens group ARN)
- bucket_name: The name of the bucket (when record_type is BUCKET or PREFIX)
- metric_name: The name of the metric (e.g., 'StorageBytes', 'ObjectCount', 'EncryptedStorageBytes')
- metric_value: The numeric value of the metric

IMPORTANT: Metrics are stored in rows, not columns. Each row represents one metric value for a specific combination of dimensions.

Environment variables:
- STORAGE_LENS_MANIFEST_LOCATION: S3 URI to manifest file or folder (required)
- STORAGE_LENS_OUTPUT_LOCATION: S3 location for Athena query results (optional)

Example queries:
1. Top 10 buckets by storage size:
   SELECT
       bucket_name,
       SUM(CAST(metric_value AS BIGINT)) as total_size
   FROM {table}
   WHERE metric_name = 'StorageBytes'
   GROUP BY bucket_name
   ORDER BY total_size DESC
   LIMIT 10

2. Storage distribution by storage class:
   SELECT
       storage_class,
       SUM(CAST(metric_value AS BIGINT)) as total_size
   FROM {table}
   WHERE metric_name = 'StorageBytes'
   GROUP BY storage_class
   ORDER BY total_size DESC

3. Buckets with incomplete multipart uploads:
   SELECT
       bucket_name,
       SUM(CAST(metric_value AS BIGINT)) as incomplete_bytes
   FROM {table}
   WHERE metric_name = 'IncompleteMultipartUploadStorageBytes'
     AND CAST(metric_value AS BIGINT) > 0
   GROUP BY bucket_name
   ORDER BY incomplete_bytes DESC

4. Storage Distribution by Region and Storage Class:
   SELECT
       aws_region,
       storage_class,
       SUM(CAST(metric_value AS BIGINT)) as total_bytes
   FROM {table}
   WHERE metric_name = 'StorageBytes'
   GROUP BY aws_region, storage_class
   ORDER BY total_bytes DESC

5. Object Lifecycle Management Opportunities:
   SELECT
       aws_region,
       storage_class,
       SUM(CASE WHEN metric_name = 'NonCurrentVersionStorageBytes' THEN CAST(metric_value AS BIGINT) ELSE 0 END) as noncurrent_bytes,
       SUM(CASE WHEN metric_name = 'StorageBytes' THEN CAST(metric_value AS BIGINT) ELSE 0 END) as total_bytes
   FROM {table}
   WHERE metric_name IN ('NonCurrentVersionStorageBytes', 'StorageBytes')
   GROUP BY aws_region, storage_class
   HAVING SUM(CASE WHEN metric_name = 'NonCurrentVersionStorageBytes' THEN CAST(metric_value AS BIGINT) ELSE 0 END) > 0
   ORDER BY noncurrent_bytes DESC

6. Lifecycle Rule Analysis:
   SELECT
       bucket_name,
       SUM(CASE WHEN metric_name = 'TotalLifecycleRuleCount' THEN CAST(metric_value AS INTEGER) ELSE 0 END) as lifecycle_rule_count,
       SUM(CASE WHEN metric_name = 'StorageBytes' THEN CAST(metric_value AS BIGINT) ELSE 0 END) as total_bytes
   FROM {table}
   WHERE metric_name IN ('TotalLifecycleRuleCount', 'StorageBytes')
   GROUP BY bucket_name
   ORDER BY lifecycle_rule_count ASC, total_bytes DESC

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes |  |
| `manifest_location` | string | No |  |
| `output_location` | string | No |  |
| `database_name` | string | No |  |
| `table_name` | string | No |  |

## AWS CLI

```bash
aws athena start-query-execution --query-string <query> --result-configuration <output_location> --query-execution-context <database_name>
```

## boto3

```python
import boto3

client = boto3.client('athena')
response = client.start_query_execution(
    QueryString=query,
    ResultConfiguration={'OutputLocation': 'output_location'},
    QueryExecutionContext={'Database': 'database_name'},
)
```
