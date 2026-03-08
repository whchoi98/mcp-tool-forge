---
name: ExecuteTerragruntCommand
description: Execute Terragrunt workflow commands against an AWS account.

    This tool runs Terragrunt commands (init, plan, validate, apply, destroy, run-all) in the
    specified working directory, with optional variables and region settings. Terragrunt extends
    Terraform's functionality by providing features like remote state management, dependencies
    between modules, and the ability to execute Terraform commands on multiple modules at once.

    Parameters:
        command: Terragrunt command to execute
        working_directory: Directory containing Terragrunt files
        variables: Terraform variables to pass
        aws_region: AWS region to use
        strip_ansi: Whether to strip ANSI color codes from output
        include_dirs: Directories to include in a multi-module run
        exclude_dirs: Directories to exclude from a multi-module run
        run_all: Run command on all modules in subdirectories
        terragrunt_config: Path to a custom terragrunt config file (not valid with run-all)

    Returns:
        A TerragruntExecutionResult object containing command output and status
    
---

# Executeterragruntcommand

Execute Terragrunt workflow commands against an AWS account.

    This tool runs Terragrunt commands (init, plan, validate, apply, destroy, run-all) in the
    specified working directory, with optional variables and region settings. Terragrunt extends
    Terraform's functionality by providing features like remote state management, dependencies
    between modules, and the ability to execute Terraform commands on multiple modules at once.

    Parameters:
        command: Terragrunt command to execute
        working_directory: Directory containing Terragrunt files
        variables: Terraform variables to pass
        aws_region: AWS region to use
        strip_ansi: Whether to strip ANSI color codes from output
        include_dirs: Directories to include in a multi-module run
        exclude_dirs: Directories to exclude from a multi-module run
        run_all: Run command on all modules in subdirectories
        terragrunt_config: Path to a custom terragrunt config file (not valid with run-all)

    Returns:
        A TerragruntExecutionResult object containing command output and status
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `command` | string | Yes | Terragrunt command to execute |
| `working_directory` | string | Yes | Directory containing Terragrunt files |
| `variables` | string | No | Terraform variables to pass |
| `aws_region` | string | No | AWS region to use |
| `strip_ansi` | boolean | No | Whether to strip ANSI color codes from output |
| `include_dirs` | string | No | Directories to include in a multi-module run |
| `exclude_dirs` | string | No | Directories to exclude from a multi-module run |
| `run_all` | boolean | No | Run command on all modules in subdirectories |
| `terragrunt_config` | string | No | Path to a custom terragrunt config file (not valid with run-all) |

