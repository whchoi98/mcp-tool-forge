---
name: connect-jump-host-cache-cluster
description: Configures an existing EC2 instance as a jump host to access an ElastiCache cluster.

    Args:
        cache_cluster_id (str): ID of the ElastiCache cluster to connect to
        instance_id (str): ID of the EC2 instance to use as jump host

    Returns:
        Dict[str, Any]: Dictionary containing connection details and configuration status

    Raises:
        ValueError: If VPC compatibility check fails or required resources not found
    
---

# Connect-Jump-Host-Cache-Cluster

Configures an existing EC2 instance as a jump host to access an ElastiCache cluster.

    Args:
        cache_cluster_id (str): ID of the ElastiCache cluster to connect to
        instance_id (str): ID of the EC2 instance to use as jump host

    Returns:
        Dict[str, Any]: Dictionary containing connection details and configuration status

    Raises:
        ValueError: If VPC compatibility check fails or required resources not found
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cache_cluster_id` | string | Yes |  |
| `instance_id` | string | Yes |  |

## AWS CLI

```bash
aws elasticache describe-cache-clusters --cache-cluster-id <cache_cluster_id>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.describe_cache_clusters(
    CacheClusterId=cache_cluster_id,
)
```
