---
name: ValidateHealthOmicsECRConfig
description: Validate ECR configuration for HealthOmics workflows.

    Performs a comprehensive validation of the ECR configuration to ensure
    HealthOmics workflows can access container images through pull-through caches.
    This includes checking:
    1. All pull-through cache rules in the region
    2. Registry permissions policy for HealthOmics principal
    3. Repository creation templates for each pull-through cache prefix
    4. Template permissions include required actions

    For each issue found, provides specific remediation steps.

    Args:
        ctx: MCP context for error reporting

    Returns:
        Dictionary containing:
        - valid: Whether the configuration is valid for HealthOmics
        - issues: List of validation issues with remediation steps
        - pull_through_caches_checked: Number of pull-through cache rules checked
        - repositories_checked: Number of repositories checked
    
---

# Validatehealthomicsecrconfig

Validate ECR configuration for HealthOmics workflows.

    Performs a comprehensive validation of the ECR configuration to ensure
    HealthOmics workflows can access container images through pull-through caches.
    This includes checking:
    1. All pull-through cache rules in the region
    2. Registry permissions policy for HealthOmics principal
    3. Repository creation templates for each pull-through cache prefix
    4. Template permissions include required actions

    For each issue found, provides specific remediation steps.

    Args:
        ctx: MCP context for error reporting

    Returns:
        Dictionary containing:
        - valid: Whether the configuration is valid for HealthOmics
        - issues: List of validation issues with remediation steps
        - pull_through_caches_checked: Number of pull-through cache rules checked
        - repositories_checked: Number of repositories checked
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|

