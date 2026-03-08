---
name: modify-cache-cluster
description: Modify an existing Amazon ElastiCache cache cluster.
---

# Modify-Cache-Cluster

Modify an existing Amazon ElastiCache cache cluster.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | string | Yes |  |

## AWS CLI

```bash
aws elasticache modify-cache-cluster --cache-cluster-id <request>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.modify_cache_cluster(
    CacheClusterId=request,
)
```
