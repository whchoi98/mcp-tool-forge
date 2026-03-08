---
name: generate-data-access-layer
description: Generate Python code for a data access layer to interact with your DynamoDB tables.

    🔴 PREREQUISITE: Before calling this tool, you MUST first call `dynamodb_data_model_schema_converter`
    to generate schema.json from dynamodb_data_model.md. This tool ONLY accepts schema.json.

    TYPICAL WORKFLOW:
    1. Complete data modeling with `dynamodb_data_modeling` tool (creates dynamodb_data_model.md)
    2. Validate with `dynamodb_data_model_validation` tool (optional but recommended)
    3. Optionally deploy infrastructure with `generate_resources` tool (resource_type='cdk')
    4. Convert to schema: Call `dynamodb_data_model_schema_converter` tool (creates schema.json)
    5. Generate code: Call this `generate_data_access_layer` tool with the path to schema.json

    This tool generates a complete data access layer from your schema including:
    - Type-safe entity classes with field validation using Pydantic
    - Repository classes with optimistic locking and error handling for all operations
    - Fully implemented access patterns
    - Working usage examples with realistic sample data (if usage_data_path provided)

    Args:
        schema_path: Path to the schema JSON file
        language: Target programming language for generated code (currently only 'python' supported)
        generate_sample_usage: Generate usage examples and test cases
        usage_data_path: Path to usage_data.json file for realistic sample data (optional)

    Returns:
        Success message with output location and implementation guidance
    
---

# Generate Data Access Layer

Generate Python code for a data access layer to interact with your DynamoDB tables.

    🔴 PREREQUISITE: Before calling this tool, you MUST first call `dynamodb_data_model_schema_converter`
    to generate schema.json from dynamodb_data_model.md. This tool ONLY accepts schema.json.

    TYPICAL WORKFLOW:
    1. Complete data modeling with `dynamodb_data_modeling` tool (creates dynamodb_data_model.md)
    2. Validate with `dynamodb_data_model_validation` tool (optional but recommended)
    3. Optionally deploy infrastructure with `generate_resources` tool (resource_type='cdk')
    4. Convert to schema: Call `dynamodb_data_model_schema_converter` tool (creates schema.json)
    5. Generate code: Call this `generate_data_access_layer` tool with the path to schema.json

    This tool generates a complete data access layer from your schema including:
    - Type-safe entity classes with field validation using Pydantic
    - Repository classes with optimistic locking and error handling for all operations
    - Fully implemented access patterns
    - Working usage examples with realistic sample data (if usage_data_path provided)

    Args:
        schema_path: Path to the schema JSON file
        language: Target programming language for generated code (currently only 'python' supported)
        generate_sample_usage: Generate usage examples and test cases
        usage_data_path: Path to usage_data.json file for realistic sample data (optional)

    Returns:
        Success message with output location and implementation guidance
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `schema_path` | string | Yes | Path to the schema JSON file |
| `language` | string | No | Target programming language (python) |
| `generate_sample_usage` | boolean | No | Generate usage examples and test cases |
| `usage_data_path` | string | No | Path to usage_data.json file for realistic sample data (optional) |

