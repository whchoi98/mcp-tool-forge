---
name: generate-cost-report
description: Generate a detailed cost analysis report based on pricing data for one or more AWS services.

This tool requires AWS pricing data and provides options for adding detailed cost information.

IMPORTANT REQUIREMENTS:
- ALWAYS include detailed unit pricing information (e.g., "$0.0008 per 1K input tokens")
- ALWAYS show calculation breakdowns (unit price × usage = total cost)
- ALWAYS specify the pricing model (e.g., "ON DEMAND")
- ALWAYS list all assumptions and exclusions explicitly

Output Format Options:
- 'markdown' (default): Generates a well-formatted markdown report
- 'csv': Generates a CSV format report with sections for service information, unit pricing, cost calculations, etc.

Example usage:

```json
{
  // Required parameters
  "pricing_data": {
    // This should contain pricing data retrieved from get_pricing
    "status": "success",
    "service_name": "bedrock",
    "data": "... pricing information ...",
    "message": "Retrieved pricing for bedrock from AWS Pricing url"
  },
  "service_name": "Amazon Bedrock",

  // Core parameters (commonly used)
  "related_services": ["Lambda", "S3"],
  "pricing_model": "ON DEMAND",
  "assumptions": [
    "Standard ON DEMAND pricing model",
    "No caching or optimization applied",
    "Average request size of 4KB"
  ],
  "exclusions": [
    "Data transfer costs between regions",
    "Custom model training costs",
    "Development and maintenance costs"
  ],
  "output_file": "cost_analysis_report.md",  // or "cost_analysis_report.csv" for CSV format
  "format": "markdown",  // or "csv" for CSV format

  // Advanced parameter for complex scenarios
  "detailed_cost_data": {
    "services": {
      "Amazon Bedrock Foundation Models": {
        "usage": "Processing 1M input tokens and 500K output tokens with Claude 3.5 Haiku",
        "estimated_cost": "$80.00",
        "free_tier_info": "No free tier for Bedrock foundation models",
        "unit_pricing": {
          "input_tokens": "$0.0008 per 1K tokens",
          "output_tokens": "$0.0016 per 1K tokens"
        },
        "usage_quantities": {
          "input_tokens": "1,000,000 tokens",
          "output_tokens": "500,000 tokens"
        },
        "calculation_details": "$0.0008/1K × 1,000K input tokens + $0.0016/1K × 500K output tokens = $80.00"
      },
      "AWS Lambda": {
        "usage": "6,000 requests per month with 512 MB memory",
        "estimated_cost": "$0.38",
        "free_tier_info": "First 12 months: 1M requests/month free",
        "unit_pricing": {
          "requests": "$0.20 per 1M requests",
          "compute": "$0.0000166667 per GB-second"
        },
        "usage_quantities": {
          "requests": "6,000 requests",
          "compute": "6,000 requests × 1s × 0.5GB = 3,000 GB-seconds"
        },
        "calculation_details": "$0.20/1M × 0.006M requests + $0.0000166667 × 3,000 GB-seconds = $0.38"
      }
    }
  },

  // Recommendations parameter - can be provided directly or generated
  "recommendations": {
    "immediate": [
      "Optimize prompt engineering to reduce token usage for Claude 3.5 Haiku",
      "Configure Knowledge Base OCUs based on actual query patterns",
      "Implement response caching for common queries to reduce token usage"
    ],
    "best_practices": [
      "Monitor OCU utilization metrics and adjust capacity as needed",
      "Use prompt caching for repeated context across API calls",
      "Consider provisioned throughput for predictable workloads"
    ]
  }
}
```

---

# Generate Cost Report

Generate a detailed cost analysis report based on pricing data for one or more AWS services.

This tool requires AWS pricing data and provides options for adding detailed cost information.

IMPORTANT REQUIREMENTS:
- ALWAYS include detailed unit pricing information (e.g., "$0.0008 per 1K input tokens")
- ALWAYS show calculation breakdowns (unit price × usage = total cost)
- ALWAYS specify the pricing model (e.g., "ON DEMAND")
- ALWAYS list all assumptions and exclusions explicitly

Output Format Options:
- 'markdown' (default): Generates a well-formatted markdown report
- 'csv': Generates a CSV format report with sections for service information, unit pricing, cost calculations, etc.

Example usage:

```json
{
  // Required parameters
  "pricing_data": {
    // This should contain pricing data retrieved from get_pricing
    "status": "success",
    "service_name": "bedrock",
    "data": "... pricing information ...",
    "message": "Retrieved pricing for bedrock from AWS Pricing url"
  },
  "service_name": "Amazon Bedrock",

  // Core parameters (commonly used)
  "related_services": ["Lambda", "S3"],
  "pricing_model": "ON DEMAND",
  "assumptions": [
    "Standard ON DEMAND pricing model",
    "No caching or optimization applied",
    "Average request size of 4KB"
  ],
  "exclusions": [
    "Data transfer costs between regions",
    "Custom model training costs",
    "Development and maintenance costs"
  ],
  "output_file": "cost_analysis_report.md",  // or "cost_analysis_report.csv" for CSV format
  "format": "markdown",  // or "csv" for CSV format

  // Advanced parameter for complex scenarios
  "detailed_cost_data": {
    "services": {
      "Amazon Bedrock Foundation Models": {
        "usage": "Processing 1M input tokens and 500K output tokens with Claude 3.5 Haiku",
        "estimated_cost": "$80.00",
        "free_tier_info": "No free tier for Bedrock foundation models",
        "unit_pricing": {
          "input_tokens": "$0.0008 per 1K tokens",
          "output_tokens": "$0.0016 per 1K tokens"
        },
        "usage_quantities": {
          "input_tokens": "1,000,000 tokens",
          "output_tokens": "500,000 tokens"
        },
        "calculation_details": "$0.0008/1K × 1,000K input tokens + $0.0016/1K × 500K output tokens = $80.00"
      },
      "AWS Lambda": {
        "usage": "6,000 requests per month with 512 MB memory",
        "estimated_cost": "$0.38",
        "free_tier_info": "First 12 months: 1M requests/month free",
        "unit_pricing": {
          "requests": "$0.20 per 1M requests",
          "compute": "$0.0000166667 per GB-second"
        },
        "usage_quantities": {
          "requests": "6,000 requests",
          "compute": "6,000 requests × 1s × 0.5GB = 3,000 GB-seconds"
        },
        "calculation_details": "$0.20/1M × 0.006M requests + $0.0000166667 × 3,000 GB-seconds = $0.38"
      }
    }
  },

  // Recommendations parameter - can be provided directly or generated
  "recommendations": {
    "immediate": [
      "Optimize prompt engineering to reduce token usage for Claude 3.5 Haiku",
      "Configure Knowledge Base OCUs based on actual query patterns",
      "Implement response caching for common queries to reduce token usage"
    ],
    "best_practices": [
      "Monitor OCU utilization metrics and adjust capacity as needed",
      "Use prompt caching for repeated context across API calls",
      "Consider provisioned throughput for predictable workloads"
    ]
  }
}
```


## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pricing_data` | object | Yes | Raw pricing data from AWS pricing tools |
| `service_name` | string | Yes | Name of the AWS service |
| `related_services` | string | No | List of related AWS services |
| `pricing_model` | string | No | Pricing model (e.g., "ON DEMAND", "Reserved") |
| `assumptions` | string | No | List of assumptions for cost analysis |
| `exclusions` | string | No | List of items excluded from cost analysis |
| `output_file` | string | No | Path to save the report file |
| `format` | string | No | Output format ("markdown" or "csv") |
| `detailed_cost_data` | string | No | Detailed cost information for complex scenarios |
| `recommendations` | string | No | Direct recommendations or guidance for generation |

## AWS CLI

```bash
aws ce get-cost-and-usage --service-name <service_name> --metrics <detailed_cost_data> --filter <related_services> --time-period <pricing_model>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_cost_and_usage(
    ServiceName=service_name,
    Metrics=detailed_cost_data,
    Filter=related_services,
    TimePeriod=pricing_model,
)
```
