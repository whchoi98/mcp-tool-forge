---
name: list-metadata-transfer-jobs
description: List metadata transfer jobs.

    Args:
        source_type: Filter by source type (s3, iotsitewise) - REQUIRED
        destination_type: Filter by destination type (s3, iotsitewise) - REQUIRED
        region: AWS region (default: us-east-1)
        max_results: Maximum number of results to return (1-200, default: 50)
        next_token: Token for pagination

    Returns:
        Dictionary containing list of metadata transfer jobs
    
---

# List Metadata Transfer Jobs

List metadata transfer jobs.

    Args:
        source_type: Filter by source type (s3, iotsitewise) - REQUIRED
        destination_type: Filter by destination type (s3, iotsitewise) - REQUIRED
        region: AWS region (default: us-east-1)
        max_results: Maximum number of results to return (1-200, default: 50)
        next_token: Token for pagination

    Returns:
        Dictionary containing list of metadata transfer jobs
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source_type` | string | Yes | Filter by source type (s3, iotsitewise) - REQUIRED |
| `destination_type` | string | Yes | Filter by destination type (s3, iotsitewise) - REQUIRED |
| `region` | string | No | AWS region |
| `max_results` | integer | No | Maximum number of results to return (1-200) |
| `next_token` | string | No | Token for pagination |

## AWS CLI

```bash
aws iotsitewise list-metadata-transfer-jobs --source-type <source_type> --destination-type <destination_type> --region <region> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.list_metadata_transfer_jobs(
    SourceType=source_type,
    DestinationType=destination_type,
    Region=region,
    MaxResults=max_results,
    NextToken=next_token,
)
```
