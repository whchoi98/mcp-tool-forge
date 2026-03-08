---
name: get-alarm-history
description: Gets the history for a CloudWatch alarm with time range suggestions for investigation.

        This tool retrieves the history for a specified CloudWatch alarm, focusing primarily
        on state transitions to ALARM state. It also provides suggested time ranges for
        investigation based on the alarm's configuration and history.

        Usage: Use this tool to understand when an alarm fired and get useful time ranges
        for investigating the underlying issue using other CloudWatch tools. The tool is
        particularly useful for identifying patterns like alarm flapping (going in and out
        of alarm state frequently).

        Args:
            ctx: The MCP context object for error handling and logging.
            region: AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.
            alarm_name: Name of the alarm to retrieve history for.
            start_time: Optional start time for the history query. Defaults to 24 hours ago.
            end_time: Optional end time for the history query. Defaults to current time.
            history_item_type: Optional type of history items to retrieve. Defaults to 'StateUpdate'.
            max_items: Maximum number of history items to return. Defaults to 50.
            include_component_alarms: For composite alarms, whether to include details about component alarms.
            profile_name: AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.

        Returns:
            Union[AlarmHistoryResponse, CompositeAlarmComponentResponse]: Either a response containing
            alarm history with time range suggestions, or component alarm details for composite alarms.

        Example:
            result = await get_alarm_history(
                ctx,
                alarm_name="my-cpu-alarm",
                start_time="2025-06-18T00:00:00Z",
                end_time="2025-06-19T00:00:00Z"
            )
            if isinstance(result, AlarmHistoryResponse):
                print(f"Found {len(result.history_items)} history items")
                for suggestion in result.time_range_suggestions:
                    print(f"Suggested investigation time range: {suggestion.start_time} to {suggestion.end_time}")
        
---

# Get Alarm History

Gets the history for a CloudWatch alarm with time range suggestions for investigation.

        This tool retrieves the history for a specified CloudWatch alarm, focusing primarily
        on state transitions to ALARM state. It also provides suggested time ranges for
        investigation based on the alarm's configuration and history.

        Usage: Use this tool to understand when an alarm fired and get useful time ranges
        for investigating the underlying issue using other CloudWatch tools. The tool is
        particularly useful for identifying patterns like alarm flapping (going in and out
        of alarm state frequently).

        Args:
            ctx: The MCP context object for error handling and logging.
            region: AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.
            alarm_name: Name of the alarm to retrieve history for.
            start_time: Optional start time for the history query. Defaults to 24 hours ago.
            end_time: Optional end time for the history query. Defaults to current time.
            history_item_type: Optional type of history items to retrieve. Defaults to 'StateUpdate'.
            max_items: Maximum number of history items to return. Defaults to 50.
            include_component_alarms: For composite alarms, whether to include details about component alarms.
            profile_name: AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.

        Returns:
            Union[AlarmHistoryResponse, CompositeAlarmComponentResponse]: Either a response containing
            alarm history with time range suggestions, or component alarm details for composite alarms.

        Example:
            result = await get_alarm_history(
                ctx,
                alarm_name="my-cpu-alarm",
                start_time="2025-06-18T00:00:00Z",
                end_time="2025-06-19T00:00:00Z"
            )
            if isinstance(result, AlarmHistoryResponse):
                print(f"Found {len(result.history_items)} history items")
                for suggestion in result.time_range_suggestions:
                    print(f"Suggested investigation time range: {suggestion.start_time} to {suggestion.end_time}")
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `alarm_name` | string | Yes | Name of the alarm to retrieve history for |
| `start_time` | string | No | The start time for the history query in ISO format (e.g., '2023-01-01T00:00:00Z') or as a datetime object. Defaults to 24 hours ago. |
| `end_time` | string | No | The end time for the history query in ISO format (e.g., '2023-01-01T00:00:00Z') or as a datetime object. Defaults to current time. |
| `history_item_type` | string | No | Type of history items to retrieve. Possible values: 'ConfigurationUpdate', 'StateUpdate', 'Action'. Defaults to 'StateUpdate'. |
| `max_items` | string | No | Maximum number of history items to return (default: 50). Large values may cause context window overflow and impact LLM performance. Adjust time-range to limit responses. |
| `include_component_alarms` | string | No | For composite alarms, whether to include details about component alarms. Defaults to false. |
| `region` | string | No | AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set. |
| `profile_name` | string | No | AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain. |

## AWS CLI

```bash
aws cloudwatch describe-alarm-history --alarm-name <alarm_name> --start-date <start_time> --end-date <end_time> --history-item-type <history_item_type> --max-records <max_items> --scan-by <include_component_alarms> --region <region> --profile <profile_name>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.describe_alarm_history(
    AlarmName=alarm_name,
    StartDate=start_time,
    EndDate=end_time,
    HistoryItemType=history_item_type,
    MaxRecords=max_items,
    ScanBy=include_component_alarms,
)
```
