---
name: rec-details
description: Get detailed cost optimization recommendation with integrated data from multiple AWS services.

This tool combines data from:
- Cost Optimization Hub (base recommendation)
- AWS Compute Optimizer (detailed metrics for compute resources)
- Cost Explorer (Savings Plans/RI purchase recommendations)

It provides comprehensive analysis with utilization metrics, savings calculations, and implementation guidance.

RESPONSE FORMATTING INSTRUCTIONS:
The tool may return both raw recommendation data and a formatting template.
When presenting the recommendation:
1. If a template is provided, use it to organize your response
2. If no template is provided, structure your response in a clear, logical manner
3. Always include key information like resource details, savings amounts, and implementation steps
4. Ensure all numeric values (costs, savings, metrics) are included
5. Add natural language explanations to make the information more accessible
---

# Rec-Details

Get detailed cost optimization recommendation with integrated data from multiple AWS services.

This tool combines data from:
- Cost Optimization Hub (base recommendation)
- AWS Compute Optimizer (detailed metrics for compute resources)
- Cost Explorer (Savings Plans/RI purchase recommendations)

It provides comprehensive analysis with utilization metrics, savings calculations, and implementation guidance.

RESPONSE FORMATTING INSTRUCTIONS:
The tool may return both raw recommendation data and a formatting template.
When presenting the recommendation:
1. If a template is provided, use it to organize your response
2. If no template is provided, structure your response in a clear, logical manner
3. Always include key information like resource details, savings amounts, and implementation steps
4. Ensure all numeric values (costs, savings, metrics) are included
5. Add natural language explanations to make the information more accessible

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `recommendation_id` | string | Yes |  |

## AWS CLI

```bash
aws ce get-cost-recommendation-details --recommendation-id <recommendation_id>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_cost_recommendation_details(
    RecommendationId=recommendation_id,
)
```
