---
name: search-schema
description: Search for schemas in a registry using keywords.

        REQUIREMENTS:
        - You MUST use this tool to find schemas for AWS service events
        - You MUST search in the "aws.events" registry for AWS service events
        - You MUST use this tool when implementing Lambda functions that consume events from EventBridge
        - You SHOULD prefix search keywords with "aws." for optimal results (e.g., "aws.s3", "aws.ec2")
        - You MAY filter results using additional keywords for specific event types

        USE CASES:

        1. Lambda Function Development with EventBridge:
        - CRITICAL: Required for Lambda functions consuming events from EventBridge
        - Search for event schemas your function needs to process
        - Example: "aws.s3" for S3 events, "aws.dynamodb" for DynamoDB streams
        - Use results with describe_schema to get complete event structure

        2. EventBridge Rule Creation:
        - Find schemas to create properly structured event patterns
        - Example: "aws.ec2" for EC2 instance state changes
        - Ensure exact field names and types in rule patterns

        IMPLEMENTATION FLOW:
        1. Search aws.events registry for service schemas
        2. Note relevant schema names from results
        3. Use describe_schema to get complete definitions
        4. Implement handlers using exact schema structure
        
---

# Search Schema

Search for schemas in a registry using keywords.

        REQUIREMENTS:
        - You MUST use this tool to find schemas for AWS service events
        - You MUST search in the "aws.events" registry for AWS service events
        - You MUST use this tool when implementing Lambda functions that consume events from EventBridge
        - You SHOULD prefix search keywords with "aws." for optimal results (e.g., "aws.s3", "aws.ec2")
        - You MAY filter results using additional keywords for specific event types

        USE CASES:

        1. Lambda Function Development with EventBridge:
        - CRITICAL: Required for Lambda functions consuming events from EventBridge
        - Search for event schemas your function needs to process
        - Example: "aws.s3" for S3 events, "aws.dynamodb" for DynamoDB streams
        - Use results with describe_schema to get complete event structure

        2. EventBridge Rule Creation:
        - Find schemas to create properly structured event patterns
        - Example: "aws.ec2" for EC2 instance state changes
        - Ensure exact field names and types in rule patterns

        IMPLEMENTATION FLOW:
        1. Search aws.events registry for service schemas
        2. Note relevant schema names from results
        3. Use describe_schema to get complete definitions
        4. Implement handlers using exact schema structure
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keywords` | string | Yes | Keywords to search for. Prefix service names with "aws." for better results (e.g., "aws.s3" for S3 events, "aws.ec2" for EC2 events). |
| `registry_name` | string | Yes | For AWS service events, use "aws.events" to search the EventBridge schema registry. |
| `limit` | string | No | Maximum number of results to return. If you specify 0, the operation returns up to 10 results. |
| `next_token` | string | No | Next token returned by the previous operation. |

## AWS CLI

```bash
aws schemas search-schemas --keywords <keywords> --registry-name <registry_name> --limit <limit> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('schemas')
response = client.search_schemas(
    Keywords=keywords,
    RegistryName=registry_name,
    Limit=limit,
    NextToken=next_token,
)
```
