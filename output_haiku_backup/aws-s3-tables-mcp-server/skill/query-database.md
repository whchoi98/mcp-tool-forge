---
name: query-database
description: Execute SQL queries against S3 Tables using PyIceberg/Daft.

    This tool provides a secure interface to run read-only SQL queries against your S3 Tables data using the PyIceberg and Daft engine.
    Use a correct region for warehouse, region, and uri.

    Example input values:
        warehouse: 'arn:aws:s3tables:<Region>:<accountID>:bucket/<bucketname>'
        region: 'us-west-2'
        namespace: 'retail_data'
        query: 'SELECT * FROM customers LIMIT 10'
        uri: 'https://s3tables.us-west-2.amazonaws.com/iceberg'
        catalog_name: 's3tablescatalog'
        rest_signing_name: 's3tables'
        rest_sigv4_enabled: 'true'
    
---

# Query Database

Execute SQL queries against S3 Tables using PyIceberg/Daft.

    This tool provides a secure interface to run read-only SQL queries against your S3 Tables data using the PyIceberg and Daft engine.
    Use a correct region for warehouse, region, and uri.

    Example input values:
        warehouse: 'arn:aws:s3tables:<Region>:<accountID>:bucket/<bucketname>'
        region: 'us-west-2'
        namespace: 'retail_data'
        query: 'SELECT * FROM customers LIMIT 10'
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
| `query` | string | No | Optional SQL query. If not provided, will execute SELECT * FROM table. Must be a read operation. |
| `uri` | string | Yes | REST URI for Iceberg catalog |
| `catalog_name` | string | No | Catalog name |
| `rest_signing_name` | string | No | REST signing name |
| `rest_sigv4_enabled` | string | No | Enable SigV4 signing |

## AWS CLI

```bash
aws athena start-query-execution --query-string <query> --work-group <catalog_name> --result-configuration <OutputLocation={warehouse}>
```

## boto3

```python
import boto3

client = boto3.client('athena')
response = client.start_query_execution(
    QueryString=query,
    WorkGroup=catalog_name,
    ResultConfiguration={'OutputLocation': 'warehouse'},
)
```
