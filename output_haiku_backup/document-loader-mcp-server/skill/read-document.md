---
name: read-document
description: Extract content from various document formats (PDF, Word, Excel, PowerPoint).
---

# Read Document

Extract content from various document formats (PDF, Word, Excel, PowerPoint).

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | string | Yes | Path to the document file to read |
| `file_type` | string | Yes | Type of document: 'pdf', 'docx', 'doc', 'xlsx', 'xls', 'pptx', or 'ppt' |
| `timeout_seconds` | integer | No | Timeout in seconds (min: 5, max: 300) |

## AWS CLI

```bash
aws textract detect-document-text --document <file_path> --max-results <timeout_seconds>
```

## boto3

```python
import boto3

client = boto3.client('textract')
response = client.detect_document_text(
    Document=file_path,
    MaxResults=timeout_seconds,
)
```
