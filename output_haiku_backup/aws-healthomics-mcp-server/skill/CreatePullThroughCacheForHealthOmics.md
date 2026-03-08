---
name: CreatePullThroughCacheForHealthOmics
description: Create a pull-through cache rule configured for HealthOmics.

    Creates an ECR pull-through cache rule for the specified upstream registry
    and configures the necessary permissions for HealthOmics to use it. This includes:
    1. Creating the pull-through cache rule
    2. Updating the registry permissions policy to allow HealthOmics to create
       repositories and import images
    3. Creating a repository creation template that grants HealthOmics the
       required permissions to pull images

    Args:
        ctx: MCP context for error reporting
        upstream_registry: Upstream registry type (docker-hub, quay, or ecr-public)
        ecr_repository_prefix: ECR repository prefix (defaults to registry type name)
        credential_arn: Secrets Manager ARN for registry credentials
                       (required for docker-hub, optional for others)

    Returns:
        Dictionary containing:
        - success: Whether the operation was successful
        - rule: Created pull-through cache rule details
        - registry_policy_updated: Whether the registry policy was updated
        - repository_template_created: Whether the repository template was created
        - message: Human-readable status message
    
---

# Createpullthroughcacheforhealthomics

Create a pull-through cache rule configured for HealthOmics.

    Creates an ECR pull-through cache rule for the specified upstream registry
    and configures the necessary permissions for HealthOmics to use it. This includes:
    1. Creating the pull-through cache rule
    2. Updating the registry permissions policy to allow HealthOmics to create
       repositories and import images
    3. Creating a repository creation template that grants HealthOmics the
       required permissions to pull images

    Args:
        ctx: MCP context for error reporting
        upstream_registry: Upstream registry type (docker-hub, quay, or ecr-public)
        ecr_repository_prefix: ECR repository prefix (defaults to registry type name)
        credential_arn: Secrets Manager ARN for registry credentials
                       (required for docker-hub, optional for others)

    Returns:
        Dictionary containing:
        - success: Whether the operation was successful
        - rule: Created pull-through cache rule details
        - registry_policy_updated: Whether the registry policy was updated
        - repository_template_created: Whether the repository template was created
        - message: Human-readable status message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `upstream_registry` | string | Yes | Upstream registry type: docker-hub, quay, or ecr-public |
| `ecr_repository_prefix` | string | No | ECR repository prefix (defaults to registry type name) |
| `credential_arn` | string | No | Secrets Manager ARN for registry credentials (required for docker-hub) |

## AWS CLI

```bash
aws ecr create-pull-through-cache-rule --registry-id <ecr_repository_prefix> --repository-prefix <ecr_repository_prefix> --upstream-registry-type <upstream_registry> --credential-arn <credential_arn>
```

## boto3

```python
import boto3

client = boto3.client('ecr')
response = client.create_pull_through_cache_rule(
    RegistryId=ecr_repository_prefix,
    RepositoryPrefix=ecr_repository_prefix,
    UpstreamRegistryType=upstream_registry,
    CredentialArn=credential_arn,
)
```
