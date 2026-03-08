---
name: generate-resources
description: Generates resources from a DynamoDB data model JSON file (dynamodb_data_model.json).

    This tool generates various resources based on the provided `dynamodb_data_model.json` file.
    Currently supports generating a CDK app for deploying DynamoDB tables.

    Supported resource types:
    - cdk: CDK app for deploying DynamoDB tables.
           Generates a CDK app that provisions DynamoDB tables and GSIs as defined in `dynamodb_data_model.json`.

    WHEN TO USE:
    - After completing data model validation with `dynamodb_data_model_validation` tool
    - When user asks to "deploy", "create CDK app", "generate CDK", or "provision infrastructure"
    - When user wants to deploy their DynamoDB tables and GSIs to AWS using a CDK app

    WHEN NOT TO USE:
    - Before completing data model validation with `dynamodb_data_model_validation` tool
    - Before having created the `dynamodb_data_model.json` file
    - When user only wants to generate Python code without deploying infrastructure

    WHAT TO DO ON SUCCESSFUL COMPLETION:
    After CDK generation completes, you MUST ask the user if they want to:
    1. Deploy the CDK app now (provide deployment instructions)
    2. Generate Python data access layer code to interact with the tables (call `dynamodb_data_model_schema_converter` then `generate_data_access_layer`)

    Args:
        dynamodb_data_model_json_file: Absolute path to the `dynamodb_data_model.json` file
        resource_type: Type of resource to generate, possible values: cdk

    Returns:
        Success message with the destination path, or error message if generation fails
    
---

# Generate Resources

Generates resources from a DynamoDB data model JSON file (dynamodb_data_model.json).

    This tool generates various resources based on the provided `dynamodb_data_model.json` file.
    Currently supports generating a CDK app for deploying DynamoDB tables.

    Supported resource types:
    - cdk: CDK app for deploying DynamoDB tables.
           Generates a CDK app that provisions DynamoDB tables and GSIs as defined in `dynamodb_data_model.json`.

    WHEN TO USE:
    - After completing data model validation with `dynamodb_data_model_validation` tool
    - When user asks to "deploy", "create CDK app", "generate CDK", or "provision infrastructure"
    - When user wants to deploy their DynamoDB tables and GSIs to AWS using a CDK app

    WHEN NOT TO USE:
    - Before completing data model validation with `dynamodb_data_model_validation` tool
    - Before having created the `dynamodb_data_model.json` file
    - When user only wants to generate Python code without deploying infrastructure

    WHAT TO DO ON SUCCESSFUL COMPLETION:
    After CDK generation completes, you MUST ask the user if they want to:
    1. Deploy the CDK app now (provide deployment instructions)
    2. Generate Python data access layer code to interact with the tables (call `dynamodb_data_model_schema_converter` then `generate_data_access_layer`)

    Args:
        dynamodb_data_model_json_file: Absolute path to the `dynamodb_data_model.json` file
        resource_type: Type of resource to generate, possible values: cdk

    Returns:
        Success message with the destination path, or error message if generation fails
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `dynamodb_data_model_json_file` | string | Yes | Absolute path to the dynamodb_data_model.json file. Resources will be generated in the same directory. |
| `resource_type` | string | Yes | Type of resource to generate: 'cdk' for CDK app |

