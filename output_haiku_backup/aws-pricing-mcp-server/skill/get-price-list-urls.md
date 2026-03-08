---
name: get-price-list-urls
description: Get download URLs for bulk pricing data files.

    **PURPOSE:** Access complete AWS pricing datasets as downloadable files for historical analysis and bulk processing.

    **WORKFLOW:** Use this for historical pricing analysis or bulk data processing when current pricing from get_pricing() isn't sufficient.

    **PARAMETERS:**
    - Service code from get_pricing_service_codes() (e.g., 'AmazonEC2', 'AmazonS3')
    - AWS region (e.g., 'us-east-1', 'eu-west-1')
    - Optional: effective_date for historical pricing (default: current date)

    **RETURNS:** Dictionary with download URLs for different formats:
    - 'csv': Direct download URL for CSV format
    - 'json': Direct download URL for JSON format

    **USE CASES:**
    - Historical pricing analysis (get_pricing() only provides current pricing)
    - Bulk data processing without repeated API calls
    - Offline analysis of complete pricing datasets
    - Savings Plans analysis across services

    **FILE PROCESSING:**
    - CSV files: Lines 1-5 are metadata, Line 6 contains headers, Line 7+ contains pricing data
    - Use `tail -n +7 pricing.csv | grep "t3.medium"` to filter data
    
---

# Get Price List Urls

Get download URLs for bulk pricing data files.

    **PURPOSE:** Access complete AWS pricing datasets as downloadable files for historical analysis and bulk processing.

    **WORKFLOW:** Use this for historical pricing analysis or bulk data processing when current pricing from get_pricing() isn't sufficient.

    **PARAMETERS:**
    - Service code from get_pricing_service_codes() (e.g., 'AmazonEC2', 'AmazonS3')
    - AWS region (e.g., 'us-east-1', 'eu-west-1')
    - Optional: effective_date for historical pricing (default: current date)

    **RETURNS:** Dictionary with download URLs for different formats:
    - 'csv': Direct download URL for CSV format
    - 'json': Direct download URL for JSON format

    **USE CASES:**
    - Historical pricing analysis (get_pricing() only provides current pricing)
    - Bulk data processing without repeated API calls
    - Offline analysis of complete pricing datasets
    - Savings Plans analysis across services

    **FILE PROCESSING:**
    - CSV files: Lines 1-5 are metadata, Line 6 contains headers, Line 7+ contains pricing data
    - Use `tail -n +7 pricing.csv | grep "t3.medium"` to filter data
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `service_code` | string | Yes | AWS service code (e.g., "AmazonEC2", "AmazonS3", "AmazonES") |
| `region` | string | Yes | AWS region (e.g., "us-east-1", "eu-west-1") |
| `effective_date` | string | No | Effective date for pricing in format "YYYY-MM-DD HH:MM" (default: current timestamp) |

## AWS CLI

```bash
aws pricing get-price-list-urls --service-code <service_code> --region-code <region> --effective-date <effective_date>
```

## boto3

```python
import boto3

client = boto3.client('pricing')
response = client.get_price_list_urls(
    ServiceCode=service_code,
    RegionCode=region,
    EffectiveDate=effective_date,
)
```
