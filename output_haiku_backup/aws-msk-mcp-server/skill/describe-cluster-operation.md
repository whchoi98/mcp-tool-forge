---
name: describe-cluster-operation
description: Gets information about a cluster operation.
---

# Describe Cluster Operation

Gets information about a cluster operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region |
| `cluster_operation_arn` | string | Yes | The Amazon Resource Name (ARN) of the cluster operation |

## AWS CLI

```bash
aws kafka describe-cluster-operation --cluster-operation-arn <cluster_operation_arn> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('kafka')
response = client.describe_cluster_operation(
    ClusterOperationArn=cluster_operation_arn,
)
```
