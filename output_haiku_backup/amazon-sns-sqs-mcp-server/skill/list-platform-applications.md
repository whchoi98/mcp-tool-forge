---
name: list-platform-applications
description: Execute the AWS Amazon SNS `list_platform_applications` operation.
---

# List Platform Applications

Execute the AWS Amazon SNS `list_platform_applications` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `NextToken` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns list-platform-applications --next-token <NextToken> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.list_platform_applications(
    NextToken=NextToken,
    Region=region,
)
```
