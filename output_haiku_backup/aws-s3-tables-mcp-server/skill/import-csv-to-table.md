---
name: import-csv-to-table
description: Import data from a CSV file into an S3 table.

    This tool reads data from a CSV file stored in S3 and imports it into an S3 table.
    If the table doesn't exist, it will be created with a schema inferred from the CSV file.
    If the table exists, the CSV file schema must be compatible with the table's schema.
    The tool will validate the schema before attempting to import the data.
    If preserve_case is True, the column names will not be converted to snake_case. Otherwise, the column names will be converted to snake_case.

    Returns error dictionary with status and error message if:
        - URL is not a valid S3 URL
        - File is not a CSV file
        - File cannot be accessed
        - Table does not exist
        - CSV headers don't match table schema
        - Any other error occurs

    Example input values:
        warehouse: 'arn:aws:s3tables:<Region>:<accountID>:bucket/<bucketname>'
        region: 'us-west-2'
        namespace: 'retail_data'
        table_name: 'customers'
        s3_url: 's3://bucket-name/path/to/file.csv'
        uri: 'https://s3tables.us-west-2.amazonaws.com/iceberg'
        catalog_name: 's3tablescatalog'
        rest_signing_name: 's3tables'
        rest_sigv4_enabled: 'true'
        preserve_case: False

    Permissions:
    You must have:
    - s3:GetObject permission for the CSV file
    - s3tables:GetTable and s3tables:GetTables permissions to access table information
    - s3tables:PutTableData permission to write to the table
    
---

# Import Csv To Table

Import data from a CSV file into an S3 table.

    This tool reads data from a CSV file stored in S3 and imports it into an S3 table.
    If the table doesn't exist, it will be created with a schema inferred from the CSV file.
    If the table exists, the CSV file schema must be compatible with the table's schema.
    The tool will validate the schema before attempting to import the data.
    If preserve_case is True, the column names will not be converted to snake_case. Otherwise, the column names will be converted to snake_case.

    Returns error dictionary with status and error message if:
        - URL is not a valid S3 URL
        - File is not a CSV file
        - File cannot be accessed
        - Table does not exist
        - CSV headers don't match table schema
        - Any other error occurs

    Example input values:
        warehouse: 'arn:aws:s3tables:<Region>:<accountID>:bucket/<bucketname>'
        region: 'us-west-2'
        namespace: 'retail_data'
        table_name: 'customers'
        s3_url: 's3://bucket-name/path/to/file.csv'
        uri: 'https://s3tables.us-west-2.amazonaws.com/iceberg'
        catalog_name: 's3tablescatalog'
        rest_signing_name: 's3tables'
        rest_sigv4_enabled: 'true'
        preserve_case: False

    Permissions:
    You must have:
    - s3:GetObject permission for the CSV file
    - s3tables:GetTable and s3tables:GetTables permissions to access table information
    - s3tables:PutTableData permission to write to the table
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `warehouse` | string | Yes | Warehouse string for Iceberg catalog |
| `region` | string | Yes | AWS region for S3Tables/Iceberg REST endpoint |
| `namespace` | string | Yes | The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `table_name` | string | Yes | The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `s3_url` | string | Yes | The S3 URL of the file to preview (format: s3://bucket-name/key) |
| `uri` | string | Yes | REST URI for Iceberg catalog |
| `catalog_name` | string | No | Catalog name |
| `rest_signing_name` | string | No | REST signing name |
| `rest_sigv4_enabled` | string | No | Enable SigV4 signing |
| `preserve_case` | boolean | No | Preserve case of column names |

