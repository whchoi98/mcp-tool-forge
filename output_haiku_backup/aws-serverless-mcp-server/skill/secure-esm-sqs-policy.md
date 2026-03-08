---
name: secure-esm-sqs-policy
description: Generate security-approved IAM policy for SQS ESM with scoped permissions. Uses pre-approved templates, not LLM generation.
---

# Secure Esm Sqs Policy

Generate security-approved IAM policy for SQS ESM with scoped permissions. Uses pre-approved templates, not LLM generation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region (e.g., us-east-1) |
| `account` | string | Yes | AWS account ID (12 digits) |
| `queue_name` | string | Yes | SQS queue name |
| `function_name` | string | Yes | Lambda function name that will process SQS messages |
| `partition` | string | No | AWS partition (aws, aws-cn, aws-us-gov) |

## AWS CLI

```bash
aws iam create-policy --policy-name <queue_name> --policy-document <function_name> --description <queue_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.create_policy(
    PolicyName=queue_name,
    PolicyDocument=function_name,
    Description=queue_name,
)
```
