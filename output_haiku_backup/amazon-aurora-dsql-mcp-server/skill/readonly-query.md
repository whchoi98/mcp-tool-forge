---
name: readonly-query
description: Run a read-only SQL query against the configured Aurora DSQL cluster.

Aurora DSQL is distributed SQL database with Postgres compatibility. The following table
summarizes `SELECT` functionality that is expected to work. Items not in this table may
also be supported, as this is a point in time snapshot.
| Primary clause                  | Supported clauses     |
|---------------------------------|-----------------------|
| FROM                            |                       |
| GROUP BY                        | ALL, DISTINCT         |
| ORDER BY                        | ASC, DESC, NULLS      |
| LIMIT                           |                       |
| DISTINCT                        |                       |
| HAVING                          |                       |
| USING                           |                       |
| WITH (common table expressions) |                       |
| INNER JOIN                      | ON                    |
| OUTER JOIN                      | LEFT, RIGHT, FULL, ON |
| CROSS JOIN                      | ON                    |
| UNION                           | ALL                   |
| INTERSECT                       | ALL                   |
| EXCEPT                          | ALL                   |
| OVER                            | RANK (), PARTITION BY |
| FOR UPDATE                      |                       |

---

# Readonly Query

Run a read-only SQL query against the configured Aurora DSQL cluster.

Aurora DSQL is distributed SQL database with Postgres compatibility. The following table
summarizes `SELECT` functionality that is expected to work. Items not in this table may
also be supported, as this is a point in time snapshot.
| Primary clause                  | Supported clauses     |
|---------------------------------|-----------------------|
| FROM                            |                       |
| GROUP BY                        | ALL, DISTINCT         |
| ORDER BY                        | ASC, DESC, NULLS      |
| LIMIT                           |                       |
| DISTINCT                        |                       |
| HAVING                          |                       |
| USING                           |                       |
| WITH (common table expressions) |                       |
| INNER JOIN                      | ON                    |
| OUTER JOIN                      | LEFT, RIGHT, FULL, ON |
| CROSS JOIN                      | ON                    |
| UNION                           | ALL                   |
| INTERSECT                       | ALL                   |
| EXCEPT                          | ALL                   |
| OVER                            | RANK (), PARTITION BY |
| FOR UPDATE                      |                       |


## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sql` | string | Yes | The SQL query to run |

## AWS CLI

```bash
aws rds-data execute-statement --cluster-arn <cluster_arn> --secret-arn <secret_arn> --sql <sql>
```

## boto3

```python
import boto3

client = boto3.client('rds-data')
response = client.execute_statement(
    ClusterArn=cluster_arn,
    SecretArn=secret_arn,
    Sql=sql,
)
```
