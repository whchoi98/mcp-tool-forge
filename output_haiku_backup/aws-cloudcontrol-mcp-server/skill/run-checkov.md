---
name: run-checkov
description: Run Checkov security and compliance scanner on server-stored CloudFormation template.

    SECURITY: This tool only scans CloudFormation templates stored server-side from generate_infrastructure_code().
    AI agents cannot provide different content to bypass security scanning.

    CRITICAL WORKFLOW REQUIREMENTS:
    ALWAYS after running this tool:
    1. Call explain() to show the security scan results to the user (both passed and failed checks)

    If scan_status='FAILED' (security issues found):
    2. Ask the user how they want to proceed: "fix", "proceed anyway", or "cancel"
    3. WAIT for the user's actual response - do not assume their decision
    4. Only after receiving user input, call approve_security_findings() with their decision

    If scan_status='PASSED' (all checks passed):
    2. You can proceed directly to create_resource() after showing the results

    WORKFLOW REQUIREMENTS:
    1. ALWAYS provide a concise summary of security findings (passed/failed checks)
    2. Only show detailed output if user specifically requests it
    3. If CRITICAL security issues found: BLOCK resource creation, explain risks, provide resolution steps, ask multiple times for confirmation with warnings
    4. If non-critical security issues found: Ask user how to proceed (fix issues, proceed anyway, or cancel)
    
---

# Run Checkov

Run Checkov security and compliance scanner on server-stored CloudFormation template.

    SECURITY: This tool only scans CloudFormation templates stored server-side from generate_infrastructure_code().
    AI agents cannot provide different content to bypass security scanning.

    CRITICAL WORKFLOW REQUIREMENTS:
    ALWAYS after running this tool:
    1. Call explain() to show the security scan results to the user (both passed and failed checks)

    If scan_status='FAILED' (security issues found):
    2. Ask the user how they want to proceed: "fix", "proceed anyway", or "cancel"
    3. WAIT for the user's actual response - do not assume their decision
    4. Only after receiving user input, call approve_security_findings() with their decision

    If scan_status='PASSED' (all checks passed):
    2. You can proceed directly to create_resource() after showing the results

    WORKFLOW REQUIREMENTS:
    1. ALWAYS provide a concise summary of security findings (passed/failed checks)
    2. Only show detailed output if user specifically requests it
    3. If CRITICAL security issues found: BLOCK resource creation, explain risks, provide resolution steps, ask multiple times for confirmation with warnings
    4. If non-critical security issues found: Ask user how to proceed (fix issues, proceed anyway, or cancel)
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `explained_token` | string | Yes | Explained token from explain() containing CloudFormation template to scan |
| `framework` | string | No | The framework to scan (cloudformation, terraform, kubernetes, etc.) |

