---
name: SearchUserProvidedModule
description: Search for a user-provided Terraform registry module and understand its inputs, outputs, and usage.

    This tool takes a Terraform registry module URL and analyzes its input variables,
    output variables, README, and other details to provide comprehensive information
    about the module.

    The module URL should be in the format "namespace/name/provider" (e.g., "hashicorp/consul/aws")
    or "registry.terraform.io/namespace/name/provider".

    Examples:
        - To search for the HashiCorp Consul module:
          search_user_provided_module(module_url='hashicorp/consul/aws')

        - To search for a specific version of a module:
          search_user_provided_module(module_url='terraform-aws-modules/vpc/aws', version='3.14.0')

        - To search for a module with specific variables:
          search_user_provided_module(
              module_url='terraform-aws-modules/eks/aws',
              variables={'cluster_name': 'my-cluster', 'vpc_id': 'vpc-12345'}
          )

    Parameters:
        module_url: URL or identifier of the Terraform module (e.g., "hashicorp/consul/aws")
        version: Optional specific version of the module to analyze
        variables: Optional dictionary of variables to use when analyzing the module

    Returns:
        A SearchUserProvidedModuleResult object containing module information
    
---

# Searchuserprovidedmodule

Search for a user-provided Terraform registry module and understand its inputs, outputs, and usage.

    This tool takes a Terraform registry module URL and analyzes its input variables,
    output variables, README, and other details to provide comprehensive information
    about the module.

    The module URL should be in the format "namespace/name/provider" (e.g., "hashicorp/consul/aws")
    or "registry.terraform.io/namespace/name/provider".

    Examples:
        - To search for the HashiCorp Consul module:
          search_user_provided_module(module_url='hashicorp/consul/aws')

        - To search for a specific version of a module:
          search_user_provided_module(module_url='terraform-aws-modules/vpc/aws', version='3.14.0')

        - To search for a module with specific variables:
          search_user_provided_module(
              module_url='terraform-aws-modules/eks/aws',
              variables={'cluster_name': 'my-cluster', 'vpc_id': 'vpc-12345'}
          )

    Parameters:
        module_url: URL or identifier of the Terraform module (e.g., "hashicorp/consul/aws")
        version: Optional specific version of the module to analyze
        variables: Optional dictionary of variables to use when analyzing the module

    Returns:
        A SearchUserProvidedModuleResult object containing module information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `module_url` | string | Yes | URL or identifier of the Terraform module (e.g., "hashicorp/consul/aws") |
| `version` | string | No | Specific version of the module to analyze |
| `variables` | string | No | Variables to use when analyzing the module |

