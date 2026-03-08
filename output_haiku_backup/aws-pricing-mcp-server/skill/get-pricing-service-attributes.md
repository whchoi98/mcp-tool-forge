---
name: get-pricing-service-attributes
description: Get filterable attributes available for an AWS service in the Pricing API.

    **PURPOSE:** Discover what pricing dimensions (filters) are available for a specific AWS service.

    **WORKFLOW:** Use this after get_pricing_service_codes() to see what filters you can apply to narrow down pricing queries.

    **PARAMETERS:**
    - service_code: AWS service code from get_pricing_service_codes() (e.g., 'AmazonEC2', 'AmazonRDS')
    - filter (optional): Case-insensitive regex pattern to filter attribute names (e.g., "instance" matches "instanceType", "instanceFamily")

    **RETURNS:** List of attribute names (e.g., 'instanceType', 'location', 'storageClass') that can be used as filters.

    **NEXT STEPS:**
    - Use get_pricing_attribute_values() to see valid values for each attribute
    - Use these attributes in get_pricing() filters to get specific pricing data

    **EXAMPLE:** For 'AmazonRDS' you might get ['engineCode', 'instanceType', 'deploymentOption', 'location'].
    
---

# Get Pricing Service Attributes

Get filterable attributes available for an AWS service in the Pricing API.

    **PURPOSE:** Discover what pricing dimensions (filters) are available for a specific AWS service.

    **WORKFLOW:** Use this after get_pricing_service_codes() to see what filters you can apply to narrow down pricing queries.

    **PARAMETERS:**
    - service_code: AWS service code from get_pricing_service_codes() (e.g., 'AmazonEC2', 'AmazonRDS')
    - filter (optional): Case-insensitive regex pattern to filter attribute names (e.g., "instance" matches "instanceType", "instanceFamily")

    **RETURNS:** List of attribute names (e.g., 'instanceType', 'location', 'storageClass') that can be used as filters.

    **NEXT STEPS:**
    - Use get_pricing_attribute_values() to see valid values for each attribute
    - Use these attributes in get_pricing() filters to get specific pricing data

    **EXAMPLE:** For 'AmazonRDS' you might get ['engineCode', 'instanceType', 'deploymentOption', 'location'].
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `service_code` | string | Yes | AWS service code (e.g., "AmazonEC2", "AmazonS3", "AmazonES") |
| `filter` | string | No | Optional case-insensitive regex pattern to filter service attribute names |

## AWS CLI

```bash
aws pricing describe-services --service-code <service_code>
```

## boto3

```python
import boto3

client = boto3.client('pricing')
response = client.describe_services(
    ServiceCode=service_code,
    FormatVersion=SERVICELIST,
)
```
