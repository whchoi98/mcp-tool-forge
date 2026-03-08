---
name: get-cluster-info
description: Gets comprehensive information about MSK clusters.
---

# Get Cluster Info

Gets comprehensive information about MSK clusters.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region |
| `cluster_arn` | string | Yes | The ARN of the cluster to get information for |
| `info_type` | string | No | Type of information to retrieve (metadata, brokers, nodes, compatible_versions, policy, operations, client_vpc_connections, scram_secrets, all) |
| `kwargs` | object | No | Additional arguments specific to each info type |

