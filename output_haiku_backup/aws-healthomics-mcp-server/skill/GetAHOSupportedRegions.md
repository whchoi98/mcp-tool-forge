---
name: GetAHOSupportedRegions
description: Get the list of AWS regions where HealthOmics is available.

    Args:
        ctx: MCP context for error reporting

    Returns:
        Dictionary containing the list of supported region codes and the total count
        of regions where HealthOmics is available
    
---

# Getahosupportedregions

Get the list of AWS regions where HealthOmics is available.

    Args:
        ctx: MCP context for error reporting

    Returns:
        Dictionary containing the list of supported region codes and the total count
        of regions where HealthOmics is available
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|

## AWS CLI

```bash
aws omics list-regions
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.list_regions(
)
```
