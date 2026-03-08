---
name: get-pod-logs
description: Get logs from a pod in a Kubernetes cluster.

        This tool retrieves logs from a specified pod in an EKS cluster, with options
        to filter by container, time range, and size. It's useful for debugging application
        issues, monitoring behavior, investigating crashes, and verifying startup configuration.

        IMPORTANT: Use this tool instead of 'kubectl logs' commands.

        ## Requirements
        - The server must be run with the `--allow-sensitive-data-access` flag
        - The pod must exist and be accessible in the specified namespace
        - The EKS cluster must exist and be accessible

        ## Response Information
        The response includes pod name, namespace, container name (if specified),
        and log lines as an array of strings.

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster
            namespace: Namespace of the pod
            pod_name: Name of the pod
            container_name: Container name (optional, if pod contains more than one container)
            since_seconds: Only return logs newer than this many seconds (optional)
            tail_lines: Number of lines to return from the end of the logs (defaults to 100)
            limit_bytes: Maximum number of bytes to return (defaults to 10KB)
            previous: Return previous terminated container logs (defaults to false)

        Returns:
            PodLogsResponse with pod logs
        
---

# Get Pod Logs

Get logs from a pod in a Kubernetes cluster.

        This tool retrieves logs from a specified pod in an EKS cluster, with options
        to filter by container, time range, and size. It's useful for debugging application
        issues, monitoring behavior, investigating crashes, and verifying startup configuration.

        IMPORTANT: Use this tool instead of 'kubectl logs' commands.

        ## Requirements
        - The server must be run with the `--allow-sensitive-data-access` flag
        - The pod must exist and be accessible in the specified namespace
        - The EKS cluster must exist and be accessible

        ## Response Information
        The response includes pod name, namespace, container name (if specified),
        and log lines as an array of strings.

        Args:
            ctx: MCP context
            cluster_name: Name of the EKS cluster
            namespace: Namespace of the pod
            pod_name: Name of the pod
            container_name: Container name (optional, if pod contains more than one container)
            since_seconds: Only return logs newer than this many seconds (optional)
            tail_lines: Number of lines to return from the end of the logs (defaults to 100)
            limit_bytes: Maximum number of bytes to return (defaults to 10KB)
            previous: Return previous terminated container logs (defaults to false)

        Returns:
            PodLogsResponse with pod logs
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_name` | string | Yes | Name of the EKS cluster where the pod is running. |
| `namespace` | string | Yes | Kubernetes namespace where the pod is located. |
| `pod_name` | string | Yes | Name of the pod to retrieve logs from. |
| `container_name` | string | No | Name of the specific container to get logs from. Required only if the pod contains multiple containers. |
| `since_seconds` | string | No | Only return logs newer than this many seconds. Useful for getting recent logs without retrieving the entire history. |
| `tail_lines` | integer | No | Number of lines to return from the end of the logs. Default: 100. Use higher values for more context. |
| `limit_bytes` | integer | No | Maximum number of bytes to return. Default: 10KB (10240 bytes). Prevents retrieving extremely large log files. |
| `previous` | boolean | No | Return previous terminated container logs. Default: false. Useful to get logs for pods that are restarting. |

