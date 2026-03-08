---
name: sam-deploy
description: Deploys a serverless application onto AWS Cloud using AWS SAM (Serverless Application Model) CLI and CloudFormation.

        Requirements:
        - AWS SAM CLI MUST be installed and configured in your environment
        - SAM project MUST be initialized using sam_init tool and built with sam_build.

        This command deploys your SAM application's build artifacts located in the .aws-sam directory
        to AWS Cloud using AWS CloudFormation. The only required parameter is project_directory. SAM will automatically
        create a S3 bucket where build artifacts are uploaded and referenced by the SAM template.

        Usage tips:
        - When you make changes to your application's original files, run sam build to update the .aws-sam directory before deploying.

        Returns:
            Dict: SAM deploy command output
        
---

# Sam Deploy

Deploys a serverless application onto AWS Cloud using AWS SAM (Serverless Application Model) CLI and CloudFormation.

        Requirements:
        - AWS SAM CLI MUST be installed and configured in your environment
        - SAM project MUST be initialized using sam_init tool and built with sam_build.

        This command deploys your SAM application's build artifacts located in the .aws-sam directory
        to AWS Cloud using AWS CloudFormation. The only required parameter is project_directory. SAM will automatically
        create a S3 bucket where build artifacts are uploaded and referenced by the SAM template.

        Usage tips:
        - When you make changes to your application's original files, run sam build to update the .aws-sam directory before deploying.

        Returns:
            Dict: SAM deploy command output
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `application_name` | string | Yes | Name of the application to be deployed |
| `project_directory` | string | Yes | Absolute path to directory containing the SAM project (defaults to current directory) |
| `template_file` | string | No | Absolute path to the template file (defaults to template.yaml) |
| `s3_bucket` | string | No | S3 bucket to deploy artifacts to. You cannot set both s3_bucket and resolve_s3 parameters |
| `s3_prefix` | string | No | S3 prefix for the artifacts |
| `region` | string | No | AWS region to deploy to |
| `profile` | string | No | AWS profile to use |
| `parameter_overrides` | string | No | CloudFormation parameter overrides encoded as key-value pairs |
| `capabilities` | string | No | IAM capabilities required for the deployment |
| `config_file` | string | No | Absolute path to the SAM configuration file |
| `config_env` | string | No | Environment name specifying default parameter values in the configuration file |
| `metadata` | string | No | Metadata to include with the stack |
| `tags` | string | No | Tags to apply to the stack |
| `resolve_s3` | boolean | No | Automatically create an S3 bucket for deployment artifacts.  You cannot set both s3_bucket and resolve_s3 parameters |
| `debug` | boolean | No | Turn on debug logging |

