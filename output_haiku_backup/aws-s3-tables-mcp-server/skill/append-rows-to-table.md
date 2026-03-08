---
name: append-rows-to-table
description: Append rows to an Iceberg table using PyIceberg/Daft.

    This tool appends data rows to an existing Iceberg table using the PyIceberg engine.
    The rows parameter must be a list of dictionaries, each representing a row.
    Check the schema of the table before appending rows.

    Example input values:
        warehouse: 'arn:aws:s3tables:<Region>:<accountID>:bucket/<bucketname>'
        region: 'us-west-2'
        namespace: 'retail_data'
        table_name: 'customers'
        rows: [{"customer_id": 1, "customer_name": "Alice"}, ...]
        uri: 'https://s3tables.us-west-2.amazonaws.com/iceberg'
        catalog_name: 's3tablescatalog'
        rest_signing_name: 's3tables'
        rest_sigv4_enabled: 'true'
    
---

# Append Rows To Table

Append rows to an Iceberg table using PyIceberg/Daft.

    This tool appends data rows to an existing Iceberg table using the PyIceberg engine.
    The rows parameter must be a list of dictionaries, each representing a row.
    Check the schema of the table before appending rows.

    Example input values:
        warehouse: 'arn:aws:s3tables:<Region>:<accountID>:bucket/<bucketname>'
        region: 'us-west-2'
        namespace: 'retail_data'
        table_name: 'customers'
        rows: [{"customer_id": 1, "customer_name": "Alice"}, ...]
        uri: 'https://s3tables.us-west-2.amazonaws.com/iceberg'
        catalog_name: 's3tablescatalog'
        rest_signing_name: 's3tables'
        rest_sigv4_enabled: 'true'
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `warehouse` | string | Yes | Warehouse string for Iceberg catalog |
| `region` | string | Yes | AWS region for S3Tables/Iceberg REST endpoint |
| `namespace` | string | Yes | The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `table_name` | string | Yes | The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `rows` | array | Yes | List of rows to append, each as a dict |
| `uri` | string | Yes | REST URI for Iceberg catalog |
| `catalog_name` | string | No | Catalog name |
| `rest_signing_name` | string | No | REST signing name |
| `rest_sigv4_enabled` | string | No | Enable SigV4 signing |

