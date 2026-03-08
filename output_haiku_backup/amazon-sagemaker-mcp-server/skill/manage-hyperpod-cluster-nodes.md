---
name: manage-hyperpod-cluster-nodes
description: Manage SageMaker HyperPod clusters and nodes with both read and write operations.

        This tool provides operations for managing SageMaker HyperPod clusters and nodes, including listing clusters,
        listing nodes, describing a specific node, updating cluster software, and deleting nodes. It serves as a consolidated
        interface for all cluster and node-related operations, simplifying the management of HyperPod resources.

        ## Operations
        - **list_clusters**: List SageMaker HyperPod clusters with options for pagination and filtering
        - **list_nodes**: List nodes in a SageMaker HyperPod cluster with options for pagination and filtering
        - **describe_node**: Get detailed information about a specific node in a SageMaker HyperPod cluster
        - **update_software**: Update the software for a SageMaker HyperPod cluster IMMEDIATELY
        - **batch_delete**: Delete multiple nodes from a SageMaker HyperPod cluster in a single operation

        ## Response Information
        The response type varies based on the operation:
        - list_clusters: Returns ListClustersResponse with a list of clusters
        - list_nodes: Returns ListClusterNodesResponse with a list of nodes
        - describe_node: Returns DescribeClusterNodeResponse with detailed node information
        - update_software: Returns UpdateClusterSoftwareResponse with the cluster ARN
        - batch_delete: Returns BatchDeleteClusterNodesResponse with details of the deletion operation

        ## Important Notes
        - ALWAYS show the important notes for operations batch_delete and update_software BEFORE execute the operations
        - For update_software: (BEFORE executing: ALWAYS ask user whether they want to update immediately or schedule for later; follow "update_hp_cluster" tool instructions for scheduled updates)
            The UpgradeClusterSoftware API call may impact your SageMaker HyperPod cluster uptime and availability. Plan accordingly to mitigate potential disruptions to your workloads
        - For batch_delete:
            - BEFORE running the tool, ALWAYS remind user all followings
            - To safeguard your work, back up your data to Amazon S3 or an FSx for Lustre file system before invoking
            the API on a worker node group. This will help prevent any potential data loss from the instance root volume.
            For more information about backup, see Use the backup script provided by SageMaker HyperPod:
            https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-backup-restore.html
            - If you want to invoke this API on an existing cluster, you'll first need to patch the cluster by running
            the UpdateClusterSoftware API. For more information about patching a cluster, see Update the SageMaker
            HyperPod platform software of a cluster:
            https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-update-software.html
            - Deleting nodes will permanently remove them from the cluster
            - This operation cannot be undone
            - Ensure you have selected the correct nodes before proceeding
            - This operation requires write access to be enabled for the handler

        ## Usage Tips
        - Use "list_clusters" operation to get an overview of all available clusters in a specified region
        - Use "list_nodes" operation to get an overview of all nodes in a specific cluster
        - Use "describe_node" operation to get detailed information about a specific node
        - Use "update_software" operation to update the software IMMEDIATELY on all nodes or specific instance groups
        - Use "batch_delete" operation to delete multiple nodes in a single request
        - Specify region_name to operate on a cluster in a specific region
        - Specify profile_name to use a specific AWS profile with appropriate permissions

        ## Fallback Options:
        - If this tool fails, advise using AWS SageMaker CLI alternatives:
            - List clusters: `aws sagemaker list-clusters --region <cluster_region>`
            - List nodes: `aws sagemaker list-cluster-nodes --cluster-name <name> --region <cluster_region>`
            - Describe node: `aws sagemaker describe-cluster-node --cluster-name <name> --node-id <id> --region <cluster_region>`
            - Update software: `aws sagemaker update-cluster-software --cluster-name <name> --region <cluster_region>`
            - Delete nodes: `aws sagemaker batch-delete-cluster-nodes --cluster-name <name> --node-ids <ids> --region <cluster_region>`
        - Or, as another alternative: Advise using SageMaker HyperPod console for cluster and node management

        Args:
            ctx: MCP context
            operation: Operation to perform (list_clusters, list_nodes, describe_node, update_software, or batch_delete)
            cluster_name: The name of the cluster (required for all operations except list_clusters)
            node_id: The ID of the node (required for describe_node operation)
            node_ids: List of node IDs to delete (required for batch_delete operation)
            max_results: Maximum number of results to return (for list_clusters and list_nodes operations)
            next_token: Token for pagination (for list_clusters and list_nodes operations)
            name_contains: Filter clusters by name (for list_clusters operation)
            creation_time_after: Filter by creation time after (for list_clusters and list_nodes operations)
            creation_time_before: Filter by creation time before (for list_clusters and list_nodes operations)
            instance_group_name_contains: Filter by instance group name (for list_nodes operation)
            sort_by: Sort field (for list_clusters and list_nodes operations)
            sort_order: Sort order (for list_clusters and list_nodes operations)
            training_plan_arn: Filter clusters by training plan ARN (for list_clusters operation)
            deployment_config: Configuration for the update process (for update_software operation)
            instance_groups: Specific instance groups to update (for update_software operation)
            region_name: AWS region name (default: us-east-1)
            profile_name: AWS profile name (optional)

        Returns:
            Union[ListClustersResponse, ListClusterNodesResponse, DescribeClusterNodeResponse, UpdateClusterSoftwareResponse, BatchDeleteClusterNodesResponse]:
            Response specific to the operation performed
        
---

# Manage Hyperpod Cluster Nodes

Manage SageMaker HyperPod clusters and nodes with both read and write operations.

        This tool provides operations for managing SageMaker HyperPod clusters and nodes, including listing clusters,
        listing nodes, describing a specific node, updating cluster software, and deleting nodes. It serves as a consolidated
        interface for all cluster and node-related operations, simplifying the management of HyperPod resources.

        ## Operations
        - **list_clusters**: List SageMaker HyperPod clusters with options for pagination and filtering
        - **list_nodes**: List nodes in a SageMaker HyperPod cluster with options for pagination and filtering
        - **describe_node**: Get detailed information about a specific node in a SageMaker HyperPod cluster
        - **update_software**: Update the software for a SageMaker HyperPod cluster IMMEDIATELY
        - **batch_delete**: Delete multiple nodes from a SageMaker HyperPod cluster in a single operation

        ## Response Information
        The response type varies based on the operation:
        - list_clusters: Returns ListClustersResponse with a list of clusters
        - list_nodes: Returns ListClusterNodesResponse with a list of nodes
        - describe_node: Returns DescribeClusterNodeResponse with detailed node information
        - update_software: Returns UpdateClusterSoftwareResponse with the cluster ARN
        - batch_delete: Returns BatchDeleteClusterNodesResponse with details of the deletion operation

        ## Important Notes
        - ALWAYS show the important notes for operations batch_delete and update_software BEFORE execute the operations
        - For update_software: (BEFORE executing: ALWAYS ask user whether they want to update immediately or schedule for later; follow "update_hp_cluster" tool instructions for scheduled updates)
            The UpgradeClusterSoftware API call may impact your SageMaker HyperPod cluster uptime and availability. Plan accordingly to mitigate potential disruptions to your workloads
        - For batch_delete:
            - BEFORE running the tool, ALWAYS remind user all followings
            - To safeguard your work, back up your data to Amazon S3 or an FSx for Lustre file system before invoking
            the API on a worker node group. This will help prevent any potential data loss from the instance root volume.
            For more information about backup, see Use the backup script provided by SageMaker HyperPod:
            https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-backup-restore.html
            - If you want to invoke this API on an existing cluster, you'll first need to patch the cluster by running
            the UpdateClusterSoftware API. For more information about patching a cluster, see Update the SageMaker
            HyperPod platform software of a cluster:
            https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-update-software.html
            - Deleting nodes will permanently remove them from the cluster
            - This operation cannot be undone
            - Ensure you have selected the correct nodes before proceeding
            - This operation requires write access to be enabled for the handler

        ## Usage Tips
        - Use "list_clusters" operation to get an overview of all available clusters in a specified region
        - Use "list_nodes" operation to get an overview of all nodes in a specific cluster
        - Use "describe_node" operation to get detailed information about a specific node
        - Use "update_software" operation to update the software IMMEDIATELY on all nodes or specific instance groups
        - Use "batch_delete" operation to delete multiple nodes in a single request
        - Specify region_name to operate on a cluster in a specific region
        - Specify profile_name to use a specific AWS profile with appropriate permissions

        ## Fallback Options:
        - If this tool fails, advise using AWS SageMaker CLI alternatives:
            - List clusters: `aws sagemaker list-clusters --region <cluster_region>`
            - List nodes: `aws sagemaker list-cluster-nodes --cluster-name <name> --region <cluster_region>`
            - Describe node: `aws sagemaker describe-cluster-node --cluster-name <name> --node-id <id> --region <cluster_region>`
            - Update software: `aws sagemaker update-cluster-software --cluster-name <name> --region <cluster_region>`
            - Delete nodes: `aws sagemaker batch-delete-cluster-nodes --cluster-name <name> --node-ids <ids> --region <cluster_region>`
        - Or, as another alternative: Advise using SageMaker HyperPod console for cluster and node management

        Args:
            ctx: MCP context
            operation: Operation to perform (list_clusters, list_nodes, describe_node, update_software, or batch_delete)
            cluster_name: The name of the cluster (required for all operations except list_clusters)
            node_id: The ID of the node (required for describe_node operation)
            node_ids: List of node IDs to delete (required for batch_delete operation)
            max_results: Maximum number of results to return (for list_clusters and list_nodes operations)
            next_token: Token for pagination (for list_clusters and list_nodes operations)
            name_contains: Filter clusters by name (for list_clusters operation)
            creation_time_after: Filter by creation time after (for list_clusters and list_nodes operations)
            creation_time_before: Filter by creation time before (for list_clusters and list_nodes operations)
            instance_group_name_contains: Filter by instance group name (for list_nodes operation)
            sort_by: Sort field (for list_clusters and list_nodes operations)
            sort_order: Sort order (for list_clusters and list_nodes operations)
            training_plan_arn: Filter clusters by training plan ARN (for list_clusters operation)
            deployment_config: Configuration for the update process (for update_software operation)
            instance_groups: Specific instance groups to update (for update_software operation)
            region_name: AWS region name (default: us-east-1)
            profile_name: AWS profile name (optional)

        Returns:
            Union[ListClustersResponse, ListClusterNodesResponse, DescribeClusterNodeResponse, UpdateClusterSoftwareResponse, BatchDeleteClusterNodesResponse]:
            Response specific to the operation performed
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | Yes | Operation to perform: list_clusters, list_nodes, describe_node, update_software, or batch_delete. Choose "list_clusters" or "list_nodes" or "describe_node" for read-only operations when write access is disabled. |
| `cluster_name` | string | No | The name of the cluster. Required for all operations except "list_clusters". |
| `node_id` | string | No | The ID of the SageMaker HyperPod cluster node. Required for "describe_node" operation. |
| `node_ids` | string | No | The list of node IDs to delete from the cluster. Required for "batch_delete" operation. |
| `max_results` | string | No | The maximum number of results to return in the response. Default: 10. Used for "list_clusters" and "list_nodes" operations. |
| `next_token` | string | No | If the response to a previous request was truncated, the response includes a NextToken. To retrieve the next set of results, use the token in the next request. Used for "list_clusters" and "list_nodes" operations. |
| `name_contains` | string | No | A filter that returns only clusters whose name contains the specified string. Used for "list_clusters" operation. |
| `creation_time_after` | string | No | Filter for nodes/clusters created after the specified time. Accepts formats: ISO 8601 (e.g., 2014-10-01T20:30:00Z), date only (e.g., 2014-10-01), or Unix time in seconds. Used for "list_clusters" and "list_nodes" operations. |
| `creation_time_before` | string | No | Filter for nodes/clusters created before the specified time. Accepts formats: ISO 8601 (e.g., 2014-10-01T20:30:00Z), date only (e.g., 2014-10-01), or Unix time in seconds. Used for "list_clusters" and "list_nodes" operations. |
| `instance_group_name_contains` | string | No | Filter for nodes in instance groups whose name contains the specified string. Used for "list_nodes" operation. |
| `sort_by` | string | No | The field to sort results by... |
| `sort_order` | string | No | The sort order for results. The default is Ascending. Used for "list_clusters" and "list_nodes" operations. |
| `training_plan_arn` | string | No | The Amazon Resource Name (ARN) of the training plan to filter clusters by. Used for "list_clusters" operation. |
| `deployment_config` | string | No | The configuration to use when updating the AMI versions. Used for "update_software" operation. |
| `instance_groups` | string | No | The array of instance groups for which to update AMI versions. Used for "update_software" operation. |
| `region_name` | string | No | AWS region name. Default is us-east-1. |
| `profile_name` | string | No | AWS profile name. If not provided, uses the default profile. |

## AWS CLI

```bash
aws sagemaker list-clusters --max-results <max_results> --next-token <next_token> --name-contains <name_contains> --creation-time-after <creation_time_after> --creation-time-before <creation_time_before> --sort-by <sort_by> --sort-order <sort_order> --training-plan-arn <training_plan_arn>
```

## boto3

```python
import boto3

client = boto3.client('sagemaker')
response = client.list_clusters(
    MaxResults=max_results,
    NextToken=next_token,
    NameContains=name_contains,
    CreationTimeAfter=creation_time_after,
    CreationTimeBefore=creation_time_before,
    SortBy=sort_by,
    SortOrder=sort_order,
    TrainingPlanArn=training_plan_arn,
)
```
