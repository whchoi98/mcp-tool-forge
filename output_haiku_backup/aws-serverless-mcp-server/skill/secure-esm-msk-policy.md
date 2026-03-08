---
name: secure-esm-msk-policy
description: Generate security-approved IAM policy for MSK Kafka ESM with scoped permissions. Uses pre-approved templates, not LLM generation.
---

# Secure Esm Msk Policy

Generate security-approved IAM policy for MSK Kafka ESM with scoped permissions. Uses pre-approved templates, not LLM generation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region (e.g., us-east-1) |
| `account` | string | Yes | AWS account ID (12 digits) |
| `cluster_name` | string | Yes | MSK cluster name |
| `cluster_uuid` | string | Yes | MSK cluster UUID |
| `function_name` | string | Yes | Lambda function name that will process Kafka events |
| `topic_pattern` | string | No | Kafka topic pattern (default: *) |
| `consumer_group_pattern` | string | No | Consumer group pattern (default: *) |
| `partition` | string | No | AWS partition (aws, aws-cn, aws-us-gov) |

