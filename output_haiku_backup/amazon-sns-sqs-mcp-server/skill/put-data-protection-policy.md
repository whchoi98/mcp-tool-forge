---
name: put-data-protection-policy
description: Execute the AWS Amazon SNS `put_data_protection_policy` operation.
---

# Put Data Protection Policy

Execute the AWS Amazon SNS `put_data_protection_policy` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `DataProtectionPolicy` | string | Yes |  |
| `ResourceArn` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns put-data-protection-policy --data-protection-policy <DataProtectionPolicy> --resource-arn <ResourceArn> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.put_data_protection_policy(
    DataProtectionPolicy=DataProtectionPolicy,
    ResourceArn=ResourceArn,
)
```
