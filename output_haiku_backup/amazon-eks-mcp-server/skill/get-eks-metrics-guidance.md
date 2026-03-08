---
name: get-eks-metrics-guidance
description: Get CloudWatch metrics guidance for specific resource types in EKS clusters.

        This tool provides information about available CloudWatch metrics that are in the `ContainerInsights` naemspace for different resource types
        in EKS clusters, including metric names, dimensions, and descriptions to help with monitoring and troubleshooting.
        It's particularly useful for determining the correct dimensions to use with the get_cloudwatch_metrics tool.

        ## Response Information
        The response includes a list of metrics with their names, descriptions, and required dimensions
        for the specified resource type.

        ## Usage Tips
        - Use this tool before calling get_cloudwatch_metrics to determine the correct dimensions
        - For pod metrics, note that FullPodName has a random suffix while PodName doesn't
        - Different metrics require different dimension combinations

        Args:
            ctx: MCP context
            resource_type: Type of resource to get metrics for (cluster, node, pod, namespace, service)

        Returns:
            List of metrics with their details
        
---

# Get Eks Metrics Guidance

Get CloudWatch metrics guidance for specific resource types in EKS clusters.

        This tool provides information about available CloudWatch metrics that are in the `ContainerInsights` naemspace for different resource types
        in EKS clusters, including metric names, dimensions, and descriptions to help with monitoring and troubleshooting.
        It's particularly useful for determining the correct dimensions to use with the get_cloudwatch_metrics tool.

        ## Response Information
        The response includes a list of metrics with their names, descriptions, and required dimensions
        for the specified resource type.

        ## Usage Tips
        - Use this tool before calling get_cloudwatch_metrics to determine the correct dimensions
        - For pod metrics, note that FullPodName has a random suffix while PodName doesn't
        - Different metrics require different dimension combinations

        Args:
            ctx: MCP context
            resource_type: Type of resource to get metrics for (cluster, node, pod, namespace, service)

        Returns:
            List of metrics with their details
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_type` | string | Yes | Type of resource to get metrics for (cluster, node, pod, namespace, service) |

## AWS CLI

```bash
aws cloudwatch list-metrics --namespace <AWS/EKS> --metric-name <resource_type>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.list_metrics(
    Namespace=AWS/EKS,
    MetricName=resource_type,
)
```
