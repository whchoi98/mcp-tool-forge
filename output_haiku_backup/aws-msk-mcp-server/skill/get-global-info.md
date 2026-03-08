---
name: get-global-info
description: Gets global information about MSK resources.
---

# Get Global Info

Gets global information about MSK resources.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region |
| `info_type` | string | No | Type of information to retrieve (clusters, configurations, vpc_connections, kafka_versions, all) |
| `kwargs` | object | No | Additional arguments specific to each info type |

