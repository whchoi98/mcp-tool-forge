---
name: list-databases
description: List all databases in a specified Amazon Redshift cluster.

    This tool queries the SVV_REDSHIFT_DATABASES system view to discover all databases
    that the user has access to in the specified cluster, including local databases
    and databases created from datashares.

    ## Usage Requirements

    - Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
    - The cluster must be available and accessible.
    - Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
    - The user must have access to the specified database to query system views.

    ## Parameters

    - cluster_identifier: The unique identifier of the Redshift cluster to query.
                         IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
    - database_name: The database to connect to for querying system views (defaults to 'dev').

    ## Response Structure

    Returns a list of RedshiftDatabase objects with the following structure:

    - database_name: The name of the database.
    - database_owner: The database owner user ID.
    - database_type: The type of database (local or shared).
    - database_acl: Access control information (for internal use).
    - database_options: The properties of the database.
    - database_isolation_level: The isolation level (Snapshot Isolation or Serializable).

    ## Usage Tips

    1. First use list_clusters to get valid cluster identifiers.
    2. Ensure the cluster status is 'available' before querying databases.
    3. Use the default database name unless you know a specific database exists.
    4. Note database types to understand if they are local or shared from datashares.

    ## Interpretation Best Practices

    1. Focus on 'local' database types for cluster-native databases.
    2. 'shared' database types indicate databases from datashares.
    3. Use database names for subsequent schema and table discovery.
    4. Consider database isolation levels for transaction planning.
    
---

# List Databases

List all databases in a specified Amazon Redshift cluster.

    This tool queries the SVV_REDSHIFT_DATABASES system view to discover all databases
    that the user has access to in the specified cluster, including local databases
    and databases created from datashares.

    ## Usage Requirements

    - Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
    - The cluster must be available and accessible.
    - Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
    - The user must have access to the specified database to query system views.

    ## Parameters

    - cluster_identifier: The unique identifier of the Redshift cluster to query.
                         IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
    - database_name: The database to connect to for querying system views (defaults to 'dev').

    ## Response Structure

    Returns a list of RedshiftDatabase objects with the following structure:

    - database_name: The name of the database.
    - database_owner: The database owner user ID.
    - database_type: The type of database (local or shared).
    - database_acl: Access control information (for internal use).
    - database_options: The properties of the database.
    - database_isolation_level: The isolation level (Snapshot Isolation or Serializable).

    ## Usage Tips

    1. First use list_clusters to get valid cluster identifiers.
    2. Ensure the cluster status is 'available' before querying databases.
    3. Use the default database name unless you know a specific database exists.
    4. Note database types to understand if they are local or shared from datashares.

    ## Interpretation Best Practices

    1. Focus on 'local' database types for cluster-native databases.
    2. 'shared' database types indicate databases from datashares.
    3. Use database names for subsequent schema and table discovery.
    4. Consider database isolation levels for transaction planning.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_identifier` | string | Yes | The cluster identifier to query for databases. Must be a valid cluster identifier from the list_clusters tool. |
| `database_name` | string | No | The database to connect to for querying system views. Defaults to "dev". |

