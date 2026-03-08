---
name: LintAHOWorkflowBundle
description: Lint multi-file WDL or CWL workflow bundles and return validation findings.

    This tool validates multi-file workflow bundles using appropriate linting tools:
    - WDL workflows: Uses miniwdl package for parsing and validation with import support
    - CWL workflows: Uses cwltool package for parsing and validation with dependency resolution

    The tool creates a temporary directory structure that preserves the relative file paths,
    allowing proper resolution of imports and dependencies between workflow files.

    The tool checks for:
    - Syntax errors and parsing issues across all files
    - Missing required fields (inputs, outputs, steps)
    - Import/dependency resolution
    - Runtime requirements for tasks
    - Common workflow structure issues

    Args:
        ctx: MCP context for error reporting
        workflow_files: Dictionary mapping relative file paths to their content
        workflow_format: The workflow format ('wdl' or 'cwl')
        main_workflow_file: Path to the main workflow file within the bundle

    Returns:
        Dictionary containing:
        - status: 'success' or 'error'
        - format: The workflow format that was linted
        - main_file: The main workflow file that was processed
        - files_processed: List of all files that were processed
        - linter: Name of the linting tool used
        - raw_output: Raw output from the linter command execution
    
---

# Lintahoworkflowbundle

Lint multi-file WDL or CWL workflow bundles and return validation findings.

    This tool validates multi-file workflow bundles using appropriate linting tools:
    - WDL workflows: Uses miniwdl package for parsing and validation with import support
    - CWL workflows: Uses cwltool package for parsing and validation with dependency resolution

    The tool creates a temporary directory structure that preserves the relative file paths,
    allowing proper resolution of imports and dependencies between workflow files.

    The tool checks for:
    - Syntax errors and parsing issues across all files
    - Missing required fields (inputs, outputs, steps)
    - Import/dependency resolution
    - Runtime requirements for tasks
    - Common workflow structure issues

    Args:
        ctx: MCP context for error reporting
        workflow_files: Dictionary mapping relative file paths to their content
        workflow_format: The workflow format ('wdl' or 'cwl')
        main_workflow_file: Path to the main workflow file within the bundle

    Returns:
        Dictionary containing:
        - status: 'success' or 'error'
        - format: The workflow format that was linted
        - main_file: The main workflow file that was processed
        - files_processed: List of all files that were processed
        - linter: Name of the linting tool used
        - raw_output: Raw output from the linter command execution
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workflow_files` | object | Yes | Dictionary mapping file paths to their content |
| `workflow_format` | string | Yes | The workflow format: 'wdl' or 'cwl' |
| `main_workflow_file` | string | Yes | Path to the main workflow file within the bundle |

## AWS CLI

```bash
aws omics validate-workflow-definition --workflow-definition <workflow_files> --type <workflow_format> --main-workflow-path <main_workflow_file>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.validate_workflow_definition(
    WorkflowDefinition=workflow_files,
    Type=workflow_format,
    MainWorkflowPath=main_workflow_file,
)
```
