---
name: list-tables
description: List all tables in a specified schema within a Redshift database.

    This tool queries the SVV_ALL_TABLES system view to discover all tables
    that the user has access to in the specified schema, including base tables,
    views, external tables, and shared tables.

    ## Usage Requirements

    - Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
    - The cluster must be available and accessible.
    - Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
    - The user must have access to the database to query system views.

    ## Parameters

    - cluster_identifier: The unique identifier of the Redshift cluster to query.
                         IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
    - table_database_name: The database name to list tables for.
                          IMPORTANT: Use a valid database name from the list_databases tool.
    - table_schema_name: The schema name to list tables for.
                        IMPORTANT: Use a valid schema name from the list_schemas tool.

    ## Response Structure

    Returns a list of RedshiftTable objects with the following structure:

    - database_name: The name of the database where the table exists.
    - schema_name: The schema name for the table.
    - table_name: The name of the table.
    - table_acl: The permissions for the specified user or user group for the table.
    - table_type: The type of the table (views, base tables, external tables, shared tables).
    - remarks: Remarks about the table.

    ## Usage Tips

    1. First use list_clusters to get valid cluster identifiers.
    2. Then use list_databases to get valid database names for the cluster.
    3. Then use list_schemas to get valid schema names for the database.
    4. Ensure the cluster status is 'available' before querying tables.
    5. Note table types to understand if they are base tables, views, external tables, or shared tables.

    ## Interpretation Best Practices

    1. Focus on 'TABLE' table types for regular database tables.
    2. 'VIEW' table types indicate database views.
    3. 'EXTERNAL TABLE' types indicate connections to external data sources.
    4. 'SHARED TABLE' types indicate tables from datashares.
    5. Use table names for subsequent column discovery and query operations.
    6. Consider table permissions (table_acl) for access planning.
    
---

# List Tables

List all tables in a specified schema within a Redshift database.

    This tool queries the SVV_ALL_TABLES system view to discover all tables
    that the user has access to in the specified schema, including base tables,
    views, external tables, and shared tables.

    ## Usage Requirements

    - Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
    - The cluster must be available and accessible.
    - Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
    - The user must have access to the database to query system views.

    ## Parameters

    - cluster_identifier: The unique identifier of the Redshift cluster to query.
                         IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
    - table_database_name: The database name to list tables for.
                          IMPORTANT: Use a valid database name from the list_databases tool.
    - table_schema_name: The schema name to list tables for.
                        IMPORTANT: Use a valid schema name from the list_schemas tool.

    ## Response Structure

    Returns a list of RedshiftTable objects with the following structure:

    - database_name: The name of the database where the table exists.
    - schema_name: The schema name for the table.
    - table_name: The name of the table.
    - table_acl: The permissions for the specified user or user group for the table.
    - table_type: The type of the table (views, base tables, external tables, shared tables).
    - remarks: Remarks about the table.

    ## Usage Tips

    1. First use list_clusters to get valid cluster identifiers.
    2. Then use list_databases to get valid database names for the cluster.
    3. Then use list_schemas to get valid schema names for the database.
    4. Ensure the cluster status is 'available' before querying tables.
    5. Note table types to understand if they are base tables, views, external tables, or shared tables.

    ## Interpretation Best Practices

    1. Focus on 'TABLE' table types for regular database tables.
    2. 'VIEW' table types indicate database views.
    3. 'EXTERNAL TABLE' types indicate connections to external data sources.
    4. 'SHARED TABLE' types indicate tables from datashares.
    5. Use table names for subsequent column discovery and query operations.
    6. Consider table permissions (table_acl) for access planning.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_identifier` | string | Yes | The cluster identifier to query for tables. Must be a valid cluster identifier from the list_clusters tool. |
| `table_database_name` | string | Yes | The database name to list tables for. Must be a valid database name from the list_databases tool. |
| `table_schema_name` | string | Yes | The schema name to list tables for. Also used to connect to. Must be a valid schema name from the list_schemas tool. |

## AWS CLI

```bash
aws redshift describe-tables --cluster-identifier <cluster_identifier> --database-name <table_database_name> --schema-name <table_schema_name>
```

## boto3

```python
import boto3

client = boto3.client('redshift')
response = client.describe_tables(
    ClusterIdentifier=cluster_identifier,
    DatabaseName=table_database_name,
    SchemaName=table_schema_name,
)
```
