---
name: manage-k8s-resource
description: Manage a single Kubernetes resource with various operations.

        This tool provides complete CRUD (Create, Read, Update, Delete) operations
        for Kubernetes resources in an EKS cluster. It supports all resource types
        and allows for precise control over individual resources, enabling you to create
        custom resources, update specific fields, read detailed information, and delete
        resources that are no longer needed.

        IMPORTANT: Use this tool instead of 'kubectl create', 'kubectl edit', 'kubectl patch',
        'kubectl delete', or 'kubectl get' commands.

        ## Requirements
        - The server must be run with the `--allow-write` flag for mutating operations
        - The server must be run with the `--allow-sensitive-data-access` flag for Secret resources
        - The EKS cluster must exist and be accessible

        ## Operations
        - **create**: Create a new resource with the provided definition
        - **replace**: Replace an existing resource with a new definition
        - **patch**: Update specific fields of an existing resource
        - **delete**: Remove an existing resource
        - **read**: Get details of an existing resource

        ## Usage Tips
        - Use list_api_versions to find available API versions
        - For namespaced resources, always provide the namespace
        - When creating resources, ensure the name in the body matches the name parameter
        - For patch operations, only include the fields you want to update

        Args:
            ctx: MCP context
            operation: Operation to perform (create, replace, patch, delete, read)
            cluster_name: Name of the EKS cluster
            kind: Kind of the Kubernetes resource (e.g., 'Pod', 'Service')
            api_version: API version of the Kubernetes resource (e.g., 'v1', 'apps/v1')
            name: Name of the Kubernetes resource
            namespace: Namespace of the Kubernetes resource (optional)
            body: Resource definition

        Returns:
            KubernetesResourceResponse with operation result
        
---

# Manage K8s Resource

Manage a single Kubernetes resource with various operations.

        This tool provides complete CRUD (Create, Read, Update, Delete) operations
        for Kubernetes resources in an EKS cluster. It supports all resource types
        and allows for precise control over individual resources, enabling you to create
        custom resources, update specific fields, read detailed information, and delete
        resources that are no longer needed.

        IMPORTANT: Use this tool instead of 'kubectl create', 'kubectl edit', 'kubectl patch',
        'kubectl delete', or 'kubectl get' commands.

        ## Requirements
        - The server must be run with the `--allow-write` flag for mutating operations
        - The server must be run with the `--allow-sensitive-data-access` flag for Secret resources
        - The EKS cluster must exist and be accessible

        ## Operations
        - **create**: Create a new resource with the provided definition
        - **replace**: Replace an existing resource with a new definition
        - **patch**: Update specific fields of an existing resource
        - **delete**: Remove an existing resource
        - **read**: Get details of an existing resource

        ## Usage Tips
        - Use list_api_versions to find available API versions
        - For namespaced resources, always provide the namespace
        - When creating resources, ensure the name in the body matches the name parameter
        - For patch operations, only include the fields you want to update

        Args:
            ctx: MCP context
            operation: Operation to perform (create, replace, patch, delete, read)
            cluster_name: Name of the EKS cluster
            kind: Kind of the Kubernetes resource (e.g., 'Pod', 'Service')
            api_version: API version of the Kubernetes resource (e.g., 'v1', 'apps/v1')
            name: Name of the Kubernetes resource
            namespace: Namespace of the Kubernetes resource (optional)
            body: Resource definition

        Returns:
            KubernetesResourceResponse with operation result
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | Yes | Operation to perform on the resource. Valid values:
            - create: Create a new resource
            - replace: Replace an existing resource
            - patch: Update specific fields of an existing resource
            - delete: Delete an existing resource
            - read: Get details of an existing resource
            Use list_k8s_resources for listing multiple resources. |
| `cluster_name` | string | Yes | Name of the EKS cluster where the resource is located or will be created. |
| `kind` | string | Yes | Kind of the Kubernetes resource (e.g., "Pod", "Service", "Deployment"). |
| `api_version` | string | Yes | API version of the Kubernetes resource (e.g., "v1", "apps/v1", "networking.k8s.io/v1"). |
| `name` | string | No | Name of the Kubernetes resource. Required for all operations except create (where it can be specified in the body). |
| `namespace` | string | No | Namespace of the Kubernetes resource. Required for namespaced resources.
            Not required for cluster-scoped resources (like Nodes, PersistentVolumes). |
| `body` | string | No | Resource definition as a dictionary. Required for create, replace, and patch operations.
            For create and replace, this should be a complete resource definition.
            For patch, this should contain only the fields to update. |

