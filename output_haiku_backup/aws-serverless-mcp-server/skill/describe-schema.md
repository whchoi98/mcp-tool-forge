---
name: describe-schema
description: Retrieve the schema definition for the specified schema version.

        REQUIREMENTS:
        - You MUST use this tool to get complete schema definitions before implementing handlers
        - You MUST use this tool when implementing Lambda functions that consume events from EventBridge
        - You MUST use the returned schema structure for type-safe event handling
        - You SHOULD use the latest schema version unless specifically required otherwise
        - You MUST validate all required fields defined in the schema

        USE CASES:

        1. Lambda Function Handlers with EventBridge:
        You MUST:
        - CRITICAL: Required for Lambda functions consuming events from EventBridge
        - Implement handlers using the exact event structure
        - Validate all required fields defined in schema
        - Handle optional fields appropriately
        - Ensure type safety for EventBridge-sourced events

        You SHOULD:
        - Generate strongly typed code based on schema
        - Implement error handling for missing fields
        - Document any assumptions about structure

        2. EventBridge Rules:
        You MUST:
        - Create patterns that exactly match schema
        - Use correct field names and value types
        - Include all required fields in patterns

        You SHOULD:
        - Test patterns against sample events
        - Document pattern matching logic
        - Consider schema versions in design

        The schema content provides complete event structure with all fields and types, ensuring correct event handling.
        
---

# Describe Schema

Retrieve the schema definition for the specified schema version.

        REQUIREMENTS:
        - You MUST use this tool to get complete schema definitions before implementing handlers
        - You MUST use this tool when implementing Lambda functions that consume events from EventBridge
        - You MUST use the returned schema structure for type-safe event handling
        - You SHOULD use the latest schema version unless specifically required otherwise
        - You MUST validate all required fields defined in the schema

        USE CASES:

        1. Lambda Function Handlers with EventBridge:
        You MUST:
        - CRITICAL: Required for Lambda functions consuming events from EventBridge
        - Implement handlers using the exact event structure
        - Validate all required fields defined in schema
        - Handle optional fields appropriately
        - Ensure type safety for EventBridge-sourced events

        You SHOULD:
        - Generate strongly typed code based on schema
        - Implement error handling for missing fields
        - Document any assumptions about structure

        2. EventBridge Rules:
        You MUST:
        - Create patterns that exactly match schema
        - Use correct field names and value types
        - Include all required fields in patterns

        You SHOULD:
        - Test patterns against sample events
        - Document pattern matching logic
        - Consider schema versions in design

        The schema content provides complete event structure with all fields and types, ensuring correct event handling.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `registry_name` | string | Yes | For AWS service events, use "aws.events" to access the EventBridge schema registry. |
| `schema_name` | string | Yes | The name of the schema to retrieve (e.g., "aws.s3@ObjectCreated" for S3 events). |
| `schema_version` | string | No | Version number of the schema. For AWS service events, use latest version (default) to ensure up-to-date event handling. |

## AWS CLI

```bash
aws schemas describe-schema --registry-name <registry_name> --schema-name <schema_name> --schema-version <schema_version>
```

## boto3

```python
import boto3

client = boto3.client('schemas')
response = client.describe_schema(
    RegistryName=registry_name,
    SchemaName=schema_name,
    SchemaVersion=schema_version,
)
```
