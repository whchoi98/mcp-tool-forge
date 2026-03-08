---
name: dynamodb-data-model-schema-converter
description: Retrieves the DynamoDB Data Model Schema Converter Expert prompt.

    This tool returns a specialized prompt for converting DynamoDB data models (dynamodb_data_model.md)
    into schema.json - a structured JSON representation used for generating type-safe entities and repositories.
    By default, also includes instructions for generating usage_data.json with realistic sample data.

    The prompt guides through:
    - Reading and parsing dynamodb_data_model.md files
    - Converting table designs, GSIs, and access patterns into structured JSON format
    - Validating generated schemas using the dynamodb_data_model_schema_validator tool
    - Iteratively fixing validation errors (up to 8 iterations)
    - Generating usage_data.json with realistic sample data from markdown tables (unless generate_usage_data=False)
    - Creating isolated output folders with schema.json (and optionally usage_data.json)

    When to set generate_usage_data=False:
    - User explicitly asks for "schema only", "just schema", "without usage data", "without examples"
    - User wants to skip sample data generation
    - User only needs the schema structure for validation or review

    Args:
        generate_usage_data: If True (default), includes instructions for generating usage_data.json.
                           If False, only generates schema.json.

    Returns: Complete schema converter expert prompt as text
    
---

# Dynamodb Data Model Schema Converter

Retrieves the DynamoDB Data Model Schema Converter Expert prompt.

    This tool returns a specialized prompt for converting DynamoDB data models (dynamodb_data_model.md)
    into schema.json - a structured JSON representation used for generating type-safe entities and repositories.
    By default, also includes instructions for generating usage_data.json with realistic sample data.

    The prompt guides through:
    - Reading and parsing dynamodb_data_model.md files
    - Converting table designs, GSIs, and access patterns into structured JSON format
    - Validating generated schemas using the dynamodb_data_model_schema_validator tool
    - Iteratively fixing validation errors (up to 8 iterations)
    - Generating usage_data.json with realistic sample data from markdown tables (unless generate_usage_data=False)
    - Creating isolated output folders with schema.json (and optionally usage_data.json)

    When to set generate_usage_data=False:
    - User explicitly asks for "schema only", "just schema", "without usage data", "without examples"
    - User wants to skip sample data generation
    - User only needs the schema structure for validation or review

    Args:
        generate_usage_data: If True (default), includes instructions for generating usage_data.json.
                           If False, only generates schema.json.

    Returns: Complete schema converter expert prompt as text
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `generate_usage_data` | boolean | No | Set to False if user only wants schema.json without usage examples/sample data. Set to True (default) to generate both schema.json and usage_data.json with realistic sample data for code generation |

