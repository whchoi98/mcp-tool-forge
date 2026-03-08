---
name: get-dimension-values
description: Retrieve available dimension values for AWS Cost Explorer.

    This tool retrieves all available and valid values for a specified dimension (e.g., SERVICE, REGION)
    over a period of time. This is useful for validating filter values or exploring available options
    for cost analysis.

    Args:
        ctx: MCP context
        date_range: The billing period start and end dates in YYYY-MM-DD format
        dimension: The dimension key to retrieve values for (e.g., SERVICE, REGION, LINKED_ACCOUNT)

    Returns:
        Dictionary containing the dimension name and list of available values
    
---

# Get Dimension Values

Retrieve available dimension values for AWS Cost Explorer.

    This tool retrieves all available and valid values for a specified dimension (e.g., SERVICE, REGION)
    over a period of time. This is useful for validating filter values or exploring available options
    for cost analysis.

    Args:
        ctx: MCP context
        date_range: The billing period start and end dates in YYYY-MM-DD format
        dimension: The dimension key to retrieve values for (e.g., SERVICE, REGION, LINKED_ACCOUNT)

    Returns:
        Dictionary containing the dimension name and list of available values
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `date_range` | string | Yes |  |
| `dimension` | string | Yes |  |

## AWS CLI

```bash
aws ce get-dimension-values --time-period <date_range> --dimension <dimension>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_dimension_values(
    TimePeriod=date_range,
    Dimension=dimension,
)
```
