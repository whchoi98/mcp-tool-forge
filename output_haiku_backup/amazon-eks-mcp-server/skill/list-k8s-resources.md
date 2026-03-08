---
name: list-k8s-resources
description: List Kubernetes resources of a specific kind.

        This tool lists Kubernetes resources of a specified kind in an EKS cluster,
        with options to filter by namespace, labels, and fields. It returns a summary
        of each resource including name, namespace, creation time, and metadata, useful
        for listing pods in a namespace, finding services with specific labels, or
        checking resources in a specific state.

        IMPORTANT: Use this tool instead of 'kubectl get' commands.

        ## Response Information
        The response includes a summary of each resource with name, namespace, creation timestamp,
        labels, and annotations.

        ## Usage Tips
        - Use the list_api_versions tool first to find available API versions
        - For non-namespaced resources (like Nodes), the namespace parameter is ignored
        - Combine label and field selectors for more precise filtering
        - Results are summarized to avoid overwhelming responses

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster
            kind: Kind of the Kubernetes resources (e.g., 'Pod', 'Service')
            api_version: API version of the Kubernetes resources (e.g., 'v1', 'apps/v1')
            namespace: Namespace of the Kubernetes resources (optional)
            label_selector: Label selector to filter resources (optional)
            field_selector: Field selector to filter resources (optional)

        Returns:
            KubernetesResourceListResponse with operation result
        
---

# List K8s Resources

List Kubernetes resources of a specific kind.

        This tool lists Kubernetes resources of a specified kind in an EKS cluster,
        with options to filter by namespace, labels, and fields. It returns a summary
        of each resource including name, namespace, creation time, and metadata, useful
        for listing pods in a namespace, finding services with specific labels, or
        checking resources in a specific state.

        IMPORTANT: Use this tool instead of 'kubectl get' commands.

        ## Response Information
        The response includes a summary of each resource with name, namespace, creation timestamp,
        labels, and annotations.

        ## Usage Tips
        - Use the list_api_versions tool first to find available API versions
        - For non-namespaced resources (like Nodes), the namespace parameter is ignored
        - Combine label and field selectors for more precise filtering
        - Results are summarized to avoid overwhelming responses

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster
            kind: Kind of the Kubernetes resources (e.g., 'Pod', 'Service')
            api_version: API version of the Kubernetes resources (e.g., 'v1', 'apps/v1')
            namespace: Namespace of the Kubernetes resources (optional)
            label_selector: Label selector to filter resources (optional)
            field_selector: Field selector to filter resources (optional)

        Returns:
            KubernetesResourceListResponse with operation result
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_name` | string | Yes | Name of the EKS cluster where the resources are located. |
| `kind` | string | Yes | Kind of the Kubernetes resources to list (e.g., 'Pod', 'Service', 'Deployment').
            Use the list_api_versions tool to find available resource kinds. |
| `api_version` | string | Yes | API version of the Kubernetes resources (e.g., 'v1', 'apps/v1', 'networking.k8s.io/v1').
            Use the list_api_versions tool to find available API versions. |
| `namespace` | string | No | Namespace of the Kubernetes resources to list.
            If not provided, resources will be listed across all namespaces (for namespaced resources). |
| `label_selector` | string | No | Label selector to filter resources (e.g., 'app=nginx,tier=frontend').
            Uses the same syntax as kubectl's --selector flag. |
| `field_selector` | string | No | Field selector to filter resources (e.g., 'metadata.name=my-pod,status.phase=Running').
            Uses the same syntax as kubectl's --field-selector flag. |

