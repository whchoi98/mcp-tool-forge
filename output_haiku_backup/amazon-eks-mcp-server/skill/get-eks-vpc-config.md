---
name: get-eks-vpc-config
description: Get VPC configuration for an EKS cluster.

        This tool retrieves comprehensive VPC configuration details for any EKS cluster,
        including CIDR blocks and route tables which are essential for understanding
        network connectivity. For hybrid node setups, it also automatically identifies
        and includes remote node and pod CIDR configurations.

        ## Requirements
        - The server must be run with the `--allow-sensitive-data-access` flag

        ## Response Information
        The response includes VPC CIDR blocks, route tables, and when available,
        remote CIDR configurations for hybrid node connectivity.

        ## Usage Tips
        - Understand VPC networking configuration for any EKS cluster
        - Examine route tables to verify proper network connectivity
        - For hybrid setups: Check that remote node CIDR blocks are correctly configured
        - For hybrid setups: Verify that VPC route tables include routes for hybrid node CIDRs

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster
            vpc_id: Optional ID of the specific VPC to query

        Returns:
            EksVpcConfigResponse with VPC configuration details
        
---

# Get Eks Vpc Config

Get VPC configuration for an EKS cluster.

        This tool retrieves comprehensive VPC configuration details for any EKS cluster,
        including CIDR blocks and route tables which are essential for understanding
        network connectivity. For hybrid node setups, it also automatically identifies
        and includes remote node and pod CIDR configurations.

        ## Requirements
        - The server must be run with the `--allow-sensitive-data-access` flag

        ## Response Information
        The response includes VPC CIDR blocks, route tables, and when available,
        remote CIDR configurations for hybrid node connectivity.

        ## Usage Tips
        - Understand VPC networking configuration for any EKS cluster
        - Examine route tables to verify proper network connectivity
        - For hybrid setups: Check that remote node CIDR blocks are correctly configured
        - For hybrid setups: Verify that VPC route tables include routes for hybrid node CIDRs

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster
            vpc_id: Optional ID of the specific VPC to query

        Returns:
            EksVpcConfigResponse with VPC configuration details
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_name` | string | Yes | Name of the EKS cluster to get VPC configuration for |
| `vpc_id` | string | No | ID of the specific VPC to query (optional, will use cluster VPC if not specified) |

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
