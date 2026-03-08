---
name: update-resource
description: Update an AWS resource.

    IMPORTANT: Always check the response for 'security_warning' field and display any warnings to the user.
    
---

# Update Resource

Update an AWS resource.

    IMPORTANT: Always check the response for 'security_warning' field and display any warnings to the user.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_type` | string | Yes | The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance") |
| `identifier` | string | Yes | The primary identifier of the resource to get (e.g., bucket name for S3 buckets) |
| `patch_document` | array | No | A list of RFC 6902 JSON Patch operations to apply |
| `region` | string | No | The AWS region that the operation should be performed in |
| `credentials_token` | string | Yes | Credentials token from get_aws_session_info() to ensure AWS credentials are valid |
| `explained_token` | string | Yes | Explained token from explain() to ensure exact properties with default tags are used |
| `security_scan_token` | string | No | Security scan token from run_checkov() to ensure security checks were performed (only required when SECURITY_SCANNING=enabled) |
| `skip_security_check` | boolean | No | Skip security checks (not recommended) |

## AWS CLI

```bash
aws cloudcontrol update-resource --type-name <resource_type> --identifier <identifier> --patch-document <patch_document> --role-arn <credentials_token>
```

## boto3

```python
import boto3

client = boto3.client('cloudcontrol')
response = client.update_resource(
    TypeName=resource_type,
    Identifier=identifier,
    PatchDocument=patch_document,
    RoleArn=credentials_token,
)
```
