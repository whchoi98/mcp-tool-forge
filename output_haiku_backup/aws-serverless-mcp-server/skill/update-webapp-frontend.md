---
name: update-webapp-frontend
description: Update the frontend assets of a deployed web application.

        This tool uploads new frontend assets to S3 and optionally invalidates the CloudFront cache.
        
---

# Update Webapp Frontend

Update the frontend assets of a deployed web application.

        This tool uploads new frontend assets to S3 and optionally invalidates the CloudFront cache.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `project_name` | string | Yes | Project name |
| `project_root` | string | Yes | Project root |
| `built_assets_path` | string | Yes | Absolute path to pre-built frontend assets |
| `invalidate_cache` | string | No | Whether to invalidate the CloudFront cache |
| `region` | string | No | AWS region to use (e.g., us-east-1) |

## AWS CLI

```bash
aws s3 sync --bucket <project_name> --prefix <project_root> --source <built_assets_path>
```

## boto3

```python
import boto3

client = boto3.client('s3')
response = client.sync(
    Bucket=project_name,
    Prefix=project_root,
    SourceDir=built_assets_path,
)
```
