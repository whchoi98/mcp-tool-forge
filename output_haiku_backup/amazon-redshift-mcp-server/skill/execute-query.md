---
name: execute-query
description: Execute a SQL query against a Redshift cluster or serverless workgroup.

    This tool uses the Redshift Data API to execute SQL queries and return results.
    It supports both provisioned clusters and serverless workgroups, and handles
    various data types in the result set.

    ## Usage Requirements

    - Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
    - The cluster must be available and accessible.
    - Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
    - The user must have appropriate permissions to execute queries in the specified database.

    ## Parameters

    - cluster_identifier: The unique identifier of the Redshift cluster to query.
                         IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
    - database_name: The database name to execute the query against.
                    IMPORTANT: Use a valid database name from the list_databases tool.
    - sql: The SQL statement to execute. Should be a single SQL statement.

    ## Response Structure

    Returns a QueryResult object with the following structure:

    - columns: List of column names in the result set.
    - rows: List of rows, where each row is a list of values.
    - row_count: Number of rows returned.
    - execution_time_ms: Query execution time in milliseconds.
    - query_id: Unique identifier for the query execution.

    ## Usage Tips

    1. First use list_clusters to get valid cluster identifiers.
    2. Then use list_databases to get valid database names for the cluster.
    3. Ensure the cluster status is 'available' before executing queries.
    4. Use LIMIT clauses for exploratory queries to avoid large result sets.
    5. Consider using the metadata discovery tools to understand table structures before querying.

    ## Data Type Handling

    The tool automatically handles various Redshift data types:
    - String values (VARCHAR, CHAR, TEXT).
    - Numeric values (INTEGER, BIGINT, DECIMAL, FLOAT).
    - Boolean values.
    - NULL values.
    - Date and timestamp values (returned as strings).

    ## Security Considerations

    - Avoid dynamic SQL construction with user input.
    - Consider database object permissions.
    - Currently, the execute_query tool runs the query in a READ ONLY transaction to prevent unintentional modifications.
    - The READ WRITE mode will be added in the future versions with additional protection mechanisms.
    
---

# Execute Query

Execute a SQL query against a Redshift cluster or serverless workgroup.

    This tool uses the Redshift Data API to execute SQL queries and return results.
    It supports both provisioned clusters and serverless workgroups, and handles
    various data types in the result set.

    ## Usage Requirements

    - Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
    - The cluster must be available and accessible.
    - Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
    - The user must have appropriate permissions to execute queries in the specified database.

    ## Parameters

    - cluster_identifier: The unique identifier of the Redshift cluster to query.
                         IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
    - database_name: The database name to execute the query against.
                    IMPORTANT: Use a valid database name from the list_databases tool.
    - sql: The SQL statement to execute. Should be a single SQL statement.

    ## Response Structure

    Returns a QueryResult object with the following structure:

    - columns: List of column names in the result set.
    - rows: List of rows, where each row is a list of values.
    - row_count: Number of rows returned.
    - execution_time_ms: Query execution time in milliseconds.
    - query_id: Unique identifier for the query execution.

    ## Usage Tips

    1. First use list_clusters to get valid cluster identifiers.
    2. Then use list_databases to get valid database names for the cluster.
    3. Ensure the cluster status is 'available' before executing queries.
    4. Use LIMIT clauses for exploratory queries to avoid large result sets.
    5. Consider using the metadata discovery tools to understand table structures before querying.

    ## Data Type Handling

    The tool automatically handles various Redshift data types:
    - String values (VARCHAR, CHAR, TEXT).
    - Numeric values (INTEGER, BIGINT, DECIMAL, FLOAT).
    - Boolean values.
    - NULL values.
    - Date and timestamp values (returned as strings).

    ## Security Considerations

    - Avoid dynamic SQL construction with user input.
    - Consider database object permissions.
    - Currently, the execute_query tool runs the query in a READ ONLY transaction to prevent unintentional modifications.
    - The READ WRITE mode will be added in the future versions with additional protection mechanisms.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_identifier` | string | Yes | The cluster identifier to execute the query on. Must be a valid cluster identifier from the list_clusters tool. |
| `database_name` | string | Yes | The database name to execute the query against. Must be a valid database name from the list_databases tool. |
| `sql` | string | Yes | The SQL statement to execute. Should be a single SQL statement. |

## AWS CLI

```bash
aws redshift-data execute-statement --cluster-identifier <cluster_identifier> --database <database_name> --sql <sql>
```

## boto3

```python
import boto3

client = boto3.client('redshift-data')
response = client.execute_statement(
    ClusterIdentifier=cluster_identifier,
    Database=database_name,
    Sql=sql,
)
```
