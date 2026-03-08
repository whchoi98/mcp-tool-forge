---
name: create-template
description: Create a CloudFormation template from existing resources using the IaC Generator API.

    This tool allows you to generate CloudFormation templates from existing AWS resources
    that are not already managed by CloudFormation. The template generation process is
    asynchronous, so you can check the status of the process and retrieve the template
    once it's complete. You can pass up to 500 resources at a time.

    IMPORTANT FOR LLMs: This tool only generates CloudFormation templates. If users request
    other IaC formats (Terraform, CDK, etc.), follow this workflow:
    1. Use create_template() to generate CloudFormation template from existing resources
    2. Convert the CloudFormation to the requested format using your native capabilities
    3. For Terraform specifically: Create both resource definitions AND import blocks
       so users can import existing resources into Terraform state
       ⚠️ ALWAYS USE TERRAFORM IMPORT BLOCKS (NOT TERRAFORM IMPORT COMMANDS) ⚠️
    4. Provide both the original CloudFormation and converted IaC to the user

    Example workflow for "create Terraform import for these resources":
    1. create_template() → get CloudFormation template
    2. Convert to Terraform resource blocks
    3. Generate corresponding Terraform import blocks (NOT terraform import commands)
       Example: import { to = aws_s3_bucket.example, id = "my-bucket" }
    4. Provide complete Terraform configuration with import blocks

    Examples:
    1. Start template generation for an S3 bucket:
       create_template(
           template_name="my-template",
           resources=[{"ResourceType": "AWS::S3::Bucket", "ResourceIdentifier": {"BucketName": "my-bucket"}}],
           deletion_policy="RETAIN",
           update_replace_policy="RETAIN"
       )

    2. Check status of template generation:
       create_template(template_id="arn:aws:cloudformation:us-east-1:123456789012:generatedtemplate/abcdef12-3456-7890-abcd-ef1234567890")

    3. Retrieve and save generated template:
       create_template(
           template_id="arn:aws:cloudformation:us-east-1:123456789012:generatedtemplate/abcdef12-3456-7890-abcd-ef1234567890",
           save_to_file="/path/to/template.yaml",
           output_format="YAML"
       )
    
---

# Create Template

Create a CloudFormation template from existing resources using the IaC Generator API.

    This tool allows you to generate CloudFormation templates from existing AWS resources
    that are not already managed by CloudFormation. The template generation process is
    asynchronous, so you can check the status of the process and retrieve the template
    once it's complete. You can pass up to 500 resources at a time.

    IMPORTANT FOR LLMs: This tool only generates CloudFormation templates. If users request
    other IaC formats (Terraform, CDK, etc.), follow this workflow:
    1. Use create_template() to generate CloudFormation template from existing resources
    2. Convert the CloudFormation to the requested format using your native capabilities
    3. For Terraform specifically: Create both resource definitions AND import blocks
       so users can import existing resources into Terraform state
       ⚠️ ALWAYS USE TERRAFORM IMPORT BLOCKS (NOT TERRAFORM IMPORT COMMANDS) ⚠️
    4. Provide both the original CloudFormation and converted IaC to the user

    Example workflow for "create Terraform import for these resources":
    1. create_template() → get CloudFormation template
    2. Convert to Terraform resource blocks
    3. Generate corresponding Terraform import blocks (NOT terraform import commands)
       Example: import { to = aws_s3_bucket.example, id = "my-bucket" }
    4. Provide complete Terraform configuration with import blocks

    Examples:
    1. Start template generation for an S3 bucket:
       create_template(
           template_name="my-template",
           resources=[{"ResourceType": "AWS::S3::Bucket", "ResourceIdentifier": {"BucketName": "my-bucket"}}],
           deletion_policy="RETAIN",
           update_replace_policy="RETAIN"
       )

    2. Check status of template generation:
       create_template(template_id="arn:aws:cloudformation:us-east-1:123456789012:generatedtemplate/abcdef12-3456-7890-abcd-ef1234567890")

    3. Retrieve and save generated template:
       create_template(
           template_id="arn:aws:cloudformation:us-east-1:123456789012:generatedtemplate/abcdef12-3456-7890-abcd-ef1234567890",
           save_to_file="/path/to/template.yaml",
           output_format="YAML"
       )
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template_name` | string | No | Name for the generated template |
| `resources` | string | No | List of resources to include in the template, each with 'ResourceType' and 'ResourceIdentifier' |
| `output_format` | string | No | Output format for the template (JSON or YAML) |
| `deletion_policy` | string | No | Default DeletionPolicy for resources in the template (RETAIN, DELETE, or SNAPSHOT) |
| `update_replace_policy` | string | No | Default UpdateReplacePolicy for resources in the template (RETAIN, DELETE, or SNAPSHOT) |
| `template_id` | string | No | ID of an existing template generation process to check status or retrieve template |
| `save_to_file` | string | No | Path to save the generated template to a file |
| `region` | string | No | The AWS region that the operation should be performed in |

## AWS CLI

```bash
aws cloudcontrol generate-template --template-name <template_name> --resources <resources> --output-format <output_format> --deletion-policy <deletion_policy> --update-replace-policy <update_replace_policy> --template-id <template_id> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('cloudcontrol')
response = client.generate_template(
    TemplateName=template_name,
    Resources=resources,
    OutputFormat=output_format,
    DeletionPolicy=deletion_policy,
    UpdateReplacePolicy=update_replace_policy,
    TemplateId=template_id,
    Region=region,
)
```
