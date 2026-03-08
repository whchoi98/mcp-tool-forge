---
name: list-origination-numbers
description: Execute the AWS Amazon SNS `list_origination_numbers` operation.
---

# List Origination Numbers

Execute the AWS Amazon SNS `list_origination_numbers` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `NextToken` | string | No |  |
| `MaxResults` | string | No |  |
| `region` | string | No | AWS region |

## AWS CLI

```bash
aws sns list-origination-numbers --next-token <NextToken> --max-results <MaxResults> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('sns')
response = client.list_origination_numbers(
    NextToken=NextToken,
    MaxResults=MaxResults,
)
```
