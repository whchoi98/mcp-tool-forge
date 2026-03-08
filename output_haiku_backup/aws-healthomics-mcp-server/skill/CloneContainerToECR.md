---
name: CloneContainerToECR
description: Clone a container image to a private ECR repository for HealthOmics use.

    This tool copies a container image from an upstream registry (Docker Hub, Quay.io,
    ECR Public) to your private ECR repository with appropriate HealthOmics access
    permissions. It uses ECR pull-through cache to perform the copy.

    The tool will:
    1. Parse the source image reference (handling Docker Hub shorthand like "ubuntu:latest")
    2. Find an existing pull-through cache rule for the source registry
    3. Use the pull-through cache to pull the image into ECR
    4. Grant HealthOmics access permissions to the repository
    5. Return the ECR URI and digest for use in workflows

    Image reference formats supported:
    - "ubuntu:latest" -> registry-1.docker.io/library/ubuntu:latest
    - "myorg/myimage:v1" -> registry-1.docker.io/myorg/myimage:v1
    - "quay.io/biocontainers/samtools:1.17" -> quay.io/biocontainers/samtools:1.17
    - "public.ecr.aws/lts/ubuntu:22.04" -> public.ecr.aws/lts/ubuntu:22.04

    Args:
        ctx: MCP context for error reporting
        source_image: Source container image reference
        target_repository_name: Target ECR repository name (only used if no pull-through
            cache exists; optional)
        target_image_tag: Target image tag (optional)

    Returns:
        Dictionary containing:
        - success: Whether the operation was successful
        - source_image: Original source image reference
        - source_registry: Source registry URL
        - source_digest: Source image digest (if available)
        - ecr_uri: ECR URI of the cloned image
        - ecr_digest: ECR image digest
        - repository_created: Whether a new repository was created
        - used_pull_through_cache: Whether pull-through cache was used
        - pull_through_cache_prefix: The pull-through cache prefix used (if any)
        - healthomics_accessible: Whether HealthOmics can access the image
        - message: Human-readable status message
    
---

# Clonecontainertoecr

Clone a container image to a private ECR repository for HealthOmics use.

    This tool copies a container image from an upstream registry (Docker Hub, Quay.io,
    ECR Public) to your private ECR repository with appropriate HealthOmics access
    permissions. It uses ECR pull-through cache to perform the copy.

    The tool will:
    1. Parse the source image reference (handling Docker Hub shorthand like "ubuntu:latest")
    2. Find an existing pull-through cache rule for the source registry
    3. Use the pull-through cache to pull the image into ECR
    4. Grant HealthOmics access permissions to the repository
    5. Return the ECR URI and digest for use in workflows

    Image reference formats supported:
    - "ubuntu:latest" -> registry-1.docker.io/library/ubuntu:latest
    - "myorg/myimage:v1" -> registry-1.docker.io/myorg/myimage:v1
    - "quay.io/biocontainers/samtools:1.17" -> quay.io/biocontainers/samtools:1.17
    - "public.ecr.aws/lts/ubuntu:22.04" -> public.ecr.aws/lts/ubuntu:22.04

    Args:
        ctx: MCP context for error reporting
        source_image: Source container image reference
        target_repository_name: Target ECR repository name (only used if no pull-through
            cache exists; optional)
        target_image_tag: Target image tag (optional)

    Returns:
        Dictionary containing:
        - success: Whether the operation was successful
        - source_image: Original source image reference
        - source_registry: Source registry URL
        - source_digest: Source image digest (if available)
        - ecr_uri: ECR URI of the cloned image
        - ecr_digest: ECR image digest
        - repository_created: Whether a new repository was created
        - used_pull_through_cache: Whether pull-through cache was used
        - pull_through_cache_prefix: The pull-through cache prefix used (if any)
        - healthomics_accessible: Whether HealthOmics can access the image
        - message: Human-readable status message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source_image` | string | Yes | Source container image reference (e.g., "ubuntu:latest", "myorg/myimage:v1", "quay.io/org/image:tag") |
| `target_repository_name` | string | No | Target ECR repository name. Only used if no pull-through cache exists. If not provided, derives from source image. |
| `target_image_tag` | string | No | Target image tag. If not provided, uses source tag or "latest". |

