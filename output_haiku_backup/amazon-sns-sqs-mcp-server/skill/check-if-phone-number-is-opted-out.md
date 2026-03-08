---
name: check-if-phone-number-is-opted-out
description: Execute the AWS Amazon SNS `check_if_phone_number_is_opted_out` operation.
---

# Check If Phone Number Is Opted Out

Execute the AWS Amazon SNS `check_if_phone_number_is_opted_out` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `phoneNumber` | string | Yes |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns check-phone-number-opt-out --phone-number <phoneNumber> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.check_phone_number_opt_out(
    PhoneNumber=phoneNumber,
    region=region,
)
```
