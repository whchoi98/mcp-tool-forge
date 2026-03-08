---
name: esm-optimize
description: Optimize streaming data processing performance and costs. Analyzes Lambda function configurations for Kafka, Kinesis, DynamoDB, and SQS event sources. Provides recommendations for batch sizes, concurrency, throughput, and cost optimization. Validates configurations and generates deployment templates.
---

# Esm Optimize

Optimize streaming data processing performance and costs. Analyzes Lambda function configurations for Kafka, Kinesis, DynamoDB, and SQS event sources. Provides recommendations for batch sizes, concurrency, throughput, and cost optimization. Validates configurations and generates deployment templates.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `action` | string | No | Optimization action: "analyze" for tradeoff analysis, "validate" for config validation, "generate_template" for SAM template generation |
| `optimization_targets` | string | No | Optimization goals for analysis (required for analyze action) |
| `event_source` | string | No | Event source type for validation (required for validate action) |
| `configs` | string | No | ESM configuration to validate (required for validate action) |
| `esm_uuid` | string | No | ESM UUID for template generation (required for generate_template action) |
| `optimized_configs` | string | No | Optimized configuration for template generation (required for generate_template action) |
| `region` | string | No | AWS region |
| `project_name` | string | No | Project name for template generation |

