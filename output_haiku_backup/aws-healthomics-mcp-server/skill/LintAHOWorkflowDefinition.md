---
name: LintAHOWorkflowDefinition
description: Lint WDL or CWL workflow definitions and return validation findings.

    This tool validates workflow definitions using appropriate linting tools:
    - WDL workflows: Uses miniwdl package for parsing and validation
    - CWL workflows: Uses cwltool package for parsing and validation

    The tool checks for:
    - Syntax errors and parsing issues
    - Missing required fields (inputs, outputs, steps)
    - Runtime requirements for tasks
    - Common workflow structure issues

    Args:
        ctx: MCP context for error reporting
        workflow_content: The workflow definition content to lint
        workflow_format: The workflow format ('wdl' or 'cwl')
        filename: Optional filename for context in error messages

    Returns:
        Dictionary containing:
        - status: 'success' or 'error'
        - format: The workflow format that was linted
        - filename: The filename that was processed (optional)
        - linter: Name of the linting tool used
        - raw_output: Raw output from the linter command execution
    
---

# Lintahoworkflowdefinition

Lint WDL or CWL workflow definitions and return validation findings.

    This tool validates workflow definitions using appropriate linting tools:
    - WDL workflows: Uses miniwdl package for parsing and validation
    - CWL workflows: Uses cwltool package for parsing and validation

    The tool checks for:
    - Syntax errors and parsing issues
    - Missing required fields (inputs, outputs, steps)
    - Runtime requirements for tasks
    - Common workflow structure issues

    Args:
        ctx: MCP context for error reporting
        workflow_content: The workflow definition content to lint
        workflow_format: The workflow format ('wdl' or 'cwl')
        filename: Optional filename for context in error messages

    Returns:
        Dictionary containing:
        - status: 'success' or 'error'
        - format: The workflow format that was linted
        - filename: The filename that was processed (optional)
        - linter: Name of the linting tool used
        - raw_output: Raw output from the linter command execution
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workflow_content` | string | Yes | The workflow definition content to lint |
| `workflow_format` | string | Yes | The workflow format: 'wdl' or 'cwl' |
| `filename` | string | No | Optional filename for context |

## AWS CLI

```bash
aws omics validate-workflow-definition --workflow-definition <workflow_content> --type <workflow_format> --name <filename>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.validate_workflow_definition(
    WorkflowDefinition=workflow_content,
    Type=workflow_format,
    Name=filename,
)
```
