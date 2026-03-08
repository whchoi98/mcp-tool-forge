---
name: list-event-data-stores
description: List available CloudTrail Lake Event Data Stores with their capabilities and event selectors.

        Event Data Stores are the storage and query engines for CloudTrail Lake. This tool helps you
        understand which Event Data Stores are available and their configurations.

        Usage: Use this tool to understand which Event Data Stores are available and their
        configurations. This information is needed when executing CloudTrail Lake queries.

        Returns:
        --------
        List of available Event Data Stores with their configurations
        
---

# List Event Data Stores

List available CloudTrail Lake Event Data Stores with their capabilities and event selectors.

        Event Data Stores are the storage and query engines for CloudTrail Lake. This tool helps you
        understand which Event Data Stores are available and their configurations.

        Usage: Use this tool to understand which Event Data Stores are available and their
        configurations. This information is needed when executing CloudTrail Lake queries.

        Returns:
        --------
        List of available Event Data Stores with their configurations
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `include_details` | boolean | No | Whether to include detailed event selector information (default: true) |
| `region` | string | No | AWS region to query. Defaults to us-east-1. |

## AWS CLI

```bash
aws cloudtrail list-event-data-stores --include-details <include_details> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('cloudtrail')
response = client.list_event_data_stores(
    IncludeDetails=include_details,
    Region=region,
)
```
