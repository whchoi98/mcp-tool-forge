---
name: create-cache-cluster
description: Create an Amazon ElastiCache cache cluster.
---

# Create-Cache-Cluster

Create an Amazon ElastiCache cache cluster.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | string | Yes |  |

## AWS CLI

```bash
aws elasticache create-cache-cluster --cluster-name <request>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.create_cache_cluster(
    ClusterName=request,
)
```
