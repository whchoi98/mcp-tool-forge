---
name: get-cluster-telemetry
description: Gets telemetry data for MSK clusters.
---

# Get Cluster Telemetry

Gets telemetry data for MSK clusters.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region |
| `action` | string | Yes | The operation to perform (metrics, available_metrics) |
| `cluster_arn` | string | Yes | The ARN of the cluster (required for cluster operations) |
| `kwargs` | object | No | Additional arguments based on the action type |

