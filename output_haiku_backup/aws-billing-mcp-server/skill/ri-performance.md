---
name: ri-performance
description: Retrieves AWS Reserved Instance (RI) coverage and utilization data using the Cost Explorer API.

This tool provides insights into your Reserved Instance (RI) and Savings Plans usage patterns through two main operations:

1. get_reservation_coverage: Shows how much of your eligible usage is covered by RIs
   - Helps identify opportunities to purchase additional RIs
   - Supports grouping by dimensions like REGION, INSTANCE_TYPE, etc.
   - Can filter by specific services, regions, or instance types

2. get_reservation_utilization: Shows how effectively you're using your purchased RIs
   - Reveals underutilized or idle reserved capacity
   - Can be grouped by SUBSCRIPTION_ID to see utilization per RI
   - Helps identify RIs that could be modified or sold in the marketplace

Supported dimensions for grouping reservation coverage:
- AZ: Availability Zone
- INSTANCE_TYPE: Instance type (e.g., m4.xlarge)
- LINKED_ACCOUNT: Member accounts in organization
- PLATFORM: Operating system
- REGION: AWS Region
- SERVICE: AWS service (EC2, RDS, etc.)
- TENANCY: Instance tenancy (default, dedicated)

Reservation utilization can only be grouped by SUBSCRIPTION_ID.
---

# Ri-Performance

Retrieves AWS Reserved Instance (RI) coverage and utilization data using the Cost Explorer API.

This tool provides insights into your Reserved Instance (RI) and Savings Plans usage patterns through two main operations:

1. get_reservation_coverage: Shows how much of your eligible usage is covered by RIs
   - Helps identify opportunities to purchase additional RIs
   - Supports grouping by dimensions like REGION, INSTANCE_TYPE, etc.
   - Can filter by specific services, regions, or instance types

2. get_reservation_utilization: Shows how effectively you're using your purchased RIs
   - Reveals underutilized or idle reserved capacity
   - Can be grouped by SUBSCRIPTION_ID to see utilization per RI
   - Helps identify RIs that could be modified or sold in the marketplace

Supported dimensions for grouping reservation coverage:
- AZ: Availability Zone
- INSTANCE_TYPE: Instance type (e.g., m4.xlarge)
- LINKED_ACCOUNT: Member accounts in organization
- PLATFORM: Operating system
- REGION: AWS Region
- SERVICE: AWS service (EC2, RDS, etc.)
- TENANCY: Instance tenancy (default, dedicated)

Reservation utilization can only be grouped by SUBSCRIPTION_ID.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | Yes |  |
| `start_date` | string | No |  |
| `end_date` | string | No |  |
| `granularity` | string | No |  |
| `metrics` | string | No |  |
| `group_by` | string | No |  |
| `filter` | string | No |  |
| `sort_by` | string | No |  |
| `max_results` | string | No |  |

## AWS CLI

```bash
aws ce get-reservation-coverage --time-period <start_date> --granularity <granularity> --metrics <metrics> --group-by <group_by> --filter <filter> --sort-by <sort_by> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_reservation_coverage(
    TimePeriod=start_date,
    Granularity=granularity,
    Metrics=metrics,
    GroupBy=group_by,
    Filter=filter,
    SortBy=sort_by,
    MaxResults=max_results,
)
```
