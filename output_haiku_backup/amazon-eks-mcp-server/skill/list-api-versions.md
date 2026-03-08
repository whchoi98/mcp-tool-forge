---
name: list-api-versions
description: List all available API versions in the Kubernetes cluster.

        This tool discovers all available API versions on the Kubernetes cluster,
        which is helpful for determining the correct apiVersion to use when
        managing Kubernetes resources. It returns both core APIs and API groups,
        useful for verifying API compatibility and discovering available resources.

        ## Response Information
        The response includes core APIs (like 'v1'), API groups with versions
        (like 'apps/v1'), extension APIs (like 'networking.k8s.io/v1'), and
        any Custom Resource Definition (CRD) APIs installed in the cluster.

        ## Usage Tips
        - Use this tool before creating or updating resources to ensure API compatibility
        - Different Kubernetes versions may have different available APIs
        - Some APIs may be deprecated or removed in newer Kubernetes versions
        - Custom resources will only appear if their CRDs are installed in the cluster

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster

        Returns:
            ApiVersionsResponse with list of available API versions
        
---

# List Api Versions

List all available API versions in the Kubernetes cluster.

        This tool discovers all available API versions on the Kubernetes cluster,
        which is helpful for determining the correct apiVersion to use when
        managing Kubernetes resources. It returns both core APIs and API groups,
        useful for verifying API compatibility and discovering available resources.

        ## Response Information
        The response includes core APIs (like 'v1'), API groups with versions
        (like 'apps/v1'), extension APIs (like 'networking.k8s.io/v1'), and
        any Custom Resource Definition (CRD) APIs installed in the cluster.

        ## Usage Tips
        - Use this tool before creating or updating resources to ensure API compatibility
        - Different Kubernetes versions may have different available APIs
        - Some APIs may be deprecated or removed in newer Kubernetes versions
        - Custom resources will only appear if their CRDs are installed in the cluster

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster

        Returns:
            ApiVersionsResponse with list of available API versions
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_name` | string | Yes | Name of the EKS cluster to query for available API versions. |

## AWS CLI

```bash
aws eks describe-cluster --cluster-name <cluster_name>
```

## boto3

```python
import boto3

client = boto3.client('eks')
response = client.describe_cluster(
    ClusterName=cluster_name,
)
```
