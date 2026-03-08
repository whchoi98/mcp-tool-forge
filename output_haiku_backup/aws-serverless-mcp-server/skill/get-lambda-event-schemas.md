---
name: get-lambda-event-schemas
description: Returns AWS Lambda event schemas for different event sources (e.g. s3, sns, apigw) and programming languages.

        When a event source triggers a Lambda function, the request payload comes in a specific format.
        Each Lambda event source defines its own schema and language-specific types, which should be used in
        the Lambda function handler to correctly parse the event data. If you cannot find a schema for your event source, you can directly parse
        the event data as a JSON object. For EventBridge events, you must use the list_registries, search_schema, and describe_schema
        tools to access the schema registry directly, get schema definitions, and generate code processing logic.

        Returns:
            Dict: Lambda event schema source code file for the request runtime and event source
        
---

# Get Lambda Event Schemas

Returns AWS Lambda event schemas for different event sources (e.g. s3, sns, apigw) and programming languages.

        When a event source triggers a Lambda function, the request payload comes in a specific format.
        Each Lambda event source defines its own schema and language-specific types, which should be used in
        the Lambda function handler to correctly parse the event data. If you cannot find a schema for your event source, you can directly parse
        the event data as a JSON object. For EventBridge events, you must use the list_registries, search_schema, and describe_schema
        tools to access the schema registry directly, get schema definitions, and generate code processing logic.

        Returns:
            Dict: Lambda event schema source code file for the request runtime and event source
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event_source` | string | Yes | Event source (e.g., api-gw, s3, sqs, sns, kinesis, eventbridge, dynamodb) |
| `runtime` | string | Yes | Programming language for the schema references (e.g., go, nodejs, python, java) |

