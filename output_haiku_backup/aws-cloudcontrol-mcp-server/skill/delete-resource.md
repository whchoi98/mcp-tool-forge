---
name: delete-resource
description: Delete an AWS resource.
---

# Delete Resource

Delete an AWS resource.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_type` | string | Yes | The AWS resource type (e.g., "AWS::S3::Bucket", "AWS::RDS::DBInstance") |
| `identifier` | string | Yes | The primary identifier of the resource to get (e.g., bucket name for S3 buckets) |
| `region` | string | No | The AWS region that the operation should be performed in |
| `credentials_token` | string | Yes | Credentials token from get_aws_session_info() to ensure AWS credentials are valid |
| `confirmed` | boolean | No | Confirm that you want to delete this resource |
| `explained_token` | string | Yes | Explained token from explain() to ensure deletion was explained |

## AWS CLI

```bash
aws cloudcontrol delete-resource --type-name <resource_type> --identifier <identifier> --client-token <credentials_token>
```

## boto3

```python
import boto3

client = boto3.client('cloudcontrol')
response = client.delete_resource(
    TypeName=resource_type,
    Identifier=identifier,
    ClientToken=credentials_token,
)
```
