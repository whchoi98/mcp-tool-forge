---
name: cancel-logs-insight-query
description: Cancels an ongoing CloudWatch Logs Insights query. If the query has already ended, returns an error that the given query is not running.

        Usage: If a log query is started by execute_log_insights_query tool and has a polling time out, this tool can be used to cancel
        it prematurely to avoid incurring additional costs.

        Returns:
        --------
            A LogsQueryCancelResult with a "success" key, which is True if the query was successfully cancelled.
        
---

# Cancel Logs Insight Query

Cancels an ongoing CloudWatch Logs Insights query. If the query has already ended, returns an error that the given query is not running.

        Usage: If a log query is started by execute_log_insights_query tool and has a polling time out, this tool can be used to cancel
        it prematurely to avoid incurring additional costs.

        Returns:
        --------
            A LogsQueryCancelResult with a "success" key, which is True if the query was successfully cancelled.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query_id` | string | Yes | The unique ID of the ongoing query to cancel. CRITICAL: This ID is returned by the execute_log_insights_query tool. |
| `region` | string | No | AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set. |
| `profile_name` | string | No | AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain. |

## AWS CLI

```bash
aws logs stop-query --query-id <query_id> --region <region> --profile <profile_name>
```

## boto3

```python
import boto3

client = boto3.client('logs')
response = client.stop_query(
    QueryId=query_id,
    LogGroupName=None,
)
```
