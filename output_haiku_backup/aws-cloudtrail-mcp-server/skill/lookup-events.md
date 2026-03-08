---
name: lookup-events
description: Look up CloudTrail events based on various criteria.

        This tool searches CloudTrail events using the LookupEvents API, which provides access to the
        last 90 days of management events. You can filter by time range and search for specific
        attribute values.

        Usage: Use this tool to find CloudTrail events by various attributes like username, event name,
        resource name, etc. This is useful for security investigations, troubleshooting, and audit trails.

        IMPORTANT PAGINATION REQUIREMENTS:
        - AWS CloudTrail requires pagination tokens to be used with exactly the same parameters as the original request
        - When using next_token, you must provide the exact same start_time, end_time, attribute_key, and attribute_value
        - Use the 'query_params' returned in the response for subsequent paginated requests

        Returns:
        --------
        Dictionary containing:
            - events: List of CloudTrail events matching the criteria with exact CloudTrail schema
            - next_token: Token for pagination if more results available
            - query_params: Parameters used for the query (includes pagination parameters when next_token is present)
        
---

# Lookup Events

Look up CloudTrail events based on various criteria.

        This tool searches CloudTrail events using the LookupEvents API, which provides access to the
        last 90 days of management events. You can filter by time range and search for specific
        attribute values.

        Usage: Use this tool to find CloudTrail events by various attributes like username, event name,
        resource name, etc. This is useful for security investigations, troubleshooting, and audit trails.

        IMPORTANT PAGINATION REQUIREMENTS:
        - AWS CloudTrail requires pagination tokens to be used with exactly the same parameters as the original request
        - When using next_token, you must provide the exact same start_time, end_time, attribute_key, and attribute_value
        - Use the 'query_params' returned in the response for subsequent paginated requests

        Returns:
        --------
        Dictionary containing:
            - events: List of CloudTrail events matching the criteria with exact CloudTrail schema
            - next_token: Token for pagination if more results available
            - query_params: Parameters used for the query (includes pagination parameters when next_token is present)
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `start_time` | string | No | Start time for event lookup (ISO format or relative like "1 day ago"). IMPORTANT: When using pagination (next_token), you must provide the exact same start_time as the original request. |
| `end_time` | string | No | End time for event lookup (ISO format or relative like "1 hour ago"). IMPORTANT: When using pagination (next_token), you must provide the exact same end_time as the original request. |
| `attribute_key` | string | No | Attribute to search by |
| `attribute_value` | string | No | Value to search for in the specified attribute |
| `max_results` | string | No | Maximum number of events to return (1-50, default: 10) |
| `next_token` | string | No | Token for pagination to fetch the next page of events. IMPORTANT: When using this token, all other parameters (start_time, end_time, attribute_key, attribute_value) must match exactly the original request that generated this token. |
| `region` | string | No | AWS region to query. Defaults to us-east-1. |

## AWS CLI

```bash
aws cloudtrail lookup-events --start-time <start_time> --end-time <end_time> --attribute-key <attribute_key> --attribute-value <attribute_value> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('cloudtrail')
response = client.lookup_events(
    StartTime=start_time,
    EndTime=end_time,
    AttributeKey=attribute_key,
    AttributeValue=attribute_value,
    MaxResults=max_results,
    NextToken=next_token,
)
```
