---
name: describe-topic-partitions
description: Returns partition information for a specific topic on an MSK cluster.
---

# Describe Topic Partitions

Returns partition information for a specific topic on an MSK cluster.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region |
| `cluster_arn` | string | Yes | The Amazon Resource Name (ARN) that uniquely identifies the cluster |
| `topic_name` | string | Yes | The name of the topic to describe partitions for |
| `max_results` | string | No | Maximum number of partitions to return |
| `next_token` | string | No | Token for pagination |

## AWS CLI

```bash
aws kafka list-cluster-operations --cluster-arn <cluster_arn> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('kafka')
response = client.list_cluster_operations(
    ClusterArn=cluster_arn,
    MaxResults=max_results,
    NextToken=next_token,
)
```
