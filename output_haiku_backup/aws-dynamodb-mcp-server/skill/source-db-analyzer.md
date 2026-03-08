---
name: source-db-analyzer
description: Analyzes source database to extract schema and access patterns for DynamoDB modeling.

    WHEN TO USE: Call this tool when the user selects "Existing Database Analysis" option
    after invoking the `dynamodb_data_modeling` tool. This extracts schema and query patterns
    from an existing relational database to accelerate DynamoDB data model design.

    IMPORTANT: Always ask the user which execution mode they prefer before calling this tool.

    Execution Modes:
    - self_service: Generates SQL queries for user to run manually, then parses their results.
    - managed (MySQL only): Database connection via RDS Data API or hostname.

    Supported Databases: MySQL, PostgreSQL, SQL Server

    Output: Generates analysis files (schema structure, access patterns, relationships) in
    Markdown format. These files feed into the DynamoDB data modeling workflow to inform
    table design, GSI selection, and access pattern mapping.

    Returns: Analysis summary with file locations and next steps.
    
---

# Source Db Analyzer

Analyzes source database to extract schema and access patterns for DynamoDB modeling.

    WHEN TO USE: Call this tool when the user selects "Existing Database Analysis" option
    after invoking the `dynamodb_data_modeling` tool. This extracts schema and query patterns
    from an existing relational database to accelerate DynamoDB data model design.

    IMPORTANT: Always ask the user which execution mode they prefer before calling this tool.

    Execution Modes:
    - self_service: Generates SQL queries for user to run manually, then parses their results.
    - managed (MySQL only): Database connection via RDS Data API or hostname.

    Supported Databases: MySQL, PostgreSQL, SQL Server

    Output: Generates analysis files (schema structure, access patterns, relationships) in
    Markdown format. These files feed into the DynamoDB data modeling workflow to inform
    table design, GSI selection, and access pattern mapping.

    Returns: Analysis summary with file locations and next steps.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source_db_type` | string | Yes | Database type: 'mysql', 'postgresql', or 'sqlserver' |
| `database_name` | string | No | Database name to analyze. REQUIRED for self_service. Env: MYSQL_DATABASE. |
| `execution_mode` | string | No | 'self_service': generates SQL for user to run, then parses results. 'managed' (MySQL only): RDS Data API-based access (aws_cluster_arn) or Connection-based access (hostname+port). |
| `queries_file_path` | string | No | [self_service] Output path for generated SQL queries (Step 1). |
| `query_result_file_path` | string | No | [self_service] Path to query results file for parsing (Step 2). |
| `pattern_analysis_days` | string | No | Days of query logs to analyze. Default: 30. |
| `max_query_results` | string | No | Max rows per query. Default: 500. Env: MYSQL_MAX_QUERY_RESULTS. |
| `aws_cluster_arn` | string | No | [managed/RDS Data API-based] Aurora cluster ARN. Use this OR hostname, not both. Env: MYSQL_CLUSTER_ARN. |
| `aws_secret_arn` | string | No | [managed] Secrets Manager ARN for DB credentials. REQUIRED. Env: MYSQL_SECRET_ARN. |
| `aws_region` | string | No | [managed] AWS region. REQUIRED. Env: AWS_REGION. |
| `hostname` | string | No | [managed/connection-based] MySQL hostname. Use this OR aws_cluster_arn, not both. Env: MYSQL_HOSTNAME. |
| `port` | string | No | [managed/connection-based] MySQL port. Default: 3306. Env: MYSQL_PORT. |
| `output_dir` | string | Yes | Absolute path for output folder. Must exist and be writable. REQUIRED. |

## AWS CLI

```bash
aws rds execute-statement --cluster-arn <aws_cluster_arn> --secret-arn <aws_secret_arn> --database <database_name> --sql <queries_file_path> --max-rows <max_query_results>
```

## boto3

```python
import boto3

client = boto3.client('rds')
response = client.execute_statement(
    ClusterArn=aws_cluster_arn,
    SecretArn=aws_secret_arn,
    Database=database_name,
    SqlStatements=queries_file_path,
    ResultSetOptions={'MaxRows': 'max_query_results'},
)
```
