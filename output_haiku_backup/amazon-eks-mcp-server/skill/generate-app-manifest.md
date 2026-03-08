---
name: generate-app-manifest
description: Generate Kubernetes manifest for a deployment and service.

        This tool generates Kubernetes manifests for deploying an application to an EKS cluster,
        creating both a Deployment and a LoadBalancer Service. The generated manifest can be
        applied to a cluster using the apply_yaml tool, useful for deploying containerized
        applications, creating load-balanced services, and standardizing deployment configurations.

        ## Requirements
        - The server must be run with the `--allow-write` flag

        ## Generated Resources
        - **Deployment**: Manages the application pods with specified replicas and resource requests
        - **Service**: LoadBalancer type service that exposes the application externally

        ## Usage Tips
        - Use 2 or more replicas for production workloads
        - Set appropriate resource requests based on application needs
        - Use internal load balancers for services that should only be accessible within the VPC
        - The generated manifest can be modified before applying if needed

        Args:
            ctx: MCP context
            app_name: Name of the application (used for deployment and service names)
            image_uri: Full ECR image URI with tag
            port: Container port that the application listens on
            replicas: Number of replicas to deploy
            cpu: CPU request for each container
            memory: Memory request for each container
            namespace: Kubernetes namespace to deploy to
            load_balancer_scheme: AWS load balancer scheme (internal or internet-facing)
            output_dir: Directory to save the manifest file

        Returns:
            GenerateAppManifestResponse: The complete Kubernetes manifest content and output file path
        
---

# Generate App Manifest

Generate Kubernetes manifest for a deployment and service.

        This tool generates Kubernetes manifests for deploying an application to an EKS cluster,
        creating both a Deployment and a LoadBalancer Service. The generated manifest can be
        applied to a cluster using the apply_yaml tool, useful for deploying containerized
        applications, creating load-balanced services, and standardizing deployment configurations.

        ## Requirements
        - The server must be run with the `--allow-write` flag

        ## Generated Resources
        - **Deployment**: Manages the application pods with specified replicas and resource requests
        - **Service**: LoadBalancer type service that exposes the application externally

        ## Usage Tips
        - Use 2 or more replicas for production workloads
        - Set appropriate resource requests based on application needs
        - Use internal load balancers for services that should only be accessible within the VPC
        - The generated manifest can be modified before applying if needed

        Args:
            ctx: MCP context
            app_name: Name of the application (used for deployment and service names)
            image_uri: Full ECR image URI with tag
            port: Container port that the application listens on
            replicas: Number of replicas to deploy
            cpu: CPU request for each container
            memory: Memory request for each container
            namespace: Kubernetes namespace to deploy to
            load_balancer_scheme: AWS load balancer scheme (internal or internet-facing)
            output_dir: Directory to save the manifest file

        Returns:
            GenerateAppManifestResponse: The complete Kubernetes manifest content and output file path
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `app_name` | string | Yes | Name of the application. Used for deployment and service names, and for labels. |
| `image_uri` | string | Yes | Full ECR image URI with tag (e.g., 123456789012.dkr.ecr.region.amazonaws.com/repo:tag).
            Must include the full repository path and tag. |
| `output_dir` | string | Yes | Absolute path to the directory to save the manifest file |
| `port` | integer | No | Container port that the application listens on |
| `replicas` | integer | No | Number of replicas to deploy |
| `cpu` | string | No | CPU request for each container (e.g., "100m" for 0.1 CPU cores, "500m" for half a core). |
| `memory` | string | No | Memory request for each container (e.g., "128Mi" for 128 MiB, "1Gi" for 1 GiB). |
| `namespace` | string | No | Kubernetes namespace to deploy the application to. Default: "default" |
| `load_balancer_scheme` | string | No | AWS load balancer scheme. Options: "internal" (private VPC only) or "internet-facing" (public access). |

