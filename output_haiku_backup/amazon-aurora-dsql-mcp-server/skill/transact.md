---
name: transact
description: Execute SQL statements in a transaction against the configured Aurora DSQL cluster.

Aurora DSQL is a distributed SQL database with Postgres compatibility. This tool will automatically
insert `BEGIN` and `COMMIT` statements; you only need to provide the statements to run
within the transaction scope.

## Behavior by Mode

**READ-ONLY MODE:**
- Use this tool for read operations that require transactional consistency (point-in-time snapshots)
- Multiple SELECT queries will see data as it existed at transaction start time
- All statements are validated before execution - NO write operations allowed
- Prohibited operations: mutating queries ie. INSERT, UPDATE, DELETE, CREATE, DROP etc.
- Allowed operations: SELECT, SHOW, EXPLAIN (read-only queries only)

**READ-WRITE MODE:**
- Use this tool for any write or modify operations
- Supports all DDL statements (CREATE TABLE, CREATE INDEX, etc.)
- Supports all DML statements (INSERT, UPDATE, DELETE)
- Best practice: Use UUIDs for new tables to spread workload across nodes
- Async DDL commands (like CREATE INDEX ASYNC) return a job id
- View jobs with: SELECT * FROM sys.jobs

## When to Use Transact vs readonly_query

- Use `transact` when you need multiple queries to see consistent data (same point in time)
- Use `readonly_query` for single read queries that don't need transactional isolation
- In read-only mode, both tools validate against write operations

## Examples

Read-only mode - consistent multi-query read:
```
transact(["SELECT COUNT(*) FROM orders", "SELECT SUM(total) FROM orders"])
```

Read-write mode - create and populate table:
```
transact([
  "CREATE TABLE users (id UUID PRIMARY KEY, name TEXT)",
  "INSERT INTO users VALUES (gen_random_uuid(), 'Alice')"
])
```

---

# Transact

Execute SQL statements in a transaction against the configured Aurora DSQL cluster.

Aurora DSQL is a distributed SQL database with Postgres compatibility. This tool will automatically
insert `BEGIN` and `COMMIT` statements; you only need to provide the statements to run
within the transaction scope.

## Behavior by Mode

**READ-ONLY MODE:**
- Use this tool for read operations that require transactional consistency (point-in-time snapshots)
- Multiple SELECT queries will see data as it existed at transaction start time
- All statements are validated before execution - NO write operations allowed
- Prohibited operations: mutating queries ie. INSERT, UPDATE, DELETE, CREATE, DROP etc.
- Allowed operations: SELECT, SHOW, EXPLAIN (read-only queries only)

**READ-WRITE MODE:**
- Use this tool for any write or modify operations
- Supports all DDL statements (CREATE TABLE, CREATE INDEX, etc.)
- Supports all DML statements (INSERT, UPDATE, DELETE)
- Best practice: Use UUIDs for new tables to spread workload across nodes
- Async DDL commands (like CREATE INDEX ASYNC) return a job id
- View jobs with: SELECT * FROM sys.jobs

## When to Use Transact vs readonly_query

- Use `transact` when you need multiple queries to see consistent data (same point in time)
- Use `readonly_query` for single read queries that don't need transactional isolation
- In read-only mode, both tools validate against write operations

## Examples

Read-only mode - consistent multi-query read:
```
transact(["SELECT COUNT(*) FROM orders", "SELECT SUM(total) FROM orders"])
```

Read-write mode - create and populate table:
```
transact([
  "CREATE TABLE users (id UUID PRIMARY KEY, name TEXT)",
  "INSERT INTO users VALUES (gen_random_uuid(), 'Alice')"
])
```


## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `sql_list` | array | Yes | List of one or more SQL statements to execute in a transaction |

