---
name: list-clusters
description: List all available Amazon Redshift clusters and serverless workgroups.

    This tool discovers and returns information about all Redshift clusters and serverless workgroups
    in your AWS account, including their current status, connection details, and configuration.

    ## Usage Requirements

    - Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
    - Required IAM permissions: redshift:DescribeClusters, redshift-serverless:ListWorkgroups, redshift-serverless:GetWorkgroup.

    ## Response Structure

    Returns a list of RedshiftCluster objects with the following structure:

    - identifier: Unique identifier for the cluster/workgroup.
    - type: Type of cluster (provisioned or serverless).
    - status: Current status of the cluster.
    - database_name: Default database name.
    - endpoint: Connection endpoint information.
    - port: Connection port.
    - vpc_id: VPC ID where the cluster resides.
    - node_type: Node type (for provisioned clusters).
    - number_of_nodes: Number of nodes (for provisioned clusters).
    - creation_time: When the cluster was created.
    - master_username: Master username for the cluster.
    - publicly_accessible: Whether the cluster is publicly accessible.
    - encrypted: Whether the cluster is encrypted.
    - tags: Tags associated with the cluster.

    ## Usage Tips

    1. Use this tool to discover available Redshift instances before attempting connections.
    2. Note the cluster identifiers for use with other database tools.
    3. Check the status field to ensure clusters are 'available' before querying.
    4. Use the endpoint and port information for direct database connections if needed.
    5. Consider the cluster type (provisioned vs serverless) when planning your queries.

    ## Interpretation Best Practices

    1. Filter results by status to find only available clusters.
    2. Use cluster identifiers as input for other Redshift tools.
    3. Consider cluster configuration (node type, encryption) for performance planning.
    4. Check tags for environment or team information to select appropriate clusters.
    
---

# List Clusters

List all available Amazon Redshift clusters and serverless workgroups.

    This tool discovers and returns information about all Redshift clusters and serverless workgroups
    in your AWS account, including their current status, connection details, and configuration.

    ## Usage Requirements

    - Ensure your AWS credentials are properly configured (via AWS_PROFILE or default credentials).
    - Required IAM permissions: redshift:DescribeClusters, redshift-serverless:ListWorkgroups, redshift-serverless:GetWorkgroup.

    ## Response Structure

    Returns a list of RedshiftCluster objects with the following structure:

    - identifier: Unique identifier for the cluster/workgroup.
    - type: Type of cluster (provisioned or serverless).
    - status: Current status of the cluster.
    - database_name: Default database name.
    - endpoint: Connection endpoint information.
    - port: Connection port.
    - vpc_id: VPC ID where the cluster resides.
    - node_type: Node type (for provisioned clusters).
    - number_of_nodes: Number of nodes (for provisioned clusters).
    - creation_time: When the cluster was created.
    - master_username: Master username for the cluster.
    - publicly_accessible: Whether the cluster is publicly accessible.
    - encrypted: Whether the cluster is encrypted.
    - tags: Tags associated with the cluster.

    ## Usage Tips

    1. Use this tool to discover available Redshift instances before attempting connections.
    2. Note the cluster identifiers for use with other database tools.
    3. Check the status field to ensure clusters are 'available' before querying.
    4. Use the endpoint and port information for direct database connections if needed.
    5. Consider the cluster type (provisioned vs serverless) when planning your queries.

    ## Interpretation Best Practices

    1. Filter results by status to find only available clusters.
    2. Use cluster identifiers as input for other Redshift tools.
    3. Consider cluster configuration (node type, encryption) for performance planning.
    4. Check tags for environment or team information to select appropriate clusters.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|

## AWS CLI

```bash
aws redshift describe-clusters
```

## boto3

```python
import boto3

client = boto3.client('redshift')
response = client.describe_clusters(
)
```
