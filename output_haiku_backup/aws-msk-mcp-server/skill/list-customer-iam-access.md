---
name: list-customer-iam-access
description: Lists IAM access information for an MSK cluster.
---

# List Customer Iam Access

Lists IAM access information for an MSK cluster.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region |
| `cluster_arn` | string | Yes | The ARN of the MSK cluster |

## AWS CLI

```bash
aws kafka list-cluster-operations --cluster-arn <cluster_arn> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('kafka')
response = client.list_cluster_operations(
    ClusterArn=cluster_arn,
    Region=region,
)
```
