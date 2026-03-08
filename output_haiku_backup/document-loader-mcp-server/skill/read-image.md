---
name: read-image
description: Load an image file and return it to the LLM for viewing and analysis.
---

# Read Image

Load an image file and return it to the LLM for viewing and analysis.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | string | Yes | Absolute path to the image file (supports PNG, JPG, JPEG, GIF, BMP, TIFF, WEBP) |
| `timeout_seconds` | integer | No | Timeout in seconds (min: 5, max: 300) |

## AWS CLI

```bash
aws s3 cp --source <file_path> --timeout <timeout_seconds>
```

## boto3

```python
import boto3

client = boto3.client('s3')
response = client.get_object(
    Bucket=document-loader-mcp-server,
    Key=file_path,
)
```
