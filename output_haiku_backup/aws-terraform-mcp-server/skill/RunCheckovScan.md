---
name: RunCheckovScan
description: Run Checkov security scan on Terraform code.

    This tool runs Checkov to scan Terraform code for security and compliance issues,
    identifying potential vulnerabilities and misconfigurations according to best practices.

    Checkov (https://www.checkov.io/) is an open-source static code analysis tool that
    can detect hundreds of security and compliance issues in infrastructure-as-code.

    Parameters:
        working_directory: Directory containing Terraform files to scan
        framework: Framework to scan (default: terraform)
        check_ids: Optional list of specific check IDs to run
        skip_check_ids: Optional list of check IDs to skip
        output_format: Format for scan results (default: json)

    Returns:
        A CheckovScanResult object containing scan results and identified vulnerabilities
    
---

# Runcheckovscan

Run Checkov security scan on Terraform code.

    This tool runs Checkov to scan Terraform code for security and compliance issues,
    identifying potential vulnerabilities and misconfigurations according to best practices.

    Checkov (https://www.checkov.io/) is an open-source static code analysis tool that
    can detect hundreds of security and compliance issues in infrastructure-as-code.

    Parameters:
        working_directory: Directory containing Terraform files to scan
        framework: Framework to scan (default: terraform)
        check_ids: Optional list of specific check IDs to run
        skip_check_ids: Optional list of check IDs to skip
        output_format: Format for scan results (default: json)

    Returns:
        A CheckovScanResult object containing scan results and identified vulnerabilities
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `working_directory` | string | Yes | Directory containing Terraform files |
| `framework` | string | No | Framework to scan (terraform, cloudformation, etc.) |
| `check_ids` | string | No | Specific check IDs to run |
| `skip_check_ids` | string | No | Check IDs to skip |
| `output_format` | string | No | Output format (json, cli, etc.) |

