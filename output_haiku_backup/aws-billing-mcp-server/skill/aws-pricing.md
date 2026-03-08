---
name: aws-pricing
description: Comprehensive AWS pricing analysis tool that provides access to AWS service pricing information and cost analysis capabilities.

This tool supports four main operations:
1. get_service_codes: Get a comprehensive list of AWS service codes from the AWS Price List API
2. get_service_attributes: Get filterable attributes for a specific AWS service's pricing
3. get_attribute_values: Get all valid values for a specific attribute of an AWS service
4. get_pricing_from_api: Get detailed pricing information from AWS Price List API with optional filters

USE THE OPERATIONS IN THIS ORDER:
1. get_service_codes: Entry point - discover available AWS services and their unique service codes. Note that service codes may not match your expectations, so it's best to get service codes first.
2. get_service_attributes: Second step - understand which dimensions affect pricing for a chosen service
3. get_attribute_values: Third step - get possible values you can use in pricing filters
4. get_pricing_from_api: Final step - retrieve actual pricing data based on service and filters
**If you deviate from this order of operations, you will struggle to form the correct filters, and you will not get results from the API**

IMPORTANT GUIDELINES:
- When retrieving foundation model pricing, always use the latest models for comparison
- For database compatibility with services, only include confirmed supported databases
- Providing less information is better than giving incorrect information
- Price list APIs can return large data volumes. Use narrower filters to retrieve less data when possible
- Service codes often differ from AWS console names (e.g., 'AmazonES' for OpenSearch)

ARGS:
      ctx: The MCP context object
      operation: The pricing operation to perform ('get_service_codes', 'get_service_attributes', 'get_attribute_values', 'get_pricing_from_api')
      service_code: AWS service code (e.g., 'AmazonEC2', 'AmazonS3', 'AmazonES'). Required for get_service_attributes, get_attribute_values, and get_pricing_from_api operations.
      attribute_name: Attribute name (e.g., 'instanceType', 'location', 'storageClass'). Required for get_attribute_values operation.
      region: AWS region (e.g., 'us-east-1', 'us-west-2', 'eu-west-1'). Required for get_pricing_from_api operation.
      filters: Optional filters for pricing queries. Format: {'instanceType': 't3.medium', 'location': 'US East (N. Virginia)'}

RETURNS:
        Dict containing the pricing information

SUPPORTED AWS PRICING API REGIONS:
- Classic partition: us-east-1, eu-central-1, ap-southeast-1
- China partition: cn-northwest-1
The tool automatically maps your region to the nearest pricing endpoint.
---

# Aws-Pricing

Comprehensive AWS pricing analysis tool that provides access to AWS service pricing information and cost analysis capabilities.

This tool supports four main operations:
1. get_service_codes: Get a comprehensive list of AWS service codes from the AWS Price List API
2. get_service_attributes: Get filterable attributes for a specific AWS service's pricing
3. get_attribute_values: Get all valid values for a specific attribute of an AWS service
4. get_pricing_from_api: Get detailed pricing information from AWS Price List API with optional filters

USE THE OPERATIONS IN THIS ORDER:
1. get_service_codes: Entry point - discover available AWS services and their unique service codes. Note that service codes may not match your expectations, so it's best to get service codes first.
2. get_service_attributes: Second step - understand which dimensions affect pricing for a chosen service
3. get_attribute_values: Third step - get possible values you can use in pricing filters
4. get_pricing_from_api: Final step - retrieve actual pricing data based on service and filters
**If you deviate from this order of operations, you will struggle to form the correct filters, and you will not get results from the API**

IMPORTANT GUIDELINES:
- When retrieving foundation model pricing, always use the latest models for comparison
- For database compatibility with services, only include confirmed supported databases
- Providing less information is better than giving incorrect information
- Price list APIs can return large data volumes. Use narrower filters to retrieve less data when possible
- Service codes often differ from AWS console names (e.g., 'AmazonES' for OpenSearch)

ARGS:
      ctx: The MCP context object
      operation: The pricing operation to perform ('get_service_codes', 'get_service_attributes', 'get_attribute_values', 'get_pricing_from_api')
      service_code: AWS service code (e.g., 'AmazonEC2', 'AmazonS3', 'AmazonES'). Required for get_service_attributes, get_attribute_values, and get_pricing_from_api operations.
      attribute_name: Attribute name (e.g., 'instanceType', 'location', 'storageClass'). Required for get_attribute_values operation.
      region: AWS region (e.g., 'us-east-1', 'us-west-2', 'eu-west-1'). Required for get_pricing_from_api operation.
      filters: Optional filters for pricing queries. Format: {'instanceType': 't3.medium', 'location': 'US East (N. Virginia)'}

RETURNS:
        Dict containing the pricing information

SUPPORTED AWS PRICING API REGIONS:
- Classic partition: us-east-1, eu-central-1, ap-southeast-1
- China partition: cn-northwest-1
The tool automatically maps your region to the nearest pricing endpoint.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | Yes |  |
| `service_code` | string | No |  |
| `attribute_name` | string | No |  |
| `region` | string | No |  |
| `filters` | string | No |  |
| `max_results` | string | No |  |

## AWS CLI

```bash
aws pricing describe-services --service-code <service_code> --attribute-name <attribute_name> --max-results <max_results> --filters <filters> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('pricing')
response = client.describe_services(
    ServiceCode=service_code,
    AttributeName=attribute_name,
    MaxResults=max_results,
    Filters=filters,
    Region=region,
)
```
