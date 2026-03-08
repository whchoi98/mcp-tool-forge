---
name: create-context
description: Create a DocumentationContext from a ProjectAnalysis.

    DEPRECATION WARNING: This MCP server is deprecated and will be archived.
    See https://github.com/awslabs/mcp/issues/2004 for details.

    This tool simplifies the creation of a DocumentationContext for use with
    plan_documentation and generate_documentation tools.

    Args:
        project_root: Path to the code repository
        analysis: Completed ProjectAnalysis from prepare_repository
        ctx: Optional MCP context for logging and progress reporting

    Returns:
        A DocumentationContext ready for use with other tools
    
---

# Create Context

Create a DocumentationContext from a ProjectAnalysis.

    DEPRECATION WARNING: This MCP server is deprecated and will be archived.
    See https://github.com/awslabs/mcp/issues/2004 for details.

    This tool simplifies the creation of a DocumentationContext for use with
    plan_documentation and generate_documentation tools.

    Args:
        project_root: Path to the code repository
        analysis: Completed ProjectAnalysis from prepare_repository
        ctx: Optional MCP context for logging and progress reporting

    Returns:
        A DocumentationContext ready for use with other tools
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `project_root` | string | Yes | Path to the code repository |
| `analysis` | string | Yes | Completed ProjectAnalysis from prepare_repository |

