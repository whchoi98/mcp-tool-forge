---
name: list-schemas
description: List all schemas in a specified database within a Redshift cluster.

    This tool queries the SVV_ALL_SCHEMAS system view to discover all schemas
    that the user has access to in the specified database, including local schemas,
    external schemas, and shared schemas from datashares.

    ## Usage Requirements

    - Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
    - The cluster must be available and accessible.
    - Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
    - The user must have access to the database to query system views.

    ## Parameters

    - cluster_identifier: The unique identifier of the Redshift cluster to query.
                         IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
    - schema_database_name: The database name to list schemas for. Also used to connect to.
                           IMPORTANT: Use a valid database name from the list_databases tool.

    ## Response Structure

    Returns a list of RedshiftSchema objects with the following structure:

    - database_name: The name of the database where the schema exists.
    - schema_name: The name of the schema.
    - schema_owner: The user ID of the schema owner.
    - schema_type: The type of the schema (external, local, or shared).
    - schema_acl: The permissions for the specified user or user group for the schema.
    - source_database: The name of the source database for external schema.
    - schema_option: The options of the schema (external schema attribute).

    ## Usage Tips

    1. First use list_clusters to get valid cluster identifiers.
    2. Then use list_databases to get valid database names for the cluster.
    3. Ensure the cluster status is 'available' before querying schemas.
    4. Note schema types to understand if they are local, external, or shared.
    5. External schemas connect to external data sources like S3 or other databases.

    ## Interpretation Best Practices

    1. Focus on 'local' schema types for cluster-native schemas.
    2. 'external' schema types indicate connections to external data sources.
    3. 'shared' schema types indicate schemas from datashares.
    4. Use schema names for subsequent table and column discovery.
    5. Consider schema permissions (schema_acl) for access planning.
    
---

# List Schemas

List all schemas in a specified database within a Redshift cluster.

    This tool queries the SVV_ALL_SCHEMAS system view to discover all schemas
    that the user has access to in the specified database, including local schemas,
    external schemas, and shared schemas from datashares.

    ## Usage Requirements

    - Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
    - The cluster must be available and accessible.
    - Required IAM permissions: redshift-data:ExecuteStatement, redshift-data:DescribeStatement, redshift-data:GetStatementResult.
    - The user must have access to the database to query system views.

    ## Parameters

    - cluster_identifier: The unique identifier of the Redshift cluster to query.
                         IMPORTANT: Use a valid cluster identifier from the list_clusters tool.
    - schema_database_name: The database name to list schemas for. Also used to connect to.
                           IMPORTANT: Use a valid database name from the list_databases tool.

    ## Response Structure

    Returns a list of RedshiftSchema objects with the following structure:

    - database_name: The name of the database where the schema exists.
    - schema_name: The name of the schema.
    - schema_owner: The user ID of the schema owner.
    - schema_type: The type of the schema (external, local, or shared).
    - schema_acl: The permissions for the specified user or user group for the schema.
    - source_database: The name of the source database for external schema.
    - schema_option: The options of the schema (external schema attribute).

    ## Usage Tips

    1. First use list_clusters to get valid cluster identifiers.
    2. Then use list_databases to get valid database names for the cluster.
    3. Ensure the cluster status is 'available' before querying schemas.
    4. Note schema types to understand if they are local, external, or shared.
    5. External schemas connect to external data sources like S3 or other databases.

    ## Interpretation Best Practices

    1. Focus on 'local' schema types for cluster-native schemas.
    2. 'external' schema types indicate connections to external data sources.
    3. 'shared' schema types indicate schemas from datashares.
    4. Use schema names for subsequent table and column discovery.
    5. Consider schema permissions (schema_acl) for access planning.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_identifier` | string | Yes | The cluster identifier to query for schemas. Must be a valid cluster identifier from the list_clusters tool. |
| `schema_database_name` | string | Yes | The database name to list schemas for. Also used to connect to. Must be a valid database name from the list_databases tool. |

## AWS CLI

```bash
aws redshift describe-schemas --cluster-identifier <cluster_identifier> --database-name <schema_database_name>
```

## boto3

```python
import boto3

client = boto3.client('redshift')
response = client.describe_schemas(
    ClusterIdentifier=cluster_identifier,
    DatabaseName=schema_database_name,
)
```
