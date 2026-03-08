---
name: CheckContainerAvailability
description: Check if a container image is available in ECR and accessible by HealthOmics.

    Queries ECR to determine if a specific container image exists in a repository
    and whether HealthOmics has the required permissions to pull the image.
    For pull-through cache repositories, indicates that the image may be pulled
    on first access even if not currently cached.

    When initiate_pull_through is True and the image is not found in a pull-through
    cache repository that is accessible to HealthOmics, this function will attempt
    to initiate the pull-through using ECR's batch_get_image API call. This triggers
    ECR to pull the image from the upstream registry and cache it locally.

    Args:
        ctx: MCP context for error reporting
        repository_name: ECR repository name (e.g., "my-repo" or "docker-hub/library/ubuntu")
        image_tag: Image tag to check (default: "latest")
        image_digest: Image digest (sha256:...) - if provided, takes precedence over tag
        initiate_pull_through: If True, attempt to initiate pull-through cache for
            missing images in accessible pull-through cache repositories

    Returns:
        Dictionary containing:
        - available: Whether the image is available
        - image: Image details if available (digest, size, push timestamp)
        - repository_exists: Whether the repository exists
        - is_pull_through_cache: Whether this is a pull-through cache repository
        - healthomics_accessible: Whether HealthOmics can access the image
        - missing_permissions: List of missing ECR permissions for HealthOmics
        - message: Human-readable status message
        - pull_through_initiated: Whether a pull-through was initiated
        - pull_through_initiation_message: Message about pull-through initiation result
    
---

# Checkcontaineravailability

Check if a container image is available in ECR and accessible by HealthOmics.

    Queries ECR to determine if a specific container image exists in a repository
    and whether HealthOmics has the required permissions to pull the image.
    For pull-through cache repositories, indicates that the image may be pulled
    on first access even if not currently cached.

    When initiate_pull_through is True and the image is not found in a pull-through
    cache repository that is accessible to HealthOmics, this function will attempt
    to initiate the pull-through using ECR's batch_get_image API call. This triggers
    ECR to pull the image from the upstream registry and cache it locally.

    Args:
        ctx: MCP context for error reporting
        repository_name: ECR repository name (e.g., "my-repo" or "docker-hub/library/ubuntu")
        image_tag: Image tag to check (default: "latest")
        image_digest: Image digest (sha256:...) - if provided, takes precedence over tag
        initiate_pull_through: If True, attempt to initiate pull-through cache for
            missing images in accessible pull-through cache repositories

    Returns:
        Dictionary containing:
        - available: Whether the image is available
        - image: Image details if available (digest, size, push timestamp)
        - repository_exists: Whether the repository exists
        - is_pull_through_cache: Whether this is a pull-through cache repository
        - healthomics_accessible: Whether HealthOmics can access the image
        - missing_permissions: List of missing ECR permissions for HealthOmics
        - message: Human-readable status message
        - pull_through_initiated: Whether a pull-through was initiated
        - pull_through_initiation_message: Message about pull-through initiation result
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `repository_name` | string | Yes | ECR repository name (e.g., "my-repo" or "docker-hub/library/ubuntu") |
| `image_tag` | string | No | Image tag to check (default: "latest") |
| `image_digest` | string | No | Image digest (sha256:...) - if provided, takes precedence over tag |
| `initiate_pull_through` | boolean | No | If True and the image is not found in a pull-through cache repository that is accessible to HealthOmics, attempt to initiate the pull-through using batch_get_image API call |

## AWS CLI

```bash
aws ecr batch-get-image --repository-name <repository_name> --image-tag <image_tag> --image-digest <image_digest>
```

## boto3

```python
import boto3

client = boto3.client('ecr')
response = client.batch_get_image(
    RepositoryName=repository_name,
    ImageIds=[{'ImageTag': 'image_tag', 'ImageDigest': 'image_digest'}],
)
```
