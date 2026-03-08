---
name: secure-esm-kinesis-policy
description: Generate security-approved IAM policy for Kinesis ESM with scoped permissions. Uses pre-approved templates, not LLM generation.
---

# Secure Esm Kinesis Policy

Generate security-approved IAM policy for Kinesis ESM with scoped permissions. Uses pre-approved templates, not LLM generation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region (e.g., us-east-1) |
| `account` | string | Yes | AWS account ID (12 digits) |
| `stream_name` | string | Yes | Kinesis stream name |
| `function_name` | string | Yes | Lambda function name that will process Kinesis records |
| `partition` | string | No | AWS partition (aws, aws-cn, aws-us-gov) |

## AWS CLI

```bash
aws iam create-policy --policy-name <stream_name> --policy-document <function_name> --description <stream_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.create_policy(
    PolicyName=stream_name,
    PolicyDocument=function_name,
    Description=stream_name,
)
```
