---
name: session-sql
description: Execute SQL queries on the persistent session database.

This tool queries tables created by other tools (like cost_explorer_sql) within the current session.
All tools share the same database, allowing cross-tool data analysis and joins.

Use this tool to:
- Query tables created by cost_explorer_sql and other tools
- Join data from multiple AWS APIs
- Perform complex analysis across different data sources

Common queries:
- SELECT name FROM sqlite_master WHERE type='table' -- List all tables
- SELECT * FROM [table_name] LIMIT 10 -- Preview table data
---

# Session-Sql

Execute SQL queries on the persistent session database.

This tool queries tables created by other tools (like cost_explorer_sql) within the current session.
All tools share the same database, allowing cross-tool data analysis and joins.

Use this tool to:
- Query tables created by cost_explorer_sql and other tools
- Join data from multiple AWS APIs
- Perform complex analysis across different data sources

Common queries:
- SELECT name FROM sqlite_master WHERE type='table' -- List all tables
- SELECT * FROM [table_name] LIMIT 10 -- Preview table data

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes |  |
| `schema` | string | No |  |
| `data` | string | No |  |
| `table_name` | string | No |  |

