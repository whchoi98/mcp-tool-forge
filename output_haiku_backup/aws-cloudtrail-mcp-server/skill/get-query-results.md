---
name: get-query-results
description: Get the results of a completed CloudTrail Lake query with pagination support.

        This tool retrieves the results of a previously executed CloudTrail Lake query. It supports
        pagination for large result sets, allowing you to fetch results in chunks.

        Usage: Use this tool to get the results of a query that has completed (status = 'FINISHED').
        For large result sets, use the next_token to fetch subsequent pages of results.

        Pagination workflow:
        1. Call get_query_results with just the query_id to get the first page
        2. If next_token is returned, call again with the same query_id and the next_token
        3. Repeat until next_token is null/empty

        Returns:
        --------
        QueryResult containing:
            - query_id: The query identifier
            - query_status: Current status of the query
            - query_result_rows: Results for this page
            - next_token: Token for next page (null if no more pages)
            - query_statistics: Performance statistics for the query
        
---

# Get Query Results

Get the results of a completed CloudTrail Lake query with pagination support.

        This tool retrieves the results of a previously executed CloudTrail Lake query. It supports
        pagination for large result sets, allowing you to fetch results in chunks.

        Usage: Use this tool to get the results of a query that has completed (status = 'FINISHED').
        For large result sets, use the next_token to fetch subsequent pages of results.

        Pagination workflow:
        1. Call get_query_results with just the query_id to get the first page
        2. If next_token is returned, call again with the same query_id and the next_token
        3. Repeat until next_token is null/empty

        Returns:
        --------
        QueryResult containing:
            - query_id: The query identifier
            - query_status: Current status of the query
            - query_result_rows: Results for this page
            - next_token: Token for next page (null if no more pages)
            - query_statistics: Performance statistics for the query
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query_id` | string | Yes | The ID of the query to get results for |
| `max_results` | string | No | Maximum number of results to return per page (1-50, default: 50) |
| `next_token` | string | No | Token for pagination to fetch the next page of results. Use the next_token returned from a previous call to get successive pages. |
| `region` | string | No | AWS region to query. Defaults to us-east-1. |

## AWS CLI

```bash
aws cloudtrail get-query-results --query-id <query_id> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('cloudtrail')
response = client.get_query_results(
    QueryId=query_id,
    MaxResults=max_results,
    NextToken=next_token,
)
```
