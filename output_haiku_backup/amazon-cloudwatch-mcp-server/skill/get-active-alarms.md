---
name: get-active-alarms
description: Gets all CloudWatch Alarms currently in ALARM state.

        This tool retrieves all CloudWatch Alarms that are currently in the ALARM state,
        including both metric alarms and composite alarms. Results are optimized for
        LLM reasoning with summary-level information.

        Usage: Use this tool to get an overview of all active alarms in your AWS account
        for troubleshooting, monitoring, and operational awareness.

        Args:
            ctx: The MCP context object for error handling and logging.
            max_items: Maximum number of alarms to return (default: 50).
            region: AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.
            profile_name: AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.

        Returns:
            ActiveAlarmsResponse: Response containing active alarms.

        Example:
            result = await get_active_alarms(ctx, max_items=25)
            if isinstance(result, ActiveAlarmsResponse):
                print(f"Found {len(result.metric_alarms + result.composite_alarms)} active alarms")
                for alarm in result.metric_alarms:
                    print(f"Metric Alarm: {alarm.alarm_name}")
                for alarm in result.composite_alarms:
                    print(f"Composite Alarm: {alarm.alarm_name}")
        
---

# Get Active Alarms

Gets all CloudWatch Alarms currently in ALARM state.

        This tool retrieves all CloudWatch Alarms that are currently in the ALARM state,
        including both metric alarms and composite alarms. Results are optimized for
        LLM reasoning with summary-level information.

        Usage: Use this tool to get an overview of all active alarms in your AWS account
        for troubleshooting, monitoring, and operational awareness.

        Args:
            ctx: The MCP context object for error handling and logging.
            max_items: Maximum number of alarms to return (default: 50).
            region: AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set.
            profile_name: AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain.

        Returns:
            ActiveAlarmsResponse: Response containing active alarms.

        Example:
            result = await get_active_alarms(ctx, max_items=25)
            if isinstance(result, ActiveAlarmsResponse):
                print(f"Found {len(result.metric_alarms + result.composite_alarms)} active alarms")
                for alarm in result.metric_alarms:
                    print(f"Metric Alarm: {alarm.alarm_name}")
                for alarm in result.composite_alarms:
                    print(f"Composite Alarm: {alarm.alarm_name}")
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `max_items` | string | No | Maximum number of alarms to return (default: 50). Large values may cause context window overflow and impact LLM performance. |
| `region` | string | No | AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set. |
| `profile_name` | string | No | AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain. |

## AWS CLI

```bash
aws cloudwatch describe-alarms --max-records <max_items> --state-value <ALARM> --region <region> --profile <profile_name>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.describe_alarms(
    MaxRecords=max_items,
    StateValue=ALARM,
)
```
