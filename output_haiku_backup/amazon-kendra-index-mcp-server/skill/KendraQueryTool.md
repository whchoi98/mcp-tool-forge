---
name: KendraQueryTool
description: Query Amazon Kendra and retrieve content from the response.

    This tool queries the specified Amazon Kendra index with the provided query
    and returns the search results. The specified Kendra Index is either provided by the user in the chat, or the default index configured in the environemnt variables

    Parameters:
        query (str): The search query to send to Amazon Kendra.
        region (str): The region of the Kendra Index to send the search query to.
        indexId (str): The indexId of the Kendra index to send the search query to.

    Returns:
        Dict containing the query results from Amazon Kendra.
    
---

# Kendraquerytool

Query Amazon Kendra and retrieve content from the response.

    This tool queries the specified Amazon Kendra index with the provided query
    and returns the search results. The specified Kendra Index is either provided by the user in the chat, or the default index configured in the environemnt variables

    Parameters:
        query (str): The search query to send to Amazon Kendra.
        region (str): The region of the Kendra Index to send the search query to.
        indexId (str): The indexId of the Kendra index to send the search query to.

    Returns:
        Dict containing the query results from Amazon Kendra.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes |  |
| `region` | string | No |  |
| `indexId` | string | No |  |

## AWS CLI

```bash
aws kendra retrieve --query <query> --index-id <indexId> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('kendra')
response = client.retrieve(
    Query=query,
    IndexId=indexId,
    Region=region,
)
```
