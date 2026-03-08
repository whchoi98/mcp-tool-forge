---
name: compute-performances-and-costs
description: Calculate DynamoDB capacity units and monthly costs from access patterns.

    Call after completing data model design. Extracts patterns from Access Pattern Mapping
    table and tables from Table Designs section in dynamodb_data_model.md.

    Args:
        access_pattern_list: Access patterns with fields:
            - operation: GetItem|Query|Scan|PutItem|UpdateItem|DeleteItem|BatchGetItem|BatchWriteItem|TransactGetItems|TransactWriteItems
            - pattern, description, table, rps (>0), item_size_bytes (1-409600)
            - item_count: required for Query/Scan/Batch/Transact operations (>0)
            - strongly_consistent: optional for GetItem/Query/Scan/BatchGetItem (default: false)
            - gsi: optional for Query/Scan (target index name)
            - gsi_list: optional for write operations (affected index names)
        table_list: Tables with name, item_count (>0), item_size_bytes (1-409600), gsi_list (each GSI needs name, item_count, item_size_bytes)
        workspace_dir: Absolute path to the folder containing dynamodb_data_model.md - report will be appended

    Returns:
        {'status': 'success', 'message': <success_message>} or {'status': 'error', 'message': <error_reason>}

    Example:
        {
          "access_pattern_list": [
            {
              "operation": "GetItem",
              "pattern": "get-user",
              "description": "Get user by ID",
              "table": "users",
              "rps": 100,
              "item_size_bytes": 2000
            },
            {
              "operation": "Query",
              "pattern": "query-by-email",
              "description": "Query user by email",
              "table": "users",
              "rps": 50,
              "item_size_bytes": 1500,
              "item_count": 1,
              "gsi": "email-index"
            },
            {
              "operation": "PutItem",
              "pattern": "put-user",
              "description": "Create user",
              "table": "users",
              "rps": 20,
              "item_size_bytes": 2000,
              "gsi_list": ["email-index", "status-index"]
            },
            {
              "operation": "Query",
              "pattern": "query-orders",
              "description": "Query user orders",
              "table": "orders",
              "rps": 50,
              "item_size_bytes": 800,
              "item_count": 10
            }
          ],
          "table_list": [
            {
              "name": "users",
              "item_size_bytes": 2500,
              "item_count": 10000,
              "gsi_list": [
                {"name": "email-index", "item_size_bytes": 1500, "item_count": 10000},
                {"name": "status-index", "item_size_bytes": 500, "item_count": 10000}
              ]
            },
            {
              "name": "orders",
              "item_size_bytes": 1024,
              "item_count": 50000
            }
          ],
          "workspace_dir": "/absolute/path/to/workspace"
        }
    
---

# Compute Performances And Costs

Calculate DynamoDB capacity units and monthly costs from access patterns.

    Call after completing data model design. Extracts patterns from Access Pattern Mapping
    table and tables from Table Designs section in dynamodb_data_model.md.

    Args:
        access_pattern_list: Access patterns with fields:
            - operation: GetItem|Query|Scan|PutItem|UpdateItem|DeleteItem|BatchGetItem|BatchWriteItem|TransactGetItems|TransactWriteItems
            - pattern, description, table, rps (>0), item_size_bytes (1-409600)
            - item_count: required for Query/Scan/Batch/Transact operations (>0)
            - strongly_consistent: optional for GetItem/Query/Scan/BatchGetItem (default: false)
            - gsi: optional for Query/Scan (target index name)
            - gsi_list: optional for write operations (affected index names)
        table_list: Tables with name, item_count (>0), item_size_bytes (1-409600), gsi_list (each GSI needs name, item_count, item_size_bytes)
        workspace_dir: Absolute path to the folder containing dynamodb_data_model.md - report will be appended

    Returns:
        {'status': 'success', 'message': <success_message>} or {'status': 'error', 'message': <error_reason>}

    Example:
        {
          "access_pattern_list": [
            {
              "operation": "GetItem",
              "pattern": "get-user",
              "description": "Get user by ID",
              "table": "users",
              "rps": 100,
              "item_size_bytes": 2000
            },
            {
              "operation": "Query",
              "pattern": "query-by-email",
              "description": "Query user by email",
              "table": "users",
              "rps": 50,
              "item_size_bytes": 1500,
              "item_count": 1,
              "gsi": "email-index"
            },
            {
              "operation": "PutItem",
              "pattern": "put-user",
              "description": "Create user",
              "table": "users",
              "rps": 20,
              "item_size_bytes": 2000,
              "gsi_list": ["email-index", "status-index"]
            },
            {
              "operation": "Query",
              "pattern": "query-orders",
              "description": "Query user orders",
              "table": "orders",
              "rps": 50,
              "item_size_bytes": 800,
              "item_count": 10
            }
          ],
          "table_list": [
            {
              "name": "users",
              "item_size_bytes": 2500,
              "item_count": 10000,
              "gsi_list": [
                {"name": "email-index", "item_size_bytes": 1500, "item_count": 10000},
                {"name": "status-index", "item_size_bytes": 500, "item_count": 10000}
              ]
            },
            {
              "name": "orders",
              "item_size_bytes": 1024,
              "item_count": 50000
            }
          ],
          "workspace_dir": "/absolute/path/to/workspace"
        }
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `access_pattern_list` | array | Yes | List of access patterns with operation details (required) |
| `table_list` | array | Yes | List of table definitions for storage cost calculation (required) |
| `workspace_dir` | string | Yes | Absolute path of the workspace directory (required). Cost analysis will be appended to dynamodb_data_model.md |

