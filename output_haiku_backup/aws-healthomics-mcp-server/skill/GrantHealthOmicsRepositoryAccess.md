---
name: GrantHealthOmicsRepositoryAccess
description: Grant HealthOmics access to an ECR repository.

    Updates the repository policy to allow the HealthOmics service principal
    (omics.amazonaws.com) to pull images. This adds the required permissions:
    - ecr:BatchGetImage
    - ecr:GetDownloadUrlForLayer

    If the repository already has a policy, the HealthOmics permissions are added
    while preserving existing statements. If no policy exists, a new policy is created.

    Args:
        ctx: MCP context for error reporting
        repository_name: ECR repository name to grant access to

    Returns:
        Dictionary containing:
        - success: Whether the operation was successful
        - repository_name: The repository that was updated
        - policy_updated: Whether an existing policy was updated
        - policy_created: Whether a new policy was created
        - previous_healthomics_accessible: Previous accessibility status
        - current_healthomics_accessible: Current accessibility status after update
        - message: Human-readable status message
    
---

# Granthealthomicsrepositoryaccess

Grant HealthOmics access to an ECR repository.

    Updates the repository policy to allow the HealthOmics service principal
    (omics.amazonaws.com) to pull images. This adds the required permissions:
    - ecr:BatchGetImage
    - ecr:GetDownloadUrlForLayer

    If the repository already has a policy, the HealthOmics permissions are added
    while preserving existing statements. If no policy exists, a new policy is created.

    Args:
        ctx: MCP context for error reporting
        repository_name: ECR repository name to grant access to

    Returns:
        Dictionary containing:
        - success: Whether the operation was successful
        - repository_name: The repository that was updated
        - policy_updated: Whether an existing policy was updated
        - policy_created: Whether a new policy was created
        - previous_healthomics_accessible: Previous accessibility status
        - current_healthomics_accessible: Current accessibility status after update
        - message: Human-readable status message
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `repository_name` | string | Yes | ECR repository name to grant HealthOmics access to |

## AWS CLI

```bash
aws ecr set-repository-policy --repository-name <repository_name> --policy-text <{"Version":"2012-10-17","Statement":[{"Sid":"HealthOmicsAccess","Effect":"Allow","Principal":{"Service":"omics.amazonaws.com"},"Action":["ecr:BatchGetImage","ecr:GetDownloadUrlForLayer"]}]}>
```

## boto3

```python
import boto3

client = boto3.client('ecr')
response = client.set_repository_policy(
    RepositoryName=repository_name,
    PolicyText={"Version":"2012-10-17","Statement":[{"Sid":"HealthOmicsAccess","Effect":"Allow","Principal":{"Service":"omics.amazonaws.com"},"Action":["ecr:BatchGetImage","ecr:GetDownloadUrlForLayer"]}]},
)
```
