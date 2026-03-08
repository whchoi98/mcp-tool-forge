---
name: get-eks-insights
description: Get EKS Insights for cluster configuration and upgrade readiness.

        This tool retrieves Amazon EKS Insights that identify potential issues with
        your EKS cluster. These insights help identify both cluster configuration issues
        and upgrade readiness concerns that might affect hybrid nodes functionality.

        Amazon EKS provides two types of insights:
        - MISCONFIGURATION insights: Identify misconfigurations in your EKS cluster setup
        - UPGRADE_READINESS insights: Identify issues that could prevent successful cluster upgrades

        When used without an insight_id, it returns a list of all insights.
        When used with an insight_id, it returns detailed information about
        that specific insight, including recommendations.

        ## Requirements
        - The server must be run with the `--allow-sensitive-data-access` flag

        ## Response Information
        The response includes insight details such as status, description, and
        recommendations for addressing identified issues.

        ## Usage Tips
        - Review MISCONFIGURATION insights to identify cluster misconfigurations
        - Check UPGRADE_READINESS insights before upgrading your cluster
        - Pay special attention to insights with FAILING status
        - Focus on insights related to node and network configuration for hybrid nodes

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster
            insight_id: Optional ID of a specific insight to get detailed information for
            category: Optional category to filter insights by (e.g., "MISCONFIGURATION" or "UPGRADE_READINESS")
            next_token: Optional token for pagination to get the next set of results

        Returns:
            EksInsightsResponse with insights information
        
---

# Get Eks Insights

Get EKS Insights for cluster configuration and upgrade readiness.

        This tool retrieves Amazon EKS Insights that identify potential issues with
        your EKS cluster. These insights help identify both cluster configuration issues
        and upgrade readiness concerns that might affect hybrid nodes functionality.

        Amazon EKS provides two types of insights:
        - MISCONFIGURATION insights: Identify misconfigurations in your EKS cluster setup
        - UPGRADE_READINESS insights: Identify issues that could prevent successful cluster upgrades

        When used without an insight_id, it returns a list of all insights.
        When used with an insight_id, it returns detailed information about
        that specific insight, including recommendations.

        ## Requirements
        - The server must be run with the `--allow-sensitive-data-access` flag

        ## Response Information
        The response includes insight details such as status, description, and
        recommendations for addressing identified issues.

        ## Usage Tips
        - Review MISCONFIGURATION insights to identify cluster misconfigurations
        - Check UPGRADE_READINESS insights before upgrading your cluster
        - Pay special attention to insights with FAILING status
        - Focus on insights related to node and network configuration for hybrid nodes

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster
            insight_id: Optional ID of a specific insight to get detailed information for
            category: Optional category to filter insights by (e.g., "MISCONFIGURATION" or "UPGRADE_READINESS")
            next_token: Optional token for pagination to get the next set of results

        Returns:
            EksInsightsResponse with insights information
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_name` | string | Yes | Name of the EKS cluster |
| `insight_id` | string | No | ID of a specific insight to get detailed information for. If provided, returns detailed information about this specific insight. |
| `category` | string | No | Filter insights by category (e.g., "MISCONFIGURATION" or "UPGRADE_READINESS") |
| `next_token` | string | No | Token for pagination to get the next set of results |

## AWS CLI

```bash
aws eks list-insights --cluster-name <cluster_name> --insight-id <insight_id> --category <category> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('eks')
response = client.list_insights(
    ClusterName=cluster_name,
    InsightId=insight_id,
    Category=category,
    NextToken=next_token,
)
```
