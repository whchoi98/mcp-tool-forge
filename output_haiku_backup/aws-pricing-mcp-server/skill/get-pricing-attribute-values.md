---
name: get-pricing-attribute-values
description: Get valid values for pricing filter attributes.

    **PURPOSE:** Discover what values are available for specific pricing filter attributes of an AWS service.

    **WORKFLOW:** Use this after get_pricing_service_attributes() to see valid values for each filter attribute.

    **PARAMETERS:**
    - Service code from get_pricing_service_codes() (e.g., 'AmazonEC2', 'AmazonRDS')
    - List of attribute names from get_pricing_service_attributes() (e.g., ['instanceType', 'location'])
    - filters (optional): Dictionary mapping attribute names to regex patterns (e.g., {'instanceType': 't3'})

    **RETURNS:** Dictionary mapping attribute names to their valid values. Filtered attributes return only matching values, unfiltered attributes return all values.

    **EXAMPLE RETURN:**
    ```
    {
        'instanceType': ['t2.micro', 't3.medium', 'm5.large', ...],
        'location': ['US East (N. Virginia)', 'EU (London)', ...]
    }
    ```

    **NEXT STEPS:** Use these values in get_pricing() filters to get specific pricing data.

    **ERROR HANDLING:** Uses "all-or-nothing" approach - if any attribute fails, the entire operation fails.

    **EXAMPLES:**
    - Single attribute: ['instanceType'] returns {'instanceType': ['t2.micro', 't3.medium', ...]}
    - Multiple attributes: ['instanceType', 'location'] returns both mappings
    - Partial filtering: filters={'instanceType': 't3'} applies only to instanceType, location returns all values
    
---

# Get Pricing Attribute Values

Get valid values for pricing filter attributes.

    **PURPOSE:** Discover what values are available for specific pricing filter attributes of an AWS service.

    **WORKFLOW:** Use this after get_pricing_service_attributes() to see valid values for each filter attribute.

    **PARAMETERS:**
    - Service code from get_pricing_service_codes() (e.g., 'AmazonEC2', 'AmazonRDS')
    - List of attribute names from get_pricing_service_attributes() (e.g., ['instanceType', 'location'])
    - filters (optional): Dictionary mapping attribute names to regex patterns (e.g., {'instanceType': 't3'})

    **RETURNS:** Dictionary mapping attribute names to their valid values. Filtered attributes return only matching values, unfiltered attributes return all values.

    **EXAMPLE RETURN:**
    ```
    {
        'instanceType': ['t2.micro', 't3.medium', 'm5.large', ...],
        'location': ['US East (N. Virginia)', 'EU (London)', ...]
    }
    ```

    **NEXT STEPS:** Use these values in get_pricing() filters to get specific pricing data.

    **ERROR HANDLING:** Uses "all-or-nothing" approach - if any attribute fails, the entire operation fails.

    **EXAMPLES:**
    - Single attribute: ['instanceType'] returns {'instanceType': ['t2.micro', 't3.medium', ...]}
    - Multiple attributes: ['instanceType', 'location'] returns both mappings
    - Partial filtering: filters={'instanceType': 't3'} applies only to instanceType, location returns all values
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `service_code` | string | Yes | AWS service code (e.g., "AmazonEC2", "AmazonS3", "AmazonES") |
| `attribute_names` | array | Yes | List of attribute names (e.g., ["instanceType", "location", "storageClass"]) |
| `filters` | string | No | Optional dictionary mapping attribute names to regex patterns for filtering their values (e.g., {"instanceType": "t3", "operatingSystem": "Linux"}) |

## AWS CLI

```bash
aws pricing get-attribute-values --service-code <service_code> --attribute-name <attribute_names> --filters <filters>
```

## boto3

```python
import boto3

client = boto3.client('pricing')
response = client.get_attribute_values(
    ServiceCode=service_code,
    AttributeName=attribute_names,
    Filters=filters,
)
```
