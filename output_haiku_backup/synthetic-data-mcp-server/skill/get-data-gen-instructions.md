---
name: get-data-gen-instructions
description: Get instructions for generating synthetic data based on a business description.

    This tool analyzes a business description and provides detailed instructions
    for generating synthetic data in JSON Lines format.

    Parameters:
        business_description: A description of the business use case

    Returns:
        A dictionary containing detailed instructions for generating synthetic data
    
---

# Get Data Gen Instructions

Get instructions for generating synthetic data based on a business description.

    This tool analyzes a business description and provides detailed instructions
    for generating synthetic data in JSON Lines format.

    Parameters:
        business_description: A description of the business use case

    Returns:
        A dictionary containing detailed instructions for generating synthetic data
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `business_description` | string | Yes | A detailed description of the business domain and use case. The more specific and comprehensive the description, the better the data generation instructions will be. |

## AWS CLI

```bash
aws bedrock-runtime invoke-model --model-id <anthropic.claude-v2> --body <business_description> --content-type <application/json>
```

## boto3

```python
import boto3

client = boto3.client('bedrock-runtime')
response = client.invoke_model(
    ModelId=anthropic.claude-v2,
    Body=business_description,
    ContentType=application/json,
)
```
