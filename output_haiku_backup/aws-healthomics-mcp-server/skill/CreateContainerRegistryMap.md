---
name: CreateContainerRegistryMap
description: Create a container registry map for HealthOmics workflows.

    Creates a container registry map file that can be used when creating HealthOmics
    workflows. Registry mappings allow workflows to use container images from upstream
    registries (Docker Hub, Quay.io, ECR Public) without modifying the workflow
    definition. The mappings redirect container pulls to your private ECR pull-through
    caches.

    By default, this tool discovers all HealthOmics-usable pull-through cache rules
    in your ECR registry and creates mappings for them. You can also provide additional
    registry mappings or specific image mappings for container overrides.

    Args:
        ctx: MCP context for error reporting
        ecr_account_id: AWS account ID for ECR repositories. If not provided,
            uses the current AWS account.
        ecr_region: AWS region for ECR repositories. If not provided,
            uses the current configured region.
        include_pull_through_caches: If true, automatically discovers HealthOmics-usable
            ECR pull-through cache rules and creates registry mappings for them.
        additional_registry_mappings: Additional registry mappings to include beyond
            discovered pull-through caches. Each mapping should have 'upstreamRegistryUrl'
            and 'ecrRepositoryPrefix' keys.
        image_mappings: List of specific image mappings for container overrides.
            Each mapping should have 'sourceImage' and 'destinationImage' keys.
            These take precedence over registry mappings.
        output_format: Output format - 'json' for raw JSON string, 'dict' for dictionary.

    Returns:
        Dictionary containing:
        - success: Whether the operation was successful
        - account_id: AWS account ID used
        - region: AWS region used
        - discovered_healthomics_usable_caches: Number of HealthOmics-usable caches found
        - container_registry_map: The generated container registry map
        - json_output: Pretty-printed JSON string ready for use
        - usage_hint: Instructions for using the generated map
    
---

# Createcontainerregistrymap

Create a container registry map for HealthOmics workflows.

    Creates a container registry map file that can be used when creating HealthOmics
    workflows. Registry mappings allow workflows to use container images from upstream
    registries (Docker Hub, Quay.io, ECR Public) without modifying the workflow
    definition. The mappings redirect container pulls to your private ECR pull-through
    caches.

    By default, this tool discovers all HealthOmics-usable pull-through cache rules
    in your ECR registry and creates mappings for them. You can also provide additional
    registry mappings or specific image mappings for container overrides.

    Args:
        ctx: MCP context for error reporting
        ecr_account_id: AWS account ID for ECR repositories. If not provided,
            uses the current AWS account.
        ecr_region: AWS region for ECR repositories. If not provided,
            uses the current configured region.
        include_pull_through_caches: If true, automatically discovers HealthOmics-usable
            ECR pull-through cache rules and creates registry mappings for them.
        additional_registry_mappings: Additional registry mappings to include beyond
            discovered pull-through caches. Each mapping should have 'upstreamRegistryUrl'
            and 'ecrRepositoryPrefix' keys.
        image_mappings: List of specific image mappings for container overrides.
            Each mapping should have 'sourceImage' and 'destinationImage' keys.
            These take precedence over registry mappings.
        output_format: Output format - 'json' for raw JSON string, 'dict' for dictionary.

    Returns:
        Dictionary containing:
        - success: Whether the operation was successful
        - account_id: AWS account ID used
        - region: AWS region used
        - discovered_healthomics_usable_caches: Number of HealthOmics-usable caches found
        - container_registry_map: The generated container registry map
        - json_output: Pretty-printed JSON string ready for use
        - usage_hint: Instructions for using the generated map
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ecr_account_id` | string | No | AWS account ID for ECR repositories. If not provided, uses the current AWS account. |
| `ecr_region` | string | No | AWS region for ECR repositories. If not provided, uses the current configured region. |
| `include_pull_through_caches` | boolean | No | If true, automatically discovers HealthOmics-usable ECR pull-through cache rules and creates registry mappings for them. |
| `additional_registry_mappings` | string | No | Additional registry mappings to include beyond discovered pull-through caches. Each mapping has 'upstreamRegistryUrl' and 'ecrRepositoryPrefix'. |
| `image_mappings` | string | No | List of specific image mappings for container overrides. Each mapping has 'sourceImage' and 'destinationImage'. These take precedence over registry mappings. |
| `output_format` | string | No | Output format: 'json' for raw JSON string, 'dict' for Python dictionary |

