---
name: esm-guidance
description: Create and configure AWS infrastructure for streaming data processing. Handles Kafka clusters (MSK), Kinesis streams, DynamoDB streams, SQS queues with Lambda functions. Sets up VPCs, security groups, IAM roles, and Event Source Mappings. Generates complete SAM templates for deployment.
---

# Esm Guidance

Create and configure AWS infrastructure for streaming data processing. Handles Kafka clusters (MSK), Kinesis streams, DynamoDB streams, SQS queues with Lambda functions. Sets up VPCs, security groups, IAM roles, and Event Source Mappings. Generates complete SAM templates for deployment.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event_source` | string | No | Type of event source for which to get guidance |
| `guidance_type` | string | No | Type of guidance: "setup" for initial configuration, "networking" for VPC/connectivity, "troubleshooting" for issues |
| `networking_question` | string | No | Specific networking question (used with guidance_type="networking") |

