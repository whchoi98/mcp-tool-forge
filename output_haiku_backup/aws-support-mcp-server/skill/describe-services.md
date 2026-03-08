---
name: describe-services
description: Retrieve information about AWS services available for support cases.

This tool provides details about AWS services, including their service codes,
names, and categories. Use this information when creating support cases to
ensure you're using valid service and category codes.

## Usage
- You can optionally filter results by providing specific service codes
- You can specify the language for the response
- You can request the response in either JSON or Markdown format

## Example
```python
# Get all services
describe_services()

# Get specific services
describe_services(service_code_list=['amazon-elastic-compute-cloud-linux', 'amazon-s3'])

# Get services in Japanese
describe_services(language='ja')

# Get services in Markdown format
describe_services(format='markdown')
```

## Response Format
The JSON response includes service codes, names, and their categories:
```json
{
    "amazon-elastic-compute-cloud-linux": {
        "name": "Amazon Elastic Compute Cloud (Linux)",
        "categories": [
            {"code": "using-aws", "name": "Using AWS"}
        ]
    }
}
```
---

# Describe Services

Retrieve information about AWS services available for support cases.

This tool provides details about AWS services, including their service codes,
names, and categories. Use this information when creating support cases to
ensure you're using valid service and category codes.

## Usage
- You can optionally filter results by providing specific service codes
- You can specify the language for the response
- You can request the response in either JSON or Markdown format

## Example
```python
# Get all services
describe_services()

# Get specific services
describe_services(service_code_list=['amazon-elastic-compute-cloud-linux', 'amazon-s3'])

# Get services in Japanese
describe_services(language='ja')

# Get services in Markdown format
describe_services(format='markdown')
```

## Response Format
The JSON response includes service codes, names, and their categories:
```json
{
    "amazon-elastic-compute-cloud-linux": {
        "name": "Amazon Elastic Compute Cloud (Linux)",
        "categories": [
            {"code": "using-aws", "name": "Using AWS"}
        ]
    }
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `service_code_list` | string | No | Optional list of service codes to filter results |
| `language` | string | No | The language code (e.g., 'en' for English, 'ja' for Japanese) |
| `format` | string | No | The format of the response (json or markdown) |

## AWS CLI

```bash
aws support describe-services --service-code-list <service_code_list> --language <language>
```

## boto3

```python
import boto3

client = boto3.client('support')
response = client.describe_services(
    ServiceCodeList=service_code_list,
    Language=language,
)
```
