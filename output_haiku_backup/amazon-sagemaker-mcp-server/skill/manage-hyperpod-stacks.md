---
name: manage-hyperpod-stacks
description: Manage SageMaker HyperPod Cluster through CloudFormation stacks.

        This tool provides operations for managing HyperPod CloudFormation stacks, including creating parameters for cloudformation template,
        deploying stacks, retrieving hyperpod stack and deployment information, and deleting hyperpod stacks. It serves as the primary
        mechanism for creating and managing HyperPod clusters through CloudFormation, enabling standardized
        cluster creation, configuration updates, and resource cleanup.

        ## Notes
        - Tell user about the working directory which is the current directory. The tool will use directory to store all required files for the user.
        - After you asked a question, do NOT do anything until you got the user response, do NOT run manage_hyperpod_stacks yet
        - Use this tool instead of direct AWS CLI commands for creating and managing HyperPod resources.
        - Use this tool's standardized parameters for creating HyperPod clusters with proper configuration.
        - DO NOT create HyperPod clusters by generating CloudFormation templates from scratch.
        - when user asks to create a hyperpod cluster, NEVER ask to check what HyperPod clusters the user currently have
        - CRITICAL: when user asks to delete a hyperpod cluster, NEVER ask how user's hyperpod cluster was created, just proceed with 'delete' operation. The corresponding Cloudformation stack name should be in this format: "<HyperPodClusterName>-stack". If no such stack exists, then the hyperpod cluster might not be created via the MCP tools here.
          - ALWAYS confirm with user if they do intend to delete the cluster because it cannot be recovered once deleted.

        ## Parameter Collection Process
            IMPORTANT: ALWAYS first ask for ALL operation-specific REQUIRED parameters from the user BEFORE making any tool calls. NEVER assume or generate parameter values.
            IMPORTANT: ALWAYS ask one question at a time.

            For 'deploy' operation:
                - region_name: REQUIRED: ask user to region of deployment. Ensure this argument matches the AvailabilityZoneIds parameter key.
                    - available regions: us-east-1,us-east-2,us-west-1,us-west-2,eu-central-1,eu-north-1,eu-west-1,eu-west-2,eu-south-2,ap-south-1,ap-southeast-1,ap-southeast-2,ap-southeast-3,ap-southeast-4,ap-northeast-1,sa-east-1,ca-central-1
                - stack_name: REQUIRED - generate a stack name and present to the user. should be in this format: "<HyperPodClusterName>-stack".
                - cluster_orchestrator: REQUIRED: ask user to specify "eks" or "slurm"; ONLY eks has NodeProvisioningMode and AutoScalerType, remove for slurm
                - params_file: REQUIRED - the parameters file should follow the below format. Ask the user to customize the parameters marked as "<to be filled out by user>" one by one. At the end, ask user if they want to add additional instance group.
                    - when cluster_orchestrator is "slurm", InstanceGroupSettings ParameterValue should also include InstanceGroupType of value Compute or Controller or Login; place it right after InstanceType. At least 1 Controller and 1 Compute node group required. ONLY 1 Controller, 1 Login group is allowed throughout ALL specified InstanceGroupSettings; Controller can only have 1 instance, ONLY ask user controller instance type
                    - when asking questions regarding InstanceGroupSettings, ask user for both the number of instance and type of instance at the same time. Naming format: "<HyperPodClusterName>-params.json"
                    - ALWAYS ask user: AutoScalerType is OPTIONAL and preferred if user wants need dynamic infrastructure scaling for variable workloads without manual intervention; remove it if user doesn't want it
                [
                    {
                        "ParameterKey": "HyperPodClusterName",
                        "ParameterValue": "<to be filled out by user>" // can be any natural english words less than 32 characters and no space. default should be sagemaker-hyperpod
                    },
                    {
                        "ParameterKey": "ResourceNamePrefix",
                        "ParameterValue": "hp-<HyperPodClusterName>-<hash>" // Generate a new 6-digit hash randomly and silently, do NOT use execute_bash commands.
                    },
                    {
                        "ParameterKey": "Stage", // do not reveil this to user, but always include this key and value.
                        "ParameterValue": "prod"
                    },
                    {
                        "ParameterKey": "AvailabilityZoneIds",
                        "ParameterValue": "<use the region_name as base input. select at four az ids in this region. If less than four regions, use all az.>"
                    },
                    {
                        "ParameterKey": "FsxAvailabilityZoneId",
                        "ParameterValue": <MUST be 1 az id and MUST be a subset of above az ids. Always use the first AZ from the selection above. Don't ask user for input.>"
                    },
                    {
                        "ParameterKey": "NodeProvisioningMode",
                        "ParameterValue": "Continuous"
                    },
                    {
                        "ParameterKey": "AutoScalerType",
                        "ParameterValue": "Karpenter"
                    },
                    {
                        "ParameterKey": "InstanceGroupSettings1", // Hyperpod requires at least 1 instance group. By default adding this instance goup. Ask user if they want addition instance groups. For each new instance, update the counter in the key. There can be at most 20 instance groups.
                        "ParameterValue": "[{\"InstanceCount\":<to be filled by user, ask a user for a number in the range 0-100>,\"InstanceGroupName\":\"<use "controller" for slurm controller group, use "login" for slurm login group, use "worker" otherwise>-group-<use the same counter as the instance group name>\",\"InstanceType\":\"<to be filled use available ec2 instance, reference the user to the ec2 page for additonal information. default is ml.m5.xlarge, ALWAYS add "ml." prefix in front of instance type. Do not metion previous instuction to user. Ensure the instance type is valid.>\",\"TargetAvailabilityZoneId\":\"<use the first az from above>\",\"InstanceStorageConfigs\":[{\"EbsVolumeConfig\":{\"VolumeSizeInGB\":500GB}}]}]"
                    },
                    {
                        "ParameterKey": "InstanceGroupSettings2", // additional instance group template
                        "ParameterValue": ....
                    },
                    ...
                ]

                    - available AZ id in example regions
                        - us-east-1: use1-az1, az2, az4, az5, az6
                        - us-west-2: usw2-az1, az2, az3, az4

            For 'describe' and 'delete' operations:
                - stack_name: REQUIRED - the stack name to operate on. You should confirm with user that the current stack is being operated on.
                - region_name: REQUIRED - ask user for the region if not clear from context.

        ## Requirements
        - The server must be run with the `--allow-write` flag for generate, deploy, and delete operations
        - For deploy and delete operations, the stack must have been created by this tool
        - For params_file parameter, the path must be absolute and accessible to the server

        ## Operations
        - **deploy**: Create and update hyperpod cluster using cloudformation template and user specified parameters.
        - **describe**: Gather information about the hyperpod cluster deployed via cloudformation stack by this tool.
        - **delete**: Delete a hyperpod cluster via CloudFormation stack created by this tool.

        ## Response Information
        The response type varies based on the operation:
        - deploy: Returns DeployStackResponse with stack name, ARN, and stack name prefix
        - describe: Returns DescribeStackResponse with stack details, outputs, and status
        - delete: Returns DeleteStackResponse with stack name, ID, and stack name prefix

        ## Usage Tips
        - If user wants to create a new hyperpod cluster, always generate a new parameter file. Parameter file MUST exists in the working directory for the tool to update the hyperpod cluster.
        - For safety, this tool will only modify or delete stacks that it created
        - Stack creation typically takes ~30 minutes to complete
        - Specify profile_name to use a specific AWS profile with appropriate permissions

        ## Fallback Options:
        - If this tool fails, advise using CloudFormation CLIs: aws cloudformation create-stack/update-stack/describe-stacks/delete-stack with proper params
        - Alternatively: advise using AWS SageMaker CLIs: aws sagemaker with all appropriate parameters:
        - Alternatively: Advise using SageMaker HyperPod console for directly creating, updating, deleting the HyperPod cluster

        Args:
            ctx: MCP context
            operation: Operation to perform (generate, deploy, describe, or delete)
            params_file: Absolute path for the CloudFormation template parameters (for deploy operations)
            stack_name: Name of the CloudFormation stack (for deploy, describe and delete operations)
            region_name: AWS region name (default: us-east-1)
            cluster_orchestrator: cluster orchestrator
            profile_name: AWS profile name (optional)

        Returns:
            Union[DeployStackResponse, DescribeStackResponse, DeleteStackResponse]:
            Response specific to the operation performed
        
---

# Manage Hyperpod Stacks

Manage SageMaker HyperPod Cluster through CloudFormation stacks.

        This tool provides operations for managing HyperPod CloudFormation stacks, including creating parameters for cloudformation template,
        deploying stacks, retrieving hyperpod stack and deployment information, and deleting hyperpod stacks. It serves as the primary
        mechanism for creating and managing HyperPod clusters through CloudFormation, enabling standardized
        cluster creation, configuration updates, and resource cleanup.

        ## Notes
        - Tell user about the working directory which is the current directory. The tool will use directory to store all required files for the user.
        - After you asked a question, do NOT do anything until you got the user response, do NOT run manage_hyperpod_stacks yet
        - Use this tool instead of direct AWS CLI commands for creating and managing HyperPod resources.
        - Use this tool's standardized parameters for creating HyperPod clusters with proper configuration.
        - DO NOT create HyperPod clusters by generating CloudFormation templates from scratch.
        - when user asks to create a hyperpod cluster, NEVER ask to check what HyperPod clusters the user currently have
        - CRITICAL: when user asks to delete a hyperpod cluster, NEVER ask how user's hyperpod cluster was created, just proceed with 'delete' operation. The corresponding Cloudformation stack name should be in this format: "<HyperPodClusterName>-stack". If no such stack exists, then the hyperpod cluster might not be created via the MCP tools here.
          - ALWAYS confirm with user if they do intend to delete the cluster because it cannot be recovered once deleted.

        ## Parameter Collection Process
            IMPORTANT: ALWAYS first ask for ALL operation-specific REQUIRED parameters from the user BEFORE making any tool calls. NEVER assume or generate parameter values.
            IMPORTANT: ALWAYS ask one question at a time.

            For 'deploy' operation:
                - region_name: REQUIRED: ask user to region of deployment. Ensure this argument matches the AvailabilityZoneIds parameter key.
                    - available regions: us-east-1,us-east-2,us-west-1,us-west-2,eu-central-1,eu-north-1,eu-west-1,eu-west-2,eu-south-2,ap-south-1,ap-southeast-1,ap-southeast-2,ap-southeast-3,ap-southeast-4,ap-northeast-1,sa-east-1,ca-central-1
                - stack_name: REQUIRED - generate a stack name and present to the user. should be in this format: "<HyperPodClusterName>-stack".
                - cluster_orchestrator: REQUIRED: ask user to specify "eks" or "slurm"; ONLY eks has NodeProvisioningMode and AutoScalerType, remove for slurm
                - params_file: REQUIRED - the parameters file should follow the below format. Ask the user to customize the parameters marked as "<to be filled out by user>" one by one. At the end, ask user if they want to add additional instance group.
                    - when cluster_orchestrator is "slurm", InstanceGroupSettings ParameterValue should also include InstanceGroupType of value Compute or Controller or Login; place it right after InstanceType. At least 1 Controller and 1 Compute node group required. ONLY 1 Controller, 1 Login group is allowed throughout ALL specified InstanceGroupSettings; Controller can only have 1 instance, ONLY ask user controller instance type
                    - when asking questions regarding InstanceGroupSettings, ask user for both the number of instance and type of instance at the same time. Naming format: "<HyperPodClusterName>-params.json"
                    - ALWAYS ask user: AutoScalerType is OPTIONAL and preferred if user wants need dynamic infrastructure scaling for variable workloads without manual intervention; remove it if user doesn't want it
                [
                    {
                        "ParameterKey": "HyperPodClusterName",
                        "ParameterValue": "<to be filled out by user>" // can be any natural english words less than 32 characters and no space. default should be sagemaker-hyperpod
                    },
                    {
                        "ParameterKey": "ResourceNamePrefix",
                        "ParameterValue": "hp-<HyperPodClusterName>-<hash>" // Generate a new 6-digit hash randomly and silently, do NOT use execute_bash commands.
                    },
                    {
                        "ParameterKey": "Stage", // do not reveil this to user, but always include this key and value.
                        "ParameterValue": "prod"
                    },
                    {
                        "ParameterKey": "AvailabilityZoneIds",
                        "ParameterValue": "<use the region_name as base input. select at four az ids in this region. If less than four regions, use all az.>"
                    },
                    {
                        "ParameterKey": "FsxAvailabilityZoneId",
                        "ParameterValue": <MUST be 1 az id and MUST be a subset of above az ids. Always use the first AZ from the selection above. Don't ask user for input.>"
                    },
                    {
                        "ParameterKey": "NodeProvisioningMode",
                        "ParameterValue": "Continuous"
                    },
                    {
                        "ParameterKey": "AutoScalerType",
                        "ParameterValue": "Karpenter"
                    },
                    {
                        "ParameterKey": "InstanceGroupSettings1", // Hyperpod requires at least 1 instance group. By default adding this instance goup. Ask user if they want addition instance groups. For each new instance, update the counter in the key. There can be at most 20 instance groups.
                        "ParameterValue": "[{\"InstanceCount\":<to be filled by user, ask a user for a number in the range 0-100>,\"InstanceGroupName\":\"<use "controller" for slurm controller group, use "login" for slurm login group, use "worker" otherwise>-group-<use the same counter as the instance group name>\",\"InstanceType\":\"<to be filled use available ec2 instance, reference the user to the ec2 page for additonal information. default is ml.m5.xlarge, ALWAYS add "ml." prefix in front of instance type. Do not metion previous instuction to user. Ensure the instance type is valid.>\",\"TargetAvailabilityZoneId\":\"<use the first az from above>\",\"InstanceStorageConfigs\":[{\"EbsVolumeConfig\":{\"VolumeSizeInGB\":500GB}}]}]"
                    },
                    {
                        "ParameterKey": "InstanceGroupSettings2", // additional instance group template
                        "ParameterValue": ....
                    },
                    ...
                ]

                    - available AZ id in example regions
                        - us-east-1: use1-az1, az2, az4, az5, az6
                        - us-west-2: usw2-az1, az2, az3, az4

            For 'describe' and 'delete' operations:
                - stack_name: REQUIRED - the stack name to operate on. You should confirm with user that the current stack is being operated on.
                - region_name: REQUIRED - ask user for the region if not clear from context.

        ## Requirements
        - The server must be run with the `--allow-write` flag for generate, deploy, and delete operations
        - For deploy and delete operations, the stack must have been created by this tool
        - For params_file parameter, the path must be absolute and accessible to the server

        ## Operations
        - **deploy**: Create and update hyperpod cluster using cloudformation template and user specified parameters.
        - **describe**: Gather information about the hyperpod cluster deployed via cloudformation stack by this tool.
        - **delete**: Delete a hyperpod cluster via CloudFormation stack created by this tool.

        ## Response Information
        The response type varies based on the operation:
        - deploy: Returns DeployStackResponse with stack name, ARN, and stack name prefix
        - describe: Returns DescribeStackResponse with stack details, outputs, and status
        - delete: Returns DeleteStackResponse with stack name, ID, and stack name prefix

        ## Usage Tips
        - If user wants to create a new hyperpod cluster, always generate a new parameter file. Parameter file MUST exists in the working directory for the tool to update the hyperpod cluster.
        - For safety, this tool will only modify or delete stacks that it created
        - Stack creation typically takes ~30 minutes to complete
        - Specify profile_name to use a specific AWS profile with appropriate permissions

        ## Fallback Options:
        - If this tool fails, advise using CloudFormation CLIs: aws cloudformation create-stack/update-stack/describe-stacks/delete-stack with proper params
        - Alternatively: advise using AWS SageMaker CLIs: aws sagemaker with all appropriate parameters:
        - Alternatively: Advise using SageMaker HyperPod console for directly creating, updating, deleting the HyperPod cluster

        Args:
            ctx: MCP context
            operation: Operation to perform (generate, deploy, describe, or delete)
            params_file: Absolute path for the CloudFormation template parameters (for deploy operations)
            stack_name: Name of the CloudFormation stack (for deploy, describe and delete operations)
            region_name: AWS region name (default: us-east-1)
            cluster_orchestrator: cluster orchestrator
            profile_name: AWS profile name (optional)

        Returns:
            Union[DeployStackResponse, DescribeStackResponse, DeleteStackResponse]:
            Response specific to the operation performed
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | Yes | Operation to perform: deploy, describe, or delete. Choose "describe" for read-only operations when write access is disabled. |
| `region_name` | string | Yes | AWS region name. Default is us-east-1. |
| `stack_name` | string | Yes | Name of the CloudFormation stack (for deploy, describe and delete operations). |
| `cluster_orchestrator` | string | No | Cluster orchestrator type. Must be either "eks" or "slurm". Default is "eks". |
| `params_file` | string | No | Absolute path for the CloudFormation template parameters(for deploy operations).
            IMPORTANT: Assistant must provide the full absolute path to the template file, as the MCP client and server might not run from the same location. |
| `profile_name` | string | No | AWS profile name. If not provided, uses the default profile. |

