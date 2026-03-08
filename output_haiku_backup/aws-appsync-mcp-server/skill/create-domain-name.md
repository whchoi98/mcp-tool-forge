---
name: create-domain-name
description: Creates a custom domain name for use with AppSync APIs.

        This operation creates a custom domain name that can be associated with
        AppSync APIs, allowing you to use your own domain instead of the default
        AppSync domain. Requires an SSL certificate from AWS Certificate Manager.
        
---

# Create Domain Name

Creates a custom domain name for use with AppSync APIs.

        This operation creates a custom domain name that can be associated with
        AppSync APIs, allowing you to use your own domain instead of the default
        AppSync domain. Requires an SSL certificate from AWS Certificate Manager.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `domain_name` | string | Yes | The domain name to create (e.g., api.example.com) |
| `certificate_arn` | string | Yes | The ARN of the certificate from AWS Certificate Manager |
| `description` | string | No | A description of the domain name |
| `tags` | string | No | A map of tags to assign to the resource |

## AWS CLI

```bash
aws appsync create-domain-name --domain-name <domain_name> --certificate-arn <certificate_arn> --description <description> --tags <tags>
```

## boto3

```python
import boto3

client = boto3.client('appsync')
response = client.create_domain_name(
    DomainName=domain_name,
    CertificateArn=certificate_arn,
    Description=description,
    Tags=tags,
)
```
