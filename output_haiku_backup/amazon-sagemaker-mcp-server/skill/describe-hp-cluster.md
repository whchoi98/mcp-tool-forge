---
name: describe-hp-cluster
description: Describe a SageMaker HyperPod cluster.

        Args:
            ctx: MCP context
            cluster_name: REQUIRED - Target cluster for describe cluster api
            region_name: REQUIRED - AWS region name
            profile_name: AWS profile name (optional)

        ## Fallback Options:
        - If this tool fails, advise using AWS SageMaker CLI option: `aws sagemaker describe-cluster --cluster-name <name> --region <cluster_region>`
        - Or as another alternative, advise checking directly in the SageMaker HyperPod console (Amazon SageMaker AI → HyperPod Clusters → Cluster Management → select cluster)

        Returns:
            describe cluster response
        
---

# Describe Hp Cluster

Describe a SageMaker HyperPod cluster.

        Args:
            ctx: MCP context
            cluster_name: REQUIRED - Target cluster for describe cluster api
            region_name: REQUIRED - AWS region name
            profile_name: AWS profile name (optional)

        ## Fallback Options:
        - If this tool fails, advise using AWS SageMaker CLI option: `aws sagemaker describe-cluster --cluster-name <name> --region <cluster_region>`
        - Or as another alternative, advise checking directly in the SageMaker HyperPod console (Amazon SageMaker AI → HyperPod Clusters → Cluster Management → select cluster)

        Returns:
            describe cluster response
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_name` | string | Yes | The name of the cluster to describe. |
| `region_name` | string | Yes | AWS region name. Default is us-east-1. |
| `profile_name` | string | No | AWS profile name. If not provided, uses the default profile. |

## AWS CLI

```bash
aws sagemaker describe-cluster --cluster-name <cluster_name>
```

## boto3

```python
import boto3

client = boto3.client('sagemaker')
response = client.describe_cluster(
    ClusterName=cluster_name,
)
```
