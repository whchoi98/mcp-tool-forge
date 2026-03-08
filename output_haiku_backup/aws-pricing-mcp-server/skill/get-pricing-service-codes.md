---
name: get-pricing-service-codes
description: Get AWS service codes available in the Price List API.

    **PURPOSE:** Discover which AWS services have pricing information available in the AWS Price List API.

    **PARAMETERS:**
    - filter (optional): Case-insensitive regex pattern to filter service codes (e.g., "bedrock" matches "AmazonBedrock", "AmazonBedrockService")

    **WORKFLOW:** This is the starting point for any pricing query. Use this first to find the correct service code.

    **RETURNS:** List of service codes (e.g., 'AmazonEC2', 'AmazonS3', 'AWSLambda') that can be used with other pricing tools.

    **NEXT STEPS:**
    - Use get_pricing_service_attributes() to see what filters are available for a service
    - Use get_pricing() to get actual pricing data for a service

    **NOTE:** Service codes may differ from AWS console names (e.g., 'AmazonES' for OpenSearch, 'AWSLambda' for Lambda).
    
---

# Get Pricing Service Codes

Get AWS service codes available in the Price List API.

    **PURPOSE:** Discover which AWS services have pricing information available in the AWS Price List API.

    **PARAMETERS:**
    - filter (optional): Case-insensitive regex pattern to filter service codes (e.g., "bedrock" matches "AmazonBedrock", "AmazonBedrockService")

    **WORKFLOW:** This is the starting point for any pricing query. Use this first to find the correct service code.

    **RETURNS:** List of service codes (e.g., 'AmazonEC2', 'AmazonS3', 'AWSLambda') that can be used with other pricing tools.

    **NEXT STEPS:**
    - Use get_pricing_service_attributes() to see what filters are available for a service
    - Use get_pricing() to get actual pricing data for a service

    **NOTE:** Service codes may differ from AWS console names (e.g., 'AmazonES' for OpenSearch, 'AWSLambda' for Lambda).
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `filter` | string | No | Optional case-insensitive regex pattern to filter service codes |

## AWS CLI

```bash
aws pricing describe-services --service-code <filter>
```

## boto3

```python
import boto3

client = boto3.client('pricing')
response = client.describe_services(
    ServiceCode=filter,
)
```
