---
name: get-cluster-best-practices
description: Gets best practices and quotas for AWS MSK clusters.
---

# Get Cluster Best Practices

Gets best practices and quotas for AWS MSK clusters.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `instance_type` | string | Yes | The AWS MSK broker instance type (e.g., kafka.m5.large, kafka.m5.xlarge, express.m7g.large) |
| `number_of_brokers` | integer | Yes | The total number of brokers in the MSK cluster |

## AWS CLI

```bash
aws kafka describe-cluster-operation --cluster-operation-arn <instance_type> --number-of-broker-nodes <number_of_brokers>
```

## boto3

```python
import boto3

client = boto3.client('kafka')
response = client.describe_cluster_operation(
    ClusterOperationArn=instance_type,
    NumberOfBrokerNodes=number_of_brokers,
)
```
