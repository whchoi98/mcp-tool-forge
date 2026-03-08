---
name: get-data-protection-policy
description: Execute the AWS Amazon SNS `get_data_protection_policy` operation.
---

# Get Data Protection Policy

Execute the AWS Amazon SNS `get_data_protection_policy` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ResourceArn` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns get-data-protection-policy --resource-arn <ResourceArn> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.get_data_protection_policy(
    ResourceArn=ResourceArn,
)
```
