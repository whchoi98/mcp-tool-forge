---
name: dynamodb-data-model-schema-validator
description: Validates a schema.json file - the structured JSON representation of your DynamoDB data model.

    This tool validates that your schema.json file is properly formatted and contains all required fields
    for use with the repository generation tool and other automation tools. It provides detailed error
    messages with suggestions for fixing any issues found.

    Optionally, if usage_data_path is provided, it will also validate the usage_data.json file against
    the schema to ensure consistency.

    The validation checks:
    - Required sections (table_config, entities) exist
    - All required fields are present
    - Field types are valid (string, integer, decimal, boolean, array, object, uuid)
    - Enum values are correct (operation types, return types, etc.)
    - Pattern IDs are unique across all entities
    - GSI names match between gsi_list and gsi_mappings
    - Fields referenced in templates exist in entity fields
    - Range conditions are valid and have correct parameter counts
    - Access patterns have valid operations and return types
    - Usage data validation (if usage_data_path provided)

    Security:
    - Schema files must be within the current working directory or subdirectories
    - Path traversal attempts (e.g., ../../../../etc/passwd) are blocked

    Args:
        schema_path: Absolute path to the schema.json file to validate
        usage_data_path: Optional absolute path to the usage_data.json file to validate

    Returns:
        Validation result with either success message or detailed error messages with suggestions

    Example Usage:
        dynamodb_data_model_schema_validator("/path/to/schema.json")
        dynamodb_data_model_schema_validator("/path/to/schema.json", "/path/to/usage_data.json")

    Example Success Output:
        "✅ Schema validation passed!"
        or
        "✅ Schema validation passed!
         ✅ Usage data validation passed!"

    Example Error Output:
        "❌ Schema validation failed:
          • entities.User.fields[0].type: Invalid type value 'strng'
            💡 Did you mean 'string'? Valid options: string, integer, decimal, boolean, array, object, uuid"
    
---

# Dynamodb Data Model Schema Validator

Validates a schema.json file - the structured JSON representation of your DynamoDB data model.

    This tool validates that your schema.json file is properly formatted and contains all required fields
    for use with the repository generation tool and other automation tools. It provides detailed error
    messages with suggestions for fixing any issues found.

    Optionally, if usage_data_path is provided, it will also validate the usage_data.json file against
    the schema to ensure consistency.

    The validation checks:
    - Required sections (table_config, entities) exist
    - All required fields are present
    - Field types are valid (string, integer, decimal, boolean, array, object, uuid)
    - Enum values are correct (operation types, return types, etc.)
    - Pattern IDs are unique across all entities
    - GSI names match between gsi_list and gsi_mappings
    - Fields referenced in templates exist in entity fields
    - Range conditions are valid and have correct parameter counts
    - Access patterns have valid operations and return types
    - Usage data validation (if usage_data_path provided)

    Security:
    - Schema files must be within the current working directory or subdirectories
    - Path traversal attempts (e.g., ../../../../etc/passwd) are blocked

    Args:
        schema_path: Absolute path to the schema.json file to validate
        usage_data_path: Optional absolute path to the usage_data.json file to validate

    Returns:
        Validation result with either success message or detailed error messages with suggestions

    Example Usage:
        dynamodb_data_model_schema_validator("/path/to/schema.json")
        dynamodb_data_model_schema_validator("/path/to/schema.json", "/path/to/usage_data.json")

    Example Success Output:
        "✅ Schema validation passed!"
        or
        "✅ Schema validation passed!
         ✅ Usage data validation passed!"

    Example Error Output:
        "❌ Schema validation failed:
          • entities.User.fields[0].type: Invalid type value 'strng'
            💡 Did you mean 'string'? Valid options: string, integer, decimal, boolean, array, object, uuid"
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `schema_path` | string | Yes | Absolute path to the schema.json file to validate |
| `usage_data_path` | string | No | Optional absolute path to the usage_data.json file to validate alongside the schema |

