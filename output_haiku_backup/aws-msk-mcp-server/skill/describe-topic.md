---
name: describe-topic
description: Returns details for a specific topic on an MSK cluster.
---

# Describe Topic

Returns details for a specific topic on an MSK cluster.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region |
| `cluster_arn` | string | Yes | The Amazon Resource Name (ARN) that uniquely identifies the cluster |
| `topic_name` | string | Yes | The name of the topic to describe |

## AWS CLI

```bash
aws kafka describe-topic --cluster-arn <cluster_arn> --topic-name <topic_name> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('kafka')
response = client.describe_topic(
    ClusterArn=cluster_arn,
    TopicName=topic_name,
)
```
