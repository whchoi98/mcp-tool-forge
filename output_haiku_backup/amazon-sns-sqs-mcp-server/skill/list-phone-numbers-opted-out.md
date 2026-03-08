---
name: list-phone-numbers-opted-out
description: Execute the AWS Amazon SNS `list_phone_numbers_opted_out` operation.
---

# List Phone Numbers Opted Out

Execute the AWS Amazon SNS `list_phone_numbers_opted_out` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `nextToken` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns list-phone-numbers-opted-out --next-token <nextToken> --phone-number-region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.list_phone_numbers_opted_out(
    NextToken=nextToken,
    PhoneNumberRegion=region,
)
```
