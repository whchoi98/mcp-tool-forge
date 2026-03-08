---
name: list-topics
description: Returns all topics in an MSK cluster.
---

# List Topics

Returns all topics in an MSK cluster.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region |
| `cluster_arn` | string | Yes | The Amazon Resource Name (ARN) that uniquely identifies the cluster |
| `topic_name_filter` | string | No | Returns topics starting with given name |
| `max_results` | string | No | The maximum number of results to return in the response (default maximum 100 results per API call) |
| `next_token` | string | No | The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response |

## AWS CLI

```bash
aws kafka list-topics --cluster-arn <cluster_arn> --max-results <max_results> --next-token <next_token> --filter <topic_name_filter>
```

## boto3

```python
import boto3

client = boto3.client('kafka')
response = client.list_topics(
    ClusterArn=cluster_arn,
    MaxResults=max_results,
    NextToken=next_token,
    Filter=topic_name_filter,
)
```
