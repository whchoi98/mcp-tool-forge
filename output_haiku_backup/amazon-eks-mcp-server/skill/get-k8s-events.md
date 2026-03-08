---
name: get-k8s-events
description: Get events related to a specific Kubernetes resource.

        This tool retrieves Kubernetes events related to a specific resource, providing
        detailed information about what has happened to the resource over time. Events
        are useful for troubleshooting pod startup failures, investigating deployment issues,
        understanding resource modifications, and diagnosing scheduling problems.

        IMPORTANT: Use this tool instead of 'kubectl describe' or 'kubectl get events' commands.

        ## Requirements
        - The server must be run with the `--allow-sensitive-data-access` flag
        - The resource must exist and be accessible in the specified namespace

        ## Response Information
        The response includes events with timestamps (first and last), occurrence counts,
        messages, reasons, reporting components, and event types (Normal or Warning).

        ## Usage Tips
        - Warning events often indicate problems that need attention
        - Normal events provide information about expected lifecycle operations
        - The count field shows how many times the same event has occurred
        - Recent events are most relevant for current issues

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster
            kind: Kind of the involved object
            name: Name of the involved object
            namespace: Namespace of the involved object (optional for non-namespaced resources)

        Returns:
            EventsResponse with events related to the specified object
        
---

# Get K8s Events

Get events related to a specific Kubernetes resource.

        This tool retrieves Kubernetes events related to a specific resource, providing
        detailed information about what has happened to the resource over time. Events
        are useful for troubleshooting pod startup failures, investigating deployment issues,
        understanding resource modifications, and diagnosing scheduling problems.

        IMPORTANT: Use this tool instead of 'kubectl describe' or 'kubectl get events' commands.

        ## Requirements
        - The server must be run with the `--allow-sensitive-data-access` flag
        - The resource must exist and be accessible in the specified namespace

        ## Response Information
        The response includes events with timestamps (first and last), occurrence counts,
        messages, reasons, reporting components, and event types (Normal or Warning).

        ## Usage Tips
        - Warning events often indicate problems that need attention
        - Normal events provide information about expected lifecycle operations
        - The count field shows how many times the same event has occurred
        - Recent events are most relevant for current issues

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster
            kind: Kind of the involved object
            name: Name of the involved object
            namespace: Namespace of the involved object (optional for non-namespaced resources)

        Returns:
            EventsResponse with events related to the specified object
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_name` | string | Yes | Name of the EKS cluster where the resource is located. |
| `kind` | string | Yes | Kind of the involved object (e.g., "Pod", "Deployment", "Service"). Must match the resource kind exactly. |
| `name` | string | Yes | Name of the involved object to get events for. |
| `namespace` | string | No | Namespace of the involved object. Required for namespaced resources (like Pods, Deployments).
            Not required for cluster-scoped resources (like Nodes, PersistentVolumes). |

