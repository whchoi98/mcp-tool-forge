---
name: get-job-status
description: get background job status
---

# Get Job Status

get background job status

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `job_id` | string | Yes |  |

## AWS CLI

```bash
aws rds describe-db-cluster-backtrack --db-cluster-backtrack-identifier <job_id>
```

## boto3

```python
import boto3

client = boto3.client('rds')
response = client.describe_db_cluster_bactrack(
    BacktrackIdentifier=job_id,
)
```
