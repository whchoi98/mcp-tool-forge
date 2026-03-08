---
name: run-query
description: Run a SQL query against PostgreSQL
---

# Run Query

Run a SQL query against PostgreSQL

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sql` | string | Yes | The SQL query to run |
| `connection_method` | string | Yes | connection method |
| `cluster_identifier` | string | Yes | Cluster identifier |
| `db_endpoint` | string | Yes | database endpoint |
| `database` | string | Yes | database name |
| `query_parameters` | string | No | Parameters for the SQL query |

## AWS CLI

```bash
aws rds-data execute-statement --cluster-arn <cluster_identifier> --database <database> --sql <sql> --parameters <query_parameters>
```

## boto3

```python
import boto3

client = boto3.client('rds-data')
response = client.execute_statement(
    ClusterArn=cluster_identifier,
    Database=database,
    Sql=sql,
    Parameters=query_parameters,
)
```
