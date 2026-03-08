---
name: esm-kafka-troubleshoot
description: Troubleshoot Kafka streaming issues and connectivity problems. Diagnoses MSK cluster connectivity, Lambda function timeouts, authentication failures, and network configuration issues. Provides step-by-step resolution guidance for Kafka and Lambda integration problems.
---

# Esm Kafka Troubleshoot

Troubleshoot Kafka streaming issues and connectivity problems. Diagnoses MSK cluster connectivity, Lambda function timeouts, authentication failures, and network configuration issues. Provides step-by-step resolution guidance for Kafka and Lambda integration problems.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `kafka_type` | string | No | Type of Kafka cluster: "msk" for Amazon MSK, "self-managed" for self-managed Apache Kafka, "auto-detect" to determine automatically |
| `issue_type` | string | No | Type of troubleshooting: "diagnosis" for identifying issues, or specific issue type for resolution steps |

