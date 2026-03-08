---
name: get-logs-insight-query-results
description: Retrieves the results of a previously started CloudWatch Logs Insights query.

        Usage: If a log query is started by execute_log_insights_query tool and has a polling time out, this tool can be used to try to retrieve
        the query results again.

        Returns:
        --------
            A dictionary containing the final query results, including:
                - status: The current status of the query (e.g., Scheduled, Running, Complete, Failed, etc.)
                - results: A list of the actual query results if the status is Complete.
                - statistics: Query performance statistics
                - messages: Any informational messages about the query
        
---

# Get Logs Insight Query Results

Retrieves the results of a previously started CloudWatch Logs Insights query.

        Usage: If a log query is started by execute_log_insights_query tool and has a polling time out, this tool can be used to try to retrieve
        the query results again.

        Returns:
        --------
            A dictionary containing the final query results, including:
                - status: The current status of the query (e.g., Scheduled, Running, Complete, Failed, etc.)
                - results: A list of the actual query results if the status is Complete.
                - statistics: Query performance statistics
                - messages: Any informational messages about the query
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query_id` | string | Yes | The unique ID of the query to retrieve the results for. CRITICAL: This ID is returned by the execute_log_insights_query tool. |
| `region` | string | No | AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set. |
| `profile_name` | string | No | AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain. |

## AWS CLI

```bash
aws logs get-query-results --query-id <query_id> --region <region> --profile <profile_name>
```

## boto3

```python
import boto3

client = boto3.client('logs')
response = client.get_query_results(
    QueryId=query_id,
    LogGroupName=None,
)
```
