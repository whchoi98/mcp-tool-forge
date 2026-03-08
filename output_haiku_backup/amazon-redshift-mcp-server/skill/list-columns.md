---
name: list-columns
description: List all columns in a specified table within a Redshift schema.

    This tool queries the SVV_ALL_COLUMNS system view to discover all columns
    that the user has access to in the specified table, including detailed information
    about data types, constraints, and column properties.

    ## Usage Requirements

    - Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
    - The cluster must be available and accessible.
    - Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
    - The user must have access to the database to query system views.

    ## Parameters

    - cluster_identifier: The unique identifier of the Redshift cluster to query.
                         IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
    - column_database_name: The database name to list columns for.
                           IMPORTANT: Use a valid database name from the list_databases tool.
    - column_schema_name: The schema name to list columns for.
                         IMPORTANT: Use a valid schema name from the list_schemas tool.
    - column_table_name: The table name to list columns for.
                        IMPORTANT: Use a valid table name from the list_tables tool.

    ## Response Structure

    Returns a list of RedshiftColumn objects with the following structure:

    - database_name: The name of the database.
    - schema_name: The name of the schema.
    - table_name: The name of the table.
    - column_name: The name of the column.
    - ordinal_position: The position of the column in the table.
    - column_default: The default value of the column.
    - is_nullable: Whether the column is nullable (yes or no).
    - data_type: The data type of the column.
    - character_maximum_length: The maximum number of characters in the column.
    - numeric_precision: The numeric precision.
    - numeric_scale: The numeric scale.
    - remarks: Remarks about the column.

    ## Usage Tips

    1. First use list_clusters to get valid cluster identifiers.
    2. Then use list_databases to get valid database names for the cluster.
    3. Then use list_schemas to get valid schema names for the database.
    4. Then use list_tables to get valid table names for the schema.
    5. Ensure the cluster status is 'available' before querying columns.
    6. Note data types and constraints for query planning and data validation.

    ## Interpretation Best Practices

    1. Use ordinal_position to understand column order in the table.
    2. Check is_nullable for required vs optional fields.
    3. Use data_type information for proper data handling in queries.
    4. Consider character_maximum_length for string field validation.
    5. Use numeric_precision and numeric_scale for numeric field handling.
    6. Use column names for SELECT statements and query construction.
    
---

# List Columns

List all columns in a specified table within a Redshift schema.

    This tool queries the SVV_ALL_COLUMNS system view to discover all columns
    that the user has access to in the specified table, including detailed information
    about data types, constraints, and column properties.

    ## Usage Requirements

    - Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
    - The cluster must be available and accessible.
    - Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
    - The user must have access to the database to query system views.

    ## Parameters

    - cluster_identifier: The unique identifier of the Redshift cluster to query.
                         IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
    - column_database_name: The database name to list columns for.
                           IMPORTANT: Use a valid database name from the list_databases tool.
    - column_schema_name: The schema name to list columns for.
                         IMPORTANT: Use a valid schema name from the list_schemas tool.
    - column_table_name: The table name to list columns for.
                        IMPORTANT: Use a valid table name from the list_tables tool.

    ## Response Structure

    Returns a list of RedshiftColumn objects with the following structure:

    - database_name: The name of the database.
    - schema_name: The name of the schema.
    - table_name: The name of the table.
    - column_name: The name of the column.
    - ordinal_position: The position of the column in the table.
    - column_default: The default value of the column.
    - is_nullable: Whether the column is nullable (yes or no).
    - data_type: The data type of the column.
    - character_maximum_length: The maximum number of characters in the column.
    - numeric_precision: The numeric precision.
    - numeric_scale: The numeric scale.
    - remarks: Remarks about the column.

    ## Usage Tips

    1. First use list_clusters to get valid cluster identifiers.
    2. Then use list_databases to get valid database names for the cluster.
    3. Then use list_schemas to get valid schema names for the database.
    4. Then use list_tables to get valid table names for the schema.
    5. Ensure the cluster status is 'available' before querying columns.
    6. Note data types and constraints for query planning and data validation.

    ## Interpretation Best Practices

    1. Use ordinal_position to understand column order in the table.
    2. Check is_nullable for required vs optional fields.
    3. Use data_type information for proper data handling in queries.
    4. Consider character_maximum_length for string field validation.
    5. Use numeric_precision and numeric_scale for numeric field handling.
    6. Use column names for SELECT statements and query construction.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_identifier` | string | Yes | The cluster identifier to query for columns. Must be a valid cluster identifier from the list_clusters tool. |
| `column_database_name` | string | Yes | The database name to list columns for. Must be a valid database name from the list_databases tool. |
| `column_schema_name` | string | Yes | The schema name to list columns for. Must be a valid schema name from the list_schemas tool. |
| `column_table_name` | string | Yes | The table name to list columns for. Must be a valid table name from the list_tables tool. |

## AWS CLI

```bash
aws redshift describe-table-restore-status --cluster-identifier <cluster_identifier> --database-name <column_database_name> --schema-name <column_schema_name> --table-name <column_table_name>
```

## boto3

```python
import boto3

client = boto3.client('redshift')
response = client.describe_table_restore_status(
    ClusterIdentifier=cluster_identifier,
    DatabaseName=column_database_name,
    SchemaName=column_schema_name,
    TableName=column_table_name,
)
```
