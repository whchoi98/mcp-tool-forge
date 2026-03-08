---
name: dsql-search-documentation
description: Search Aurora DSQL documentation
---

# Dsql Search Documentation

Search Aurora DSQL documentation

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `search_phrase` | string | Yes | Search phrase to use |
| `limit` | string | No | Maximum number of results to return |

## AWS CLI

```bash
aws rds search-documentation --search-phrase <search_phrase> --max-results <limit>
```

## boto3

```python
import boto3

client = boto3.client('rds')
response = client.search_documentation(
    SearchPhrase=search_phrase,
    MaxResults=limit,
)
```
