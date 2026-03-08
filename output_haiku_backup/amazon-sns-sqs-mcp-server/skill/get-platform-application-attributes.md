---
name: get-platform-application-attributes
description: Execute the AWS Amazon SNS `get_platform_application_attributes` operation.
---

# Get Platform Application Attributes

Execute the AWS Amazon SNS `get_platform_application_attributes` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `PlatformApplicationArn` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns get-platform-application-attributes --platform-application-arn <PlatformApplicationArn>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.get_platform_application_attributes(
    PlatformApplicationArn=PlatformApplicationArn,
)
```
