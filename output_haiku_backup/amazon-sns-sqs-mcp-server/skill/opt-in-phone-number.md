---
name: opt-in-phone-number
description: Execute the AWS Amazon SNS `opt_in_phone_number` operation.
---

# Opt In Phone Number

Execute the AWS Amazon SNS `opt_in_phone_number` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `phoneNumber` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns opt-in-phone-number --phone-number <phoneNumber> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.opt_in_phone_number(
    PhoneNumber=phoneNumber,
    Region=region,
)
```
