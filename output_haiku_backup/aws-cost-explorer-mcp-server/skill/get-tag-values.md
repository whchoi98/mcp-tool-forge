---
name: get-tag-values
description: Retrieve available tag values for AWS Cost Explorer.

    This tool retrieves all available values for a specified tag key over a period of time.
    This is useful for validating tag filter values or exploring available tag options for cost analysis.

    Args:
        ctx: MCP context
        date_range: The billing period start and end dates in YYYY-MM-DD format
        tag_key: The tag key to retrieve values for

    Returns:
        Dictionary containing the tag key and list of available values
    
---

# Get Tag Values

Retrieve available tag values for AWS Cost Explorer.

    This tool retrieves all available values for a specified tag key over a period of time.
    This is useful for validating tag filter values or exploring available tag options for cost analysis.

    Args:
        ctx: MCP context
        date_range: The billing period start and end dates in YYYY-MM-DD format
        tag_key: The tag key to retrieve values for

    Returns:
        Dictionary containing the tag key and list of available values
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `date_range` | string | Yes |  |
| `tag_key` | string | Yes | The tag key to retrieve values for |

## AWS CLI

```bash
aws ce get-tags --time-period <date_range> --tag-key <tag_key>
```

## boto3

```python
import boto3

client = boto3.client('ce')
response = client.get_tags(
    TimePeriod=date_range,
    TagKey=tag_key,
)
```
