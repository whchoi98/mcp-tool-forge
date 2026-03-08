---
name: KendraListIndexesTool
description: List all Amazon Kendra indexes in the specified region.

    This tool lists all the Kendra indexes available in the region specified in the mcp configuration.

    Parameters:
        region (str, optional): The AWS region to list Kendra indexes from.

    Returns:
        Dict containing the list of Kendra indexes.
    
---

# Kendralistindexestool

List all Amazon Kendra indexes in the specified region.

    This tool lists all the Kendra indexes available in the region specified in the mcp configuration.

    Parameters:
        region (str, optional): The AWS region to list Kendra indexes from.

    Returns:
        Dict containing the list of Kendra indexes.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | No |  |

## AWS CLI

```bash
aws kendra list-indexes --region <region>
```

## boto3

```python
import boto3

client = boto3.client('kendra')
response = client.list_indexes(
    MaxResults=None,
)
```
