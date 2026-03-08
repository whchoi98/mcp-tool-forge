---
name: cost-anomaly
description: Retrieves AWS cost anomalies using the Cost Explorer GetAnomalies API.

This tool allows you to retrieve cost anomalies detected on your AWS account during a specified time period.
Anomalies are available for up to 90 days.

You can filter anomalies by:
- Date range (required)
- Monitor ARN (optional)
- Feedback status (optional)
- Total impact (optional)

Feedback status options:
- YES: Anomalies marked as accurate
- NO: Anomalies marked as inaccurate
- PLANNED_ACTIVITY: Anomalies marked as planned activities
---

# Cost-Anomaly

Retrieves AWS cost anomalies using the Cost Explorer GetAnomalies API.

This tool allows you to retrieve cost anomalies detected on your AWS account during a specified time period.
Anomalies are available for up to 90 days.

You can filter anomalies by:
- Date range (required)
- Monitor ARN (optional)
- Feedback status (optional)
- Total impact (optional)

Feedback status options:
- YES: Anomalies marked as accurate
- NO: Anomalies marked as inaccurate
- PLANNED_ACTIVITY: Anomalies marked as planned activities

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `start_date` | string | Yes |  |
| `end_date` | string | Yes |  |
| `monitor_arn` | string | No |  |
| `feedback` | string | No |  |
| `max_results` | string | No |  |
| `total_impact_operator` | string | No |  |
| `total_impact_start` | string | No |  |
| `total_impact_end` | string | No |  |

## AWS CLI

```bash
aws ce get-anomalies --start-date <start_date> --end-date <end_date> --monitor-arn <monitor_arn> --feedback <feedback> --max-results <max_results> --total-impact-operator <total_impact_operator> --total-impact-start <total_impact_start> --total-impact-end <total_impact_end>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_anomalies(
    StartDate=start_date,
    EndDate=end_date,
    MonitorArn=monitor_arn,
    Feedback=feedback,
    MaxResults=max_results,
    TotalImpact={'Operator': 'total_impact_operator', 'StartValue': 'total_impact_start', 'EndValue': 'total_impact_end'},
)
```
