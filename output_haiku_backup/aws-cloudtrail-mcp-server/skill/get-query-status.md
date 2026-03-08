---
name: get-query-status
description: Get the status of a CloudTrail Lake query.

        This tool checks the status of a previously started CloudTrail Lake query. Use this
        when you need to check if a long-running query has completed or if you want to get
        details about query execution.

        Usage: Use this tool to monitor the progress of CloudTrail Lake queries, especially
        long-running ones that may take time to complete.

        Returns:
        --------
        QueryStatus containing:
            - query_id: The query identifier
            - query_status: Current status (QUEUED, RUNNING, FINISHED, FAILED, CANCELLED, TIMED_OUT)
            - query_statistics: Performance and execution statistics
            - error_message: Error details if the query failed
        
---

# Get Query Status

Get the status of a CloudTrail Lake query.

        This tool checks the status of a previously started CloudTrail Lake query. Use this
        when you need to check if a long-running query has completed or if you want to get
        details about query execution.

        Usage: Use this tool to monitor the progress of CloudTrail Lake queries, especially
        long-running ones that may take time to complete.

        Returns:
        --------
        QueryStatus containing:
            - query_id: The query identifier
            - query_status: Current status (QUEUED, RUNNING, FINISHED, FAILED, CANCELLED, TIMED_OUT)
            - query_statistics: Performance and execution statistics
            - error_message: Error details if the query failed
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query_id` | string | Yes | The ID of the query to check status for |
| `region` | string | No | AWS region to query. Defaults to us-east-1. |

## AWS CLI

```bash
aws cloudtrail get-query-results --query-id <query_id> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('cloudtrail')
response = client.get_query_results(
    QueryId=query_id,
    Region=region,
)
```
