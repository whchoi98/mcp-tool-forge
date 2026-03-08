---
name: generate-infrastructure-code
description: Generate infrastructure code before resource creation or update.
---

# Generate Infrastructure Code

Generate infrastructure code before resource creation or update.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_type` | string | Yes | The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance") |
| `properties` | object | No | A dictionary of properties for the resource |
| `identifier` | string | No | The primary identifier of the resource for update operations |
| `patch_document` | array | No | A list of RFC 6902 JSON Patch operations for update operations |
| `region` | string | No | The AWS region that the operation should be performed in |
| `credentials_token` | string | Yes | Credentials token from get_aws_session_info() to ensure AWS credentials are valid |

