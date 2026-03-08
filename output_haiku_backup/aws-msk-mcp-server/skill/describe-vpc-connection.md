---
name: describe-vpc-connection
description: Gets detailed information about a VPC connection.
---

# Describe Vpc Connection

Gets detailed information about a VPC connection.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region |
| `vpc_connection_arn` | string | Yes | The Amazon Resource Name (ARN) of the VPC connection |

## AWS CLI

```bash
aws kafka describe-vpc-connection --vpc-connection-arn <vpc_connection_arn> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('kafka')
response = client.describe_vpc_connection(
    VpcConnectionArn=vpc_connection_arn,
)
```
