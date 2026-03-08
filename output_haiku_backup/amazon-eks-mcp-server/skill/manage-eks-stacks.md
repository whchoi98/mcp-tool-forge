---
name: manage-eks-stacks
description: Manage EKS CloudFormation stacks with both read and write operations.

        This tool provides operations for managing EKS CloudFormation stacks, including creating templates,
        deploying stacks, retrieving stack information, and deleting stacks. It serves as the primary
        mechanism for creating and managing EKS clusters through CloudFormation, enabling standardized
        cluster creation, configuration updates, and resource cleanup.

        IMPORTANT: Use this tool instead of 'aws eks create-cluster', 'aws eks delete-cluster',
        'eksctl create cluster', 'eksctl delete cluster', or similar CLI commands.

        IMPORTANT: Use this tool's standardized templates for creating EKS clusters with proper VPC configuration,
        networking, security groups, and EKS auto mode. DO NOT create EKS clusters by generating CloudFormation
        templates from scratch.

        ## Requirements
        - The server must be run with the `--allow-write` flag for generate, deploy, and delete operations
        - For deploy and delete operations, the stack must have been created by this tool
        - For template_file parameter, the path must be absolute and accessible to the server

        ## Operations
        - **generate**: Create a CloudFormation template at the specified absolute path with the cluster name embedded
        - **deploy**: Deploy a CloudFormation template from the specified absolute path (creates a new stack or updates an existing one)
        - **describe**: Get detailed information about a CloudFormation stack for a specific cluster
        - **delete**: Delete a CloudFormation stack for the specified cluster

        ## Response Information
        The response type varies based on the operation:
        - generate: Returns CallToolResult with the template path
        - deploy: Returns CallToolResult with stack name, ARN, and cluster name
        - describe: Returns CallToolResult with stack details, outputs, and status
        - delete: Returns CallToolResult with stack name, ID, and cluster name

        ## Usage Tips
        - Use the describe operation first to check if a cluster already exists
        - For safety, this tool will only modify or delete stacks that it created
        - Stack creation typically takes 15-20 minutes to complete
        - Use absolute paths for template files (e.g., '/home/user/templates/eks-template.yaml')
        - The cluster name is used to derive the CloudFormation stack name

        Args:
            ctx: MCP context
            operation: Operation to perform (generate, deploy, describe, or delete)
            template_file: Absolute path for the CloudFormation template (for generate and deploy operations)
            cluster_name: Name of the EKS cluster (for all operations)

        Returns:
            ManageEksStacksResponse: Response with fields populated based on the operation performed
        
---

# Manage Eks Stacks

Manage EKS CloudFormation stacks with both read and write operations.

        This tool provides operations for managing EKS CloudFormation stacks, including creating templates,
        deploying stacks, retrieving stack information, and deleting stacks. It serves as the primary
        mechanism for creating and managing EKS clusters through CloudFormation, enabling standardized
        cluster creation, configuration updates, and resource cleanup.

        IMPORTANT: Use this tool instead of 'aws eks create-cluster', 'aws eks delete-cluster',
        'eksctl create cluster', 'eksctl delete cluster', or similar CLI commands.

        IMPORTANT: Use this tool's standardized templates for creating EKS clusters with proper VPC configuration,
        networking, security groups, and EKS auto mode. DO NOT create EKS clusters by generating CloudFormation
        templates from scratch.

        ## Requirements
        - The server must be run with the `--allow-write` flag for generate, deploy, and delete operations
        - For deploy and delete operations, the stack must have been created by this tool
        - For template_file parameter, the path must be absolute and accessible to the server

        ## Operations
        - **generate**: Create a CloudFormation template at the specified absolute path with the cluster name embedded
        - **deploy**: Deploy a CloudFormation template from the specified absolute path (creates a new stack or updates an existing one)
        - **describe**: Get detailed information about a CloudFormation stack for a specific cluster
        - **delete**: Delete a CloudFormation stack for the specified cluster

        ## Response Information
        The response type varies based on the operation:
        - generate: Returns CallToolResult with the template path
        - deploy: Returns CallToolResult with stack name, ARN, and cluster name
        - describe: Returns CallToolResult with stack details, outputs, and status
        - delete: Returns CallToolResult with stack name, ID, and cluster name

        ## Usage Tips
        - Use the describe operation first to check if a cluster already exists
        - For safety, this tool will only modify or delete stacks that it created
        - Stack creation typically takes 15-20 minutes to complete
        - Use absolute paths for template files (e.g., '/home/user/templates/eks-template.yaml')
        - The cluster name is used to derive the CloudFormation stack name

        Args:
            ctx: MCP context
            operation: Operation to perform (generate, deploy, describe, or delete)
            template_file: Absolute path for the CloudFormation template (for generate and deploy operations)
            cluster_name: Name of the EKS cluster (for all operations)

        Returns:
            ManageEksStacksResponse: Response with fields populated based on the operation performed
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | Yes | Operation to perform: generate, deploy, describe, or delete. Choose "describe" for read-only operations when write access is disabled. |
| `template_file` | string | No | Absolute path for the CloudFormation template (for generate and deploy operations).
            IMPORTANT: Assistant must provide the full absolute path to the template file, as the MCP client and server might not run from the same location. |
| `cluster_name` | string | No | Name of the EKS cluster (for generate, deploy, describe and delete operations).
            This name will be used to derive the CloudFormation stack name and will be embedded in the cluster resources. |

