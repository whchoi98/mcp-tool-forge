---
name: dynamodb-data-model-validation
description: Validates and tests DynamoDB data models against DynamoDB Local.

    Use this tool to validate, test, and verify your DynamoDB data model after completing the design phase.
    This tool automatically checks that all access patterns work correctly by executing them against a local
    DynamoDB instance.

    WHEN TO USE:
    - After completing data model design with dynamodb_data_modeling tool
    - When user asks to "validate", "test", "check", or "verify" their DynamoDB data model
    - To ensure all access patterns execute correctly before deploying to production

    WHAT IT DOES:
    1. If dynamodb_data_model.json doesn't exist:
       - Returns complete JSON generation guide from json_generation_guide.md
       - Follow the guide to create the JSON file with tables, items, and access_patterns
       - Call this tool again after creating the JSON to validate

    2. If dynamodb_data_model.json exists:
       - Validates the JSON structure (checks for required keys: tables, items, access_patterns)
       - Sets up DynamoDB Local environment (Docker/Podman/Finch/nerdctl or Java fallback)
       - Cleans up existing tables from previous validation runs
       - Creates tables and inserts test data from your model specification
       - Tests all defined access patterns by executing their AWS CLI implementations
       - Saves detailed validation results to dynamodb_model_validation.json
       - Transforms results to markdown format for comprehensive review

    WHAT TO DO ON SUCCESSFUL COMPLETION:
    After validation completes, you MUST present the user with TWO options:
    1. Deploy to AWS: Call `generate_resources` tool with resource_type='cdk' to create a CDK app for provisioning tables
    2. Generate Python code: Call `dynamodb_data_model_schema_converter` to convert the model to schema.json, then generate code

    The user can choose one or both options. If they choose CDK first, you can still generate Python code afterward.

    Args:
        workspace_dir: Absolute path of the workspace directory

    Returns:
        JSON generation guide (if file missing) or validation results with transformation prompt (if file exists)
    
---

# Dynamodb Data Model Validation

Validates and tests DynamoDB data models against DynamoDB Local.

    Use this tool to validate, test, and verify your DynamoDB data model after completing the design phase.
    This tool automatically checks that all access patterns work correctly by executing them against a local
    DynamoDB instance.

    WHEN TO USE:
    - After completing data model design with dynamodb_data_modeling tool
    - When user asks to "validate", "test", "check", or "verify" their DynamoDB data model
    - To ensure all access patterns execute correctly before deploying to production

    WHAT IT DOES:
    1. If dynamodb_data_model.json doesn't exist:
       - Returns complete JSON generation guide from json_generation_guide.md
       - Follow the guide to create the JSON file with tables, items, and access_patterns
       - Call this tool again after creating the JSON to validate

    2. If dynamodb_data_model.json exists:
       - Validates the JSON structure (checks for required keys: tables, items, access_patterns)
       - Sets up DynamoDB Local environment (Docker/Podman/Finch/nerdctl or Java fallback)
       - Cleans up existing tables from previous validation runs
       - Creates tables and inserts test data from your model specification
       - Tests all defined access patterns by executing their AWS CLI implementations
       - Saves detailed validation results to dynamodb_model_validation.json
       - Transforms results to markdown format for comprehensive review

    WHAT TO DO ON SUCCESSFUL COMPLETION:
    After validation completes, you MUST present the user with TWO options:
    1. Deploy to AWS: Call `generate_resources` tool with resource_type='cdk' to create a CDK app for provisioning tables
    2. Generate Python code: Call `dynamodb_data_model_schema_converter` to convert the model to schema.json, then generate code

    The user can choose one or both options. If they choose CDK first, you can still generate Python code afterward.

    Args:
        workspace_dir: Absolute path of the workspace directory

    Returns:
        JSON generation guide (if file missing) or validation results with transformation prompt (if file exists)
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workspace_dir` | string | Yes | Absolute path of the workspace directory |

