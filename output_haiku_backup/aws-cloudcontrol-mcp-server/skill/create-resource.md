---
name: create-resource
description: Create an AWS resource.

    This tool automatically adds default identification tags to all resources for support and troubleshooting purposes.

    IMPORTANT: Always check the response for 'security_warning' field and display any warnings to the user.
    
---

# Create Resource

Create an AWS resource.

    This tool automatically adds default identification tags to all resources for support and troubleshooting purposes.

    IMPORTANT: Always check the response for 'security_warning' field and display any warnings to the user.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_type` | string | Yes | The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance") |
| `region` | string | No | The AWS region that the operation should be performed in |
| `credentials_token` | string | Yes | Credentials token from get_aws_session_info() to ensure AWS credentials are valid |
| `explained_token` | string | Yes | Explained token from explain() - properties will be retrieved from this token |
| `security_scan_token` | string | No | Security scan token from approve_security_findings() to ensure security checks were performed (only required when SECURITY_SCANNING=enabled) |
| `skip_security_check` | boolean | No | Skip security checks (only when SECURITY_SCANNING=disabled) |

## AWS CLI

```bash
aws cloudcontrol create-resource --type-name <resource_type> --desired-state <explained_token> --client-token <credentials_token> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('cloudcontrol')
response = client.create_resource(
    TypeName=resource_type,
    DesiredState=explained_token,
    ClientToken=credentials_token,
    RoleArn=None,
)
```
