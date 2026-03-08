---
name: prepare-repository
description: Prepare repository for the MCP client's analysis.

    DEPRECATION WARNING: This MCP server is deprecated and will be archived.
    See https://github.com/awslabs/mcp/issues/2004 for details.

    This tool:
    1. Extracts directory structure from the repository
    2. Returns an EMPTY ProjectAnalysis for you to fill out
    3. Provides directory structure in file_structure["directory_structure"]
    4. Provides repository statistics in file_structure["statistics"] (file count, character count, etc.)

    You should:
    1. Review the directory structure in file_structure["directory_structure"]
    2. Use read_file to examine key files you identify from the structure
    3. Fill out the empty fields in ProjectAnalysis based on your analysis
    4. Set has_infrastructure_as_code=True if you detect CDK, Terraform, or other infrastructure as code
    5. Use create_context to create a DocumentationContext from your analysis
    6. Use the DocumentationContext with plan_documentation

    NOTE: This tool does NOT analyze the code - that's your job!
    The tool only extracts the directory structure and statistics to help you identify important files.
    
---

# Prepare Repository

Prepare repository for the MCP client's analysis.

    DEPRECATION WARNING: This MCP server is deprecated and will be archived.
    See https://github.com/awslabs/mcp/issues/2004 for details.

    This tool:
    1. Extracts directory structure from the repository
    2. Returns an EMPTY ProjectAnalysis for you to fill out
    3. Provides directory structure in file_structure["directory_structure"]
    4. Provides repository statistics in file_structure["statistics"] (file count, character count, etc.)

    You should:
    1. Review the directory structure in file_structure["directory_structure"]
    2. Use read_file to examine key files you identify from the structure
    3. Fill out the empty fields in ProjectAnalysis based on your analysis
    4. Set has_infrastructure_as_code=True if you detect CDK, Terraform, or other infrastructure as code
    5. Use create_context to create a DocumentationContext from your analysis
    6. Use the DocumentationContext with plan_documentation

    NOTE: This tool does NOT analyze the code - that's your job!
    The tool only extracts the directory structure and statistics to help you identify important files.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `project_root` | string | Yes | Path to the code repository |

