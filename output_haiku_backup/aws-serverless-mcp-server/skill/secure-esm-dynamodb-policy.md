---
name: secure-esm-dynamodb-policy
description: Generate security-approved IAM policy for DynamoDB Streams ESM with scoped permissions. Uses pre-approved templates, not LLM generation.
---

# Secure Esm Dynamodb Policy

Generate security-approved IAM policy for DynamoDB Streams ESM with scoped permissions. Uses pre-approved templates, not LLM generation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region (e.g., us-east-1) |
| `account` | string | Yes | AWS account ID (12 digits) |
| `table_name` | string | Yes | DynamoDB table name |
| `function_name` | string | Yes | Lambda function name that will process DynamoDB stream records |
| `partition` | string | No | AWS partition (aws, aws-cn, aws-us-gov) |

## AWS CLI

```bash
aws iam create-policy --policy-name <table_name> --policy-document <function_name> --description <DynamoDB Streams ESM Policy>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.create_policy(
    PolicyName=table_name,
    PolicyDocument=function_name,
    Description=DynamoDB Streams ESM Policy,
)
```
