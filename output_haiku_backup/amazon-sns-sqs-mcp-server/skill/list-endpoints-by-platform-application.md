---
name: list-endpoints-by-platform-application
description: Execute the AWS Amazon SNS `list_endpoints_by_platform_application` operation.
---

# List Endpoints By Platform Application

Execute the AWS Amazon SNS `list_endpoints_by_platform_application` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `PlatformApplicationArn` | string | Yes |  |
| `NextToken` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns list-endpoints-by-platform-application --platform-application-arn <PlatformApplicationArn> --next-token <NextToken> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.list_endpoints_by_platform_application(
    PlatformApplicationArn=PlatformApplicationArn,
    NextToken=NextToken,
)
```
