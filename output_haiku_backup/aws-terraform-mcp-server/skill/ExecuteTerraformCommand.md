---
name: ExecuteTerraformCommand
description: Execute Terraform workflow commands against an AWS account.

    This tool runs Terraform commands (init, plan, validate, apply, destroy) in the
    specified working directory, with optional variables and region settings.

    Parameters:
        command: Terraform command to execute
        working_directory: Directory containing Terraform files
        variables: Terraform variables to pass
        aws_region: AWS region to use
        strip_ansi: Whether to strip ANSI color codes from output

    Returns:
        A TerraformExecutionResult object containing command output and status
    
---

# Executeterraformcommand

Execute Terraform workflow commands against an AWS account.

    This tool runs Terraform commands (init, plan, validate, apply, destroy) in the
    specified working directory, with optional variables and region settings.

    Parameters:
        command: Terraform command to execute
        working_directory: Directory containing Terraform files
        variables: Terraform variables to pass
        aws_region: AWS region to use
        strip_ansi: Whether to strip ANSI color codes from output

    Returns:
        A TerraformExecutionResult object containing command output and status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `command` | string | Yes | Terraform command to execute |
| `working_directory` | string | Yes | Directory containing Terraform files |
| `variables` | string | No | Terraform variables to pass |
| `aws_region` | string | No | AWS region to use |
| `strip_ansi` | boolean | No | Whether to strip ANSI color codes from output |

