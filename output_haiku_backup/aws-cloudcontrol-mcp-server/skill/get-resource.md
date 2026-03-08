---
name: get-resource
description: Get details of a specific AWS resource.
---

# Get Resource

Get details of a specific AWS resource.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_type` | string | Yes | The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance") |
| `identifier` | string | Yes | The primary identifier of the resource to get (e.g., bucket name for S3 buckets) |
| `region` | string | No | The AWS region that the operation should be performed in |
| `analyze_security` | boolean | No | Whether to perform security analysis on the resource using Checkov |

