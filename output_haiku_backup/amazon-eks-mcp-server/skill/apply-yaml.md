---
name: apply-yaml
description: Apply a Kubernetes YAML from a local file.

        This tool applies Kubernetes resources defined in a YAML file to an EKS cluster,
        similar to the `kubectl apply` command. It supports multi-document YAML files
        and can create or update resources, useful for deploying applications, creating
        Kubernetes resources, and applying complete application stacks.

        IMPORTANT: Use this tool instead of 'kubectl apply -f' commands.

        ## Requirements
        - The server must be run with the `--allow-write` flag
        - The YAML file must exist and be accessible to the server
        - The path must be absolute (e.g., '/home/user/manifests/app.yaml')
        - The EKS cluster must exist and be accessible

        ## Response Information
        The response includes the number of resources created, number of resources
        updated (when force=True), and whether force was applied.

        Args:
            ctx: MCP context
            yaml_path: Absolute path to the YAML file to apply
            cluster_name: Name of the EKS cluster
            namespace: Default namespace to use for resources
            force: Whether to update resources if they already exist (like kubectl apply)

        Returns:
            ApplyYamlResponse with operation result
        
---

# Apply Yaml

Apply a Kubernetes YAML from a local file.

        This tool applies Kubernetes resources defined in a YAML file to an EKS cluster,
        similar to the `kubectl apply` command. It supports multi-document YAML files
        and can create or update resources, useful for deploying applications, creating
        Kubernetes resources, and applying complete application stacks.

        IMPORTANT: Use this tool instead of 'kubectl apply -f' commands.

        ## Requirements
        - The server must be run with the `--allow-write` flag
        - The YAML file must exist and be accessible to the server
        - The path must be absolute (e.g., '/home/user/manifests/app.yaml')
        - The EKS cluster must exist and be accessible

        ## Response Information
        The response includes the number of resources created, number of resources
        updated (when force=True), and whether force was applied.

        Args:
            ctx: MCP context
            yaml_path: Absolute path to the YAML file to apply
            cluster_name: Name of the EKS cluster
            namespace: Default namespace to use for resources
            force: Whether to update resources if they already exist (like kubectl apply)

        Returns:
            ApplyYamlResponse with operation result
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `yaml_path` | string | Yes | Absolute path to the YAML file to apply.
            IMPORTANT: Must be an absolute path (e.g., '/home/user/manifests/app.yaml') as the MCP client and server might not run from the same location. |
| `cluster_name` | string | Yes | Name of the EKS cluster where the resources will be created or updated. |
| `namespace` | string | Yes | Kubernetes namespace to apply resources to. Will be used for namespaced resources that do not specify a namespace. |
| `force` | boolean | No | Whether to update resources if they already exist (similar to kubectl apply). Set to false to only create new resources. |

